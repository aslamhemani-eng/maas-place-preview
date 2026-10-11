# Weekly Update Guide – Maa's Place pages

## Update the weekly schedule (2 min)
Edit `schedule.json`:
- `week_of`: e.g. "Oct 19–24, 2026"
- each day: `time`, `activities`, `led_by` (first names only)
- `note`: optional; set to "" to hide
Any text containing the word PLACEHOLDER shows as a highlighted box – remove it when filled.
Check the commas/quotes are kept (paste into https://jsonlint.com if unsure).

## Update the gallery (3 min)
1. Resize photos to ~1200px on the long side (JPG). Only people with signed photo consent.
2. Upload them into the `gallery/` folder. Name: `YYYY-MM-DD-short-name.jpg`.
3. Add one line per photo to `gallery.json` (newest first):
   `{"file": "2026-10-17-bingo-01.jpg", "caption": "Bingo Wednesday", "program": "maas-place"}`
4. Remove old entries (and files) you no longer want shown; keep ~6–12 photos.

## Text changes / placeholders
Page text lives in `build.py`. Edit, then run `python3 build.py` (preview) or
`PREVIEW=0 python3 build.py` (live: removes preview banner + noindex). Placeholders use `ph("...")`.

## Publishing on the live site (GoDaddy cPanel)
Upload via cPanel File Manager to `public_html/`: `maas-place.html`, `blooming-star-village.html`,
`programs.html`, `site-chrome.css`, `section.css`, `section.js`, `schedule.json`, `gallery.json`,
`img/site-logo.png`, `gallery/`. Weekly, only `schedule.json`, `gallery.json` and new photos change.
Do not upload `index.html` from this folder (it would replace the homepage).
