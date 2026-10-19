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
mp=head("Maa’s Place").replace('<main class="mi">','<main class="mi purple">')+f'''<div class="sub"><a href="#what">What We Do</a><a href="#schedule">Schedule</a><a href="#gallery">Gallery</a><a href="#visit">Visit / Enroll</a><a href="#volunteer">Volunteer</a><a href="#donate">Donate</a><a href="#contact">Contact &amp; FAQ</a><a href="get-involved.html#maas-place">Get Involved</a></div>
<header class="hero" style="--img:url(gallery/maas-place-seniors-painting.jpg)"><p class="eyebrow">Programs · MAA's Inspiration</p><span class="soon-badge">🌱 Opening soon</span>
<h1>Maa’s Place</h1>
<p class="tagline">Place where everybody knows your name</p>
<p class="soon-line">The Maa’s Place is opening soon. Join the interest list below and we'll let you know when doors open.</p>
<p>A warm, welcoming place where seniors in Dallas–Fort Worth gather for activities, homestyle snacks, chai and companionship, carried forward in the spirit of Maa, whose greatest joy was feeding others.</p>
<div class="facts"><div>🕙 Monday to Thursday, 10 AM to 2 PM</div><div>👵 Ages 55+</div><div>📞 <a href="tel:+14692708156" style="color:#fff">(469) 270-8156</a></div><div>📍 <a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75007" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75007</a></div></div>
<a class="btn alt" href="#visit">Plan a Visit</a> &nbsp; <a class="btn ghost" href="{VOL}" style="color:#fff">Volunteer</a></header>
<section id="what"><div class="wrap"><h2>What We Do</h2><p>Every activity at the Maa’s Place is chosen to keep seniors active in body and mind, from gentle exercise and brain games to arts, music, and learning something new. Just as important, it’s a place to share laughter, snacks, and friendship, where every senior feels valued and no one is alone.</p>
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
<section id="gallery"><div class="wrap"><h2>Photo Gallery</h2><p class="soon-line">Photos coming soon. The Maa’s Place opens its doors shortly!</p></div></section>
<section id="visit"><div class="wrap"><h2>Visit or Enroll <span class="soon-badge sm">Opening soon</span></h2>
<div class="grid"><div class="card"><h3>1. Come say hello</h3><p>Drop in Monday to Thursday, 10 AM to 2 PM, call <a href="tel:+14692708156">(469) 270-8156</a>, or email <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a> to schedule a tour.</p></div>
<div class="card"><h3>2. Sign up</h3><p><a href="form-maas-place.html">Sign up online</a> on one short page; family members can fill it out on a senior's behalf.</p></div>
<div class="card"><h3>3. One agreement covers it</h3><p>Signing up includes our <a href="maas-place-terms.html">Maa’s Place Terms, Policies &amp; Waiver</a>: the participation waiver, emergency care, texts, photos and video. There are no separate consent forms. You can opt out of texts or photos anytime by replying STOP or calling <a href="tel:+14692708156">(469) 270-8156</a>.</p></div></div>
<p style="margin-top:18px">Who can attend: Adults 55 and up · Cost: Free · Transportation: not provided</p>
<div id="enroll" class="mp-enroll" style="margin-top:22px;text-align:center"><h3>Sign up online</h3><p>The Maa’s Place is opening soon. Sign up now on one short page and we'll contact you when it opens. A family member can fill it out for you.</p>
<p><a class="btn" href="form-maas-place.html" style="display:inline-block;font-size:1.25rem;padding:18px 34px;min-width:260px">Sign up for Maa’s Place →</a></p>
<p style="font-size:.95rem">Need help? Call <a href="tel:+14692708156">(469) 270-8156</a>.</p></div></div></section>
<section id="volunteer"><div class="wrap"><h2>Volunteer at the Maa’s Place</h2>
<p>Share a skill, lead an activity, or simply sit and talk.</p>
<div class="grid"><div class="card"><h3>Lead an activity</h3><p>Yoga, crafts, games, planting, karaoke.</p></div><div class="card"><h3>Share expertise</h3><p>Health, insurance, phone and tech help.</p></div><div class="card"><h3>Serve &amp; connect</h3><p>Snacks, chai, conversation and companionship.</p></div></div>
<p style="margin-top:24px"><a class="btn" href="{VOL}">Sign Up to Volunteer</a></p></div></section>
{donate("the Maa’s Place")}
<section id="contact"><div class="wrap"><h2>Contact &amp; FAQ</h2>
<p>📧 <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a> · 📍 <a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75007" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75007</a> · 📞 <a href="tel:+14692708156">(469) 270-8156</a></p>
<details><summary>Who can attend the Maa’s Place?</summary><p>Adults 55 and up</p></details>
<details><summary>Where is the Maa’s Place?</summary><p><a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75007" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75007</a></p></details>
<details><summary>What are your hours?</summary><p>Monday to Thursday, 10 AM to 2 PM.</p></details>
<details><summary>Is there a cost?</summary><p>No. The Maa’s Place is free.</p></details>
<details><summary>Do you provide transportation?</summary><p>No, transportation is not provided.</p></details>
<details><summary>Are snacks provided?</summary><p>Yes, homestyle snacks and chai. Please tell staff about any food allergies.</p></details>
<details><summary>How do I volunteer?</summary><p>Sign up on our <a href="{VOL}">volunteer page</a> and we'll reach out to get you started.</p></details>
<div style="margin-top:20px;border-radius:14px;overflow:hidden"><iframe title="Map to the Maa’s Place" src="https://www.google.com/maps?q=2700+Old+Denton+Rd+Suite+102,+Carrollton,+TX+75007&output=embed" width="100%" height="320" style="border:0" loading="lazy"></iframe></div>
</div></section>
'''+foot.replace('<h4>Follow Us</h4>','<h4>Maa’s Place</h4><p class="footer-description">2700 Old Denton Rd, Suite 102, Carrollton, TX 75007<br><a href="tel:+14692708156" style="color:inherit">(469) 270-8156</a><br><a href="mailto:aslam@maasinspiration.org" style="color:inherit">aslam@maasinspiration.org</a></p><h4 style="margin-top:1rem">Follow Us</h4>')
import bv_page
bsv=bv_page.page(head,foot,DON,'https://maasinspiration.org/thank-you.html')
pg=head("Our Programs").replace('<main class="mi">','<main class="mi purple">')+f'''<header class="hero" style="--img:url(gallery/2026-10-10-service-03.jpg)"><p class="eyebrow">Under the MAA's Inspiration umbrella</p><h1>Our Programs</h1><p>Beyond our weekly meal service, MAA's Inspiration cares for our community through the Maa’s Place and Bloom Village.</p></header>
<section><div class="wrap"><div class="grid">
<div class="card"><img class="pc-img" src="gallery/maas-meals-volunteers.jpg" alt="Maa's Meals volunteers"><h3>🍲 Maa's Meals</h3><p>2,200 fresh meals every Saturday for seniors, the homeless and shelter homes across DFW.</p><a class="btn" href="meals.html">See Schedule</a></div>
<div class="card purple-card"><img class="pc-img" src="gallery/maas-place-seniors-painting.jpg" alt="Seniors painting at the Maa’s Place"><h3>🏡 Maa’s Place</h3><p><span class="soon-badge sm">Opening soon</span> Activities, snacks, chai and companionship for seniors. Ages 55+. Monday to Thursday, 10 AM to 2 PM.</p><a class="btn" href="maas-place.html">Visit the Maa’s Place</a></div>
<div class="card bv-card"><img class="pc-img" src="img/bv-art.jpg" alt="A Bloom Village member with Down syndrome painting with staff"><h3>🌸 Bloom Village</h3><p><span class="soon-badge sm bv">Licensing pending</span> Adult enrichment for adults 18+ with intellectual and developmental disabilities. 9 AM–1 PM; 2–3 days/week pilot, then Mon–Fri. Begins after HHSC license is issued.</p><a class="btn" href="bloom-village.html">Learn More</a></div>
</div></div></section>
<section style="text-align:center"><div class="wrap"><h2>Ready to help?</h2><p>Donate, volunteer or see schedules for any program in one place.</p><a class="btn" href="get-involved.html">Get Involved</a> &nbsp; <a class="btn alt" href="forms.html">Forms</a></div></section>
{donate("our programs")}
'''+foot
ty=head('Thank You').replace('<main class="mi">','<main class="mi purple">')+'''<section style="text-align:center;min-height:50vh"><div class="wrap"><h1>Thank you! 💚</h1><p id="tymsg">We received your form and will reach out soon. Questions? Email <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a>.</p><p><a class="btn" href="https://maasinspiration.org/">Back to Home</a></p></div></section><script>if(location.search.includes("error"))document.getElementById("tymsg").innerHTML="Sorry, something went wrong sending your form. Please email <a href=mailto:aslam@maasinspiration.org>aslam@maasinspiration.org</a>."</script>'''+foot

