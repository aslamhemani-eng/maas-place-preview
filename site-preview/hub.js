const P={
 meals:{name:"Maa's Meals",desc:"Every Saturday our volunteers cook, pack and deliver 2,200 fresh meals to seniors, the homeless and shelter homes across DFW.",cls:"p-meals",
  sched:[["Saturday","10am–noon","Meal packing & delivery"]],more:'Full schedule: <a href="schedule.html">maasinspiration.org/schedule.html</a>'},
 "maas-place":{name:"Senior Center",desc:"Opening soon! Free activities, snacks, chai and companionship for adults 55+, Monday to Thursday 10 AM–2 PM. 2700 Old Denton Rd, Suite 102, Carrollton, TX 75006 · 214-517-1938.",cls:"p-mp",more:'<a href="maas-place.html">Visit the Senior Center page</a>'},
 bsv:{name:"Star Village",desc:"A free day program for recreation and care for children with special needs. Coming soon.",cls:"p-bsv",sched:[["Mon–Thu","9 AM–2 PM","Coming soon"]],more:'<a href="blooming-star-village.html">Visit the Star Village page</a>'}
};
let MPS=null;
fetch('schedule.json',{cache:'no-store'}).then(r=>r.json()).then(d=>{MPS=d.days.filter(x=>!x.hidden).map(x=>[x.day,'10 AM–2 PM',x.slots?x.slots.filter(c=>c!=='TBD').join(' · '):x.all_day]);if(cur==='maas-place')show(cur)});
let cur='meals';
function show(p){if(!P[p])p='meals';cur=p;const c=P[p];
 document.querySelectorAll('.psel button').forEach(b=>b.setAttribute('aria-selected',b.dataset.p===p));
 document.getElementById('panel').dataset.p=p;
 pname.textContent=c.name;pimg.src='gallery/'+({meals:'maas-meals-volunteers.jpg','maas-place':'maas-place-seniors-painting.jpg',bsv:'bsv-girl-at-desk.jpg'}[p]||'maas-meals-volunteers.jpg');pimg.alt=c.name;pdesc.textContent=c.desc;pmore.innerHTML=c.more;
 actDonate.href='donate.html?program='+p;
 const rows=p==='maas-place'?(MPS||[["Loading…","",""]]):c.sched;
 hsched.innerHTML=rows.map(r=>'<tr>'+r.map(x=>'<td>'+(/PLACEHOLDER/.test(x)?'<span class="ph">To be scheduled</span>':x)+'</td>').join('')+'</tr>').join('');
 if(window.VF)VF.select(p);
 if(p!=='meals')volprog.value=p==='bsv'?'Star Village':"Senior Center";
 if(location.hash.slice(1)!==p)history.replaceState(null,'','#'+p);}
document.querySelectorAll('.psel button').forEach(b=>b.onclick=()=>show(b.dataset.p));
addEventListener('hashchange',()=>{const h=location.hash.slice(1);if(P[h])show(h)});
show(location.hash.slice(1));

