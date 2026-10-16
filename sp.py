import re,sys
L='https://maasinspiration.org/'
NEW={'programs.html','maas-place.html','bloom-village.html','get-involved.html','thank-you.html','volunteer-policy.html'}
LOCAL={'enroll.php','vol-form.css','vol-form.js'}
for p in sys.argv[1:]:
  s=open(f'live-upload/{p}.html').read()
  def fix(m):
    a,u=m.group(1),m.group(2)
    if re.match(r'(https?:|#|mailto:|tel:|data:|javascript:|//)',u) or u=='maas-theme.css': return m.group(0)
    base=u.split('#')[0].split('?')[0]
    if base in LOCAL: return f'{a}="../{u}"'
    if base.endswith('.html'): return f'{a}="../{u}"' if base in NEW else m.group(0)
    return f'{a}="{L}{u}"'
  s=re.sub(r'\b(src|href|poster|action)="([^"]*)"',fix,s)
  s=re.sub(r"url\((['\"]?)(?!https?:|data:)([^)'\"]+)\1\)",lambda m:f"url({m.group(1)}{L}{m.group(2)}{m.group(1)})",s)
  s=re.sub(r"(['\"`])(?!https?:|data:|/)([A-Za-z0-9_./-]+\.(?:jpe?g|png|webp|mp4|gif))\1",lambda m:m.group(1)+L+m.group(2)+m.group(1),s)
  s=s.replace('<head>','<head>\n    <meta name="robots" content="noindex,nofollow">',1)
  s=s.replace('<body>','<body><div style="background:#C0392B;color:#fff;text-align:center;font:14px sans-serif;padding:6px">PREVIEW of the whole site in the new theme — not live.</div>',1)
  open(f'site-preview/{p}.html','w').write(s)
