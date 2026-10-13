"""Package the existing OpenAI listing without replacing its saved MCP connection."""
import hashlib
import json
from pathlib import Path
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / '.codex-plugin/plugin.json').read_text())
manifest['name'] = 'app-6abab8682c508191ba77499620af8241'
# Preserve the exact server URL already saved in the publishing portal.
manifest['mcpServers'] = './.mcp.json'
listing = manifest['interface']
assert len(listing['displayName']) <= 30
assert len(listing['shortDescription']) <= 30
assert len(listing['longDescription']) <= 4000
assert len(listing['defaultPrompt']) <= 3
assert len(set(listing['defaultPrompt'])) == len(listing['defaultPrompt'])
assert all(len(prompt) <= 128 and '\n' not in prompt for prompt in listing['defaultPrompt'])
assert all(len(capability) <= 120 for capability in listing['capabilities'])
output = Path(sys.argv[1])
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
    archive.writestr('.codex-plugin/plugin.json', json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    archive.writestr('.mcp.json', json.dumps({'mcpServers': {'magicinterview': {'url': 'https://magicinterview.ai/mcp?toolset=directory'}}}, indent=2) + '\n')
    for relative in ['skills/meeting-prep/SKILL.md', 'skills/meeting-prep/agents/openai.yaml', 'assets/icon-192.png', 'assets/icon-512.png']:
        archive.write(root / relative, relative)
with zipfile.ZipFile(output) as archive:
    assert json.loads(archive.read('.codex-plugin/plugin.json')) == manifest
    print(json.dumps({'path': str(output), 'version': manifest['version'], 'files': archive.namelist(), 'sha256': hashlib.sha256(output.read_bytes()).hexdigest()}))
