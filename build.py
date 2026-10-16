# Regenerates the 3 pages. Run: python3 build.py   (PREVIEW=0 python3 build.py for live build without banner/noindex)
import os,re
P=os.environ.get('PREVIEW','1')=='1'
B=''
head=lambda t:f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {'<meta name="robots" content="noindex,nofollow">' if P else ''}
    <title>{t} - MAA's Inspiration</title>
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="site-chrome.css">
    <link rel="stylesheet" href="section.css">
</head>
<body>
'''+('<div class="preview-banner">PREVIEW FOR APPROVAL — not live yet. <b style="background:#FFF4D6;color:#7a4b1f;padding:0 6px;border-radius:4px">Dashed boxes</b> = info still needed.</div>\n' if P else '')+f'''    <nav>
        <div class="navbar-container">
            <a href="index.html" class="logo-section">
                <img src="img/site-logo.png" alt="MAA's Inspiration Logo">
                <span class="logo-text">MAA's Inspiration</span>
            </a>
            <ul class="nav-links" id="navLinks">
                <li><a href="index.html">Home</a></li>
                <li><a href="{B}about.html">About</a></li>
                <li><a href="{B}volunteer.html">Volunteer</a></li>
                <li><a href="{B}schedule.html">Schedule</a></li>
                <li><a href="{B}gallery.html">Gallery</a></li>
                <li><a href="programs.html">Programs</a></li>
                <li><a href="contact.html">Contact</a></li>
                <li><button class="donate-btn" onclick="window.location.href='{B}donate.html'">Donate</button></li>
            </ul>
            <div class="hamburger" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>
<main class="mi">
'''
foot=f'''</main>
<div id="lb" onclick="this.style.display='none'"><img alt=""></div>
    <footer>
        <div class="footer-container">
            <div class="footer-section">
                <div class="footer-logo-section">
                    <img src="img/site-logo.png" alt="MAA's Inspiration Logo">
                </div>
                <div class="footer-motto">LOVE ALL SERVE ALL</div>
                <p class="footer-description">Serving our community with warmth, dignity, and compassion through nourishing meals and genuine care.</p>
            </div>
            <div class="footer-section">
                <h4>Quick Links</h4>
                <ul class="footer-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="{B}about.html">About</a></li>
                    <li><a href="{B}volunteer.html">Volunteer</a></li>
                    <li><a href="{B}schedule.html">Schedule</a></li>
                    <li><a href="{B}gallery.html">Gallery</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Follow Us</h4>
                <div class="social-icons">
                    <a href="https://www.facebook.com/maasinspiration" target="_blank" rel="noopener noreferrer" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                    <a href="https://www.instagram.com/maasinspiration/" target="_blank" rel="noopener noreferrer" title="Instagram"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            © 2026 MAA's Inspiration. 501(c)(3) Nonprofit Organization · EIN 86-2221897.
        </div>
    </footer>
