# Regenerates the 3 pages. Run: python3 build.py   (PREVIEW=0 python3 build.py for live build without banner/noindex)
import os,re
P=os.environ.get('PREVIEW','1')=='1'
B='https://maasinspiration.org/'
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
            <a href="{B}" class="logo-section">
                <img src="img/site-logo.png" alt="MAA's Inspiration Logo">
                <span class="logo-text">MAA's Inspiration</span>
            </a>
            <ul class="nav-links" id="navLinks">
                <li><a href="{B}">Home</a></li>
                <li><a href="{B}about.html">About</a></li>
                <li><a href="{B}volunteer.html">Volunteer</a></li>
                <li><a href="{B}schedule.html">Schedule</a></li>
                <li><a href="{B}gallery.html">Gallery</a></li>
                <li><a href="programs.html">Programs</a></li>
                <li><a href="{B}meals.html#contact">Contact</a></li>
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
                    <li><a href="{B}">Home</a></li>
                    <li><a href="{B}about.html">About</a></li>
                    <li><a href="{B}volunteer.html">Volunteer</a></li>
                    <li><a href="{B}schedule.html">Schedule</a></li>
                    <li><a href="{B}gallery.html">Gallery</a></li>
                    <li><a href="{B}meals.html#contact">Contact</a></li>
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
mp=head("Maa's Place Senior Center").replace('<main class="mi">','<main class="mi purple">')+f'''<div class="sub"><a href="#what">What We Do</a><a href="#schedule">Schedule</a><a href="#gallery">Gallery</a><a href="#visit">Visit / Enroll</a><a href="#volunteer">Volunteer</a><a href="#donate">Donate</a><a href="#contact">Contact &amp; FAQ</a><a href="get-involved.html#maas-place">Get Involved</a></div>
<header class="hero" style="--img:url(gallery/maas-place-seniors-painting.jpg)"><p class="eyebrow">Programs · MAA's Inspiration</p><span class="soon-badge">🌱 Opening soon</span>
<h1>Maa's Place Senior Center</h1>
<p class="tagline">Place where everybody knows your name</p>
<p class="soon-line">Maa's Place is opening soon. Join the interest list below and we'll let you know when doors open.</p>
<p>A warm, welcoming place where seniors in Dallas–Fort Worth gather for activities, homestyle snacks, chai and companionship, carried forward in the spirit of Maa, whose greatest joy was feeding others.</p>
<div class="facts"><div>🕙 Monday to Thursday, 10 AM to 2 PM</div><div>👵 Ages 55+</div><div>📞 <a href="tel:+12145171938" style="color:#fff">214-517-1938</a></div><div>📍 <a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75006" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75006</a></div></div>
<a class="btn alt" href="#visit">Plan a Visit</a> &nbsp; <a class="btn ghost" href="{VOL}" style="color:#fff">Volunteer</a></header>
<section id="what"><div class="wrap"><h2>What We Do</h2><p>Every activity at Maa’s Place is chosen to keep seniors active in body and mind, from gentle exercise and brain games to arts, music, and learning something new. Just as important, it’s a place to share laughter, snacks, and friendship, where every senior feels valued and no one is alone.</p>
<div class="grid">
<div class="card"><h3>💪 Physical</h3><ul class="ticks"><li>Chair exercises and gentle stretching</li><li>Balance and fall-prevention exercises</li><li>Group walks</li><li>Light dance and movement to music</li><li>Chair yoga or tai chi</li><li>Fun movement games (balloon toss, bean bag games)</li><li>Healthy snacks</li><li>Health checks and wellness talks</li></ul></div>
<div class="card"><h3>🧠 Mental</h3><ul class="ticks"><li>Puzzles, word games, and trivia</li><li>Memory and brain-training games</li><li>Reading and storytelling circles</li><li>Learning sessions (technology, health talks, new skills)</li><li>Music, singing, and sing-alongs</li><li>Arts and crafts for creativity and focus</li><li>Group discussions and sharing life stories</li><li>Bingo, cards, and board games</li></ul></div>
<div class="card"><h3>📚 Educational</h3><ul class="ticks"><li>Smartphone, tablet, and video-call help (staying in touch with family)</li><li>Health, nutrition, and medication-safety talks</li><li>Scam and fraud awareness</li><li>Guest speakers from the community</li><li>Cooking and healthy-eating demonstrations</li><li>Language and conversation classes</li><li>Gardening and nature sessions</li><li>Cultural and history discussions</li></ul></div>
<div class="card"><h3>🎲 Fun &amp; Entertainment</h3><ul class="ticks"><li>Bingo, cards, and board games</li><li>Movie and music afternoons</li><li>Sing-alongs and karaoke</li><li>Birthday celebrations</li><li>Holiday and cultural festivals</li><li>Talent shows and storytelling</li><li>Outings and field trips</li><li>Tea, snacks, and social hours</li></ul></div>
<div class="card"><h3>🍵 Snacks &amp; Chai</h3><ul class="ticks"><li>Light snacks</li><li>Tea and coffee</li><li>Fresh fruit</li><li>Special treats for birthdays and holidays</li><li>Prepared with care for senior dietary needs</li></ul></div>
</div></div></section>
<section id="schedule"><div class="wrap"><h2>Weekly Schedule of Activities</h2>
<p>Open: <b id="weekOf">…</b> · <span id="schedNote" class="ph"></span></p>
<div class="tw"><table><thead id="schedHead"></thead><tbody id="sched"><tr><td>Loading…</td></tr></tbody></table></div></div></section>
<section id="gallery"><div class="wrap"><h2>Photo Gallery</h2><p>A look at what's happening this week. {ph("Maa's Place photos of consenting seniors to be added")}</p><div class="gal" id="gal" data-program="maas-place"></div></div></section>
<section id="visit"><div class="wrap"><h2>Visit or Enroll <span class="soon-badge sm">Opening soon</span></h2>
<div class="grid"><div class="card"><h3>1. Come say hello</h3><p>Drop in Monday to Thursday, 10 AM to 2 PM, call <a href="tel:+12145171938">214-517-1938</a>, or email <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a> to schedule a tour.</p></div>
<div class="card"><h3>2. Enroll</h3><p>Complete the short form below; family members can fill it out on a senior's behalf.</p></div>
<div class="card"><h3>3. Sign the waiver</h3><p>Sign our participation waiver and optional photo/video consent on your first visit.</p></div></div>
<p style="margin-top:18px">Who can attend: Adults 55 and up · Cost: Free · Transportation: not provided</p>
<h3>Enrollment / Interest Form</h3><p>Maa's Place is opening soon – sign up now and we'll contact you when it opens.</p>
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
<label class="full" style="flex-direction:row;align-items:center;gap:8px"><input type="checkbox" required> I agree to the participation waiver.</label>
<div class="full"><button class="btn">Submit Enrollment</button> <span class="ph">Form not connected yet – submission destination to be decided</span></div></form></div></section>
<section id="volunteer"><div class="wrap"><h2>Volunteer at Maa's Place</h2>
<p>Share a skill, lead an activity, or simply sit and talk.</p>
<div class="grid"><div class="card"><h3>Lead an activity</h3><p>Yoga, crafts, games, planting, karaoke.</p></div><div class="card"><h3>Share expertise</h3><p>Health, insurance, phone and tech help.</p></div><div class="card"><h3>Serve &amp; connect</h3><p>Snacks, chai, conversation and companionship.</p></div></div>
<p style="margin-top:24px"><a class="btn" href="{VOL}">Sign Up to Volunteer</a></p></div></section>
{donate("Maa's Place")}
<section id="contact"><div class="wrap"><h2>Contact &amp; FAQ</h2>
<p>📧 <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a> · 📍 <a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75006" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75006</a> · 📞 <a href="tel:+12145171938">214-517-1938</a></p>
<details><summary>Who can attend Maa's Place?</summary><p>Adults 55 and up</p></details>
<details><summary>Where is Maa's Place?</summary><p><a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75006" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75006</a></p></details>
<details><summary>What are your hours?</summary><p>Monday to Thursday, 10 AM to 2 PM.</p></details>
<details><summary>Is there a cost?</summary><p>No. Maa's Place is free.</p></details>
<details><summary>Do you provide transportation?</summary><p>No, transportation is not provided.</p></details>
<details><summary>Are snacks provided?</summary><p>Yes, homestyle snacks and chai. Tell us about any allergies on the enrollment form.</p></details>
<details><summary>How do I volunteer?</summary><p>Sign up on our <a href="{VOL}">volunteer page</a> and we'll reach out to get you started.</p></details>
<div style="margin-top:20px;border-radius:14px;overflow:hidden"><iframe title="Map to Maa's Place" src="https://www.google.com/maps?q=2700+Old+Denton+Rd+Suite+102,+Carrollton,+TX+75006&output=embed" width="100%" height="320" style="border:0" loading="lazy"></iframe></div>
</div></section>
'''+foot.replace('<h4>Follow Us</h4>','<h4>Maa\'s Place</h4><p class="footer-description">2700 Old Denton Rd, Suite 102, Carrollton, TX 75006<br><a href="tel:+12145171938" style="color:inherit">214-517-1938</a><br><a href="mailto:aslam@maasinspiration.org" style="color:inherit">aslam@maasinspiration.org</a></p><h4 style="margin-top:1rem">Follow Us</h4>')
bsv=head("Blooming Star Village").replace('<main class="mi">','<main class="mi purple bsvp">')+f'''<div class="sub"><a href="#mission">Mission</a><a href="#serve">Who We Serve</a><a href="#programs">Activities</a><a href="#visit">Your Visit</a><a href="#schedule">Schedule</a><a href="#enroll">Get Involved</a><a href="#volunteer">Volunteer</a><a href="#donate">Donate</a><a href="#faq">FAQ</a><a href="get-involved.html#bsv">Get Involved</a></div>
<header class="hero" style="--img:url(gallery/bsv-girl-at-desk.jpg)"><p class="eyebrow">Programs · MAA's Inspiration · Coming soon</p>
<h1>Blooming Star Village</h1><p>A free, caring day program where children with sensory, developmental and other special needs can play, learn and belong, and their families can find support.</p>
<div class="facts"><div>📍 <a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75006" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75006</a></div><div>🧒 Ages: {ph("Ages served")}</div><div>🕙 Mon – Thu, 9 AM – 2 PM</div><div>💛 Free</div></div>
<a class="btn alt" href="#enroll">Join the Interest List</a> &nbsp; <a class="btn ghost" href="{VOL}" style="color:#fff">Volunteer</a></header>
<section id="mission"><div class="wrap"><h2>Our Mission</h2><p>Every person deserves a place where they are understood, included and helped to grow. A free day program for recreation and care, Blooming Star Village carries Maa's spirit of unconditional care to neurodiverse individuals and the families who love them, offering a calm, supportive community so no family has to find its way alone.</p>
<div class="grid"><div class="card"><h3>🌱 Belonging</h3><p>A place where differences are welcomed, not just accommodated.</p></div><div class="card"><h3>🤝 Family support</h3><p>Caring for the whole family, including parents, siblings and caregivers.</p></div><div class="card"><h3>⭐ Growth</h3><p>Helping each person build skills and confidence at their own pace.</p></div></div></div></section>
<section id="serve"><div class="wrap"><h2>Who We Serve</h2><p>Blooming Star Village is planned for individuals with sensory processing differences, autism, developmental delays and other special needs, together with their families, across Dallas–Fort Worth.</p>
<p>Ages served: {ph("to confirm")} · Eligibility / referral needed?: {ph("to confirm")}</p></div></section>
<section id="programs"><div class="wrap"><h2>What Your Child Will Do</h2><p>Each day blends play, routine and gentle skill-building, at each child's own pace.</p>
<div class="grid">
<div class="card"><h3>🧩 Sensory Play &amp; Movement</h3><p>Swinging, climbing, balance and hands-on sensory activities that help the body and mind feel calm and ready.</p></div>
<div class="card"><h3>💬 Friendship &amp; Communication</h3><p>Small, friendly groups to practice taking turns, sharing, expressing feelings and making friends.</p></div>
<div class="card"><h3>🎨 Arts, Music &amp; Stories</h3><p>Painting, crafts, music, movement and story time to spark creativity and joy.</p></div>
<div class="card"><h3>🗓️ Daily Routine &amp; Life Skills</h3><p>A predictable, visual daily routine with simple everyday skills that build independence.</p></div>
<div class="card"><h3>🌳 Active &amp; Outdoor Play</h3><p>Games, ball play and outdoor time to build strength, coordination and confidence.</p></div>
<div class="card"><h3>👨‍👩‍👧 Family &amp; Caregiver Support</h3><p>A few hours of peace of mind for parents, plus a friendly community of families who understand.</p></div>
<div class="card"><h3>🍎 Snacks</h3><p>Healthy snacks in the MAA's Inspiration tradition, with care for dietary and sensory needs.</p></div>
</div></div></section>
<section id="visit"><div class="wrap"><h2>What a Visit Looks Like</h2><div class="grid">
<div class="card"><h3>1. Reach out</h3><p>Tell us about your family by email or the interest form below.</p></div>
<div class="card"><h3>2. Tour &amp; meet</h3><p>Visit with your child, meet our team and see the space once we open.</p></div>
<div class="card"><h3>3. A plan that fits</h3><p>We talk through needs, interests and comfort to suggest the right activities.</p></div>
<div class="card"><h3>4. Join in</h3><p>Start attending at a pace that feels right.</p></div></div></div></section>
<section id="schedule"><div class="wrap"><h2>Schedule</h2><p><b>Monday – Thursday, 9 AM – 2 PM</b> <span class="soon-badge sm">Coming soon</span></p><p>Cost: Free · Transportation: not provided · 2700 Old Denton Rd, Suite 102, Carrollton</p></div></section>
<section id="enroll"><div class="wrap"><h2>Enroll &amp; Get Involved</h2><p>Blooming Star Village is coming soon. Join our interest list and we'll contact you as programs open.</p>
<form id="enroll"><label>Parent / caregiver name *<input required></label><label>Phone *<input type="tel" required></label>
<label>Email<input type="email"></label><label>Participant's age<input type="number" min="0"></label>
<label class="full">Programs of interest<input placeholder="e.g. sensory play, social skills, family support"></label>
<label class="full">Anything you'd like us to know (needs, communication, interests)<textarea rows="3"></textarea></label>
<div class="full"><button class="btn">Join Interest List</button> <span class="ph">Form not connected yet</span></div></form></div></section>
<section id="volunteer"><div class="wrap"><h2>Volunteer</h2><p>Patient, caring volunteers will be at the heart of Blooming Star Village. Educators, students, parents and anyone with a big heart are welcome.</p><a class="btn" href="{VOL}">Sign Up to Volunteer</a></div></section>
{donate("Blooming Star Village")}
<section id="faq"><div class="wrap"><h2>FAQ</h2>
<details><summary>What are the hours?</summary><p>Monday to Thursday, 9 AM to 2 PM.</p></details>
<details><summary>When will Blooming Star Village open?</summary><p>{ph("Opening date")}</p></details>
<details><summary>Where is it located?</summary><p><a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Rd+Suite+102+Carrollton+TX+75006" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Rd, Suite 102, Carrollton, TX 75006</a> (same location as MAA's Inspiration)</p></details>
<details><summary>What ages do you serve?</summary><p>{ph("Ages served")}</p></details>
<details><summary>Is there a cost?</summary><p>No. Blooming Star Village is free.</p></details>
<details><summary>Is this therapy?</summary><p>No. Blooming Star Village is a day program for recreation and care: fun, inclusive activities and community. It does not provide therapy or medical services.</p></details>
<details><summary>Do you provide transportation?</summary><p>No, families arrange their own transportation.</p></details>
<details><summary>How can I help now?</summary><p>Volunteer, donate, or share this page with families who may benefit.</p></details>
<p>📧 <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a></p></div></section>
'''+foot
pg=head("Our Programs").replace('<main class="mi">','<main class="mi purple">')+f'''<header class="hero" style="--img:url(gallery/2026-10-10-service-03.jpg)"><p class="eyebrow">Under the MAA's Inspiration umbrella</p><h1>Our Programs</h1><p>Beyond our weekly meal service, MAA's Inspiration cares for our community through Maa's Place and Blooming Star Village.</p></header>
<section><div class="wrap"><div class="grid">
<div class="card"><h3>🍲 Maa's Meals</h3><p>2,200 fresh meals every Saturday for seniors, the homeless and shelter homes across DFW.</p><a class="btn" href="meals.html">See Schedule</a></div>
<div class="card purple-card"><h3>🏡 Maa's Place Senior Center</h3><p><span class="soon-badge sm">Opening soon</span> Activities, snacks, chai and companionship for seniors. Ages 55+. Monday to Thursday, 10 AM to 2 PM.</p><a class="btn" href="maas-place.html">Visit Maa's Place</a></div>
<div class="card"><h3>🌟 Blooming Star Village</h3><p>A free day program for recreation and care for children with special needs. Mon–Thu, 9 AM–2 PM. Coming soon.</p><a class="btn" href="blooming-star-village.html">Learn More</a></div>
</div></div></section>
<section style="text-align:center"><div class="wrap"><h2>Ready to help?</h2><p>Donate, volunteer or see schedules for any program in one place.</p><a class="btn" href="get-involved.html">Get Involved</a></div></section>
{donate("our programs")}
'''+foot
ty=head('Thank You').replace('<main class="mi">','<main class="mi purple">')+'''<section style="text-align:center;min-height:50vh"><div class="wrap"><h1>Thank you! 💚</h1><p id="tymsg">We received your form and will reach out soon. Questions? Email <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a>.</p><p><a class="btn" href="https://maasinspiration.org/">Back to Home</a></p></div></section><script>if(location.search.includes("error"))document.getElementById("tymsg").innerHTML="Sorry, something went wrong sending your form. Please email <a href=mailto:aslam@maasinspiration.org>aslam@maasinspiration.org</a>."</script>'''+foot

