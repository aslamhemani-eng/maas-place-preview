// Hamburger (same as live site)
const hamburger=document.getElementById('hamburger'),navLinks=document.getElementById('navLinks');
hamburger.addEventListener('click',()=>navLinks.classList.toggle('active'));
navLinks.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>navLinks.classList.remove('active')));
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const mark=s=>/PLACEHOLDER/.test(s)?'<span class="ph">'+esc(s)+'</span>':esc(s);
const sc=document.getElementById('sched');
if(sc)fetch('schedule.json',{cache:'no-store'}).then(r=>r.json()).then(d=>{
 document.getElementById('weekOf').innerHTML=mark(d.week_of);
 const n=document.getElementById('schedNote'); if(n){if(d.note)n.textContent=d.note; else n.remove();}
 const S=d.slots||[];document.getElementById('schedHead').innerHTML='<tr><th>Day</th>'+S.map(x=>'<th>'+esc(x)+'</th>').join('')+'</tr>';
 sc.innerHTML=d.days.filter(x=>!x.hidden).map(x=>'<tr><td><b>'+esc(x.day)+'</b></td>'+(x.slots?x.slots.map(c=>'<td>'+(c==='TBD'?'<span class="ph">TBD</span>':esc(c))+'</td>').join(''):'<td colspan="'+S.length+'">'+esc(x.all_day)+(x.led_by?' <small>– led by '+esc(x.led_by)+'</small>':'')+'</td>')+'</tr>').join('');
}).catch(()=>sc.innerHTML='<tr><td>Schedule unavailable.</td></tr>');
const g=document.getElementById('gal');
if(g)fetch('gallery.json',{cache:'no-store'}).then(r=>r.json()).then(d=>{
 g.innerHTML=d.photos.filter(p=>!p.program||p.program===g.dataset.program).map(p=>`<figure><img loading="lazy" src="gallery/${esc(p.file)}" alt="${esc(p.caption)}"><figcaption>${esc(p.caption)}</figcaption></figure>`).join('');
 g.querySelectorAll('img').forEach(i=>i.onclick=()=>{const lb=document.getElementById('lb');lb.querySelector('img').src=i.src;lb.style.display='flex'});
});
const f=document.getElementById('enroll'); if(f&&/github\.io$/.test(location.hostname))f.onsubmit=e=>{e.preventDefault();location.href='thank-you.html'}; // preview only; live site posts to enroll.php