<script src="section.js"></script>
</body>
</html>
'''
DON=B+'donate.html'; VOL=B+'volunteer.html'; ph=lambda t:f'<span class="ph">{t}</span>'
donate=lambda w:f'''<section id="donate" class="donate"><div class="wrap"><h2>Support {w}</h2>
<p>Donations are taken through our existing secure donation page.</p>
<a class="btn alt" href="{DON}">Donate Now</a>
<p style="font-size:.85rem;margin-top:14px">MAA's Inspiration is a 501(c)(3) nonprofit · EIN 86-2221897</p></div></section>'''
mp=head("Senior Center").replace('<main class="mi">','<main class="mi purple">')+f'''<div class="sub"><a href="#what">What We Do</a><a href="#schedule">Schedule</a><a href="#gallery">Gallery</a><a href="#visit">Visit / Enroll</a><a href="#volunteer">Volunteer</a><a href="#donate">Donate</a><a href="#contact">Contact &amp; FAQ</a><a href="get-involved.html#maas-place">Get Involved</a></div>
<header class="hero" style="--img:url(gallery/maas-place-seniors-painting.jpg)"><p class="eyebrow">Programs · MAA's Inspiration</p><span class="soon-badge">🌱 Opening soon</span>
<h1>Senior Center</h1>
<p class="tagline">Place where everybody knows your name</p>
<p class="soon-line">The Senior Center is opening soon. Join the interest list below and we'll let you know when doors open.</p>
<p>A warm, welcoming place where seniors in Dallas–Fort Worth gather for activities, homestyle snacks, chai and companionship, carried forward in the spirit of Maa, whose greatest joy was feeding others.</p>
<div class="facts"><div>🕙 Monday to Thursday, 10 AM to 2 PM</div><div>👵 Ages 55+</div><div>📞 <a href="tel:+14692708156" style="color:#fff">(469) 270-8156</a></div><div>📍 <a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75007" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75007</a></div></div>
<a class="btn alt" href="#visit">Plan a Visit</a> &nbsp; <a class="btn ghost" href="{VOL}" style="color:#fff">Volunteer</a></header>
<section id="what"><div class="wrap"><h2>What We Do</h2><p>Every activity at the Senior Center is chosen to keep seniors active in body and mind, from gentle exercise and brain games to arts, music, and learning something new. Just as important, it’s a place to share laughter, snacks, and friendship, where every senior feels valued and no one is alone.</p>
<div class="grid">
<div class="card"><h3>💪 Physical</h3><ul class="ticks"><li>Chair exercises and gentle stretching</li><li>Balance and fall-prevention exercises</li><li>Group walks</li><li>Light dance and movement to music</li><li>Chair yoga or tai chi</li><li>Fun movement games (balloon toss, bean bag games)</li><li>Healthy snacks</li><li>Health checks and wellness talks</li></ul></div>
<div class="card"><h3>🧠 Mental</h3><ul class="ticks"><li>Puzzles, word games, and trivia</li><li>Memory and brain-training games</li><li>Reading and storytelling circles</li><li>Learning sessions (technology, health talks, new skills)</li><li>Music, singing, and sing-alongs</li><li>Arts and crafts for creativity and focus</li><li>Group discussions and sharing life stories</li><li>Bingo, cards, and board games</li></ul></div>
<div class="card"><h3>📚 Educational</h3><ul class="ticks"><li>Smartphone, tablet, and video-call help (staying in touch with family)</li><li>Health, nutrition, and medication-safety talks</li><li>Scam and fraud awareness</li><li>Guest speakers from the community</li><li>Cooking and healthy-eating demonstrations</li><li>Language and conversation classes</li><li>Gardening and nature sessions</li><li>Cultural and history discussions</li></ul></div>
<div class="card"><h3>🎲 Fun &amp; Entertainment</h3><ul class="ticks"><li>Bingo, cards, and board games</li><li>Movie and music afternoons</li><li>Sing-alongs and karaoke</li><li>Birthday celebrations</li><li>Holiday and cultural festivals</li><li>Talent shows and storytelling</li><li>Outings and field trips</li><li>Tea, snacks, and social hours</li></ul></div>
<div class="card"><h3>🍵 Snacks &amp; Chai</h3><ul class="ticks"><li>Light snacks</li><li>Tea and coffee</li><li>Fresh fruit</li><li>Special treats for birthdays and holidays</li><li>Prepared with care for senior dietary needs</li></ul></div>
</div></div></section>
<section id="schedule"><div class="wrap"><h2>Weekly Schedule of Activities</h2>
<p>Open: <b id="weekOf">…</b></p>
<div class="tw"><table><thead id="schedHead"></thead><tbody id="sched"><tr><td>Loading…</td></tr></tbody></table></div></div></section>
<section id="gallery"><div class="wrap"><h2>Photo Gallery</h2><p class="soon-line">Photos coming soon. The Senior Center opens its doors shortly!</p></div></section>
<section id="visit"><div class="wrap"><h2>Visit or Enroll <span class="soon-badge sm">Opening soon</span></h2>
<div class="grid"><div class="card"><h3>1. Come say hello</h3><p>Drop in Monday to Thursday, 10 AM to 2 PM, call <a href="tel:+14692708156">(469) 270-8156</a>, or email <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a> to schedule a tour.</p></div>
<div class="card"><h3>2. Enroll</h3><p>Complete the short form below; family members can fill it out on a senior's behalf.</p></div>
<div class="card"><h3>3. Sign the waiver</h3><p>Sign our participation waiver and optional photo/video consent on your first visit. <a href="maas-place-waiver.html">Read &amp; print the participation waiver</a></p></div></div>
<p style="margin-top:18px">Who can attend: Adults 55 and up · Cost: Free · Transportation: not provided</p>
<h3>Enrollment / Interest Form</h3><p>The Senior Center is opening soon – sign up now and we'll contact you when it opens.</p>
<form id="enroll"><label>Senior's full name *<input required></label><label>Date of birth<input type="date"></label>
<label>Phone *<input type="tel" required></label><label>Email (optional)<input type="email"></label>
<label class="full">Home address / city &amp; ZIP<input></label>
<label>Preferred language<select><option>English</option><option>Urdu / Hindi</option><option>Gujarati</option><option>Other</option></select></label>
<label>Days you plan to attend<select multiple size="3"><option>Monday</option><option>Tuesday</option><option>Wednesday</option><option>Thursday</option></select></label>
<label class="full">Activities of interest<input placeholder="e.g. yoga, bingo, crafts, planting"></label>
<label>Emergency contact name &amp; relationship *<input required></label><label>Emergency contact phone *<input type="tel" required></label>
<label class="full">Dietary needs / food allergies<input></label>
<label class="full">Mobility or health needs (optional)<textarea rows="2"></textarea></label>

<label>Photo/video consent<select><option>Yes, I consent</option><option>No</option></select></label>
<label class="full">How did you hear about us?<input></label>
<label class="full" style="flex-direction:row;align-items:center;gap:8px"><input type="checkbox" required> I agree to the <a href="maas-place-waiver.html" target="_blank">participation waiver</a>.</label>
<div class="full"><button class="btn">Submit Enrollment</button> <span class="ph">Form not connected yet – submission destination to be decided</span></div></form></div></section>
<section id="volunteer"><div class="wrap"><h2>Volunteer at the Senior Center</h2>
<p>Share a skill, lead an activity, or simply sit and talk.</p>
<div class="grid"><div class="card"><h3>Lead an activity</h3><p>Yoga, crafts, games, planting, karaoke.</p></div><div class="card"><h3>Share expertise</h3><p>Health, insurance, phone and tech help.</p></div><div class="card"><h3>Serve &amp; connect</h3><p>Snacks, chai, conversation and companionship.</p></div></div>
<p style="margin-top:24px"><a class="btn" href="{VOL}">Sign Up to Volunteer</a></p></div></section>
{donate("the Senior Center")}
<section id="contact"><div class="wrap"><h2>Contact &amp; FAQ</h2>
<p>📧 <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a> · 📍 <a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75007" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75007</a> · 📞 <a href="tel:+14692708156">(469) 270-8156</a></p>
<details><summary>Who can attend the Senior Center?</summary><p>Adults 55 and up</p></details>
<details><summary>Where is the Senior Center?</summary><p><a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75007" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75007</a></p></details>
<details><summary>What are your hours?</summary><p>Monday to Thursday, 10 AM to 2 PM.</p></details>
<details><summary>Is there a cost?</summary><p>No. The Senior Center is free.</p></details>
<details><summary>Do you provide transportation?</summary><p>No, transportation is not provided.</p></details>
<details><summary>Are snacks provided?</summary><p>Yes, homestyle snacks and chai. Tell us about any allergies on the enrollment form.</p></details>
<details><summary>How do I volunteer?</summary><p>Sign up on our <a href="{VOL}">volunteer page</a> and we'll reach out to get you started.</p></details>
<div style="margin-top:20px;border-radius:14px;overflow:hidden"><iframe title="Map to the Senior Center" src="https://www.google.com/maps?q=2700+Old+Denton+Rd+Suite+102,+Carrollton,+TX+75007&output=embed" width="100%" height="320" style="border:0" loading="lazy"></iframe></div>
</div></section>
'''+foot.replace('<h4>Follow Us</h4>','<h4>Senior Center</h4><p class="footer-description">2700 Old Denton Rd, Suite 102, Carrollton, TX 75007<br><a href="tel:+14692708156" style="color:inherit">(469) 270-8156</a><br><a href="mailto:aslam@maasinspiration.org" style="color:inherit">aslam@maasinspiration.org</a></p><h4 style="margin-top:1rem">Follow Us</h4>')
import bv_page
bsv=bv_page.page(head,foot,DON,'https://maasinspiration.org/thank-you.html')
pg=head("Our Programs").replace('<main class="mi">','<main class="mi purple">')+f'''<header class="hero" style="--img:url(gallery/2026-10-10-service-03.jpg)"><p class="eyebrow">Under the MAA's Inspiration umbrella</p><h1>Our Programs</h1><p>Beyond our weekly meal service, MAA's Inspiration cares for our community through the Senior Center and Bloom Village.</p></header>
<section><div class="wrap"><div class="grid">
<div class="card"><img class="pc-img" src="gallery/maas-meals-volunteers.jpg" alt="Maa's Meals volunteers"><h3>🍲 Maa's Meals</h3><p>2,200 fresh meals every Saturday for seniors, the homeless and shelter homes across DFW.</p><a class="btn" href="meals.html">See Schedule</a></div>
<div class="card purple-card"><img class="pc-img" src="gallery/maas-place-seniors-painting.jpg" alt="Seniors painting at the Senior Center"><h3>🏡 Senior Center</h3><p><span class="soon-badge sm">Opening soon</span> Activities, snacks, chai and companionship for seniors. Ages 55+. Monday to Thursday, 10 AM to 2 PM.</p><a class="btn" href="maas-place.html">Visit the Senior Center</a></div>
<div class="card"><h3>🌸 Bloom Village</h3><p><span class="soon-badge sm">Licensing pending</span> Adult enrichment for adults 18+ with intellectual and developmental disabilities. Mon–Fri, 9 AM–1 PM. Begins after HHSC license is issued.</p><a class="btn" href="bloom-village.html">Learn More</a></div>
</div></div></section>
<section style="text-align:center"><div class="wrap"><h2>Ready to help?</h2><p>Donate, volunteer or see schedules for any program in one place.</p><a class="btn" href="get-involved.html">Get Involved</a></div></section>
{donate("our programs")}
'''+foot
ty=head('Thank You').replace('<main class="mi">','<main class="mi purple">')+'''<section style="text-align:center;min-height:50vh"><div class="wrap"><h1>Thank you! 💚</h1><p id="tymsg">We received your form and will reach out soon. Questions? Email <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a>.</p><p><a class="btn" href="https://maasinspiration.org/">Back to Home</a></p></div></section><script>if(location.search.includes("error"))document.getElementById("tymsg").innerHTML="Sorry, something went wrong sending your form. Please email <a href=mailto:aslam@maasinspiration.org>aslam@maasinspiration.org</a>."</script>'''+foot