hub=head("Get Involved").replace('<main class="mi">','<main class="mi hub purple">')+f'''<header class="hero" style="--img:url(gallery/2026-10-10-service-04.jpg)"><p class="eyebrow">MAA's Inspiration</p><h1>Get Involved</h1><p>Choose a program, then donate, volunteer, or see when it happens.</p></header>
<section><div class="wrap">
<div class="psel" role="tablist">
<button role="tab" data-p="meals" class="p-meals">🍲<b>Maa's Meals</b></button>
<button role="tab" data-p="maas-place" class="p-mp">🏡<b>Maa’s Place</b><small>Opening soon · 55+</small></button>
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
<div id="vol"><h3>Volunteer sign-up</h3>
'''+open('vol_form.html').read()+'''</div>
</div></div></section>
'''+foot.replace('<script src="section.js"></script>','<script src="section.js"></script><script src="hub.js"></script>')

pol=head("Volunteer Policies").replace('<main class="mi">','<main class="mi purple">')+'''<header class="hero"><h1>Volunteer Policies</h1><p>Texts, photos, video and code of conduct for MAA's Inspiration volunteers.</p></header>
<section id="consent"><div class="wrap"><h2>Texts, Photos &amp; Video</h2><ul>
<li>By signing up and agreeing to our <a href="volunteer-terms.html">Volunteer Terms, Policies &amp; Waiver</a>, you agree to receive informational texts from Maa's Inspiration Inc. about volunteering, deliveries and programs. Message frequency varies. Message and data rates may apply. Reply STOP to opt out and HELP for help. Consent is not a condition of volunteering.</li>
<li>We take photos and videos at meal service, Maa’s Place and events and may use them on our website, social media and materials, without payment. We never sell images, use first names only, and never post phone numbers, addresses or other private details.</li>
<li>If you do not want to be photographed or featured, tell us at <a href="tel:+14692708156">(469) 270-8156</a> or <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a> and we will honor it, and remove posts we control where possible.</li>
<li>Volunteers must not post photos of seniors, guests or meal recipients on personal accounts.</li></ul></div></section>
<section id="conduct"><div class="wrap"><h2>Volunteer Code of Conduct</h2><ul>
<li><b>Dignity first:</b> treat every guest, senior, family and fellow volunteer with kindness and respect – Love All, Serve All.</li>
<li><b>Show up:</b> arrive on time, check in and check out with the shift lead, and let us know early if you can't make it.</li>
<li><b>Food safety:</b> wash hands, wear gloves and hair covering in the kitchen, and follow the lead's instructions.</li>
<li><b>Privacy:</b> keep guests' personal information private. Do not take personal photos of guests; take photos only when Maa’s asks, and never of anyone who has opted out.</li>
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
<div class="vcard"><span class="vt soon">Opening soon</span><h3>🏡 Maa’s Place</h3><p><b>Mon – Thu</b> 10 AM – 2 PM<br>Activities, exercise, tech help, snacks &amp; chai, companionship</p><small>📍 2700 Old Denton Rd, Suite 102, Carrollton, TX 75007</small></div>
<div class="vcard bv-card"><span class="vt soon bv">Licensing pending</span><h3>🌸 Bloom Village</h3><p><b>Mon – Fri</b> 9 AM – 1 PM<br>Adult enrichment for adults 18+ with I/DD: arts, music, games, gardening, life skills. Volunteers 18+, screening &amp; training required. Begins after HHSC license is issued.</p><small>📍 2700 Old Denton Rd, Suite 102, Carrollton, TX 75007 · <a href="bloom-village.html#volunteer">Bloom Village volunteer form</a></small></div>
</div></div></section>
<section id="signup" class="vsign"><div class="wrap"><h2>Volunteer sign-up</h2>
'''+open('vol_form.html').read()+'''</div></section>
<section id="forms"><div class="wrap"><h2>Volunteer forms</h2><div class="vcards">
<a class="vcard" href="form-driver.html" style="text-decoration:none;color:inherit"><h3>🚗 Volunteer Driver Agreement</h3><p>For Maa's Meals delivery drivers (18+). One short page.</p></a>
</div><p><a href="forms.html">See all forms</a></p></div></section>
'''+foot
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
    h=h.replace('<span class="ph">Form not connected yet – submission destination to be decided</span>','').replace('<span class="ph">Form not connected yet</span>','')
    for a,b in [('name="field"','name="agree_waiver" value="Yes"'),('email_optional','email'),('_amp_','_'),('senior_s_','senior_'),('participant_s_','participant_'),('anything_you_d_like_us_to_know_needs_com','notes')]: h=h.replace(a,b)
    open(fn,'w').write(h)