hub=head("Get Involved").replace('<main class="mi">','<main class="mi hub purple">')+f'''<header class="hero" style="--img:url(gallery/2026-10-10-service-04.jpg)"><p class="eyebrow">MAA's Inspiration</p><h1>Get Involved</h1><p>Choose a program, then donate, volunteer, or see when it happens.</p></header>
<section><div class="wrap">
<div class="psel" role="tablist">
<button role="tab" data-p="meals" class="p-meals">🍲<b>Maa's Meals</b></button>
<button role="tab" data-p="maas-place" class="p-mp">🏡<b>Maa's Place</b><small>Opening soon · 55+</small></button>
<button role="tab" data-p="bsv" class="p-bsv">🌟<b>Blooming Star Village</b><small>Coming soon</small></button>
</div>
<div id="panel" class="panel">
<h2 id="pname"></h2><p id="pdesc"></p>
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
<li>We take photos and videos at meal service, Maa's Place and events to share our work on our website and social media (Facebook, Instagram, TikTok).</li>
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
<div class="vcard"><span class="vt soon">Opening soon</span><h3>🏡 Maa's Place</h3><p><b>Mon – Thu</b> 10 AM – 2 PM<br>Activities, exercise, tech help, snacks &amp; chai, companionship</p><small>📍 2700 Old Denton Rd, Suite 102, Carrollton</small></div>
<div class="vcard"><span class="vt soon">Coming soon</span><h3>🌟 Blooming Star Village</h3><p><b>Mon – Thu</b> 9 AM – 2 PM<br>A free day program for children with special needs. Join the interest list – we'll contact you when it opens.</p><small>📍 2700 Old Denton Rd, Suite 102, Carrollton</small></div>
</div></div></section>
<section id="signup" class="vsign"><div class="wrap"><h2>Volunteer sign-up</h2><p class="vsub">Takes about a minute.</p>
'''+open('vol_form.html').read()+'''</div></section>
'''+foot.replace('<script src="section.js"></script>','<script src="vol-form.js"></script>')
open('volunteer-page.html','w').write(VOLP)
for n,h in [('get-involved.html',hub),('thank-you.html',ty),('maas-place.html',mp),('blooming-star-village.html',bsv),('programs.html',pg)]:open(n,'w').write(h)
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
_wire('maas-place.html',"Maa's Place enrollment"); _wire('blooming-star-village.html','Blooming Star Village interest list')