hub=head("Get Involved").replace('<main class="mi">','<main class="mi hub purple">')+f'''<header class="hero" style="--img:url(gallery/2026-10-10-service-04.jpg)"><p class="eyebrow">MAA's Inspiration</p><h1>Get Involved</h1><p>Choose a program, then donate, volunteer, or see when it happens.</p></header>
<section><div class="wrap">
<div class="psel" role="tablist">
<button role="tab" data-p="meals" class="p-meals">🍲<b>Maa's Meals</b></button>
<button role="tab" data-p="maas-place" class="p-mp">🏡<b>Senior Center</b><small>Opening soon · 55+</small></button>
<button role="tab" data-p="bsv" class="p-bsv">🌸<b>Bloom Village</b><small>Licensing pending · 18+</small></button>
</div>
<div id="panel" class="panel">
<img id="pimg" class="pc-img" src="gallery/maas-meals-volunteers.jpg" alt=""><h2 id="pname"></h2><p id="pdesc"></p>
<div class="acts">
<a id="actDonate" class="act" href="{DON}">💜<b>Donate</b><small>Secure checkout via our donation page</small></a>
<a class="act" href="#vol">🙌<b>Volunteer</b><small>Sign up in 1 minute</small></a>
<a class="act" href="#when">🗓️<b>Schedule</b><small>See when we meet</small></a>
</div>
<div id="when"><h3>Schedule</h3><div class="tw"><table><thead><tr><th>Day</th><th>Time</th><th>What</th></tr></thead><tbody id="hsched"></tbody></table></div><p id="pmore"></p></div>
<div id="vol"><h3>Volunteer sign-up</h3><p>Takes about a minute.</p>
'''+open('vol_form.html').read()+'''</div>
</div></div></section>
'''+foot.replace('<script src="section.js"></script>','<script src="section.js"></script><script src="vol-form.js"></script><script src="hub.js"></script>')

