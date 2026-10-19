# Builds the online forms (forms.html hub + 6 form pages). Called from build.py.
# Wording comes from the Draft v3 forms (Oct 19, 2026). No personal data, keys or passcodes here.
from html import escape as E
PH='(469) 270-8156'; TEL='tel:+14692708156'
ADDR="2700 Old Denton Rd, Suite 102, Carrollton, TX 75007"
LEGAL="Maa’s Inspiration Inc."
DRAFT='<p class="mf-draft" role="note">DRAFT – pending attorney review</p>'

def fld(name,label,req=True,type='text',auto='',hint='',extra=''):
    r=' required' if req else ''
    opt='' if req else ' <span class="mf-opt">(optional)</span>'
    a=f' autocomplete="{auto}"' if auto else ''
    inm={'tel':' inputmode="tel"','email':' inputmode="email"'}.get(type,'')
    h=f'<small>{hint}</small>' if hint else ''
    if type=='textarea':
        inp=f'<textarea id="f_{name}" name="{name}"{r}{extra}></textarea>'
    else:
        inp=f'<input id="f_{name}" type="{type}" name="{name}"{r}{a}{inm}{extra}>'
    return f'<div class="mf-field"><label for="f_{name}">{label}{opt}</label>{h}{inp}</div>'

def radio(name,q,opts,req=True,row=False):
    items=''.join(f'<label class="mf-choice"><input type="radio" name="{name}" value="{E(v)}"{" required" if req and i==0 else ""}> {E(v)}</label>' for i,v in enumerate(opts))
    opt='' if req else ' <span class="mf-opt">(optional)</span>'
    return f'<div class="mf-field" role="radiogroup" aria-label="{E(q)}"><p class="mf-q">{q}{opt}</p><div class="mf-choices{" row" if row else ""}">{items}</div></div>'

def checks(name,q,opts,minimum=1,row=False,hint=''):
    items=''.join(f'<label class="mf-choice"><input type="checkbox" data-group="1" name="{name}" value="{E(v)}"> {E(v)}</label>' for v in opts)
    h=f'<small>{hint}</small>' if hint else ''
    return f'<div class="mf-field" {"data-min="+chr(34)+str(minimum)+chr(34) if minimum else ""}><p class="mf-q">{q}</p>{h}<div class="mf-choices{" row" if row else ""}">{items}</div></div>'

def tick(name,text,req=True,consent=True,msg=''):
    dc=' data-consent' if consent else ''
    dm=f' data-msg="{msg}"' if msg else ''
    return f'<label class="mf-tick"><input type="checkbox" name="{name}" value="yes"{" required" if req else ""}{dm}> <span{dc}>{text}</span></label>'

def file(name,label):
    return f'<div class="mf-field mf-file"><label for="f_{name}">{label}</label><small>Take a photo or choose a file: JPG, PNG or PDF, 5 MB or less.</small><input id="f_{name}" type="file" name="{name}" accept="image/jpeg,image/png,application/pdf,.jpg,.jpeg,.png,.pdf" required></div>'

def step(title,body):return (title,body)

def sig_step(statement,roles=None,title='Sign and send',extra=''):
    rl=radio('signer_role','I am signing as',roles) if roles else ''
    return (title,f'''<div class="mf-sig"><p data-consent>{statement}</p></div>{extra}{rl}
{fld('sig_name','Type your full name to sign',auto='name',extra=' data-fullname="1"',hint='Typing your name here is your signature.')}
<label class="mf-tick"><input type="checkbox" name="sig_agree" value="yes" required data-msg="Please tick “I agree” to sign."> <span><b>I agree.</b> I am signing this form electronically.</span></label>
<p>Date: <b class="mf-date"></b></p>''')

