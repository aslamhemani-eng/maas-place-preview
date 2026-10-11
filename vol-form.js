(function(){
var R={meals:['Meal packing','Delivery driver'],mp:['Senior activities','Snacks & chai','Companionship'],bsv:['Activities & events']};
var f=document.getElementById('vf');if(!f)return;
function render(){var sel=[].map.call(f.querySelectorAll('.pk input:checked'),function(c){return c.dataset.p});
 var keep={};f.querySelectorAll('#vfRoles input:checked').forEach(function(i){keep[i.value]=1});
 var roles=[];sel.forEach(function(p){R[p].forEach(function(r){if(roles.indexOf(r)<0)roles.push(r)})});
 document.getElementById('vfRoles').innerHTML=roles.map(function(r){return '<label><input type="checkbox" name="help_with[]" value="'+r+'"'+(keep[r]?' checked':'')+'>'+r+'</label>'}).join('');
 var mp=sel.indexOf('mp')>-1;document.getElementById('vfDays').hidden=!mp;document.getElementById('vfHelp').hidden=!roles.length;
 var n=2;if(mp){f.querySelector('#vfDays .lg').textContent='2. Which days at Maa\'s Place?';n=3}
 f.querySelectorAll('.lg .n').forEach(function(s){if(s.closest('[hidden]'))return;s.textContent=(n++)+'. '})}
f.addEventListener('change',function(e){if(e.target.closest('.pk'))render()});
window.VF={select:function(k){var m={meals:'meals','maas-place':'mp',bsv:'bsv'}[k];f.querySelectorAll('.pk input').forEach(function(c){if(c.dataset.p===m)c.checked=true});render()}};
var q=new URLSearchParams(location.search).get('program');if(q)VF.select(q);else render();
f.addEventListener('submit',function(e){var ok=f.querySelector('.pk input:checked');document.getElementById('vfErr').hidden=!!ok;if(!ok){e.preventDefault();return}
 if(/github\.io$/.test(location.hostname)){e.preventDefault();location.href=(location.pathname.indexOf('/site-preview/')>-1?'../':'')+'thank-you.html'}});
})();