_wire('maas-place.html',"Maa’s Place enrollment")

# --- Design variants of the Maa’s Place (same content, different layouts) ---
d1=mp.replace('<main class="mi purple">','<main class="mi purple d1">').replace("<title>Maa’s Place","<title>Design 1 Classic – Maa’s Place")
d2=mp.replace('<main class="mi purple">','<main class="mi purple d2">').replace("<title>Maa’s Place","<title>Design 2 Magazine – Maa’s Place")
d2=d2.replace('<header class="hero" style="--img:url(gallery/maas-place-seniors-painting.jpg)">','<header class="hero split"><div class="split-text">',1)
d2=d2.replace('</header>','</div><div class="split-img"><img src="gallery/maas-place-seniors-painting.jpg" alt="Seniors painting together at the Maa’s Place"></div></header>',1)
for sid,img in [('what','04'),('visit','05'),('volunteer','03')]:
    d2=d2.replace(f'<section id="{sid}"><div class="wrap">',f'<section id="{sid}" class="row"><div class="wrap"><img class="row-img" src="gallery/2026-10-10-service-{img}.jpg" alt=""><div class="row-body">',1)
import re as _r
for sid in ['what','visit','volunteer']:
    i=d2.find(f'<section id="{sid}" class="row">'); j=d2.find('</div></section>',i)
    d2=d2[:j]+'</div>'+d2[j:]