pol=head("Volunteer Policies").replace('<main class="mi">','<main class="mi purple">')+'''<header class="hero"><h1>Volunteer Policies</h1><p>Photo consent and code of conduct for MAA's Inspiration volunteers.</p></header>
<section id="consent"><div class="wrap"><h2>Photo &amp; Video Consent</h2><ul>
<li>We take photos and videos at meal service, the Senior Center and events to share our work on our website and social media (Facebook, Instagram, TikTok).</li>
<li>Ticking the photo consent box means MAA's Inspiration may use photos/videos that include you for these purposes, without payment. We never sell images.</li>
<li>With your permission we may use your first name only. We never post phone numbers, addresses or other private details.</li>
<li>Consent is optional – you can still volunteer without it. You can withdraw consent any time by emailing <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a>; we will stop using new images and remove posts we control where possible.</li>
<li>Seniors and participants are only filmed with their own written consent. Volunteers must not post photos of seniors, guests or meal recipients on personal accounts.</li></ul></div></section>
<section id="conduct"><div class="wrap"><h2>Volunteer Code of Conduct</h2><ul>
<li><b>Dignity first:</b> treat every guest, senior, family and fellow volunteer with kindness and respect – Love All, Serve All.</li>
<li><b>Show up:</b> arrive on time, check in and check out with the shift lead, and let us know early if you can't make it.</li>
<li><b>Food safety:</b> wash hands, wear gloves and hair covering in the kitchen, and follow the lead's instructions.</li>
<li><b>Privacy:</b> keep guests' personal information private; no photos of guests without consent.</li>
<li><b>Safety:</b> no alcohol, drugs, smoking or weapons at any site; drivers must have a valid license and insurance.</li>
<li><b>No harassment or discrimination</b> of any kind. Minors volunteer only with guardian approval and adult supervision.</li>
<li><b>Ask for help:</b> report any concern or injury to the shift lead or Aslam right away.</li></ul>
<p>Questions? <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a></p></div></section>
'''+foot
open('volunteer-policy.html','w').write(pol)
hub=hub.replace('</head>','<link rel="stylesheet" href="vol-form.css"></head>',1)

VOLP=head("Volunteer").replace('<main class="mi">','<main class="mi purple volp">').replace('</head>','<link rel="stylesheet" href="vol-form.css"></head>',1)+'''<header class="hero vhero"><h1>Volunteer with us</h1><p>Give a few hours, share a smile, and help feed and care for our neighbors in Dallas–Fort Worth. No experience needed.</p><a class="btn alt" href="#signup">Sign up</a></header>
<section><div class="wrap"><h2>Where you can help</h2><div class="vcards">
<div class="vcard"><span class="vt open">✅ Open now</span><h3>🍲 Maa's Meals</h3><p><b>Saturdays only</b> 10 AM – noon<br>Packing &amp; delivery</p><small>📍 1445 MacArthur Dr, Suite 104, Carrollton</small></div>
<div class="vcard"><span class="vt soon">Opening soon</span><h3>🏡 Senior Center</h3><p><b>Mon – Thu</b> 10 AM – 2 PM<br>Activities, exercise, tech help, snacks &amp; chai, companionship</p><small>📍 2700 Old Denton Rd, Suite 102, Carrollton, TX 75007</small></div>
<div class="vcard"><span class="vt soon">Licensing pending</span><h3>🌸 Bloom Village</h3><p><b>Mon – Fri</b> 9 AM – 1 PM<br>Adult enrichment for adults 18+ with I/DD: arts, music, games, gardening, life skills. Volunteers 18+, screening &amp; training required. Begins after HHSC license is issued.</p><small>📍 2700 Old Denton Rd, Suite 102, Carrollton, TX 75007 · <a href="bloom-village.html#volunteer">Bloom Village volunteer form</a></small></div>
</div></div></section>
<section id="signup" class="vsign"><div class="wrap"><h2>Volunteer sign-up</h2><p class="vsub">Takes about a minute.</p>
'''+open('vol_form.html').read()+'''</div></section>
'''+foot.replace('<script src="section.js"></script>','<script src="vol-form.js"></script>')
open('volunteer-page.html','w').write(VOLP)
for n,h in [('get-involved.html',hub),('thank-you.html',ty),('maas-place.html',mp),('bloom-village.html',bsv),('programs.html',pg)]:open(n,'w').write(h)
open('index.html','w').write('<!DOCTYPE html><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=site-preview/index.html"><a href="site-preview/index.html">Site preview</a>')

# --- form wiring: name attributes, honeypot, action ---
import re as _re
def _wire(fn,formname):
    h=open(fn).read()
    def nm(m):
        lab=_re.sub(r'<[^>]+>|\*','',m.group(1)).strip()
        slug=_re.sub(r'[^a-z0-9]+','_',lab.lower()).strip('_')[:40] or 'field'
        return m.group(0).replace('<'+m.group(2),'<'+m.group(2)+f' name="{slug}"',1)
    h=_re.sub(r'<label[^>]*>([^<]*(?:<[^>]+>[^<]*)*?)<(input|select|textarea)(?![^>]*name=)',nm,h)
    h=h.replace('<select name="days_you_plan_to_attend" multiple','<select name="days_you_plan_to_attend[]" multiple')
    h=h.replace('<form id="enroll">',f'<form id="enroll" method="post" action="enroll.php"><input type="hidden" name="form" value="{formname}"><div style="position:absolute;left:-9999px" aria-hidden="true"><label>Leave blank<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>')
    h=h.replace('<span class="ph">Form not connected yet – submission destination to be decided</span>','').replace('<span class="ph">Form not connected yet</span>','')
    for a,b in [('name="field"','name="agree_waiver" value="Yes"'),('email_optional','email'),('_amp_','_'),('senior_s_','senior_'),('participant_s_','participant_'),('anything_you_d_like_us_to_know_needs_com','notes')]: h=h.replace(a,b)
    open(fn,'w').write(h)
