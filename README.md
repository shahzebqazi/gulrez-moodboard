# Paradise Found — Moodboard

A single-page mood board for the Paradise Found creative brief. Built for **GitHub Pages**.

## Contents

- **Black background** with a zoomed-out canvas of Polaroid-style photos
- **Click any photo** → smooth zoom into that image; **click the dark overlay or ×** (or press Escape) → zoom back to the board
- **Deliverables** listed in a post-it note (Logo variants, Still life flora, Heritage elements)
- **Email** link in the footer — replace `your@email.com` in `index.html` with your real address

## GitHub Pages

1. Push this repo to GitHub.
2. **Settings → Pages** → Source: **Deploy from a branch**.
3. Branch: **main** (or your default), folder: **/ (root)**.
4. Save. The site will be at `https://<username>.github.io/<repo>/`.

Ensure these paths exist at repo root: `index.html`, `css/style.css`, `js/main.js`, `assets/` (with floral, handicrafts, Logo.png, gulrez.png).

## Local preview

```bash
# From repo root (e.g. Moodboard-gulrez)
python3 -m http.server 8000
# Open http://localhost:8000
```

Replace `your@email.com` in `index.html` before publishing.
