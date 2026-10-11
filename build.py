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
                <li><a href="{B}#contact">Contact</a></li>
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
                    <li><a href="{B}#contact">Contact</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Follow Us</h4>
                <div class="social-icons">
                    <a href="http://www.maasinspiration.org/" target="_blank" rel="noopener noreferrer" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                    <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" title="Instagram"><i class="fab fa-instagram"></i></a>
                    <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" title="Twitter"><i class="fab fa-twitter"></i></a>
                    <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
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
mp=head("Maa's Place Senior Center")+f'''<div class="sub"><a href="#what">What We Do</a><a href="#schedule">Schedule</a><a href="#gallery">Gallery</a><a href="#visit">Visit / Enroll</a><a href="#volunteer">Volunteer</a><a href="#donate">Donate</a><a href="#contact">Contact &amp; FAQ</a></div>
<header class="hero" style="--img:url(gallery/2026-10-10-service-02.jpg)"><p class="eyebrow">Programs · MAA's Inspiration</p>
<h1>Maa's Place Senior Center</h1>
<p>A warm, welcoming place where seniors in Dallas–Fort Worth gather for activities, homestyle snacks, chai and companionship, carried forward in the spirit of Maa, whose greatest joy was feeding others.</p>
<div class="facts"><div>🕙 Mon–Fri 10am–2pm</div><div>🕤 Sat 9:30am–noon</div><div>👵 Ages 55+</div><div>📞 <a href="tel:+12145171938" style="color:#fff">214-517-1938</a></div><div>📍 <a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Dr+Suite+102+Carrollton+TX+75006" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Dr, Suite 102, Carrollton, TX 75006</a></div></div>
<a class="btn alt" href="#visit">Plan a Visit</a> &nbsp; <a class="btn ghost" href="{VOL}" style="color:#fff">Volunteer</a></header>
<section id="what"><div class="wrap"><h2>What We Do</h2><p>Every activity is chosen to keep seniors active in body and mind, learning something new, and enjoying time together.</p>
<div class="grid">
<div class="card"><h3>💪 Physical</h3><span class="tag">Yoga</span><span class="tag">Walking</span><span class="tag">Tai chi</span><span class="tag">Musical chairs</span><span class="tag">Ball in basket</span><span class="tag">Planting</span></div>
<div class="card"><h3>🧠 Mental</h3><span class="tag">Yoga</span><span class="tag">Word search</span><span class="tag">Crafts</span></div>
<div class="card"><h3>📚 Educational</h3><span class="tag">Health insurance help</span><span class="tag">Phone use</span><span class="tag">Puzzle games</span><span class="tag">Beads</span></div>
<div class="card"><h3>🎲 Fun &amp; Entertainment</h3><span class="tag">Board games</span><span class="tag">Bingo</span><span class="tag">Karaoke</span><span class="tag">Crafts</span><span class="tag">Beads &amp; jewelry</span></div>
<div class="card"><h3>🍵 Snacks &amp; Chai</h3><p>Homestyle favorites like mini samosas, dhokra, pakora, chaat, vada, nan khatai, fruit salad, banana bread, fresh cookies, and chai.</p></div>
</div></div></section>
<section id="schedule"><div class="wrap"><h2>Weekly Schedule of Activities</h2>
<p>Week of: <b id="weekOf">…</b> · <span id="schedNote" class="ph"></span></p>
<div class="tw"><table><thead><tr><th>Day</th><th>Time</th><th>Activities</th><th>Led by</th></tr></thead><tbody id="sched"><tr><td colspan="4">Loading…</td></tr></tbody></table></div></div></section>
<section id="gallery"><div class="wrap"><h2>Photo Gallery</h2><p>A look at what's happening this week. {ph("Maa's Place photos of consenting seniors to be added")}</p><div class="gal" id="gal" data-program="maas-place"></div></div></section>
<section id="visit"><div class="wrap"><h2>Visit or Enroll</h2>
<div class="grid"><div class="card"><h3>1. Come say hello</h3><p>Drop in during open hours, call <a href="tel:+12145171938">214-517-1938</a>, or email <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a> to schedule a tour.</p></div>
<div class="card"><h3>2. Enroll</h3><p>Complete the short form below; family members can fill it out on a senior's behalf.</p></div>
<div class="card"><h3>3. Sign the waiver</h3><p>Sign our participation waiver and optional photo/video consent on your first visit.</p></div></div>
<p style="margin-top:18px">Who can attend: Adults 55 and up · Cost: {ph("to confirm")} · Transportation: {ph("to confirm")}</p>
<h3>Enrollment Form</h3>
<form id="enroll"><label>Senior's full name *<input required></label><label>Date of birth<input type="date"></label>
<label>Phone *<input type="tel" required></label><label>Email (optional)<input type="email"></label>
<label class="full">Home address / city &amp; ZIP<input></label>
<label>Preferred language<select><option>English</option><option>Urdu / Hindi</option><option>Gujarati</option><option>Other</option></select></label>
<label>Days you plan to attend<select multiple size="3"><option>Monday</option><option>Tuesday</option><option>Wednesday</option><option>Thursday</option><option>Friday</option><option>Saturday</option></select></label>
<label class="full">Activities of interest<input placeholder="e.g. yoga, bingo, crafts, planting"></label>
<label>Emergency contact name &amp; relationship *<input required></label><label>Emergency contact phone *<input type="tel" required></label>
<label class="full">Dietary needs / food allergies<input></label>
<label class="full">Mobility or health needs (optional)<textarea rows="2"></textarea></label>
<label>Need transportation?<select><option>No</option><option>Yes</option></select></label>
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
<p>📧 <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a> · 📍 <a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Dr+Suite+102+Carrollton+TX+75006" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Dr, Suite 102, Carrollton, TX 75006</a> · 📞 <a href="tel:+12145171938">214-517-1938</a></p>
<details><summary>Who can attend Maa's Place?</summary><p>Adults 55 and up</p></details>
<details><summary>Where is Maa's Place?</summary><p><a href="https://www.google.com/maps/search/?api=1&query=2700+Old+Denton+Dr+Suite+102+Carrollton+TX+75006" target="_blank" rel="noopener" style="color:inherit">2700 Old Denton Dr, Suite 102, Carrollton, TX 75006</a></p></details>
<details><summary>What are your hours?</summary><p>Monday–Friday 10am–2pm and Saturday 9:30am–noon.</p></details>
<details><summary>Is there a cost?</summary><p>{ph("To confirm")}</p></details>
<details><summary>Do you provide transportation?</summary><p>{ph("To confirm")}</p></details>
<details><summary>Are snacks provided?</summary><p>Yes, homestyle snacks and chai. Tell us about any allergies on the enrollment form.</p></details>
<details><summary>How do I volunteer?</summary><p>Sign up on our <a href="{VOL}">volunteer page</a> and we'll reach out to get you started.</p></details>
<div style="margin-top:20px;border-radius:14px;overflow:hidden"><iframe title="Map to Maa's Place" src="https://www.google.com/maps?q=2700+Old+Denton+Dr+Suite+102,+Carrollton,+TX+75006&output=embed" width="100%" height="320" style="border:0" loading="lazy"></iframe></div>
</div></section>
'''+foot.replace('<h4>Follow Us</h4>','<h4>Maa\'s Place</h4><p class="footer-description">2700 Old Denton Dr, Suite 102, Carrollton, TX 75006<br><a href="tel:+12145171938" style="color:inherit">214-517-1938</a><br><a href="mailto:aslam@maasinspiration.org" style="color:inherit">aslam@maasinspiration.org</a></p><h4 style="margin-top:1rem">Follow Us</h4>')
bsv=head("Blooming Star Village")+f'''<div class="sub"><a href="#mission">Mission</a><a href="#serve">Who We Serve</a><a href="#programs">Programs</a><a href="#visit">Your Visit</a><a href="#schedule">Schedule</a><a href="#enroll">Get Involved</a><a href="#volunteer">Volunteer</a><a href="#donate">Donate</a><a href="#faq">FAQ</a></div>
<header class="hero" style="--img:url(gallery/2026-10-10-service-05.jpg)"><p class="eyebrow">Programs · MAA's Inspiration · Coming soon</p>
<h1>Blooming Star Village</h1><p>A planned, welcoming space where children and adults with sensory, developmental and special needs, and their families, can learn, play and belong.</p>
<div class="facts"><div>📍 {ph("Location")}</div><div>🧒 Ages: {ph("Ages served")}</div><div>🕙 {ph("Hours")}</div></div>
<a class="btn alt" href="#enroll">Join the Interest List</a> &nbsp; <a class="btn ghost" href="{VOL}" style="color:#fff">Volunteer</a></header>
<section id="mission"><div class="wrap"><h2>Our Mission</h2><p>Every person deserves a place where they are understood, included and helped to grow. Blooming Star Village carries Maa's spirit of unconditional care to neurodiverse individuals and the families who love them, offering a calm, supportive community so no family has to find its way alone.</p>
<div class="grid"><div class="card"><h3>🌱 Belonging</h3><p>A place where differences are welcomed, not just accommodated.</p></div><div class="card"><h3>🤝 Family support</h3><p>Caring for the whole family, including parents, siblings and caregivers.</p></div><div class="card"><h3>⭐ Growth</h3><p>Helping each person build skills and confidence at their own pace.</p></div></div></div></section>
<section id="serve"><div class="wrap"><h2>Who We Serve</h2><p>Blooming Star Village is planned for individuals with sensory processing differences, autism, developmental delays and other special needs, together with their families, across Dallas–Fort Worth.</p>
<p>Ages served: {ph("to confirm")} · Eligibility / referral needed?: {ph("to confirm")}</p></div></section>
<section id="programs"><div class="wrap"><h2>Programs &amp; Services <span class="tag">Planned</span></h2><p>These are program ideas under consideration; final programs will be announced. {ph("Confirm which programs Maa's will offer")}</p>
<div class="grid">
<div class="card"><h3>🧩 Sensory Play &amp; Regulation</h3><p>Calm, sensory-friendly activities to help participants feel settled and ready to engage. <span class="tag">Planned</span></p></div>
<div class="card"><h3>💬 Social Skills Groups</h3><p>Small, friendly groups for practicing communication, sharing and friendship. <span class="tag">Planned</span></p></div>
<div class="card"><h3>☀️ Seasonal &amp; Weekend Activities</h3><p>Routine-friendly recreation during school breaks and weekends. <span class="tag">Planned</span></p></div>
<div class="card"><h3>👨‍👩‍👧 Family &amp; Caregiver Support</h3><p>Gatherings, resources and community for parents and caregivers. <span class="tag">Planned</span></p></div>
<div class="card"><h3>🍲 Meals &amp; Snacks</h3><p>Shared meals in the MAA's Inspiration tradition, with care for dietary and sensory needs. <span class="tag">Planned</span></p></div>
</div></div></section>
<section id="visit"><div class="wrap"><h2>What a Visit Looks Like</h2><div class="grid">
<div class="card"><h3>1. Reach out</h3><p>Tell us about your family by email or the interest form below.</p></div>
<div class="card"><h3>2. Tour &amp; meet</h3><p>Visit with your loved one, meet our team and see the space. {ph("Tours: confirm once location opens")}</p></div>
<div class="card"><h3>3. A plan that fits</h3><p>We talk through needs, interests and comfort to suggest the right activities.</p></div>
<div class="card"><h3>4. Join in</h3><p>Start attending at a pace that feels right.</p></div></div></div></section>
<section id="schedule"><div class="wrap"><h2>Schedule</h2><p>{ph("Weekly schedule – coming soon")}</p><p>Hours: {ph("Hours")} · Cost: {ph("Cost / sliding scale?")} · Transportation: {ph("Transport")}</p></div></section>
<section id="enroll"><div class="wrap"><h2>Enroll &amp; Get Involved</h2><p>Blooming Star Village is coming soon. Join our interest list and we'll contact you as programs open.</p>
<form id="enroll"><label>Parent / caregiver name *<input required></label><label>Phone *<input type="tel" required></label>
<label>Email<input type="email"></label><label>Participant's age<input type="number" min="0"></label>
<label class="full">Programs of interest<input placeholder="e.g. sensory play, social skills, family support"></label>
<label class="full">Anything you'd like us to know (needs, communication, interests)<textarea rows="3"></textarea></label>
<div class="full"><button class="btn">Join Interest List</button> <span class="ph">Form not connected yet</span></div></form></div></section>
<section id="volunteer"><div class="wrap"><h2>Volunteer</h2><p>Patient, caring volunteers will be at the heart of Blooming Star Village. Educators, therapists, students and anyone with a big heart are welcome.</p><a class="btn" href="{VOL}">Sign Up to Volunteer</a></div></section>
{donate("Blooming Star Village")}
<section id="faq"><div class="wrap"><h2>FAQ</h2>
<details><summary>When will Blooming Star Village open?</summary><p>{ph("Opening date")}</p></details>
<details><summary>Where is it located?</summary><p>{ph("Location")}</p></details>
<details><summary>What ages do you serve?</summary><p>{ph("Ages served")}</p></details>
<details><summary>Is there a cost?</summary><p>{ph("Cost")}</p></details>
<details><summary>Is this a therapy or medical provider?</summary><p>{ph("Confirm: community/recreation program vs. licensed therapy services")}</p></details>
<details><summary>How can I help now?</summary><p>Volunteer, donate, or share this page with families who may benefit.</p></details>
<p>📧 <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a></p></div></section>
'''+foot
pg=head("Our Programs")+f'''<header class="hero" style="--img:url(gallery/2026-10-10-service-03.jpg)"><p class="eyebrow">Under the MAA's Inspiration umbrella</p><h1>Our Programs</h1><p>Beyond our weekly meal service, MAA's Inspiration cares for our community through Maa's Place and Blooming Star Village.</p></header>
<section><div class="wrap"><div class="grid">
<div class="card"><h3>🍽️ Weekly Meal Service</h3><p>2,200+ hot meals every week for seniors, the homeless and shelter homes across DFW.</p><a class="btn" href="{B}schedule.html">See Schedule</a></div>
<div class="card"><h3>🏡 Maa's Place Senior Center</h3><p>Activities, snacks, chai and companionship for seniors. Ages 55+. Mon–Fri 10am–2pm, Sat 9:30am–noon.</p><a class="btn" href="maas-place.html">Visit Maa's Place</a></div>
<div class="card"><h3>🌟 Blooming Star Village</h3><p>A planned, sensory-friendly community for children and adults with special needs and their families. Coming soon.</p><a class="btn" href="blooming-star-village.html">Learn More</a></div>
</div></div></section>
{donate("our programs")}
'''+foot
ty=head('Thank You')+'''<section style="text-align:center;min-height:50vh"><div class="wrap"><h1>Thank you! 💚</h1><p id="tymsg">We received your form and will reach out soon. Questions? Email <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a>.</p><p><a class="btn" href="programs.html">Back to Programs</a></p></div></section><script>if(location.search.includes("error"))document.getElementById("tymsg").innerHTML="Sorry, something went wrong sending your form. Please email <a href=mailto:hello@maasinspiration.org>hello@maasinspiration.org</a>."</script>'''+foot
for n,h in [('thank-you.html',ty),('maas-place.html',mp),('blooming-star-village.html',bsv),('programs.html',pg)]:open(n,'w').write(h)
open('index.html','w').write('<!DOCTYPE html><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=programs.html"><a href="programs.html">Programs</a>')

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
