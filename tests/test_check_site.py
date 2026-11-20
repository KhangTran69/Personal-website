import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

from scripts.check_site import check_site


class ProjectCardParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_projects = False
        self.in_heading = False
        self.card_count = 0
        self.headings: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "section" and values.get("id") == "projects":
            self.in_projects = True
        if not self.in_projects:
            return
        if tag == "article" and "project-card" in (values.get("class") or "").split():
            self.card_count += 1
        if tag == "h3":
            self.in_heading = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "h3":
            self.in_heading = False
        if tag == "section" and self.in_projects:
            self.in_projects = False

    def handle_data(self, data: str) -> None:
        if self.in_projects and self.in_heading:
            heading = data.strip()
            if heading:
                self.headings.append(heading)


class CheckSiteTests(unittest.TestCase):
    def test_projects_section_has_six_active_cards(self) -> None:
        parser = ProjectCardParser()
        parser.feed((Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8"))
        self.assertEqual(parser.card_count, 6)
        self.assertEqual(parser.headings, [
            "FlowOps",
            "Garbage Route Optimizer",
            "IT Help Desk & Asset Management System",
            "PoPify",
            "Philippine SMS Spam Detector",
            "Investagrams QA Regression Suite",
        ])

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