def page(head,foot,fn,title,eyebrow,intro,form_type,steps,bv=False):
    n=len(steps);out=[]
    for i,(t,b) in enumerate(steps):
        back='' if i==0 else '<button type="button" class="mf-btn mf-back">Back</button>'
        nxt='<button type="submit" class="mf-btn mf-send">Send form</button>' if i==n-1 else '<button type="button" class="mf-btn mf-next">Next</button>'
        out.append(f'<fieldset class="mf-step" aria-label="{E(t)}"{" hidden" if i else ""}><h2>{t}</h2>{b}'+(f'<div id="mfStatus" class="mf-status" role="alert" hidden></div>' if i==n-1 else '')+f'<div class="mf-nav">{back}{nxt}</div></fieldset>')
    cls='mi mfp bv' if bv else 'mi mfp'
    h=head(title).replace('<main class="mi">',f'<main class="{cls}">').replace('</head>','<link rel="stylesheet" href="forms.css"></head>',1)
    body=f'''{DRAFT}
<div class="mf-top"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p>{intro}</p><p class="mf-call">Need help? Call <a href="{TEL}">{PH}</a>.</p></div>
<div class="mf-wrap">
{'' if n==1 else '<div class="mf-progress"><p id="mfCount" aria-live="polite"></p><div class="mf-track"><div id="mfBar"></div></div></div>'}
<form class="mf-form" data-form-type="{form_type}" novalidate>
<div class="mf-hp" aria-hidden="true"><label>Leave this empty<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
{''.join(out)}
</form>
<div id="mfThanks" class="mf-thanks" hidden role="status"><h2>Thank you! We received your form.</h2><p id="mfRefWrap">Your reference number is<br><span id="mfRef" class="mf-ref"></span><br>Please write it down or take a picture of this screen.</p><p>We will call you if we have any questions.</p><p class="mf-call">Questions? Call <a href="{TEL}">{PH}</a>.</p><p><a class="mf-btn" href="forms.html">Back to all forms</a></p></div>
</div>
'''
    f=foot.replace('<script src="section.js"></script>','<script src="section.js"></script><script src="forms-config.js"></script><script src="forms.js"></script>')
    open(fn,'w').write(h+body+f)


MEALS_TERMS=f'''<h3>1. The service and delivery</h3><ul>
<li>Volunteer drivers bring a free meal to your door on <b>Saturdays between 10 AM and noon</b>.</li>
<li>The driver hands you the meal or leaves it as your notes say, and does not come inside unless there is an emergency.</li>
<li>If no one answers, the driver calls our coordinator and we may call you. Food is not left where it can spoil. If someone seems hurt or in danger, the driver calls 911.</li></ul>
<h3>2. Door photo and privacy</h3><ul>
<li>The driver takes one photo at every stop, showing only the meal at the door and the house number – never you or the inside of your home.</li>
<li>Photos are kept for 1 week, then deleted, and are never posted or shared.</li>
<li>We use your information only to deliver your meals. We do not sell or share it. See our <a href="privacy.html">Privacy Policy</a>.</li></ul>
<h3>3. Food and changes</h3><ul>
<li>Food may be made in a kitchen that also handles common allergens, and is not made for special medical diets. Please call us about any serious food allergy.</li>
<li>Call <a href="{TEL}">{PH}</a> if your address or phone changes, or to pause or stop deliveries.</li>
<li>By agreeing, you confirm your information is true. Someone helping you may agree for you, with your permission.</li></ul>'''

