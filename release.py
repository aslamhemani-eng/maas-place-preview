#!/usr/bin/env python3
"""ONE command to rebuild everything:  python3 release.py
1) builds the production site into release/ (PREVIEW=0) from build.py + live-upload/
2) zips it to /workspace/maas-plan/maasinspiration_upload.zip
3) regenerates site-preview/ as an exact copy of release/ (+ preview banner/noindex, links kept inside preview)
Never edit site-preview/ or release/ by hand – edit build.py / live-upload/*.html, then rerun."""
import os,re,shutil,subprocess,zipfile,glob,sys
H=os.path.dirname(os.path.abspath(__file__));os.chdir(H)
L='https://maasinspiration.org/'
T='/tmp/maas_prod'
shutil.rmtree(T,ignore_errors=True);shutil.copytree(H,T,ignore=shutil.ignore_patterns('.git','release','site-preview'))
subprocess.run([sys.executable,'build.py'],cwd=T,env={**os.environ,'PREVIEW':'0'},check=True,capture_output=True)
R=os.path.join(H,'release');shutil.rmtree(R,ignore_errors=True);os.makedirs(R+'/gallery');os.makedirs(R+'/img')
cp=lambda a,b:shutil.copy(os.path.join(T,a),os.path.join(R,b))
cp('home.html','index.html');cp('volunteer-page.html','volunteer.html')
for f in ['maas-place.html','bloom-village.html','blooming-star-village.html','programs.html','get-involved.html','thank-you.html','volunteer-policy.html','privacy.html','terms.html','sms-signup.html','contact.html','maas-place-waiver.html','enroll.php','site-chrome.css','section.css','section.js','hub.js','vol-form.css','vol-form.js','schedule.json','gallery.json']:cp(f,f)
for p in ['meals','about','schedule','gallery','donate']:cp(f'live-upload/{p}.html',f'{p}.html')
cp('live-upload/maas-theme.css','maas-theme.css');cp('img/site-logo.png','img/site-logo.png')
for g in glob.glob(T+'/gallery/*.jpg'):shutil.copy(g,R+'/gallery/')
shutil.copy(R+'/volunteer.html',H+'/live-upload/volunteer.html')
html=glob.glob(R+'/*.html')
LEGAL='<div class="footer-bottom legal-links" style="padding-top:0"><a href="privacy.html" style="color:inherit">Privacy Policy</a> · <a href="terms.html" style="color:inherit">Terms &amp; Conditions</a> · <a href="sms-signup.html" style="color:inherit">Text updates</a></div>'
for f in html:
  s=open(f).read()
  if '</footer>' in s and 'legal-links' not in s:open(f,'w').write(s.replace('</footer>',LEGAL+'</footer>',1))
subprocess.run([sys.executable,H+'/metadesc.py',*html],check=True,capture_output=True)
subprocess.run([sys.executable,H+'/cachebust.py',*html],check=True)
for f in html:
  s=open(f).read();assert 'noindex' not in s and 'class="preview-banner"' not in s,f
Z='/workspace/maas-plan/maasinspiration_upload.zip'
with zipfile.ZipFile(Z,'w',zipfile.ZIP_DEFLATED) as z:
  for r,d,fs in os.walk(R):
    for x in fs:z.write(os.path.join(r,x),os.path.relpath(os.path.join(r,x),R))
# preview
P=os.path.join(H,'site-preview');shutil.rmtree(P,ignore_errors=True);shutil.copytree(R,P)
os.remove(P+'/enroll.php')
files=set(os.path.relpath(os.path.join(r,x),P) for r,d,fs in os.walk(P) for x in fs)
BAN='<div style="background:#C0392B;color:#fff;text-align:center;font:14px sans-serif;padding:6px;position:relative;z-index:9999">PREVIEW of the final site — not live yet.</div>'
def fix(m):
  a,u=m.group(1),m.group(2)
  if re.match(r'(#|mailto:|tel:|data:|javascript:)',u):return m.group(0)
  mm=re.match(r'https?://(?:www\.)?maasinspiration\.org/?(.*)$',u)
  if mm:
    rest=mm.group(1);base=re.split(r'[?#]',rest)[0] or 'index.html'
    if base in files or base+'.html' in files:return f'{a}="{rest if rest and not rest.startswith(("#","?")) else "index.html"+rest}"'
    return m.group(0)
  if re.match(r'(https?:)?//',u):return m.group(0)
  base=re.split(r'[?#]',u)[0]
  if base=='enroll.php':return f'{a}="{u}"'
  if base and base not in files:return f'{a}="{L}{u}"'
  return m.group(0)
for f in glob.glob(P+'/*.html'):
  s=open(f).read()
  s=re.sub(r'\b(href|src|action|poster)="([^"]*)"',fix,s)
  s=re.sub(r"(window\.location\.href=')https://maasinspiration\.org/([a-z-]+\.html)'",lambda m:m.group(1)+m.group(2)+"'" if m.group(2) in files else m.group(0),s)
  s=re.sub(r"url\((['\"]?)(?!https?:|data:)([^)'\"]+)\1\)",lambda m:m.group(0) if m.group(2).split('?')[0] in files else f"url({m.group(1)}{L}{m.group(2)}{m.group(1)})",s)
  s=re.sub(r"(['\"])(?!https?:|data:|/)((?:[A-Za-z0-9_-]+/)*[A-Za-z0-9_.-]+\.(?:jpe?g|png|webp|mp4|gif))\1",lambda m:m.group(0) if m.group(2) in files else m.group(1)+L+m.group(2)+m.group(1),s)
  s=s.replace('<head>','<head>\n    <meta name="robots" content="noindex,nofollow">',1)
  s=re.sub(r'(<body[^>]*>)',r'\1'+BAN,s,1)
  s=s.replace('</body>','<script>document.querySelectorAll("form[action$=\'enroll.php\']").forEach(f=>f.addEventListener("submit",e=>{e.preventDefault();location.href="thank-you.html"}))</script></body>',1)
  open(f,'w').write(s)
print('release files',sum(len(fs) for _,_,fs in os.walk(R)),'preview pages',len(glob.glob(P+'/*.html')))
