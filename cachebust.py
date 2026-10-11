import re,sys,time
V=time.strftime('%Y%m%d%H%M')
for f in sys.argv[1:]:
  s=open(f).read()
  s=re.sub(r'\b(href|src)="((?:\.\./)?[A-Za-z0-9_-]+\.(?:css|js))(?:\?v=\d+)?"',lambda m:f'{m.group(1)}="{m.group(2)}?v={V}"',s)
  open(f,'w').write(s)