_wire('maas-place.html',"Senior Center enrollment")

# --- Design variants of the Senior Center (same content, different layouts) ---
d1=mp.replace('<main class="mi purple">','<main class="mi purple d1">').replace("<title>Senior Center","<title>Design 1 Classic – Senior Center")
d2=mp.replace('<main class="mi purple">','<main class="mi purple d2">').replace("<title>Senior Center","<title>Design 2 Magazine – Senior Center")
d2=d2.replace('<header class="hero" style="--img:url(gallery/maas-place-seniors-painting.jpg)">','<header class="hero split"><div class="split-text">',1)
d2=d2.replace('</header>','</div><div class="split-img"><img src="gallery/maas-place-seniors-painting.jpg" alt="Seniors painting together at the Senior Center"></div></header>',1)
for sid,img in [('what','04'),('visit','05'),('volunteer','03')]:
    d2=d2.replace(f'<section id="{sid}"><div class="wrap">',f'<section id="{sid}" class="row"><div class="wrap"><img class="row-img" src="gallery/2026-10-10-service-{img}.jpg" alt=""><div class="row-body">',1)
import re as _r
for sid in ['what','visit','volunteer']:
    i=d2.find(f'<section id="{sid}" class="row">'); j=d2.find('</div></section>',i)
    d2=d2[:j]+'</div>'+d2[j:]
d2=d2.replace('</main>','<aside class="side-cta"><a class="btn alt" href="donate.html?program=maas-place">💜 Donate</a><a class="btn green" href="volunteer.html">🙌 Volunteer</a><a class="btn" href="tel:+14692708156">📞 Call</a></aside></main>',1)
d3=mp.replace('<main class="mi purple">','<main class="mi purple d3">').replace("<title>Senior Center","<title>Design 3 App – Senior Center")
i=d3.find('<header class="hero"'); j=d3.find('</header>',i)+9
d3=d3[:i]+'''<header class="appbar"><div><h1>Senior Center</h1><p class="tagline">Place where everybody knows your name</p><p class="meta">Mon–Thu · 10 AM–2 PM · Ages 55+ · Free</p></div></header>
<nav class="tiles"><a href="#visit" data-tab="visit">📍<b>Visit</b></a><a href="#schedule" data-tab="schedule">🗓️<b>Schedule</b></a><a href="#volunteer" data-tab="volunteer">🙌<b>Volunteer</b></a><a href="donate.html?program=maas-place" class="gold">💜<b>Donate</b></a><a href="tel:+14692708156" class="green">📞<b>Call</b></a></nav>
<div class="apptabs" role="tablist"><button data-tab="what">What we do</button><button data-tab="schedule">Schedule</button><button data-tab="gallery">Gallery</button><button data-tab="visit">Visit / Enroll</button><button data-tab="volunteer">Volunteer</button><button data-tab="contact">FAQ</button></div>'''+d3[j:]
_s=d3.find('<div class="sub">'); _e=d3.find('</div>',_s)+6; d3=d3[:_s]+d3[_e:]
d3=d3.replace('<script src="section.js"></script>','<script src="section.js"></script><script src="design3.js"></script>')
for n,h in [('maas-place-design-1.html',d1),('maas-place-design-2.html',d2),('maas-place-design-3.html',d3)]:open(n,'w').write(h)

# --- Final main page: Design 2 + app tiles in hero ---
TILES='''<nav class="tiles hero-tiles"><a href="#visit">📍<b>Visit</b></a><a href="#schedule">🗓️<b>Schedule</b></a><a href="#volunteer">🙌<b>Volunteer</b></a><a href="donate.html?program=maas-place" class="gold">💜<b>Donate</b></a><a href="tel:+14692708156" class="green">📞<b>Call</b></a></nav>'''
main=d2.replace("<title>Design 2 Magazine – Senior Center","<title>Senior Center")
main=main.replace('<p class="tagline">Place where everybody knows your name</p>','<p class="tagline">Place where everybody knows your name</p>\n'+TILES,1)
main=_r.sub(r'<a class="btn alt" href="#visit">Plan a Visit</a> &nbsp; <a class="btn ghost"[^>]*>Volunteer</a>','',main,1)
open('maas-place.html','w').write(main)

