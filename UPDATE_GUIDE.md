# Weekly Update Guide – Maa's Place pages

## Update the weekly schedule (2 min)
Edit `schedule.json`:
- `week_of`: line shown above the table (e.g. "Monday to Thursday, 10 AM to 2 PM")
- `slots`: the column times; each day's `slots` list has one activity per column (same order). "TBD" shows highlighted.
- A day can use `all_day` (one line across all columns) instead of `slots`; optional `led_by`.
- `"hidden": true` hides a day (Friday is hidden until confirmed).
Keep commas/quotes valid (check at https://jsonlint.com).

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
Upload via cPanel File Manager to `public_html/`: `maas-place.html`, `bloom-village.html`,
`programs.html`, `thank-you.html`, `site-chrome.css`, `section.css`, `section.js`, `schedule.json`, `gallery.json`,
`img/site-logo.png`, `gallery/`. Weekly, only `schedule.json`, `gallery.json` and new photos change.
Do not upload `index.html` from this folder (it would replace the homepage).

## Online forms → secure public-forms endpoint (no email services)
Every form on the site sends JSON to the public-forms endpoint set in `forms-config.js`. No form
uses an email relay or a personal mailbox.
- Signed forms (meals, driver, volunteer, Maa's Place, Bloom Village fee/rights/complaint) use `forms.js`.
- Simple forms use `mi-post.js`: the Contact page and the Meals page contact form (`form_type: "contact"`),
  the Bloom Village tour/interest form (`form_type: "bloom_inquiry"`), and the gift dedication pop-up on the
  donate and meals pages (`contact`, program "Donation dedication").
- Volunteer and Maa's Place sign-ups are big buttons to `form-volunteer.html` and `form-maas-place.html`.
- If a send fails, the page asks the person to call (469) 270-8156. There is no email fallback.
- Spam protection: hidden "website" honeypot field.

## Donations tagged by program (donate.html)
`live-upload/donate.html` is the live donate page with one change: it reads `?program=` from the URL
(`meals`, `maas-place`, `bsv`, `general`; anything else/missing = `general`) and adds
`client_reference_id=<program>` to the Stripe Payment Link when the donor clicks "Donate via Stripe".
Wording, amounts and layout are unchanged (see `live-upload/donate.html.diff`).
- Upload: cPanel File Manager → `public_html/donate.html` (back up the current file first as `donate.backup.html`).
  The GoDaddy monitoring tag at the very end of the served page is injected by the host, so it is not in this file.
- Links to use: `donate.html?program=maas-place`, `?program=bsv`, `?program=meals`; plain `donate.html` = general.
- See the program in Stripe: Dashboard → Payments → open a payment → the Checkout summary shows **Client reference ID**
  (also under Payment Links → select link → Payments). For monthly reports: Payments → Export (or Checkout Sessions export)
  and include the `client_reference_id` column; filter/sum by program. Note it is not shown to the donor or on their receipt.
- Test page (preview only, not indexed): https://aslamhemani-eng.github.io/maas-place-preview/donate-test.html?program=bsv