# --- Design variants of Maa's Place (same content, different layouts) ---
d1=mp.replace('<main class="mi purple">','<main class="mi purple d1">').replace("<title>Maa's Place Senior Center","<title>Design 1 Classic – Maa's Place Senior Center")
d2=mp.replace('<main class="mi purple">','<main class="mi purple d2">').replace("<title>Maa's Place Senior Center","<title>Design 2 Magazine – Maa's Place Senior Center")
d2=d2.replace('<header class="hero" style="--img:url(gallery/maas-place-seniors-painting.jpg)">','<header class="hero split"><div class="split-text">',1)
d2=d2.replace('</header>','</div><div class="split-img"><img src="gallery/maas-place-seniors-painting.jpg" alt="Seniors painting together at Maa\'s Place"></div></header>',1)
for sid,img in [('what','04'),('visit','05'),('volunteer','03')]:
    d2=d2.replace(f'<section id="{sid}"><div class="wrap">',f'<section id="{sid}" class="row"><div class="wrap"><img class="row-img" src="gallery/2026-10-10-service-{img}.jpg" alt=""><div class="row-body">',1)
import re as _r
for sid in ['what','visit','volunteer']:
    i=d2.find(f'<section id="{sid}" class="row">'); j=d2.find('</div></section>',i)
    d2=d2[:j]+'</div>'+d2[j:]