d2=d2.replace('</main>','<aside class="side-cta"><a class="btn alt" href="donate.html?program=maas-place">💜 Donate</a><a class="btn green" href="volunteer.html">🙌 Volunteer</a><a class="btn" href="tel:+14692708156">📞 Call</a></aside></main>',1)
d3=mp.replace('<main class="mi purple">','<main class="mi purple d3">').replace("<title>Maa’s Place","<title>Design 3 App – Maa’s Place")
i=d3.find('<header class="hero"'); j=d3.find('</header>',i)+9
d3=d3[:i]+'''<header class="appbar"><div><h1>Maa’s Place</h1><p class="tagline">Place where everybody knows your name</p><p class="meta">Mon–Thu · 10 AM–2 PM · Ages 55+ · Free</p></div></header>
<nav class="tiles"><a href="#visit" data-tab="visit">📍<b>Visit</b></a><a href="#schedule" data-tab="schedule">🗓️<b>Schedule</b></a><a href="#volunteer" data-tab="volunteer">🙌<b>Volunteer</b></a><a href="donate.html?program=maas-place" class="gold">💜<b>Donate</b></a><a href="tel:+14692708156" class="green">📞<b>Call</b></a></nav>
<div class="apptabs" role="tablist"><button data-tab="what">What we do</button><button data-tab="schedule">Schedule</button><button data-tab="gallery">Gallery</button><button data-tab="visit">Visit / Enroll</button><button data-tab="volunteer">Volunteer</button><button data-tab="contact">FAQ</button></div>'''+d3[j:]
_s=d3.find('<div class="sub">'); _e=d3.find('</div>',_s)+6; d3=d3[:_s]+d3[_e:]
d3=d3.replace('<script src="section.js"></script>','<script src="section.js"></script><script src="design3.js"></script>')
for n,h in [('maas-place-design-1.html',d1),('maas-place-design-2.html',d2),('maas-place-design-3.html',d3)]:open(n,'w').write(h)

# --- Final main page: Design 2 + app tiles in hero ---
TILES='''<nav class="tiles hero-tiles"><a href="#visit">📍<b>Visit</b></a><a href="#schedule">🗓️<b>Schedule</b></a><a href="#volunteer">🙌<b>Volunteer</b></a><a href="donate.html?program=maas-place" class="gold">💜<b>Donate</b></a><a href="tel:+14692708156" class="green">📞<b>Call</b></a></nav>'''
main=d2.replace("<title>Design 2 Magazine – Maa’s Place","<title>Maa’s Place")
main=main.replace('<p class="tagline">Place where everybody knows your name</p>','<p class="tagline">Place where everybody knows your name</p>\n'+TILES,1)
main=_r.sub(r'<a class="btn alt" href="#visit">Plan a Visit</a> &nbsp; <a class="btn ghost"[^>]*>Volunteer</a>','',main,1)
open('maas-place.html','w').write(main)

