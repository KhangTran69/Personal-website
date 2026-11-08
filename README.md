# Personal Website

Portfolio of **Khang B. Tran** — CS student & aspiring application developer (Angeles City, PH).

Built with plain HTML/CSS/JS — no build step. Dark slate theme, emerald accent,
Poppins / Inter / Roboto Mono via Google Fonts, Typed.js typing effect.

## Structure

```
index.html    # all sections: hero, about, projects, skills, experience, contact
style.css     # theme tokens in :root, responsive at 960px / 760px
script.js     # typing effect, mobile nav, scrollspy, reveal-on-scroll, footer year
resume.pdf    # downloadable resume (generated from the fixed DOCX)
images/       # portrait, favicon.svg, projects/*.svg preview cards
```

## Behavior review map

| Behavior | Read first | Verification evidence and limits |
|----------|------------|----------------------------------|
| Mobile navigation opens, updates `aria-expanded`, and closes after a link is chosen | [`index.html` nav controls](index.html#L24-L34), [`initNav`](script.js#L38-L56), [responsive nav styles](style.css#L650-L668) | `node --check script.js` checks syntax only. No automated test exercises menu interaction or assistive-technology output. |
| Active section highlighting and reveal-on-scroll | [`initScrollspy` and `initReveal`](script.js#L58-L110), [active-link and reveal styles](style.css#L97-L106) and [motion styles](style.css#L634-L695) | `node --check script.js` checks syntax only. Static checks do not verify observer behavior, animation, or reduced-motion rendering. |
| Local section links and bundled assets | [`index.html`](index.html), [`check_site.py`](scripts/check_site.py), [`test_check_site.py`](tests/test_check_site.py) | CI runs `python scripts/check_site.py` and `python -m unittest discover -s tests -v`. These cover local paths and in-page anchors, not external destinations or visual layout. |
| Typing fallback and current footer year | [`#typed`](index.html#L44), [`#year`](index.html#L254), [`initTyped`](script.js#L15-L36), and [`initYear`](script.js#L112-L116) | `node --check script.js` checks syntax only; dynamic rendering is not covered by automated tests. |

For changes to interactive behavior, inspect the linked HTML, JavaScript, and CSS together, then check desktop and mobile behavior in a browser. The repository's automated checks do not establish visual or screen-reader behavior.

## Run locally

Run `python3 scripts/check_site.py` to verify local assets and section links,
and `node --check script.js` to check JavaScript syntax. CI runs both checks
on pushes and pull requests. External links and visual behavior are not checked.

```bash
python3 -m http.server 8123
# open http://127.0.0.1:8123
```

(Open `index.html` directly also works — no server required.)

## Deploy (GitHub Pages)

The live portfolio URL, https://khangtran-812.github.io/Personal-website/, is
served from the `KhangTran-812` account. This repository is the `KhangTran69`
fork, so pushing here does not update that live site. To publish this fork as a
separate project site, enable GitHub Pages for this repository and select the
`main` branch with the repository root as its source; its expected URL is
https://khangtran69.github.io/Personal-website/.

## Editing notes

- Theme colors and fonts are CSS custom properties at the top of `style.css`.
- Project cards live in `index.html` under `#projects`. The Garbage Route
  Optimizer and QA graphics are authored illustrations, labeled as previews;
  the PoPify, help-desk, and SMS images are app captures. Keep that distinction
  clear when replacing assets.
- `resume.pdf`: edit the DOCX source, then regenerate:
  `soffice --headless --convert-to pdf --outdir . <file>.docx` and rename to `resume.pdf`.
- Factual metrics (426 tests, 100% pass rate, 41,575 views…) come from the
  resume — keep them in sync when the resume changes.