d2=d2.replace('</main>','<aside class="side-cta"><a class="btn alt" href="https://maasinspiration.org/donate.html?program=maas-place">💜 Donate</a><a class="btn green" href="https://maasinspiration.org/volunteer.html">🙌 Volunteer</a><a class="btn" href="tel:+12145171938">📞 Call</a></aside></main>',1)
d3=mp.replace('<main class="mi purple">','<main class="mi purple d3">').replace("<title>Maa's Place Senior Center","<title>Design 3 App – Maa's Place Senior Center")
i=d3.find('<header class="hero"'); j=d3.find('</header>',i)+9
d3=d3[:i]+'''<header class="appbar"><div><h1>Maa's Place</h1><p class="tagline">Place where everybody knows your name</p><p class="meta">Mon–Thu · 10 AM–2 PM · Ages 55+ · Free</p></div></header>
<nav class="tiles"><a href="#visit" data-tab="visit">📍<b>Visit</b></a><a href="#schedule" data-tab="schedule">🗓️<b>Schedule</b></a><a href="#volunteer" data-tab="volunteer">🙌<b>Volunteer</b></a><a href="https://maasinspiration.org/donate.html?program=maas-place" class="gold">💜<b>Donate</b></a><a href="tel:+12145171938" class="green">📞<b>Call</b></a></nav>
<div class="apptabs" role="tablist"><button data-tab="what">What we do</button><button data-tab="schedule">Schedule</button><button data-tab="gallery">Gallery</button><button data-tab="visit">Visit / Enroll</button><button data-tab="volunteer">Volunteer</button><button data-tab="contact">FAQ</button></div>'''+d3[j:]
_s=d3.find('<div class="sub">'); _e=d3.find('</div>',_s)+6; d3=d3[:_s]+d3[_e:]
d3=d3.replace('<script src="section.js"></script>','<script src="section.js"></script><script src="design3.js"></script>')
for n,h in [('maas-place-design-1.html',d1),('maas-place-design-2.html',d2),('maas-place-design-3.html',d3)]:open(n,'w').write(h)

