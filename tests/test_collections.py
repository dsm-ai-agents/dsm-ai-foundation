import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from new_research import create_collection
from validate_repository import validate


class CollectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / 'templates', self.root / 'templates')
        (self.root / 'docs').mkdir()
        for name in ('WORKFLOW.md', 'CONTENT-AND-WEB.md', 'BRAND.md'):
            shutil.copy2(ROOT / 'docs' / name, self.root / 'docs' / name)
        (self.root / 'README.md').write_text('# Test studio\n')

    def test_create_with_quoted_title_and_validate(self):
        title = 'Future "work" and skills'
        folder = create_collection(self.root, 'future-skills', title, 'Agentic Accelerator')
        manifest = json.loads((folder / 'project.json').read_text())
        self.assertEqual(manifest['title'], title)
        self.assertEqual(manifest['expected_topics'], 0)
        self.assertIn('[Future "work" and skills](future-skills/README.md)',
                      (self.root / 'collections/README.md').read_text())
        self.assertEqual(validate(self.root), [])

    def test_reject_existing_without_changing_content(self):
        folder = create_collection(self.root, 'one', 'One', 'Unassigned')
        (folder / 'README.md').write_text('User work')
        with self.assertRaises(ValueError):
            create_collection(self.root, 'one', 'Replacement', 'Unassigned')
        self.assertEqual((folder / 'README.md').read_text(), 'User work')

    def test_reject_invalid_inputs(self):
        for slug in ('../outside', '/absolute', 'Upper', 'two--hyphens', ''):
            with self.subTest(slug=slug), self.assertRaises(ValueError):
                create_collection(self.root, slug, 'Title', 'Unassigned')
        with self.assertRaises(ValueError):
            create_collection(self.root, 'valid', 'Title', 'Unknown')

    def test_detect_broken_link_and_duplicate_ids(self):
        folder = create_collection(self.root, 'one', 'One', 'Unassigned')
        (folder / 'README.md').write_text('[Missing](missing.md)')
        (folder / 'production/topics.json').write_text('[{"id":"a"},{"id":"a"}]')
        errors = validate(self.root)
        self.assertTrue(any('duplicate IDs' in error for error in errors))
        self.assertTrue(any('broken link missing.md' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
