import tempfile
import unittest
from pathlib import Path

from scripts.check_site import check_site


class CheckSiteTests(unittest.TestCase):
    def test_reports_missing_asset_and_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text(
                '<main id="home"><a href="#missing">Go</a>'
                '<img src="images/missing.png"></main>', encoding="utf-8"
            )
            errors, count = check_site(root)
        self.assertEqual(count, 2)
        self.assertEqual(len(errors), 2)
        self.assertTrue(any("missing anchor" in error for error in errors))
        self.assertTrue(any("missing local asset" in error for error in errors))

    def test_accepts_existing_asset_and_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "image.svg").write_text("<svg/>", encoding="utf-8")
            (root / "index.html").write_text(
                '<main id="home"><a href="#home">Go</a>'
                '<img src="image.svg"></main>', encoding="utf-8"
            )
            errors, count = check_site(root)
        self.assertEqual((errors, count), ([], 2))
