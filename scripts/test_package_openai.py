"""Verify listing assets and onboarding cannot be omitted or escape a submitted package."""
import json
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zipfile

from package_openai import image_dimensions, package_members, root, validate_metadata, validate_screenshot


class ListingPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        for relative in ['plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json', 'server.json', 'lhm.plugin.json']:
            target = self.directory / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(root / relative, target)
        for relative in ['assets', 'skills']:
            shutil.copytree(root / relative, self.directory / relative)

    def edit(self, relative, change):
        target = self.directory / relative
        data = json.loads(target.read_text())
        change(data)
        target.write_text(json.dumps(data))

    def set_screenshots(self, screenshots):
        self.edit('plugin.json', lambda data: data['extensions']['com.openai']['interface'].update(screenshots=screenshots))
        self.edit('.codex-plugin/plugin.json', lambda data: data['interface'].update(screenshots=screenshots))

    def test_package_includes_all_advertised_images_and_onboarding(self):
        data = validate_metadata(self.directory)
        members = package_members(data)
        self.assertIn('skills/get-started/SKILL.md', members)
        self.assertIn('assets/assistant-workspace.jpg', members)
        self.assertEqual(data['interface']['screenshots'], ['./assets/assistant-workspace.jpg', './assets/notion-meeting-sync.jpg'])
        self.assertIn('assets/notion-meeting-sync.jpg', members)
        self.assertEqual(image_dimensions((root / 'assets/assistant-workspace.jpg').read_bytes()), (1280, 886))
        self.assertEqual(image_dimensions((root / 'assets/mac-coach.webp').read_bytes()), (1600, 1000))
        output = self.directory / 'fresh-upload.zip'
        subprocess.run([sys.executable, str(root / 'scripts/package_openai.py'), str(output)], check=True, capture_output=True)
        with zipfile.ZipFile(output) as archive:
            server = json.loads(archive.read('.mcp.json'))['mcpServers']['magicinterview']
            self.assertEqual(server['url'], 'https://magicinterview.ai/mcp?toolset=directory')
            self.assertEqual(server['extensions']['com.openai']['auth'], {'type': 'oauth', 'client': {'mode': 'dcr'}})
            self.assertNotIn('clientSecret', json.dumps(server))
            review = json.loads(archive.read('.codex-plugin/plugin.json'))['extensions']['com.openai']['review']
            self.assertEqual(len(review['test_cases']['positive']), 5)
            self.assertEqual(len(review['test_cases']['negative']), 3)
            self.assertEqual(review['demo_recording_url'], 'https://github.com/samihalawa/magicinterview-plugin/releases/download/v1.0.0/magicinterview-review-demo.mp4')
            self.assertNotIn('test_credentials', review)
            self.assertNotIn('reviewer_instructions', review)

    def test_screenshot_manifest_drift_is_rejected(self):
        self.edit('.codex-plugin/plugin.json', lambda data: data['interface'].update(screenshots=['./assets/mac-coach.webp']))
        with self.assertRaisesRegex(AssertionError, 'listing copies differ'):
            validate_metadata(self.directory)

    def test_onboarding_manifest_drift_is_rejected(self):
        self.edit('plugin.json', lambda data: data['extensions']['com.openai'].update(onboardingSkill='./skills/meeting-prep/SKILL.md'))
        with self.assertRaisesRegex(AssertionError, 'Onboarding skill copies differ'):
            validate_metadata(self.directory)

    def test_missing_onboarding_is_rejected(self):
        (self.directory / 'skills/get-started/SKILL.md').unlink()
        with self.assertRaisesRegex(AssertionError, 'Missing asset'):
            validate_metadata(self.directory)

    def test_missing_screenshot_is_rejected(self):
        self.set_screenshots(['./assets/missing.png'])
        with self.assertRaisesRegex(AssertionError, 'Missing asset'):
            validate_metadata(self.directory)

    def test_paths_outside_package_are_rejected(self):
        self.set_screenshots(['./../outside.png'])
        with self.assertRaisesRegex(AssertionError, 'escapes package'):
            validate_metadata(self.directory)

    def test_external_screenshot_urls_are_rejected(self):
        self.set_screenshots(['https://example.com/image.png'])
        with self.assertRaisesRegex(AssertionError, 'package-relative'):
            validate_metadata(self.directory)

    def test_duplicate_screenshots_are_rejected(self):
        self.set_screenshots(['./assets/mac-coach.webp'] * 2)
        with self.assertRaisesRegex(AssertionError, 'Duplicate screenshots'):
            validate_metadata(self.directory)

    def test_oversized_dimensions_are_rejected(self):
        target = self.directory / 'assets/oversized.png'
        target.write_bytes(b'\x89PNG\r\n\x1a\n' + b'\0' * 8 + struct.pack('>II', 4097, 1000))
        with self.assertRaisesRegex(AssertionError, 'dimensions'):
            validate_screenshot(self.directory, './assets/oversized.png')

    def test_oversized_file_is_rejected(self):
        target = self.directory / 'assets/oversized.png'
        target.write_bytes(b'\0' * (5 * 1024 * 1024 + 1))
        with self.assertRaisesRegex(AssertionError, '5 MiB'):
            validate_screenshot(self.directory, './assets/oversized.png')

    def test_unsupported_asset_is_rejected(self):
        target = self.directory / 'assets/not-an-image.txt'
        target.write_text('not an image')
        with self.assertRaisesRegex(AssertionError, 'format'):
            validate_screenshot(self.directory, './assets/not-an-image.txt')

    def test_jpeg_disguised_as_png_is_rejected(self):
        target = self.directory / 'assets/disguised.png'
        shutil.copy(root / 'assets/assistant-workspace.jpg', target)
        with self.assertRaisesRegex(AssertionError, 'extension does not match file signature'):
            validate_screenshot(self.directory, './assets/disguised.png')

    def test_all_current_image_assets_match_their_extensions(self):
        for target in (root / 'assets').iterdir():
            if target.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp', '.svg'}:
                with self.subTest(asset=target.name):
                    validate_screenshot(root, './assets/' + target.name)

    def test_invalid_image_is_rejected(self):
        target = self.directory / 'assets/broken.png'
        target.write_text('not an image')
        with self.assertRaisesRegex(AssertionError, 'invalid screenshot'):
            validate_screenshot(self.directory, './assets/broken.png')


if __name__ == '__main__':
    unittest.main()