# --- Proposed new front page (home.html) ---
def _pcard(title,img,desc,facts,href,key,badge=''):
    return f'''<div class="pcard">{'<span class="ribbon">'+badge+'</span>' if badge else ''}
<a class="pmain" href="{href}"><img src="gallery/{img}" alt="{title}"><div class="pbody"><h2>{title}</h2><p>{desc}</p><p class="pfacts">{facts}</p><span class="btn">Learn more →</span></div></a>
<div class="pquick"><a class="q-donate" href="get-involved.html#{key}">💜 Donate</a><a class="q-vol" href="get-involved.html#{key}">🙌 Volunteer</a></div></div>'''
home=head("Home").replace('<main class="mi">','<main class="mi purple home">')+'''<header class="hero home-hero"><h1>Serving with love. Feeding with dignity.</h1><p>Three ways MAA's Inspiration cares for our Dallas–Fort Worth community. Tap a program to learn more.</p></header>
<section><div class="wrap"><div class="pgrid">'''+_pcard("Maa's Meals","maas-meals-volunteers.jpg","Fresh, hot meals cooked, packed and delivered by our volunteers.","✅ Open now · 2,200 fresh meals every Saturday","meals.html","meals")+_pcard("Senior Center","maas-place-seniors-painting.jpg","A free senior center for activities, snacks, chai and friendship.","Opening soon · Mon–Thu 10 AM–2 PM · Ages 55+","maas-place.html","maas-place","Coming Soon")+_pcard("Bloom Village","2026-10-10-service-05.jpg","Adult enrichment for adults 18+ with intellectual and developmental disabilities. Meaningful Days. Meaningful Lives.","Licensing pending with HHSC · Mon–Fri · 9 AM–1 PM · Carrollton","bloom-village.html","bsv","Licensing Pending")+'''</div></div></section>
<section class="donate"><div class="wrap"><h2>Every meal, every smile, every visit</h2><p>Your gift keeps all three programs going.</p><a class="btn alt" href="donate.html">Donate Now</a> &nbsp; <a class="btn green" href="get-involved.html">Get Involved</a></div></section>
'''+foot
open('home.html','w').write(home)
sp=home
for a,b in [('href="site-chrome.css"','href="../site-chrome.css"'),('href="section.css"','href="../section.css"'),('src="img/','src="../img/'),('src="gallery/','src="../gallery/'),('href="maas-place.html"','href="../maas-place.html"'),('href="bloom-village.html"','href="../bloom-village.html"'),('href="get-involved.html','href="../get-involved.html'),('src="section.js"','src="../section.js"'),('href="programs.html"','href="../programs.html"')]: sp=sp.replace(a,b)
sp=sp.replace('href="https://maasinspiration.org/">Home','href="index.html">Home').replace('href="about.html"','href="about.html"').replace('href="volunteer.html">Volunteer</a></li>','href="volunteer.html">Volunteer</a></li>')
import os; os.makedirs('site-preview',exist_ok=True); open('site-preview/index-new.html','w').write(sp)

_wire('maas-place.html',"Senior Center enrollment")



# ---- Senior Center waiver ----
WV=head("Senior Center Participation Waiver").replace('<main class="mi">','<main class="mi purple waiver">').replace('</head>','''<style>
.mi.waiver .wv{max-width:820px;margin:0 auto;background:#fff;border-radius:14px;border-top:6px solid #5B2A86;padding:32px;box-shadow:0 2px 10px rgba(0,0,0,.06);line-height:1.6}
.mi.waiver .wv h1{color:#3D1A6E;font-size:1.9rem;margin:0 0 12px}.mi.waiver .wv h2{color:#3D1A6E;font-size:1.1rem;margin:22px 0 6px}
.mi.waiver .release{font-weight:800;text-transform:uppercase;border:3px solid #3D1A6E;padding:14px;background:#F6F1FB}
.mi.waiver .box{font-size:1.2rem;margin-right:6px}.mi.waiver .sig{display:grid;grid-template-columns:2fr 2fr 1fr;gap:18px;margin-top:22px}
.mi.waiver .sig div{border-bottom:1.5px solid #2E2438;padding-top:34px;font-size:.85rem;color:#6b5f7a}
.mi.waiver .pbar{text-align:center;margin:20px 0}
@media(max-width:640px){.mi.waiver .wv{padding:20px}.mi.waiver .sig{grid-template-columns:1fr}}
@media print{nav,footer,.preview-banner,.pbar,.sticky,.stickybar,#lb,body>div:first-child[style*="C0392B"]{display:none!important}body,.mi{background:#fff!important}.mi.waiver .wv{box-shadow:none;border:0;padding:0;max-width:none}.mi.waiver section{padding:0!important}}
</style></head>''',1)+'''<section><div class="wrap"><div class="wv">
<h1>Senior Center Participation Waiver and Release</h1>
<p>The Senior Center is a free center for seniors operated by MAA's Inspiration Inc., a 501(c)(3) nonprofit located at 2700 Old Denton Rd, Suite 102, Carrollton, TX 75007.</p>
<h2>1. Voluntary participation.</h2><p>I am choosing to take part in Senior Center activities, which may include light exercise, chair yoga, walks, games, arts and crafts, outings, and meals or snacks. I understand that participation is voluntary and that I may stop at any time.</p>
<h2>2. Health and fitness.</h2><p>I confirm that I am able to take part in these activities. I will consult my doctor if I have any doubts, and I will tell staff about any health, mobility, or dietary needs. I understand that the Senior Center does not provide medical care, supervision for memory care, or transportation.</p>
<h2>3. Risks.</h2><p>I understand that physical activities and outings carry some risk of injury, including falls, strains, and illness. I accept these risks.</p>
<h2>4. RELEASE OF LIABILITY.</h2><p class="release">I RELEASE MAA'S INSPIRATION INC., ITS DIRECTORS, VOLUNTEERS, AND STAFF FROM ANY CLAIMS FOR INJURY, ILLNESS, OR LOSS ARISING FROM MY PARTICIPATION, INCLUDING CLAIMS ARISING FROM THEIR OWN NEGLIGENCE, TO THE FULLEST EXTENT ALLOWED BY TEXAS LAW.</p>
<h2>5. Emergencies.</h2><p>In an emergency, I authorize staff to call 911 and contact my emergency contact. I am responsible for any resulting medical costs.</p>
<h2>6. Food.</h2><p>I will tell staff about any food allergies. Food may be prepared in a kitchen that also handles common allergens.</p>
<h2>7. Photo and video consent (optional).</h2><p><span class="box">☐</span> Yes, MAA's Inspiration may use photos and videos of me on its website and social media.<br><span class="box">☐</span> No, please do not include me in photos or videos.</p><p>I may withdraw consent at any time by emailing aslam@maasinspiration.org.</p>
<h2>8. Signature.</h2><p>I have read and understand this waiver.</p>
<div class="sig"><div>Participant name</div><div>Signature</div><div>Date</div></div>
<div class="sig"><div>Signed by family member / guardian on participant's behalf (if applicable)</div><div>Relationship</div><div>Date</div></div>
<p class="pbar"><button class="btn" onclick="window.print()">🖨️ Print this waiver</button> &nbsp; <a class="btn green" href="maas-place.html#visit">Back to the Senior Center</a></p>
</div></div></section>
'''+foot
open('maas-place-waiver.html','w').write(WV)