# --- Proposed new front page (home.html) ---
def _pcard(title,img,desc,facts,href,key,badge=''):
    return f'''<div class="pcard pc-{key}">{'<span class="ribbon">'+badge+'</span>' if badge else ''}
<a class="pmain" href="{href}"><img src="{img if "/" in img else "gallery/"+img}" alt="{title}"><div class="pbody"><h2>{title}</h2><p>{desc}</p><p class="pfacts">{facts}</p><span class="btn">Learn more →</span></div></a>
<div class="pquick"><a class="q-donate" href="get-involved.html#{key}">💜 Donate</a><a class="q-vol" href="get-involved.html#{key}">🙌 Volunteer</a></div></div>'''
home=head("Home").replace('<main class="mi">','<main class="mi purple home">')+'''<header class="hero home-hero"><h1>Serving with love. Feeding with dignity.</h1><p>Three ways MAA's Inspiration cares for our Dallas–Fort Worth community. Tap a program to learn more.</p></header>
<section><div class="wrap"><div class="pgrid">'''+_pcard("Maa's Meals","maas-meals-volunteers.jpg","Fresh, hot meals cooked, packed and delivered by our volunteers.","✅ Open now · 2,200 fresh meals every Saturday","meals.html","meals")+_pcard("Maa’s Place","maas-place-seniors-painting.jpg","A free senior center for activities, snacks, chai and friendship.","Opening soon · Mon–Thu 10 AM–2 PM · Ages 55+","maas-place.html","maas-place","Coming Soon")+_pcard("Bloom Village","img/bv-art.jpg","Adult enrichment for adults 18+ with intellectual and developmental disabilities. Meaningful Days. Meaningful Lives.","Licensing pending with HHSC · Mon–Fri · 9 AM–1 PM · Carrollton","bloom-village.html","bsv","Licensing Pending")+'''</div></div></section>
<section class="donate"><div class="wrap"><h2>Every meal, every smile, every visit</h2><p>Your gift keeps all three programs going.</p><a class="btn alt" href="donate.html">Donate Now</a> &nbsp; <a class="btn green" href="get-involved.html">Get Involved</a></div></section>
'''+foot
open('home.html','w').write(home)
sp=home
for a,b in [('href="site-chrome.css"','href="../site-chrome.css"'),('href="section.css"','href="../section.css"'),('src="img/','src="../img/'),('src="gallery/','src="../gallery/'),('href="maas-place.html"','href="../maas-place.html"'),('href="bloom-village.html"','href="../bloom-village.html"'),('href="get-involved.html','href="../get-involved.html'),('src="section.js"','src="../section.js"'),('href="programs.html"','href="../programs.html"')]: sp=sp.replace(a,b)
sp=sp.replace('href="https://maasinspiration.org/">Home','href="index.html">Home').replace('href="about.html"','href="about.html"').replace('href="volunteer.html">Volunteer</a></li>','href="volunteer.html">Volunteer</a></li>')
import os; os.makedirs('site-preview',exist_ok=True); open('site-preview/index-new.html','w').write(sp)

_wire('maas-place.html',"Maa’s Place enrollment")



# ---- Maa’s Place waiver ----
WV='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Maa’s Place Terms, Policies &amp; Waiver – Maa’s Inspiration</title><link rel="canonical" href="maas-place-terms.html"><meta http-equiv="refresh" content="0; url=maas-place-terms.html"><script>location.replace("maas-place-terms.html")</script></head><body><p>The Maa’s Place waiver is now part of the <a href="maas-place-terms.html">Maa’s Place Terms, Policies &amp; Waiver</a>.</p></body></html>'
open('maas-place-waiver.html','w').write(WV)

