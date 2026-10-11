const P={
 meals:{name:"Weekly Meal Service",desc:"Every week our volunteers cook, pack and deliver 2,200+ hot meals to seniors, the homeless and shelter homes across DFW.",cls:"p-meals",
  sched:[["Saturday","9:30am","Meal packing & delivery"],["Mon–Fri","10am–2pm","Hours of operation"]],more:'Full schedule: <a href="https://maasinspiration.org/schedule.html">maasinspiration.org/schedule.html</a>'},
 "maas-place":{name:"Maa's Place Senior Center",desc:"Free activities, snacks, chai and companionship for adults 55+, Monday to Thursday 10 AM–2 PM. 2700 Old Denton Rd, Suite 102, Carrollton, TX 75006 · 214-517-1938.",cls:"p-mp",more:'<a href="maas-place.html">Visit the Maa\'s Place page</a>'},
 bsv:{name:"Blooming Star Village",desc:"A free, planned recreation program for children and adults with special needs and their families. Coming soon.",cls:"p-bsv",sched:[["Coming soon","",""]],more:'<a href="blooming-star-village.html">Visit the Blooming Star Village page</a>'}
};
let MPS=null;
fetch('schedule.json',{cache:'no-store'}).then(r=>r.json()).then(d=>{MPS=d.days.filter(x=>!x.hidden).map(x=>[x.day,'10 AM–2 PM',x.slots?x.slots.filter(c=>c!=='TBD').join(' · '):x.all_day]);if(cur==='maas-place')show(cur)});
let cur='meals';
function show(p){if(!P[p])p='meals';cur=p;const c=P[p];
 document.querySelectorAll('.psel button').forEach(b=>b.setAttribute('aria-selected',b.dataset.p===p));
 document.getElementById('panel').dataset.p=p;
 pname.textContent=c.name;pdesc.textContent=c.desc;pmore.innerHTML=c.more;
 actDonate.href='https://maasinspiration.org/donate.html?program='+p;
 const rows=p==='maas-place'?(MPS||[["Loading…","",""]]):c.sched;
 hsched.innerHTML=rows.map(r=>'<tr>'+r.map(x=>'<td>'+(/PLACEHOLDER/.test(x)?'<span class="ph">To be scheduled</span>':x)+'</td>').join('')+'</tr>').join('');
 mealsVol.hidden=p!=='meals';volform.hidden=p==='meals';
 if(p!=='meals')volprog.value=p==='bsv'?'Blooming Star Village':"Maa's Place";
 if(location.hash.slice(1)!==p)history.replaceState(null,'','#'+p);}
document.querySelectorAll('.psel button').forEach(b=>b.onclick=()=>show(b.dataset.p));
addEventListener('hashchange',()=>{const h=location.hash.slice(1);if(P[h])show(h)});
show(location.hash.slice(1));
if(/github\.io$/.test(location.hostname))volform.onsubmit=e=>{e.preventDefault();location.href='thank-you.html'};
