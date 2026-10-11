(function(){const ids=['what','schedule','gallery','visit','volunteer','contact'];
function show(t){if(!ids.includes(t))t='what';ids.forEach(i=>{const s=document.getElementById(i);if(s)s.style.display=i===t?'':'none'});
document.querySelectorAll('.apptabs button').forEach(b=>b.setAttribute('aria-selected',b.dataset.tab===t));}
document.querySelectorAll('[data-tab]').forEach(b=>b.addEventListener('click',e=>{e.preventDefault();show(b.dataset.tab);history.replaceState(null,'','#'+b.dataset.tab);document.querySelector('.apptabs').scrollIntoView({behavior:'smooth'})}));
show(location.hash.slice(1));})();