DRIVER_TERMS=f'''<h3>1. Who can drive</h3><ul>
<li>You must be at least 18 years old.</li>
<li>You must hold a valid Texas driver’s license.</li>
<li>You must carry current auto liability insurance on the vehicle you use that meets at least the Texas minimum: $30,000 for injury to one person, $60,000 for injury to two or more people, and $25,000 for property damage.</li>
<li>Keep the vehicle registered and in safe working condition (lights, brakes, tires, wipers, seat belts).</li>
<li>Keep your license and insurance current. Tell Maa’s right away if either one lapses, is suspended, revoked or cancelled, or expires.</li>
<li>You do not need to send us copies. Maa’s may ask to see your license and insurance if needed.</li></ul>
<h3>2. Insurance and liability</h3><ul>
<li>Your own auto insurance is primary. If there is an accident while you are volunteering, your insurance is expected to pay first.</li>
<li>Covered under {LEGAL}’s liability insurance policy (carrier and policy number on file with the administrator).</li>
<li>Texas law that protects volunteers from some lawsuits does not fully protect volunteers who are driving, because auto insurance is expected to cover driving. Check with your insurance company that delivering meals as an unpaid volunteer is covered.</li></ul>
<h3>3. Safe driving and phone use</h3><ul>
<li>Obey all traffic laws and wear your seat belt.</li>
<li>Do not text or read messages while driving. Texas law bans it. Look at the app, call or take photos only when parked.</li>
<li>Do not drive after drinking alcohol or using drugs or medicine that make you drowsy.</li>
<li>Do not drive when you are too tired, sick, or the weather is unsafe. Tell the coordinator if you cannot drive.</li>
<li>Do not give rides to meal recipients or other people as part of Maa’s Meals unless Maa’s has approved it in writing.</li>
<li>Keep the meals in the insulated bags Maa’s gives you and deliver them on time.</li></ul>
<h3>4. At the door</h3><ul>
<li>Be friendly and respectful, and wear your Maa’s name badge (if provided).</li>
<li>Do not go inside a recipient’s home unless there is an emergency.</li>
<li><b>Photo at every stop:</b> take one delivery photo at every stop. It shows the meal at the door and the house number only – never the person, the inside of the home, or a license plate. Use only the Maa’s app, not your phone’s camera roll, and never post or share delivery photos. Maa’s keeps delivery photos for 1 week, then deletes them.</li>
<li>If no one answers, follow the app steps and call the coordinator. Do not leave food where it can spoil unless the recipient’s instructions say so.</li></ul>
<h3>5. Privacy</h3><p>Recipients’ names, addresses, phone numbers and delivery photos are private. Use them only to deliver meals. Do not share, copy, post or keep them after your route, and do not contact recipients for personal reasons.</p>
<h3>6. Emergencies and reporting</h3><ul>
<li>If someone looks hurt, very sick or in danger, call 911, then the coordinator.</li>
<li>If you think an older adult is being abused, neglected or exploited, you must report it to the Texas Abuse Hotline: <a href="tel:+18002525400">1-800-252-5400</a>, and tell the coordinator.</li></ul>
<h3>7. Accidents, tickets and problems</h3><ol>
<li>Stop safely. Call 911 if anyone is hurt. Follow the law for exchanging information.</li>
<li>Call the Maa’s Meals coordinator as soon as it is safe.</li>
<li>Report the accident to your own insurance company.</li>
<li>Tell Maa’s in writing within 24 hours about any accident, injury or traffic ticket that happened while volunteering, and within 7 days if you get a ticket or your license changes at any other time.</li></ol>
<h3>8. Costs</h3><p>Volunteer driving is unpaid. {LEGAL} does not pay for gas, mileage, tolls, parking, tickets or vehicle damage unless approved in writing before the trip. Some mileage for charity driving may be tax-deductible – ask your tax adviser.</p>
<h3>9. Your agreement</h3><p>By agreeing, you confirm that you are 18 or older, that you hold a valid Texas driver’s license and current auto insurance that meets the Texas minimums, that you will keep them current, and that you will tell Maa’s if either one lapses. You will follow these rules. {LEGAL} may stop your driving role at any time for safety reasons.</p>'''

FILES=['forms.html','form-meals-recipient.html','meals-terms.html','form-bloom-fee.html','form-bloom-rights.html','form-bloom-complaint.html','form-driver.html','driver-terms.html','form-text-consent.html']