# ---- Contact ----
MAP=lambda q:'https://www.google.com/maps/search/?api=1&query='+q
CT=head("Contact Us").replace('<main class="mi">','<main class="mi purple contactp">').replace('</head>','<link rel="stylesheet" href="vol-form.css"><style>.mi.contactp{background:#F3EBDD}.mi.contactp .hero{text-align:center;background:#F3EBDD!important;color:#3D1A6E;padding:56px 20px 24px}.mi.contactp .hero p{max-width:640px;margin:8px auto 0}.ccards{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}.ccard{background:#fff;border-radius:14px;border-top:5px solid #5B2A86;padding:22px;box-shadow:0 2px 8px rgba(0,0,0,.06)}.ccard h3{color:#3D1A6E;margin:0 0 8px}.ccard p{margin:6px 0}.ccard a{color:#5B2A86;font-weight:700}.social{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}.social a{background:#5B2A86;color:#fff;border-radius:30px;padding:10px 20px;font-weight:700;text-decoration:none}.np{text-align:center;color:#6b5f7a;font-size:.9rem;margin-top:18px}.mi.contactp h2{text-align:center;color:#3D1A6E}</style></head>',1)+f'''<header class="hero"><h1>Contact Us</h1><p>We'd love to hear from you, whether you want to volunteer, donate, partner with us, or learn more about our programs.</p></header>
<section><div class="wrap"><div class="ccards">
<div class="ccard"><h3>📍 Main Office &amp; Maa's Meals</h3><p>1445 MacArthur Drive, Suite 104<br>Carrollton, TX 75007</p><p><b>Maa's Meals:</b> Saturdays, 10 AM – 12 PM</p><p><a href="{MAP('1445+MacArthur+Drive+Suite+104+Carrollton+TX+75007')}" target="_blank" rel="noopener">Get directions →</a></p></div>
<div class="ccard"><h3>🏡 Senior Center &amp; 🌸 Bloom Village</h3><p>2700 Old Denton Rd, Suite 102<br>Carrollton, TX 75007</p><p><b>Senior Center:</b> Monday – Thursday, 10 AM – 2 PM (opening soon)</p><p><b>Bloom Village:</b> Monday – Friday, 9 AM – 1 PM (licensing pending with HHSC; services begin after the license is issued)</p><p><a href="{MAP('2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75007')}" target="_blank" rel="noopener">Get directions →</a></p></div>
<div class="ccard"><h3>📞 Phone &amp; ✉️ Email</h3><p><b>Phone:</b> <a href="tel:+14692708156">(469) 270-8156</a></p><p><b>Email:</b> <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a></p></div>
</div></div></section>
<section><div class="wrap"><h2>Send us a message</h2><div class="lvf-wrap"><form class="lvf" id="contactForm" action="https://formsubmit.co/aslamhemani@gmail.com" method="POST">
<input type="hidden" name="_subject" value="New Contact Message — MAA's Inspiration"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<div class="form-row"><div class="form-group"><label>Name <span class="req">*</span></label><input type="text" name="Name" required autocomplete="name"></div><div class="form-group"><label>Email <span class="req">*</span></label><input type="email" name="Email" required autocomplete="email"></div></div>
<div class="form-row"><div class="form-group"><label>Phone <small>(optional)</small></label><input type="tel" name="Phone" autocomplete="tel"></div><div class="form-group"><label>I'm interested in</label><select name="Interested In"><option>Volunteering</option><option>Donating</option><option>Partnering</option><option>Senior Center</option><option>Bloom Village</option><option>Other</option></select></div></div>
<div class="form-row"><div class="form-group full"><label>Message <span class="req">*</span></label><textarea name="Message" required></textarea></div></div>
<p class="err" id="cErr" hidden></p><button type="submit" class="submit-btn">Send Message</button></form></div></div></section>
<section><div class="wrap"><h2>Follow us</h2><div class="social"><a href="https://www.facebook.com/maasinspiration" target="_blank" rel="noopener"><i class="fab fa-facebook-f"></i> Facebook</a><a href="https://www.instagram.com/maasinspiration/" target="_blank" rel="noopener"><i class="fab fa-instagram"></i> Instagram</a><a href="https://www.tiktok.com/@maasinspiration" target="_blank" rel="noopener"><i class="fab fa-tiktok"></i> TikTok</a></div>
<p class="np">MAA's Inspiration Inc. is a registered 501(c)(3) nonprofit · EIN 86-2221897</p></div></section>
<script>(function(){{var f=document.getElementById('contactForm');f.addEventListener('submit',async function(e){{e.preventDefault();var b=f.querySelector('.submit-btn'),er=document.getElementById('cErr');b.disabled=true;b.textContent='Sending…';try{{var r=await fetch('https://formsubmit.co/ajax/aslamhemani@gmail.com',{{method:'POST',headers:{{Accept:'application/json'}},body:new FormData(f)}});var j=await r.json().catch(function(){{return{{}}}});if(r.ok&&(j.success===true||j.success==='true')){{location.href='thank-you.html';return}}er.textContent='Submission issue: '+(j.message||('HTTP '+r.status))+'. Please email aslam@maasinspiration.org.'}}catch(x){{er.textContent='Network error – please try again or email aslam@maasinspiration.org.'}}er.hidden=false;b.disabled=false;b.textContent='Send Message'}})}})();</script>
'''+foot
open('contact.html','w').write(CT)

