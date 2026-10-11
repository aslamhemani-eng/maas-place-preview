(function(){
var P={meals:{n:"🍲 Maa's Meals",k:'meals',groups:[['Saturday',['Sat 10 AM–12 PM (packing & delivery)']]],roles:['Packing','Kitchen / prep','Delivery driver','Setup / cleanup']},
mp:{n:"🏡 Maa's Place (opening soon)",k:'maas_place',groups:[['Days',['Monday','Tuesday','Wednesday','Thursday']],['Time slots',['10:00–11:00','11:00–12:00','12:00–12:45','12:45–2:00']]],roles:['Activity helper','Exercise / yoga leader','Tech help','Snacks & chai','Companion / conversation']},
bsv:{n:'🌟 Blooming Star Village (coming soon)',k:'bsv',groups:[['Interest',['Weekdays','Weekends','Evenings','Flexible – contact me when it opens']]],roles:['Activity helper','Events']}};
var f=document.getElementById('vf');if(!f)return;
function chips(name,arr){return '<div class="chips">'+[].concat(arr).map(function(v){return '<label><input type="checkbox" name="'+name+'[]" value="'+v+'">'+v+'</label>'}).join('')+'</div>'}
function render(){var keep={};f.querySelectorAll('#vfBlocks input:checked,#vfRoles input:checked').forEach(function(i){keep[i.name+i.value]=1});
 var h='',r='';f.querySelectorAll('.pk input').forEach(function(c){if(!c.checked)return;var p=P[c.dataset.p];
  h+='<div class="blk"><h4>'+p.n+'</h4>'+p.groups.map(function(g){return '<p>'+g[0]+'</p>'+chips(p.k+'_availability',g[1])}).join('')+'</div>';r+='<div class="blk"><h4>'+p.n+'</h4>'+chips(p.k+'_roles',p.roles)+'</div>'});
 document.getElementById('vfBlocks').innerHTML=h;document.getElementById('vfRoles').innerHTML=r;document.getElementById('vfDyn').hidden=!h;document.getElementById('vfDyn2').hidden=!h;
 f.querySelectorAll('#vfBlocks input,#vfRoles input').forEach(function(i){if(keep[i.name+i.value])i.checked=true})}
f.addEventListener('change',function(e){if(e.target.closest('.pk'))render()});
window.VF={select:function(k){var m={meals:'meals','maas-place':'mp',bsv:'bsv'}[k];f.querySelectorAll('.pk input').forEach(function(c){if(c.dataset.p===m)c.checked=true});render()}};
var q=new URLSearchParams(location.search).get('program');if(q)VF.select(q);
f.addEventListener('submit',function(e){var ok=f.querySelector('.pk input:checked');document.getElementById('vfErr').hidden=!!ok;if(!ok){e.preventDefault();return}
 if(/github\.io$/.test(location.hostname)){e.preventDefault();location.href=(location.pathname.indexOf('/site-preview/')>-1?'../':'')+'thank-you.html'}});
})();
