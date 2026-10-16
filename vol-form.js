(function(){
var f=document.getElementById('volunteerForm');if(!f)return;
var DAYS={meals:[['Saturday (10 AM – 12 PM) · Maa\'s Meals','Saturday']],mp:[['Monday (Senior Center)','Monday'],['Tuesday (Senior Center)','Tuesday'],['Wednesday (Senior Center)','Wednesday'],['Thursday (Senior Center)','Thursday']]};
var HELP={meals:['Food Packing','Meal Delivery'],mp:['Senior Activities','Snacks & Chai','Companionship / Conversation','Tech Help for Seniors'],bsv:['Activities & Events (Bloom Village)']};
var $=function(id){return document.getElementById(id)};
function sel(){return [].map.call(f.querySelectorAll('.prog input:checked'),function(c){return c.dataset.p})}
function render(){var s=sel(),keep={};f.querySelectorAll('#daysGrid input:checked').forEach(function(i){keep[i.value]=1});
 var d=[];s.forEach(function(p){(DAYS[p]||[]).forEach(function(x){d.push(x)})});
 $('daysGrid').innerHTML=d.map(function(x,i){return '<label class="opt"><input type="checkbox" name="days" value="'+x[0]+'"'+(keep[x[0]]?' checked':'')+'>'+x[1]+(x[1]==='Saturday'?' <small>10–noon</small>':'')+'</label>'}).join('');
 $('daysSec').hidden=!d.length;
 $('daysHint').textContent=s.indexOf('meals')>-1?"Maa's Meals runs on Saturdays only, 10 AM – noon.":'';
 var mp=s.indexOf('mp')>-1;$('timeSec').hidden=!mp;f.querySelectorAll('#timeSec input').forEach(function(r){r.required=mp});
 $('bsvHint').hidden=s.indexOf('bsv')<0;
 var cur=$('helpType').value,h=[];s.forEach(function(p){HELP[p].forEach(function(x){if(h.indexOf(x)<0)h.push(x)})});
 $('helpType').innerHTML='<option value="">Select an option</option>'+h.concat(['Anything — I\'m Happy to Help!']).map(function(x){return '<option'+(x===cur?' selected':'')+'>'+x+'</option>'}).join('')}
f.addEventListener('change',function(e){if(e.target.closest('.prog'))render()});
window.VF={select:function(k){var m={meals:'meals','maas-place':'mp',bsv:'bsv'}[k];f.querySelectorAll('.prog input').forEach(function(c){if(c.dataset.p===m)c.checked=true});render()}};
var q=new URLSearchParams(location.search).get('program');if(q)VF.select(q);else render();
f.addEventListener('submit',async function(e){e.preventDefault();var s=sel(),err=$('lvfErr');
 var days=[].map.call(f.querySelectorAll('#daysGrid input:checked'),function(i){return i.value});
 var msg=!s.length?'Please choose at least one program.':(!$('daysSec').hidden&&!days.length)?'Please select at least one available day.':'';
 err.textContent=msg;err.hidden=!msg;if(msg){err.scrollIntoView({block:'center'});return}
 var fd=new FormData(f);fd.delete('days');fd.delete('Program');
 fd.set('Program',[].map.call(f.querySelectorAll('.prog input:checked'),function(c){return c.value}).join(', '));
 fd.set('Available Days',days.join(', ')||'—');
 var btn=f.querySelector('.submit-btn');btn.disabled=true;btn.textContent='Sending…';
 try{var r=await fetch('https://formsubmit.co/ajax/aslamhemani@gmail.com',{method:'POST',headers:{Accept:'application/json'},body:fd});var j=await r.json().catch(function(){return{}});
  if(r.ok&&(j.success==='true'||j.success===true)){f.hidden=true;$('lvfDone').hidden=false;$('lvfDone').scrollIntoView({block:'center'})}
  else{err.textContent='Submission issue: '+(j.message||('HTTP '+r.status))+'. Please try again or email aslam@maasinspiration.org.';err.hidden=false}}
 catch(x){err.textContent='Network error – please try again or email aslam@maasinspiration.org.';err.hidden=false}
 btn.disabled=false;btn.textContent='📨 Submit Registration'});
$('lvfAgain').onclick=function(){f.reset();render();f.hidden=false;$('lvfDone').hidden=true};
})();
