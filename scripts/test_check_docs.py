import tempfile
import unittest
from pathlib import Path

from scripts.check_docs import (
    compare_language_structure,
    evaluate_translation_drift,
    find_broken_local_anchors,
    find_broken_local_links,
    find_forbidden_public_strings,
    slugify_heading,
)

class DocsChecksTests(unittest.TestCase):
    def test_detects_missing_relative_markdown_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'index.md').write_text('[Missing](missing.md)\n',encoding='utf-8')
            self.assertEqual(len(find_broken_local_links(root)),1)
    def test_ignores_external_and_anchor_links_for_file_existence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'index.md').write_text('[Web](https://example.org/) [Anchor](#section)\n',encoding='utf-8')
            self.assertEqual(find_broken_local_links(root),[])
    def test_language_structure_must_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); fa=root/'fa'; en=root/'en'; fa.mkdir(); en.mkdir()
            (fa/'index.md').write_text('# fa\n'); (en/'index.md').write_text('# en\n'); (fa/'01.md').write_text('# fa\n')
            self.assertEqual(compare_language_structure(fa,en),([],['01.md']))
    def test_slugify_heading_handles_latin_and_persian(self):
        self.assertEqual(slugify_heading('Login Result Detection'),'login-result-detection')
        self.assertEqual(slugify_heading('تشخیص نتیجه ورود'),'تشخیص-نتیجه-ورود')
    def test_local_anchor_on_same_page_must_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'index.md').write_text('# موجود\n\n[Missing](#ناموجود)\n',encoding='utf-8')
            self.assertEqual(find_broken_local_anchors(root),['index.md: #ناموجود'])
    def test_duplicate_heading_anchors_follow_suffix_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'index.md').write_text('# Test\n\n## Test\n\n[Second](#test_1)\n',encoding='utf-8')
            self.assertEqual(find_broken_local_anchors(root),[])
    def test_translation_drift_thresholds(self):
        self.assertEqual(evaluate_translation_drift(30),'ok'); self.assertEqual(evaluate_translation_drift(31),'warning'); self.assertEqual(evaluate_translation_drift(91),'error')
    def test_forbidden_real_target_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'docs').mkdir(); (root/'docs'/'fa').mkdir(); (root/'docs'/'fa'/'index.md').write_text('cpanel.tikadentplus.ir',encoding='utf-8')
            findings=find_forbidden_public_strings(root)
            self.assertTrue(findings)

if __name__ == '__main__':
    unittest.main()
