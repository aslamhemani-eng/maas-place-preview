import re
s=open('volunteer-page.html').read()
s=re.sub(r'\b(src|href|action)="(?!https?:|#|mailto:|tel:|data:|/|\.\./)([^"]+)"',r'\1="../\2"',s)
open('site-preview/volunteer.html','w').write(s)