# ---- Legal + SMS pages (for Twilio A2P compliance) ----
LEGAL='<div class="footer-bottom" style="padding-top:0"><a href="privacy.html" style="color:inherit">Privacy Policy</a> · <a href="terms.html" style="color:inherit">Terms &amp; Conditions</a> · <a href="sms-signup.html" style="color:inherit">Text updates</a></div>'
PV=head("Privacy Policy").replace('<main class="mi">','<main class="mi purple">')+'''<header class="hero"><h1>Privacy Policy</h1><p>How Maa's Inspiration Inc. collects and uses your information.</p></header>
<section><div class="wrap">
<p>This Privacy Policy applies to Maa's Inspiration Inc., a 501(c)(3) nonprofit (EIN 86-2221897) in Carrollton, Texas, including our Maa's Meals program, Senior Center and Bloom Village.</p>
<h2>What data we collect</h2><ul><li>Name</li><li>Phone number</li><li>Email address</li><li>Address (for meal delivery)</li></ul>
<h2>How we use it</h2><ul><li>Volunteer scheduling, including shift and route reminders</li><li>Meal delivery notices to meal recipients</li><li>Answering questions you send us</li></ul>
<h2>Text messages (SMS)</h2>
<p>If you opt in to text messages from Maa's Inspiration Inc., we use your phone number only to send the messages described in our <a href="terms.html">Terms &amp; Conditions</a>. You can reply STOP at any time to opt out, or HELP for help.</p>
<p><b>We do not sell or share your SMS opt-in data or personal information with third parties for marketing purposes.</b></p>
<h2>Keeping your data safe</h2><p>Only authorized Maa's Inspiration staff and volunteers can see your information, and only what they need for their role.</p>
<h2>Contact us</h2><p>Maa's Inspiration Inc., Carrollton, TX · <a href="tel:+14692708156">(469) 270-8156</a> · <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a></p>
</div></section>
'''+foot
open('privacy.html','w').write(PV)
TM=head("Terms & Conditions").replace('<main class="mi">','<main class="mi purple">')+'''<header class="hero"><h1>Terms &amp; Conditions</h1><p>Terms for using the Maa's Inspiration Inc. website and text messages.</p></header>
<section><div class="wrap">
<p>These terms apply to the website and services of Maa's Inspiration Inc., a 501(c)(3) nonprofit in Carrollton, Texas.</p>
<h2 id="sms">SMS Terms</h2><ul>
<li><b>Brand:</b> Maa's Inspiration Inc. (Maa's Meals)</li>
<li><b>Message types:</b> volunteer shift and route reminders, and meal delivery notices.</li>
<li><b>Frequency:</b> message frequency varies.</li>
<li>Message and data rates may apply.</li>
<li><b>Opt out:</b> reply STOP to any message to opt out. You will get one confirmation and no further messages.</li>
<li><b>Help:</b> reply HELP for help.</li>
<li><b>Contact:</b> <a href="tel:+14692708156">(469) 270-8156</a> or <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a></li>
<li>Carriers are not liable for delayed or undelivered messages.</li>
<li>Consent to receive texts is not a condition of volunteering or receiving meals.</li></ul>
<p>See our <a href="privacy.html">Privacy Policy</a> for how we handle your information.</p>
</div></section>
'''+foot
open('terms.html','w').write(TM)
SS=head("Get Text Updates").replace('<main class="mi">','<main class="mi purple">').replace('</head>','<link rel="stylesheet" href="vol-form.css"></head>',1)+'''<header class="hero"><h1>Get text updates from Maa's Meals</h1><p>Volunteer shift reminders and meal delivery notices from Maa's Inspiration Inc.</p></header>
<section><div class="wrap"><div class="lvf-wrap"><form class="lvf" id="smsForm" action="https://formsubmit.co/aslamhemani@gmail.com" method="POST">
<input type="hidden" name="_subject" value="New SMS Opt-in — Maa's Meals"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="https://maasinspiration.org/thank-you.html"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<div class="form-row"><div class="form-group"><label>Name <span class="req">*</span></label><input type="text" name="Name" required autocomplete="name"></div><div class="form-group"><label>Mobile phone <span class="req">*</span></label><input type="tel" name="Phone" required autocomplete="tel"></div></div>
<div class="form-row"><div class="form-group"><label>I am a <span class="req">*</span></label><select name="Role" required><option value="">Choose…</option><option>Volunteer</option><option>Recipient</option></select></div></div>
<div class="form-row"><div class="form-group full"><label style="font-weight:400"><input type="checkbox" name="SMS Consent" value="Yes" required> I agree to receive text messages from Maa's Inspiration Inc. about volunteer shifts and meal deliveries. Msg frequency varies. Msg &amp; data rates may apply. Reply STOP to opt out, HELP for help.</label>
<p><small>See our <a href="privacy.html">Privacy Policy</a> and <a href="terms.html">Terms &amp; Conditions</a>.</small></p></div></div>
<button type="submit" class="submit-btn">Sign up for texts</button></form></div></div></section>
'''+foot
open('sms-signup.html','w').write(SS)
