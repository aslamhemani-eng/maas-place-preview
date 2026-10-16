import sys,os,re
D={'index':"MAA's Inspiration serves our Dallas–Fort Worth community through Maa's Meals, the Maa’s Place and Bloom Village.",
'meals':"Maa's Meals: volunteers cook, pack and deliver 2,200 fresh meals every Saturday to seniors, shelters and neighbors in need across DFW.",
'about':"About MAA's Inspiration, a Carrollton, TX 501(c)(3) nonprofit serving neighbors with compassion, dignity and love — one meal at a time.",
'volunteer':"Volunteer with MAA's Inspiration: Maa's Meals on Saturdays 10 AM–noon, the Maa’s Place Mon–Thu 10 AM–2 PM, and Bloom Village.",
'schedule':"Weekly schedule for Maa's Meals (Saturdays 10 AM–noon), the Maa’s Place (Mon–Thu 10 AM–2 PM) and Bloom Village.",
'gallery':"Photos from MAA's Inspiration's weekly meal service and community programs in Dallas–Fort Worth.",
'donate':"Donate to MAA's Inspiration. $5 provides one hot meal for a neighbor in need in Dallas–Fort Worth. Secure checkout via Stripe.",
'programs':"MAA's Inspiration programs: Maa's Meals, the Maa’s Place (opening soon) and Bloom Village (adult enrichment, licensing pending).",
'maas-place':"Maa’s Place: a free center for seniors in Carrollton, TX for adults 55+, Monday–Thursday 10 AM–2 PM. Opening soon.",
'bloom-village':"Bloom Village, a program of Maa's Inspiration: adult enrichment in Carrollton, TX for adults 18+ with intellectual and developmental disabilities. Licensing pending with HHSC.",
'get-involved':"Get involved with MAA's Inspiration: donate, volunteer or see schedules for Maa's Meals, the Maa’s Place and Bloom Village.",
'thank-you':"Thank you for contacting MAA's Inspiration.",
'contact':"Contact MAA's Inspiration in Carrollton, TX: addresses, hours, phone (469) 270-8156 and email aslam@maasinspiration.org.",
'maas-place-waiver':"Maa’s Place participation waiver and release – read and print before your first visit.",
'volunteer-policy':"MAA's Inspiration volunteer photo consent policy and code of conduct."}
for f in sys.argv[1:]:
  k=os.path.basename(f)[:-5]
  if k not in D: continue
  s=open(f).read()
  if 'name="description"' in s: continue
  s=re.sub(r'(<title>[^<]*</title>)',lambda m:m.group(1)+'\n    <meta name="description" content="'+D[k].replace('"','&quot;')+'">',s,1)
  open(f,'w').write(s)