# ---- Contact ----
MAP=lambda q:'https://www.google.com/maps/search/?api=1&query='+q
CT=head("Contact Us").replace('<main class="mi">','<main class="mi purple contactp">').replace('</head>','<link rel="stylesheet" href="vol-form.css"><style>.mi.contactp{background:#F3EBDD}.mi.contactp .hero{text-align:center;background:#F3EBDD!important;color:#3D1A6E;padding:56px 20px 24px}.mi.contactp .hero p{max-width:640px;margin:8px auto 0}.ccards{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}.ccard{background:#fff;border-radius:14px;border-top:5px solid #5B2A86;padding:22px;box-shadow:0 2px 8px rgba(0,0,0,.06)}.ccard h3{color:#3D1A6E;margin:0 0 8px}.ccard p{margin:6px 0}.ccard a{color:#5B2A86;font-weight:700}.social{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}.social a{background:#5B2A86;color:#fff;border-radius:30px;padding:10px 20px;font-weight:700;text-decoration:none}.np{text-align:center;color:#6b5f7a;font-size:.9rem;margin-top:18px}.mi.contactp h2{text-align:center;color:#3D1A6E}</style></head>',1)+f'''<header class="hero"><h1>Contact Us</h1><p>We'd love to hear from you, whether you want to volunteer, donate, partner with us, or learn more about our programs.</p></header>
<section><div class="wrap"><div class="ccards">
<div class="ccard"><h3>📍 Main Office &amp; Maa's Meals</h3><p>1445 MacArthur Drive, Suite 104<br>Carrollton, TX 75007</p><p><b>Maa's Meals:</b> Saturdays, 10 AM – 12 PM</p><p><a href="{MAP('1445+MacArthur+Drive+Suite+104+Carrollton+TX+75007')}" target="_blank" rel="noopener">Get directions →</a></p></div>
<div class="ccard"><h3>🏡 Maa’s Place &amp; 🌸 Bloom Village</h3><p>2700 Old Denton Rd, Suite 102<br>Carrollton, TX 75007</p><p><b>Maa’s Place:</b> Monday – Thursday, 10 AM – 2 PM (opening soon)</p><p><b>Bloom Village:</b> Monday – Friday, 9 AM – 1 PM (licensing pending with HHSC; services begin after the license is issued)</p><p><a href="{MAP('2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75007')}" target="_blank" rel="noopener">Get directions →</a></p></div>
<div class="ccard"><h3>📞 Phone &amp; ✉️ Email</h3><p><b>Phone:</b> <a href="tel:+14692708156">(469) 270-8156</a></p><p><b>Email:</b> <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a></p></div>
</div></div></section>
<section><div class="wrap"><h2>Send us a message</h2><div class="lvf-wrap"><form class="lvf" id="contactForm" data-mi-type="contact" novalidate>
<div style="position:absolute;left:-9999px" aria-hidden="true"><label>Leave blank<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<div class="form-row"><div class="form-group"><label for="c_name">Name <span class="req">*</span></label><input id="c_name" type="text" name="name" required autocomplete="name"></div><div class="form-group"><label for="c_phone">Phone <small>(optional)</small></label><input id="c_phone" type="tel" name="phone" autocomplete="tel" inputmode="tel"></div></div>
<div class="form-row"><div class="form-group"><label for="c_email">Email <small>(optional)</small></label><input id="c_email" type="email" name="email" autocomplete="email"></div><div class="form-group"><label for="c_prog">I'm interested in</label><select id="c_prog" name="program"><option>Volunteering</option><option>Donating</option><option>Partnering</option><option>Maa’s Meals</option><option>Maa’s Place</option><option>Bloom Village</option><option>Other</option></select></div></div>
<div class="form-row"><div class="form-group full"><label for="c_msg">Message <span class="req">*</span></label><textarea id="c_msg" name="message" required></textarea></div></div>
<p class="np" style="text-align:left;margin:0 0 10px">Please give a phone or email so we can reply. Please don’t include health or financial details. See our <a href="privacy.html">Privacy Policy</a>.</p>
<button type="submit" class="submit-btn">Send Message</button></form></div></div></section>
<section><div class="wrap"><h2>Follow us</h2><div class="social"><a href="https://www.facebook.com/maasinspiration" target="_blank" rel="noopener"><i class="fab fa-facebook-f"></i> Facebook</a><a href="https://www.instagram.com/maasinspiration/" target="_blank" rel="noopener"><i class="fab fa-instagram"></i> Instagram</a><a href="https://www.tiktok.com/@maasinspiration" target="_blank" rel="noopener"><i class="fab fa-tiktok"></i> TikTok</a></div>
<p class="np">MAA's Inspiration Inc. is a registered 501(c)(3) nonprofit · EIN 86-2221897</p></div></section>
<script src="forms-config.js"></script><script src="mi-post.js"></script>
<script>(function(){{var f=document.getElementById('contactForm');f.addEventListener('submit',function(e){{var p=f.phone.value.trim(),m=f.email.value.trim();f.phone.setCustomValidity(p||m?'':'Please give a phone number or email so we can reply.');}},true);f.phone.addEventListener('input',function(){{f.phone.setCustomValidity('')}});f.email.addEventListener('input',function(){{f.phone.setCustomValidity('')}});}})();</script>
'''+foot
open('contact.html','w').write(CT)

