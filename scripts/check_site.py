"""Check local assets and in-page links in the static portfolio."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[tuple[int, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        for key in ("href", "src"):
            if values.get(key):
                self.links.append((self.getpos()[0], values[key]))


def main() -> None:
    parser = SiteParser()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    errors: list[str] = []
    for line, link in parser.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or link.startswith("//"):
            continue
        path = unquote(parsed.path)
        if path and (path.startswith("/") or not (ROOT / path).is_file()):
            errors.append(f"line {line}: missing local asset {link}")
        if parsed.fragment and (not path or path == "index.html") and unquote(parsed.fragment) not in parser.ids:
            errors.append(f"line {line}: missing anchor {link}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(parser.links)} links and assets")


if __name__ == "__main__":
    main()
