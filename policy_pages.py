# Public policy pages built from the Draft v2 checklist documents (policies/*.json, made from /workspace/forms-drafts/checklist).
# Internal decision notes and office-use boxes are left out. No private data.
import json
from forms_pages import DRAFT,TEL,PH
CSS='''<style>.pd-callout{background:var(--accL,#F4EFE8);border-left:5px solid var(--accD,#5B2A86);padding:12px 16px;border-radius:8px;margin:12px 0}.pd-callout p{margin:6px 0 0}
.mi.mfp .mf-terms-page h2.pd-h1{color:var(--hi,#5B2A86);border-top:3px solid var(--acc,#8DA98A);padding-top:14px;margin-top:28px}.pd-checks{list-style:none;padding-left:0}.pd-checks li{padding-left:2em;text-indent:-2em;margin:6px 0}.pd-checks li:before{content:"\\2610  ";font-size:1.2em}
.pd-line{margin:10px 0}.pd-blank{display:inline-block;min-width:180px;border-bottom:1px solid #888;height:1em}.pd-blank.sm{min-width:90px}.pd-choice span{display:inline-block;margin:4px 18px 4px 0}.pd-tw{overflow-x:auto}
.pd-dl{display:inline-block;background:var(--accD,#5B2A86);color:#fff!important;font-weight:700;padding:14px 22px;border-radius:12px;text-decoration:none;font-size:1.1rem;margin:4px 0}</style>'''
DOCS=[('volunteer-code-of-conduct.html','01_Volunteer_Code_of_Conduct_Registration_and_Event_Checklists','docs/volunteer-code-of-conduct.pdf','Volunteer Code of Conduct','Volunteers · All programs','Code of conduct, sign-up checklist and event checklists for every volunteer.',False),
('cash-check-handling.html','02_Cash_and_Check_Handling_Procedure','docs/cash-check-handling.pdf','Cash &amp; Check Handling Procedure','Finance · All programs','How we receive, count, deposit and record every cash gift and check.',False),
('maas-place-volunteer-roles.html','03_Maas_Place_Volunteer_Roles','docs/maas-place-volunteer-roles.pdf','Maa’s Place Volunteer Roles','Maa’s Place · Volunteers','The six volunteer roles at Maa’s Place and what each one does.',False),
('bloom-cash-check-handling.html','02_Cash_and_Check_Handling_Procedure','docs/cash-check-handling.pdf','Bloom Village Cash &amp; Check Handling (Policy 9)','Bloom Village · Policy book','Bloom Village follows this procedure for tuition, enrollment fees, gifts and any cash or check received.',True)]
PAGES=[d[0] for d in DOCS]
def build(head,foot):
    for fn,src,pdf,title,eb,intro,bv in DOCS:
        j=json.load(open(f'policies/{src}.json'))
        cls='mi mfp bv' if bv else 'mi mfp'
        h=head(title.replace('&amp;','&')).replace('<main class="mi">',f'<main class="{cls}">').replace('</head>','<link rel="stylesheet" href="forms.css">'+CSS+'</head>',1)
        back=('<p><a class="mf-btn mf-back" href="bloom-village.html#rights">Back to Bloom Village</a></p>' if bv else '')
        open(fn,'w').write(h+f'''{DRAFT}
<div class="mf-top"><p class="eyebrow">{eb}</p><h1>{title}</h1><p>{intro} {j['version']}.</p><p><a class="pd-dl" href="{pdf}" download>⬇ Download PDF</a></p><p class="mf-call">Questions? Call <a href="{TEL}">{PH}</a>.</p></div>
<div class="mf-wrap"><div class="mf-step mf-terms-page">{j['html']}</div>
<p style="margin-top:20px"><a class="pd-dl" href="{pdf}" download>⬇ Download PDF</a></p>{back}<p><a class="mf-btn mf-back" href="forms.html#policies">All terms, policies &amp; waivers</a></p><p><a href="javascript:print()">Print this page</a></p><p class="mf-legal">See our <a href="privacy.html">Privacy Policy</a> and <a href="terms.html">Terms of Use</a>.</p></div>
'''+foot)
