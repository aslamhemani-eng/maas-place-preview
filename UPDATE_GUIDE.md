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
Upload via cPanel File Manager to `public_html/`: `maas-place.html`, `blooming-star-village.html`,
`programs.html`, `thank-you.html`, `enroll.php`, `site-chrome.css`, `section.css`, `section.js`, `schedule.json`, `gallery.json`,
`img/site-logo.png`, `gallery/`. Weekly, only `schedule.json`, `gallery.json` and new photos change.
Do not upload `index.html` from this folder (it would replace the homepage).

## Enrollment forms → aslamhemani@gmail.com (for now)
**Current recipient: aslamhemani@gmail.com** (`$TO` in enroll.php). Switch `$TO` to hello@maasinspiration.org once that mailbox is set up in Microsoft 365.
Note: Gmail is strict about mail "From" no-reply@maasinspiration.org sent by GoDaddy's server; the first messages may land in Spam. Mark them "Not spam" / create a Gmail filter, and add GoDaddy to the domain SPF record (or use SMTP) for reliable delivery.

Both forms (Maa's Place enrollment, Blooming Star Village interest list) post to `enroll.php`,
a small PHP mail handler that emails each submission to the `$TO` address
(Reply-To = the submitter's email when given) and then shows `thank-you.html`.
- Spam protection: hidden "website" honeypot field (bots that fill it are silently dropped), plus a
  whitelist of form names, header-injection stripping, and a minimum-fields check.
- Live setup (GoDaddy cPanel): upload `enroll.php` and `thank-you.html` with the other files to `public_html/`.
  In cPanel › Email Accounts make sure `hello@maasinspiration.org` receives mail (the domain's MX is Microsoft 365,
  so create the mailbox/alias there). `$FROM` in enroll.php is `no-reply@maasinspiration.org`; GoDaddy requires a
  From on your own domain. If messages land in spam, add GoDaddy's server to the domain's SPF record
  or switch the handler to SMTP.
- Test after upload: submit each form once with your own email and confirm it arrives at hello@.
- To change the recipient, edit `$TO` at the top of enroll.php.
- Preview (github.io) cannot run PHP: there the forms just show the thank-you page and nothing is sent.
- Fallback if PHP mail is blocked: set the form `action` to `https://formsubmit.co/hello@maasinspiration.org`
  (one-time activation email to hello@).

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