# --- Final main page: Design 2 + app tiles in hero ---
TILES='''<nav class="tiles hero-tiles"><a href="#visit">📍<b>Visit</b></a><a href="#schedule">🗓️<b>Schedule</b></a><a href="#volunteer">🙌<b>Volunteer</b></a><a href="https://maasinspiration.org/donate.html?program=maas-place" class="gold">💜<b>Donate</b></a><a href="tel:+12145171938" class="green">📞<b>Call</b></a></nav>'''
main=d2.replace("<title>Design 2 Magazine – Maa's Place Senior Center","<title>Maa's Place Senior Center")
main=main.replace('<p class="tagline">Place where everybody knows your name</p>','<p class="tagline">Place where everybody knows your name</p>\n'+TILES,1)
main=_r.sub(r'<a class="btn alt" href="#visit">Plan a Visit</a> &nbsp; <a class="btn ghost"[^>]*>Volunteer</a>','',main,1)
open('maas-place.html','w').write(main)

# --- Proposed new front page (home.html) ---
def _pcard(title,img,desc,facts,href,key,badge=''):
    return f'''<div class="pcard">{'<span class="ribbon">'+badge+'</span>' if badge else ''}
<a class="pmain" href="{href}"><img src="gallery/{img}" alt="{title}"><div class="pbody"><h2>{title}</h2><p>{desc}</p><p class="pfacts">{facts}</p><span class="btn">Learn more →</span></div></a>
<div class="pquick"><a class="q-donate" href="get-involved.html#{key}">💜 Donate</a><a class="q-vol" href="get-involved.html#{key}">🙌 Volunteer</a></div></div>'''
home=head("Home").replace('<main class="mi">','<main class="mi purple home">')+'''<header class="hero home-hero"><h1>Serving with love. Feeding with dignity.</h1><p>Three ways MAA's Inspiration cares for our Dallas–Fort Worth community. Tap a program to learn more.</p></header>
<section><div class="wrap"><div class="pgrid">'''+_pcard("Maa's Meals","2026-10-10-service-03.jpg","Fresh, hot meals cooked, packed and delivered by our volunteers.","✅ Open now · 2,200 fresh meals every Saturday","meals.html","meals")+_pcard("Maa's Place","maas-place-seniors-painting.jpg","A free senior center for activities, snacks, chai and friendship.","Opening soon · Mon–Thu 10 AM–2 PM · Ages 55+","maas-place.html","maas-place","Coming Soon")+_pcard("Blooming Star Village","bsv-girl-at-desk.jpg","A free day program for recreation and care for children with special needs.","Coming soon · Mon–Thu · 9 AM–2 PM · Carrollton","blooming-star-village.html","bsv","Coming Soon")+'''</div></div></section>
<section class="donate"><div class="wrap"><h2>Every meal, every smile, every visit</h2><p>Your gift keeps all three programs going.</p><a class="btn alt" href="https://maasinspiration.org/donate.html">Donate Now</a> &nbsp; <a class="btn green" href="get-involved.html">Get Involved</a></div></section>
'''+foot
open('home.html','w').write(home)
sp=home
for a,b in [('href="site-chrome.css"','href="../site-chrome.css"'),('href="section.css"','href="../section.css"'),('src="img/','src="../img/'),('src="gallery/','src="../gallery/'),('href="maas-place.html"','href="../maas-place.html"'),('href="blooming-star-village.html"','href="../blooming-star-village.html"'),('href="get-involved.html','href="../get-involved.html'),('src="section.js"','src="../section.js"'),('href="programs.html"','href="../programs.html"')]: sp=sp.replace(a,b)
sp=sp.replace('href="https://maasinspiration.org/">Home','href="index.html">Home').replace('href="https://maasinspiration.org/about.html"','href="about.html"').replace('href="https://maasinspiration.org/volunteer.html">Volunteer</a></li>','href="volunteer.html">Volunteer</a></li>')
import os; os.makedirs('site-preview',exist_ok=True); open('site-preview/index-new.html','w').write(sp)

_wire('maas-place.html',"Maa's Place enrollment")

_b=open('blooming-star-village.html').read()
_b=_b.replace('<main class="mi purple bsvp">','<main class="mi purple bsvp d2">',1).replace('<header class="hero" style="--img:url(gallery/bsv-girl-at-desk.jpg)">','<header class="hero split"><div class="split-text">',1)
_b=_b.replace('</header>','</div><div class="split-img"><img src="gallery/bsv-girl-at-desk.jpg" alt="A child working happily at a desk"></div></header>',1)
open('blooming-star-village.html','w').write(_b)