# ---- Legal + SMS pages (for Twilio A2P compliance) ----
LEGAL='<div class="footer-bottom" style="padding-top:0"><a href="privacy.html" style="color:inherit">Privacy Policy</a> · <a href="terms.html" style="color:inherit">Terms of Use</a> · <a href="text-terms.html" style="color:inherit">Text message terms</a></div>'
LDRAFT='<p style="background:#fff;border:3px dashed #5B2A86;color:#5B2A86;text-align:center;font-weight:700;padding:10px 14px;margin:0">DRAFT – pending attorney review</p>'
LCSS='<style>.mi.legal section{padding:28px 5% 40px}.mi.legal .wrap{max-width:760px;font-size:1.1rem;line-height:1.6}.mi.legal h2{font-size:1.35rem;margin-top:1.6rem}.mi.legal ul{padding-left:1.2em}.mi.legal li{margin-bottom:.5rem}.mi.legal .hero{padding:40px 5% 28px}</style>'
CONTACT_L='<p>Maa\'s Inspiration Inc.<br>2700 Old Denton Rd, Suite 102<br>Carrollton, TX 75007<br>Phone: <a href="tel:+14692708156">(469) 270-8156</a><br>Email: <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a></p>'
PV=head("Privacy Policy").replace('<main class="mi">','<main class="mi purple legal">').replace('</head>',LCSS+'</head>',1)+LDRAFT+'''<header class="hero"><h1>Privacy Policy</h1><p>How Maa's Inspiration Inc. collects, uses and protects your information. Last updated October 19, 2026.</p></header>
<section><div class="wrap">
<p>This policy covers Maa's Inspiration Inc., a 501(c)(3) nonprofit (EIN 86-2221897) in Carrollton, Texas, and its programs: Maa's Meals, Maa's Place and Bloom Village.</p>
<h2>1. What we collect</h2><ul>
<li><b>Forms you send us:</b> your name, phone, email, address and anything you type in a form, such as delivery notes or a complaint.</li>
<li><b>Volunteers:</b> contact details, which programs you help with, and your agreement to our volunteer and driver terms.</li>
<li><b>Meal recipients:</b> name, address, phone and delivery notes.</li>
<li><b>Bloom Village families:</b> the participant's and guardian's names, phone and program days. Health and other private details are collected in person, not on this website.</li>
<li><b>Donations:</b> online gifts are processed by Stripe. Stripe handles your card details; we never see or store your full card number. We receive your name, email, amount and date.</li>
<li><b>Delivery door photos:</b> volunteer drivers take one photo at each stop showing only the meal at the door and the house number. These photos are deleted after 7 days.</li></ul>
<h2>2. How we use it</h2><ul>
<li>To run our programs: deliver meals, schedule volunteers, enroll participants and answer your questions.</li>
<li>To send receipts and thank-you notes for donations.</li>
<li>To keep records the law requires, such as signed agreements and licensing records.</li></ul>
<h2>3. We do not sell your information</h2>
<p>We never sell, rent or trade your personal information.</p>
<p><b>No mobile information will be shared with third parties or affiliates for marketing or promotional purposes. Text messaging originator opt-in data and consent will not be shared with any third parties.</b></p>
<p>We share information only with service providers who help us run our programs (for example our secure database, text message and payment providers), and only as needed; with the volunteer driver assigned to a meal delivery (name, address, phone and delivery notes, for that delivery only); with a participant's emergency contact or family if the person is hurt, ill or we are worried about their safety; or when the law requires it.</p>
<h2 id="sms">4. Text messages (SMS)</h2><ul>
<li><b>How you agree:</b> when you give us your phone number on one of our forms and agree to that form's terms, you agree to receive informational texts from Maa's Inspiration Inc. about volunteering, deliveries and programs.</li>
<li>Message frequency varies. Message and data rates may apply.</li>
<li>Reply <b>STOP</b> at any time to opt out. Reply <b>HELP</b> for help, or call (469) 270-8156.</li>
<li>Consent to texts is not a condition of receiving services or volunteering. See our <a href="text-terms.html">Text Message Terms</a>.</li></ul>
<h2>5. Donor confidentiality</h2>
<p>Donor names, amounts and contact details are kept confidential. We do not publish a donor's name without permission, and we never sell or share donor lists.</p>
<h2>6. Photos and videos</h2><ul>
<li>Our program terms explain that Maa's may take photos and video at programs and events and use them on its website, social media and materials. We use first names only.</li>
<li>If you do not want to be photographed or featured, call (469) 270-8156 or email aslam@maasinspiration.org at any time, and we will honor it.</li>
<li>Bloom Village participants appear publicly only with their guardian's agreement under the Bloom Village terms. The guardian can opt out at any time.</li>
<li>Delivery door photos are for delivery confirmation only. They are never published and are deleted after 7 days.</li></ul>
<h2>7. Keeping your information safe</h2>
<p>Only authorized staff and volunteers can see your information, and only what they need for their role. We use secure, password-protected systems. No system is perfectly secure, so please call us if you think something is wrong.</p>
<h2>8. Children</h2>
<p>This website is not for children. We do not knowingly collect information from children under 13. Bloom Village serves adults 18 and older.</p>
<h2>9. Your choices</h2>
<p>You may ask to see, correct or delete your information, or stop texts or emails, by contacting us. Some records must be kept by law.</p>
<h2>10. Changes to this policy</h2>
<p>We may update this policy. The date at the top shows the latest version.</p>
<h2>11. Contact us</h2>'''+CONTACT_L+'''
</div></section>
'''+foot
open('privacy.html','w').write(PV)
TM=head("Terms of Use").replace('<main class="mi">','<main class="mi purple legal">').replace('</head>',LCSS+'</head>',1)+LDRAFT+'''<header class="hero"><h1>Terms of Use</h1><p>The rules for using the Maa's Inspiration Inc. website. Last updated October 19, 2026.</p></header>
<section><div class="wrap">
<h2>1. Using this website</h2>
<p>By using this website you agree to these terms. Please use it only for lawful purposes, give true information in our forms, and do not try to harm or misuse the site.</p>
<h2>2. Donations</h2><ul>
<li>Online donations are processed securely by Stripe.</li>
<li>Maa's Inspiration Inc. is a 501(c)(3) nonprofit (EIN 86-2221897). Donations are tax-deductible to the extent allowed by law. No goods or services are provided in exchange for your donation.</li>
<li>If you made a donation by mistake, contact us within 30 days to ask for a refund. Refunds are given at Maa's Inspiration Inc.'s discretion.</li></ul>
<h2>3. Program information</h2>
<p>Program details, such as hours, locations, fees and opening dates, may change. Please call us to confirm before you visit. Each program also has its own terms, which you agree to when you sign its form.</p>
<h2>4. No medical advice</h2>
<p>Information on this website is general and is not medical, legal or financial advice. Talk to your doctor or another professional about your own needs.</p>
<h2>5. Links to other websites</h2>
<p>Our site links to other websites, such as Stripe, Facebook and Instagram. We are not responsible for their content or privacy practices.</p>
<h2 id="sms">6. Text messages</h2>
<p>We send informational texts to people who give us their phone number and agree to the terms of one of our forms. You can opt out anytime. Message frequency varies. Message and data rates may apply. Reply STOP to opt out or HELP for help. Carriers are not liable for delayed or undelivered messages. See our <a href="text-terms.html">Text Message Terms</a> and <a href="privacy.html#sms">Privacy Policy</a>.</p>
<h2>7. Limitation of liability</h2>
<p>This website is provided "as is." To the extent allowed by law, Maa's Inspiration Inc., its volunteers, board and partners are not liable for any loss or damage from using this website or relying on its content.</p>
<h2>8. Texas law</h2>
<p>These terms are governed by the laws of the State of Texas.</p>
<h2>9. Changes</h2>
<p>We may update these terms. The date at the top shows the latest version.</p>
<h2>10. Contact us</h2>'''+CONTACT_L+'''
</div></section>
'''+foot
open('terms.html','w').write(TM)
SS='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Text Message Terms – Maa’s Inspiration</title><link rel="canonical" href="text-terms.html"><meta http-equiv="refresh" content="0; url=text-terms.html"><script>location.replace("text-terms.html")</script></head><body><p>Text messages are now covered by the terms of each program. See our <a href="text-terms.html">Text Message Terms</a>.</p></body></html>'
open('sms-signup.html','w').write(SS)

# ---- Online forms (Draft v3) ----
import forms_pages
forms_pages.build(head,foot)
