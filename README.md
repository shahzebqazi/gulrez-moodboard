# Paradise Found — Moodboard

A single-page mood board for the Paradise Found creative brief. Built for **GitHub Pages**.

## Contents

- **Black background** with a zoomed-out canvas of Polaroid-style photos
- **Click any photo** → smooth zoom into that image; **click the dark overlay or ×** (or press Escape) → zoom back to the board
- **Deliverables** listed in a post-it note (Logo variants, Still life flora, Heritage elements)
- **Email** link in the footer — replace `your@email.com` in `index.html` with your real address

## GitHub Pages

**Live site:** [https://shahzebqazi.github.io/gulrez-moodboard/](https://shahzebqazi.github.io/gulrez-moodboard/)

Configured to deploy from the **main** branch, root folder. To change: **Settings → Pages** → Source: **Deploy from a branch** → Branch: **main**, folder: **/ (root)**.

Ensure these paths exist at repo root: `index.html`, `css/style.css`, `js/main.js`, `assets/` (with floral, handicrafts, Logo.png, gulrez.png).

## Local preview

```bash
# From repo root (e.g. Moodboard-gulrez)
python3 -m http.server 8000
# Open http://localhost:8000
```

Replace `your@email.com` in `index.html` before publishing.
