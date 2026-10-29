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

Push to `main`; Pages serves from the repo root at
https://khangtran-812.github.io/Personal-website/.

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