def build(head,foot):
    # 1. Meals recipient (simplified: 3 steps; all rules live in MEALS_TERMS / meals-terms.html)
    MV='meals-terms-v3.1-2026-10-19'
    page(head,foot,'form-meals-recipient.html',"Maa’s Meals Recipient Form","Maa’s Meals · a program of "+LEGAL,
      "Sign up for free Saturday meal delivery. One short page. A family member or volunteer can help you fill this out.",
      'meals_recipient',[
      ('Your details',fld('full_name','Full name',auto='name',extra=' data-fullname="1"')+fld('street','Street address',auto='address-line1')+fld('apt','Apt / unit',req=False,auto='address-line2')+fld('city','City',auto='address-level2',extra=' value="Carrollton"')+fld('zip','ZIP code',auto='postal-code',extra=' inputmode="numeric" data-zip="1"')+fld('phone','Phone number',type='tel',auto='tel')+fld('delivery_notes','Delivery notes',req=False,type='textarea',hint='For example: gate code, pets, which door, stairs.')+'<h3>Terms and signature</h3>'+f'''<details class="mf-terms"><summary>Read the Meal Recipient Terms &amp; Policies</summary><div class="mf-terms-box" tabindex="0">{MEALS_TERMS}</div></details>
<p><a href="meals-terms.html" target="_blank" rel="noopener">Open the Meal Recipient Terms &amp; Policies on their own page</a></p>
<input type="hidden" name="terms_version" value="{MV}">
<label class="mf-tick"><input type="checkbox" name="sig_agree" value="yes" required data-msg="Please tick the box to agree to the Meal Recipient Terms &amp; Policies."> <span data-consent>I have read and agree to the Meal Recipient Terms &amp; Policies.</span></label>
<span hidden data-consent>Terms version: {MV}</span>
{fld('sig_name','Type your full name to sign',auto='name',extra=' data-fullname="1"',hint='Typing your name here is your signature. If you are helping someone, type your own name.')}
<p>Date: <b class="mf-date"></b></p>''')])
    th=head('Meal Recipient Terms & Policies').replace('<main class="mi">','<main class="mi mfp">').replace('</head>','<link rel="stylesheet" href="forms.css"></head>',1)
    open('meals-terms.html','w').write(th+f'''{DRAFT}
<div class="mf-top"><p class="eyebrow">Maa’s Meals · a program of {LEGAL}</p><h1>Meal Recipient Terms &amp; Policies</h1><p>For seniors who get Saturday meal deliveries. Version {MV}.</p><p class="mf-call">Questions? Call <a href="{TEL}">{PH}</a>.</p></div>
<div class="mf-wrap"><div class="mf-step mf-terms-page">{MEALS_TERMS}</div>
<p style="margin-top:20px"><a class="mf-btn" href="form-meals-recipient.html">Go to the Meal Recipient Form</a></p><p><a class="mf-btn mf-back" href="forms.html">All forms</a></p></div>
'''+foot)

    # 2. Bloom fee agreement
    fee_tbl='''<table class="mf-tbl"><tr><th>Fee</th><th>Amount</th><th>When due</th></tr><tr><td>Enrollment fee (one time)</td><td>$100 – non-refundable</td><td>When this agreement is signed, before the first day</td></tr><tr><td>Tuition</td><td>$30 per program day</td><td>Billed weekly. Due on the last day of the week.</td></tr></table>
<table class="mf-tbl"><tr><th>Plan</th><th>Each week</th><th>4-week month</th></tr><tr><td>2 days a week</td><td>$60</td><td>$240</td></tr><tr><td>3 days a week</td><td>$90</td><td>$360</td></tr><tr><td>5 days a week (after the pilot)</td><td>$150</td><td>$600</td></tr></table>'''
    page(head,foot,'form-bloom-fee.html',"Bloom Village Fee Agreement","Bloom Village · a program of "+LEGAL,
      f"Tuition and fee agreement between {LEGAL} (“Bloom Village”), the participant and the person responsible for paying. Please read it carefully and call us with any question before you sign. We will not collect the enrollment fee until this agreement is signed.",
      'bloom_fee_agreement',[
      step('Who this agreement is for',fld('participant_name','Participant’s full name')+fld('participant_dob','Participant’s date of birth',type='date')+fld('legal_rep','Legal representative, if any',req=False)),
      step('Person responsible for payment',fld('payer_name','Full name',auto='name')+fld('payer_relationship','Relationship to the participant')+fld('payer_address','Address',auto='street-address')+fld('payer_phone','Phone',type='tel',auto='tel')+fld('payer_email','Email',req=False,type='email',auto='email')),
      step('Program days',f'<p class="mf-note">Bloom Village is open <b>Monday to Friday, 9:00 AM to 1:00 PM</b>. Pick up is at 1:00 PM. During the pilot, participants attend 2 or 3 days a week, with up to 8 adults in the group.</p>'+checks('program_days','Which days?',['Mon','Tue','Wed','Thu','Fri'],row=True,hint='Tap each day you want.')+'<p>Estimated tuition: <span class="mf-est" id="mfEst">choose days above</span></p>'+fld('start_date','Start date you would like',req=False,type='date')),
      step('What it costs',fee_tbl+'<div class="mf-note" data-consent><b>The $100 enrollment fee is non-refundable.</b> It is not returned if the participant does not start, leaves the program, or is discharged.</div>'+fld('fee_initials','Your initials',hint='Type your initials to show you understand the $100 fee is non-refundable.')+radio('pay_method','How will you pay?',['Check to Maa’s Inspiration Inc.','Online payment','Other'])+'<p>We give a receipt for every payment.</p>'),
      step('Absences, payment and leaving',f'''<div data-consent><h3>Absences, holidays and closures</h3><ul><li>Absences are not charged. Please tell us as early as you can.</li><li>Closed on all major holidays (no charge).</li><li>Closures for weather or emergencies are not charged.</li><li>To change days, ask the administrator. Changes start when space and staffing allow.</li></ul>
<h3>Late payment</h3><ul><li>There is no late payment fee and no late pickup fee.</li><li>If tuition is not paid by the due date, we send a written reminder. If it is still not paid 15 days after the reminder, we will talk with you about a plan. Services may end only after reasonable written notices and the discharge steps.</li></ul>
<h3>Leaving the program and refunds</h3><ul><li>Please give us <b>15 days’ written notice</b> before leaving.</li><li>Prepaid program days not yet provided are refunded, minus any balance owed. There is no deadline for this refund. The $100 enrollment fee is not refunded.</li><li>If Bloom Village must end services, we give at least <b>30 days’ written notice</b>, except in an emergency. You may use the complaint (grievance) procedure or call HHSC at 1-800-458-9858 about any discharge.</li></ul>
<h3>Tuition assistance (scholarships)</h3><p>Need-based help may be available as funds allow: Bloom 25%, Hope 50%, Legacy 75%, Full Bloom up to 100%. It is not guaranteed, and the $100 enrollment fee is not automatically covered. Awards are reviewed once every year.</p>
<h3>Medicare and Medicaid</h3><p>Within 30 days after starting, we will tell you if Medicare or Medicaid may cover any of our services.</p></div>'''+radio('scholarship_interest','Would you like information about tuition assistance?',['No','Yes'],row=True)),
      sig_step("I have read this agreement, had my questions answered, and agree to it. I will receive a copy.",['The participant','Legal representative','Person responsible for payment'])],bv=True)

    # 3a. Rights acknowledgment
    rights=[
     ('Your rights as a person',f'''<p class="mf-note">You are an adult. You have the same rights as everyone else. Bloom Village must respect them. These rights come from Texas law (Human Resources Code §102.003) and HHSC rules (26 TAC §559.228).</p><ul>
<li>You have all the rights of any person under Texas and U.S. law. No one may stop you, pressure you, treat you unfairly or punish you for using your rights.</li>
<li>You will be treated with dignity and respect, no matter your race, religion, national origin, sex, age, disability, marital status or how your services are paid for.</li>
<li>You may make your own choices about your life, care, benefits and services.</li>
<li>If you need help with decisions, you may choose a guardian or representative to help you.</li></ul>
<h3>Safety</h3><ul><li>You have the right to be free from abuse, neglect and exploitation.</li>
<li>You have the right to be free from physical and mental abuse, including punishment and restraints (holding or medicine) used to discipline you or for staff convenience. Texas law allows restraints only if a doctor authorizes them in writing or in an emergency to keep you or others from injury. Bloom Village does not use restraints.</li>
<li>If you have a court-appointed guardian, you may take part in a behavior program that uses restraints or unpleasant stimuli only if your guardian gives informed consent. Bloom Village does not run such programs.</li>
<li>You have the right to services in a safe and clean place.</li></ul>'''),
     ('Talking, privacy and choices','''<h3>Communication and complaints</h3><ul><li>You may talk in your own language with others and with staff.</li>
<li>You may complain about your care or treatment. You may complain without giving your name, or someone you choose can complain for you. We must respond quickly to fix the problem, and we may not punish you or treat you differently because you complained.</li></ul>
<h3>Privacy</h3><ul><li>You have the right to privacy when using the restroom or getting help with personal care.</li>
<li>You may have a private place to visit with people, if it does not take away other people’s rights.</li>
<li>Your phone calls and written messages are private. You may send and receive mail unopened.</li>
<li>Your records are private. You may see your own records. We share them only with your permission, with another provider if you transfer, or when the law requires it.</li></ul>
<h3>Choices, activities and visitors</h3><ul><li>You may take part in social, religious and community groups and activities.</li>
<li>You may control your own schedule and activities, have your own food at any time, have visitors you choose at any time, and get into the building. These can be limited only if your plan from your program provider says so, based on an assessed need.</li>
<li>You may say no to a scheduled activity. We will write down that you chose not to take part. You may refuse to do work for Bloom Village.</li>
<li>You may keep and use your own belongings, as space allows. Some items may be limited for everyone’s safety.</li>
<li>You may manage your own money, or choose someone in writing to help you. Choosing a helper does not take away your other rights.</li></ul>'''),
     ('Your health, money and leaving','''<h3>Your health and your plan</h3><ul><li>We will tell you, in words you understand, about your health as it relates to our services, and tell you when we notice a big change.</li>
<li>You may choose your own doctor, and be told ahead of time about care that may affect you.</li>
<li>You may take part in your plan (IPC, IPP, PDP or implementation plan) and get services that follow it, from staff who respond to your needs.</li>
<li>You may refuse medical treatment after being told what could happen and saying that you understand.</li>
<li>If you dislike or disagree with our services, we will help you raise it with your program provider.</li>
<li>You may make a living will, a medical power of attorney, or choose a guardian ahead of time.</li></ul>
<h3>Money and benefits</h3><ul><li>Within 30 days after you start, we will tell you whether you may be entitled to Medicare or Medicaid benefits and which of our items and services those benefits cover, including anything we may not charge you for.</li></ul>
<h3>Leaving the program</h3><ul><li>We may end your services only if: it is for your welfare and we cannot meet your needs; you no longer need services; your safety or someone else’s would be in danger; we close or stop taking part in the program that pays for your care; or you do not pay after reasonable notices.</li>
<li>Before ending services because we cannot meet your needs, we will try to meet your needs, talk with you, your legal representative and your program provider, and tell you in writing before you are discharged. Except in an emergency, we give written notice at least 30 days ahead with the reason, the date, and how to appeal.</li></ul>
<h3>Your responsibilities</h3><ul><li>Treat other participants, staff and visitors with respect.</li><li>Tell us about health, allergy or support changes so we can keep you safe.</li><li>Follow safety rules, such as fire drills.</li><li>Your family or representative: sign in and out, keep phone numbers current, and pay fees as agreed.</li></ul>'''),
     ('How to make a complaint',f'''<p>A complaint (grievance) is a concern about anything at Bloom Village. You will never be punished for complaining. You can get help from anyone you choose, and you can complain without giving your name.</p>
<h3>Step 1 – Tell someone</h3><p>Tell any staff member, the administrator (Yasmeen Rajwani) or the director in person, by phone, in writing, by text or email, or in the way you communicate best. A family member, friend, legal representative or advocate can do it for you. You can also use our <a href="form-bloom-complaint.html">online complaint form</a>.</p>
<h3>Step 2 – We write it down and answer</h3><p>The administrator tells you we received it within 2 business days and gives you a written answer within 10 business days. If it is about safety, we act right away.</p>
<h3>Step 3 – If you are not happy with the answer</h3><p>Ask for a review by the director of {LEGAL}, Aslam Hemani, at <a href="{TEL}">{PH}</a>. The director answers in writing within 10 business days.</p>
<h3>You can go outside Bloom Village at any time</h3><ul><li>HHSC Complaint and Incident Intake: <a href="tel:+18004589858">1-800-458-9858</a></li><li>Texas Abuse Hotline: <a href="tel:+18002525400">1-800-252-5400</a></li><li>Disability Rights Texas: <a href="tel:+18002529108">1-800-252-9108</a></li><li>Emergency: <a href="tel:911">911</a></li></ul>''')]
    page(head,foot,'form-bloom-rights.html',"Bloom Village Participant Rights","Bloom Village · a program of "+LEGAL,
      "Please read your rights, one page at a time. A staff member or family member can read them aloud with you. At the end, sign to say you received them.",
      'bloom_rights_ack',[step(t,b) for t,b in rights]+[
      step('About the participant',fld('participant_name','Participant’s full name')+fld('start_date','Start date',req=False,type='date')+radio('language','Language used to explain these rights',['English','Other'])+f'<div data-show-if="language=Other">{fld("language_other","Which language?")}</div>'+checks('explained_how','How were they explained?',['Read aloud','Pictures / easy-read','Large print','Sign language','Device','Interpreter','Other'],minimum=0,hint='Tick any that apply.')),
      step('I received my rights',tick('ack_rights','I received the rights list.')+tick('ack_grievance','I received the complaint (grievance) procedure.')+tick('ack_no_punish','I know I will not be punished for complaining or using my rights.')+tick('ack_hotlines','I know how to contact HHSC (1-800-458-9858) and the Texas Abuse Hotline (1-800-252-5400).')),
      sig_step("I have read and received the Bloom Village Participant Rights and Grievance Procedure. They were explained to me in a way I understand. I know I can complain without being punished, and I know the HHSC phone number.",['The participant','Legal representative (legally authorized)'],title='Sign: I have read and received my rights',
        extra=f'<div data-show-if="signer_role=Legal representative (legally authorized)">{fld("rep_authority","Your legal authority",hint="For example: guardianship, power of attorney.")}</div>')],bv=True)

    # 3b. Complaint
    page(head,foot,'form-bloom-complaint.html',"Bloom Village Complaint Form","Bloom Village · a program of "+LEGAL,
      "Tell us about any concern. You will never be punished for complaining. You may leave your name off. If someone is in danger right now, call 911.",
      'bloom_grievance',[
      step('Who is this about?','<p class="mf-note">Your name is optional. You can stay anonymous.</p>'+fld('person_name','Your name',req=False,auto='name')+fld('participant_name','Participant’s name, if different',req=False)+fld('contact','Phone or best way to reach you',req=False,hint='Leave blank if you do not want us to contact you.')),
      step('What is the concern?',fld('concern','Tell us in your own words',type='textarea')+fld('wanted_outcome','What would you like to happen?',req=False,type='textarea')),
      step('Safety question',radio('abuse_neglect','Is it about abuse, neglect or exploitation?',['No','Yes','Not sure'])+'<div data-show-if="abuse_neglect=Yes"><p class="mf-note"><b>Please also call HHSC now at <a href="tel:+18004589858">1-800-458-9858</a></b>, or 911 if someone is in danger. Bloom Village will report it to HHSC within 1 hour.</p></div>'+'<div class="mf-note">You can also call HHSC at <a href="tel:+18004589858">1-800-458-9858</a> or the Texas Abuse Hotline at <a href="tel:+18002525400">1-800-252-5400</a> at any time. You do not have to use our steps first.</div>'),
      ('Send your complaint',f'''<div class="mf-sig"><p data-consent>The information in this complaint is true as far as I know. I understand Bloom Village will tell me it was received within 2 business days and answer in writing within 10 business days, if I gave a way to reach me.</p></div>
{fld('sig_name','Type your name, or “Anonymous”',hint='You may type Anonymous.')}
<label class="mf-tick"><input type="checkbox" name="sig_agree" value="yes" required data-msg="Please tick to send."> <span><b>I agree.</b> Send this complaint to Bloom Village.</span></label><p>Date: <b class="mf-date"></b></p>''')],bv=True)

    # 4. Driver agreement (simplified: 3 steps; all rules live in DRIVER_TERMS / driver-terms.html)
    TV='driver-terms-v3.1-2026-10-19'
    AGREE='I have read and agree to the Driver Terms &amp; Policies.'
    page(head,foot,'form-driver.html',"Volunteer Driver Agreement","Maa’s Meals · a program of "+LEGAL,
      "Thank you for driving for Maa’s Meals! One short page: tell us about you, then agree to the Driver Terms &amp; Policies.",
      'driver_agreement',[
      ('Your details',fld('full_name','Full name',auto='name',extra=' data-fullname="1"')+fld('cell_phone','Cell phone',type='tel',auto='tel')+fld('email','Email',req=False,type='email',auto='email')+tick('age_18_plus','I am 18 or older.',consent=False,msg='Drivers must be 18 or older. Please tick to confirm.')+'<h3>Terms and signature</h3>'+f'''<details class="mf-terms"><summary>Read the Driver Terms &amp; Policies</summary><div class="mf-terms-box" tabindex="0">{DRIVER_TERMS}</div></details>
<p><a href="driver-terms.html" target="_blank" rel="noopener">Open the Driver Terms &amp; Policies on their own page</a></p>
<input type="hidden" name="terms_version" value="{TV}">
<label class="mf-tick"><input type="checkbox" name="sig_agree" value="yes" required data-msg="Please tick the box to agree to the Driver Terms &amp; Policies."> <span data-consent>{AGREE}</span></label>
<span hidden data-consent>Terms version: {TV}</span>
{fld('sig_name','Type your full name to sign',auto='name',extra=' data-fullname="1"',hint='Typing your name here is your signature.')}
<p>Date: <b class="mf-date"></b></p>''')])
    th=head('Driver Terms & Policies').replace('<main class="mi">','<main class="mi mfp">').replace('</head>','<link rel="stylesheet" href="forms.css"></head>',1)
    open('driver-terms.html','w').write(th+f'''{DRAFT}
<div class="mf-top"><p class="eyebrow">Maa’s Meals · a program of {LEGAL}</p><h1>Driver Terms &amp; Policies</h1><p>For volunteers who deliver Maa’s Meals in their own vehicles. Version {TV}.</p><p class="mf-call">Questions? Call <a href="{TEL}">{PH}</a>.</p></div>
<div class="mf-wrap"><div class="mf-step mf-terms-page">{DRIVER_TERMS}</div>
<p style="margin-top:20px"><a class="mf-btn" href="form-driver.html">Go to the Driver Agreement form</a></p><p><a class="mf-btn mf-back" href="forms.html">All forms</a></p></div>
'''+foot)

    # 5. SMS consent
    CONSENT="I agree to receive text messages from Maa’s Inspiration Inc. about volunteer shifts and meal deliveries. Msg frequency varies. Msg &amp; data rates may apply. Reply STOP to opt out, HELP for help. See our Privacy Policy and Terms &amp; Conditions."
    page(head,foot,'form-text-consent.html',"Volunteer Text Message Consent","Volunteer program · "+LEGAL,
      "Choose whether you want volunteer text messages from us. Saying yes is never required to volunteer.",
      'volunteer_sms_consent',[
      step('About you',fld('full_name','Full name',auto='name',extra=' data-fullname="1"')+fld('mobile','Mobile phone number',type='tel',auto='tel',hint='The number that will get the texts.')),
      step('What you will get',f'''<table class="mf-tbl"><tr><td><b>From</b></td><td>{LEGAL} (Maa’s Meals)</td></tr><tr><td><b>What</b></td><td>Volunteer shift and route reminders and meal delivery notices: the Thursday “are you available this Saturday?” question, a Friday reminder if there is no reply, a confirmation of your reply, your Saturday assignment (deliver or packing), and a thank-you after the shift.</td></tr><tr><td><b>How often</b></td><td>Message frequency varies.</td></tr><tr><td><b>Cost</b></td><td>Message and data rates may apply.</td></tr><tr><td><b>To stop</b></td><td>Reply <b>STOP</b> (or STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT) at any time.</td></tr><tr><td><b>For help</b></td><td>Reply <b>HELP</b>, call <a href="{TEL}">{PH}</a>, or email <a href="mailto:aslam@maasinspiration.org">aslam@maasinspiration.org</a>.</td></tr><tr><td><b>Privacy</b></td><td>We do not sell or share mobile numbers or text opt-in information with anyone for marketing. See our <a href="privacy.html">Privacy Policy</a> and <a href="terms.html">Terms &amp; Conditions</a>.</td></tr></table>'''),
      step('Your choice','<p class="mf-note">Leave the box empty if you do not want texts. You can still volunteer.</p>'+f'<label class="mf-tick"><input type="checkbox" name="sms_consent" value="yes" required data-msg="To sign up for texts, tick this box. If you do not want texts, you do not need to send this form."> <span data-consent>{CONSENT}</span></label><p><small>Consent is not a condition of volunteering.</small></p>'),
      sig_step("I am the person who uses this mobile number, and I agree to the text messages described above.")])

    # Hub
    def card(href,t,d,bv=False):return f'<a class="mf-card{" bv" if bv else ""}" href="{href}"><b>{t}</b><span>{d}</span><span class="go">Open form →</span></a>'
    h=head('Forms').replace('<main class="mi">','<main class="mi mfp">').replace('</head>','<link rel="stylesheet" href="forms.css"></head>',1)
    open('forms.html','w').write(h+f'''{DRAFT}
<div class="mf-top"><p class="eyebrow">{LEGAL}</p><h1>Forms</h1><p>Fill in and sign our forms on your phone. Each form takes a few short steps. Need help? Call <a href="{TEL}">{PH}</a>.</p></div>
<div class="mf-wrap">
<div class="mf-group"><h2>🍲 Maa’s Meals</h2>{card('form-meals-recipient.html','Meal Recipient Form','For seniors who get Saturday meal deliveries. One short page.')}{card('meals-terms.html','Meal Recipient Terms &amp; Policies','How deliveries, door photos, food and privacy work.')}{card('form-driver.html','Volunteer Driver Agreement','For volunteers who deliver meals in their own car. One short page.')}{card('driver-terms.html','Driver Terms &amp; Policies','The rules every volunteer driver agrees to.')}</div>
<div class="mf-group"><h2>🙌 Volunteers</h2>{card('form-text-consent.html','Text Message Consent','Choose whether to get volunteer text reminders. Optional.')}{card('form-driver.html','Volunteer Driver Agreement','For Maa’s Meals delivery drivers. Must be 18 or older.')}</div>
<div class="mf-group"><h2>🌸 Bloom Village</h2>{card('form-bloom-fee.html','Fee Agreement','Tuition, program days and fee terms for families.',True)}{card('form-bloom-rights.html','Participant Rights','Read your rights and sign that you received them.',True)}{card('form-bloom-complaint.html','Complaint Form','Tell us about a concern. You can stay anonymous.',True)}</div>
<p class="mf-call">Your form goes to {LEGAL}’s private system. {ADDR} · <a href="{TEL}">{PH}</a></p>
</div>
'''+foot)
