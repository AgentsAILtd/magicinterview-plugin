"""Package the existing OpenAI listing without replacing its saved MCP connection."""
import hashlib
import json
from pathlib import Path
import sys
import zipfile
import struct
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
def local_file(directory, relative):
    assert isinstance(relative, str) and relative.startswith('./'), 'Asset paths must be package-relative'
    target = (directory / relative).resolve()
    assert target.is_relative_to(directory.resolve()), 'Asset path escapes package'
    assert target.is_file(), f'Missing asset: {relative}'
    return target


def image_extension(data):
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        return '.png'
    if data.startswith(b'\xff\xd8'):
        return '.jpg'
    if data.startswith(b'RIFF') and data[8:12] == b'WEBP':
        return '.webp'
    try:
        if ET.fromstring(data).tag.rsplit('}', 1)[-1] == 'svg':
            return '.svg'
    except ET.ParseError:
        pass
    raise AssertionError('Unsupported or invalid screenshot')


def image_dimensions(data):
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        return struct.unpack('>II', data[16:24])
    if data.startswith(b'RIFF') and data[8:12] == b'WEBP':
        kind = data[12:16]
        if kind == b'VP8X':
            return (1 + int.from_bytes(data[24:27], 'little'), 1 + int.from_bytes(data[27:30], 'little'))
        if kind == b'VP8 ' and data[23:26] == b'\x9d\x01\x2a':
            return tuple(value & 0x3fff for value in struct.unpack('<HH', data[26:30]))
        if kind == b'VP8L' and data[20] == 0x2f:
            bits = int.from_bytes(data[21:25], 'little')
            return (1 + (bits & 0x3fff), 1 + ((bits >> 14) & 0x3fff))
    if data.startswith(b'\xff\xd8'):
        position = 2
        while position + 4 <= len(data):
            assert data[position] == 0xff, 'Invalid JPEG marker'
            marker = data[position + 1]
            position += 2
            if marker in (0xd8, 0xd9):
                continue
            length = int.from_bytes(data[position:position + 2], 'big')
            assert length >= 2, 'Invalid JPEG segment'
            if marker in (0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf):
                height, width = struct.unpack('>HH', data[position + 3:position + 7])
                return (width, height)
            position += length
    try:
        node = ET.fromstring(data)
        assert node.tag.rsplit('}', 1)[-1] == 'svg', 'Not an SVG image'
        if 'viewBox' in node.attrib:
            values = node.attrib['viewBox'].replace(',', ' ').split()
            return tuple(float(value) for value in values[2:4])
        return tuple(float(node.attrib[key].removesuffix('px')) for key in ('width', 'height'))
    except (ET.ParseError, KeyError, ValueError):
        raise AssertionError('Unsupported or invalid screenshot')


def validate_screenshot(directory, relative):
    target = local_file(directory, relative)
    assert target.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp', '.svg'}, 'Unsupported screenshot format'
    data = target.read_bytes()
    assert 0 < len(data) <= 5 * 1024 * 1024, 'Screenshot exceeds 5 MiB'
    suffix = '.jpg' if target.suffix.lower() == '.jpeg' else target.suffix.lower()
    assert suffix == image_extension(data), 'Image extension does not match file signature'
    dimensions = image_dimensions(data)
    assert len(dimensions) == 2 and all(0 < value <= 4096 for value in dimensions), 'Screenshot dimensions exceed 4096'
    return dimensions


def package_members(canonical):
    interface = canonical['interface']
    return list(dict.fromkeys([
        'skills/meeting-prep/SKILL.md', 'skills/meeting-prep/agents/openai.yaml',
        canonical['extensions']['com.openai']['onboardingSkill'].removeprefix('./'),
        interface['composerIcon'].removeprefix('./'), interface['logo'].removeprefix('./'),
        *(path.removeprefix('./') for path in interface.get('screenshots', [])),
    ]))


def validate_metadata(directory):
    manifests = {name: json.loads((directory / name).read_text()) for name in [
        'plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json', 'server.json', 'lhm.plugin.json',
    ]}
    canonical = manifests['.codex-plugin/plugin.json']
    listing = canonical['interface']
    assert manifests['plugin.json']['extensions']['com.openai']['interface'] == listing, 'OpenAI listing copies differ'
    for name, data in manifests.items():
        assert data['version'] == canonical['version'], f'{name}: version differs'
        if name != 'server.json':
            assert data['description'] == canonical['description'], f'{name}: product description differs'
    assert len(manifests['server.json']['description']) <= 100, 'Registry description exceeds 100 characters'
    assert len(listing['displayName']) <= 30
    assert len(listing['shortDescription']) <= 30
    assert len(listing['longDescription']) <= 4000
    assert len(listing['defaultPrompt']) <= 3
    assert len(set(listing['defaultPrompt'])) == len(listing['defaultPrompt'])
    assert all(len(prompt) <= 128 and '\n' not in prompt for prompt in listing['defaultPrompt'])
    assert all(len(capability) <= 120 for capability in listing['capabilities'])
    root_openai = manifests['plugin.json']['extensions']['com.openai']
    onboarding = canonical['extensions']['com.openai']['onboardingSkill']
    assert root_openai['onboardingSkill'] == onboarding, 'Onboarding skill copies differ'
    assert onboarding.endswith('/SKILL.md'), 'Onboarding must point to SKILL.md'
    local_file(directory, onboarding)
    local_file(directory, manifests['plugin.json']['logo'])
    screenshots = listing.get('screenshots', [])
    assert isinstance(screenshots, list) and len(screenshots) == len(set(screenshots)), 'Duplicate screenshots'
    for relative in screenshots:
        validate_screenshot(directory, relative)
    for relative in package_members(canonical):
        local_file(directory, './' + relative)
    return canonical


def main():
    manifest = validate_metadata(root)
    if sys.argv[1:] == ['--check']:
        print(json.dumps({'validated': 5, 'version': manifest['version'], 'listingCharacters': len(manifest['interface']['longDescription']), 'screenshots': manifest['interface'].get('screenshots', []), 'onboardingSkill': manifest['extensions']['com.openai']['onboardingSkill'], 'packageFiles': package_members(manifest)}))
        return
    manifest['name'] = 'app-6abab8682c508191ba77499620af8241'
    # Preserve the exact server URL already saved in the publishing portal.
    manifest['mcpServers'] = './.mcp.json'
    output = Path(sys.argv[1])
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('.codex-plugin/plugin.json', json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
        archive.writestr('.mcp.json', json.dumps({'mcpServers': {'magicinterview': {'url': 'https://magicinterview.ai/mcp?toolset=directory'}}}, indent=2) + '\n')
        for relative in package_members(manifest):
            archive.write(root / relative, relative)
    with zipfile.ZipFile(output) as archive:
        assert json.loads(archive.read('.codex-plugin/plugin.json')) == manifest
        print(json.dumps({'path': str(output), 'version': manifest['version'], 'files': archive.namelist(), 'sha256': hashlib.sha256(output.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()
