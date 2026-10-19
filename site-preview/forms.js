/* Step-by-step signable forms. No personal data is stored in the browser, logged or sent anywhere except the endpoint in forms-config.js. */
(function () {
  var C = window.MAAS_FORMS_CONFIG || {};
  var form = document.querySelector('form.mf-form');
  if (!form) return;
  var steps = [].slice.call(form.querySelectorAll('.mf-step'));
  var bar = document.getElementById('mfBar'), cnt = document.getElementById('mfCount');
  var cur = 0;

  // auto date (Central time)
  var today = new Date();
  var dateTxt = today.toLocaleDateString('en-US', { timeZone: C.timezone || 'America/Chicago', year: 'numeric', month: 'long', day: 'numeric' });
  [].forEach.call(document.querySelectorAll('.mf-date'), function (e) { e.textContent = dateTxt; });

  function visible(el) { // honours data-show-if
    var p = el.closest('[data-show-if]');
    while (p) {
      if (p.hidden) return false;
      p = p.parentElement && p.parentElement.closest('[data-show-if]');
    }
    return true;
  }
  function applyShowIf() {
    [].forEach.call(form.querySelectorAll('[data-show-if]'), function (b) {
      var rule = b.getAttribute('data-show-if'), neg = rule.indexOf('!=') > 0, kv = rule.split(neg ? '!=' : '='), on = false;
      [].forEach.call(form.querySelectorAll('[name="' + kv[0] + '"]'), function (i) { if ((i.type === 'radio' || i.type === 'checkbox') ? i.checked && i.value === kv[1] : i.value === kv[1]) on = true; });
      b.hidden = neg ? on : !on;
    });
  }
  form.addEventListener('change', applyShowIf); applyShowIf();

  // Bloom Village tuition estimate ($30 per program day)
  var est = document.getElementById('mfEst');
  if (est) form.addEventListener('change', function () {
    var n = form.querySelectorAll('[name="program_days"]:checked').length;
    est.textContent = n ? (n + ' day' + (n > 1 ? 's' : '') + ' a week = $' + (n * 30) + ' a week (about $' + (n * 120) + ' for a 4-week month)') : 'choose days above';
  });

  function show(i, quiet) {
    steps.forEach(function (s, k) { s.hidden = k !== i; });
    cur = i;
    if (cnt) cnt.textContent = 'Step ' + (i + 1) + ' of ' + steps.length;
    if (bar) bar.style.width = Math.round((i + 1) / steps.length * 100) + '%';
    var h = steps[i].querySelector('h2'); if (quiet) return; window.scrollTo({ top: form.getBoundingClientRect().top + window.scrollY - 90, behavior: 'smooth' });
    if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
  }

  function setErr(field, msg) {
    var box = field.closest('.mf-field') || field.closest('.mf-tick') || field.parentElement;
    var e = box.querySelector(':scope > .mf-err');
    if (!e) { e = document.createElement('p'); e.className = 'mf-err'; e.setAttribute('role', 'alert'); box.appendChild(e); }
    e.textContent = msg; box.classList.add('bad');
  }
  function clearErrs(scope) {
    [].forEach.call(scope.querySelectorAll('.mf-err'), function (e) { e.remove(); });
    [].forEach.call(scope.querySelectorAll('.bad'), function (e) { e.classList.remove('bad'); });
  }
  function age(v) {
    var d = new Date(v + 'T12:00:00'); if (isNaN(d)) return -1;
    var a = today.getFullYear() - d.getFullYear(); var m = today.getMonth() - d.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < d.getDate())) a--; return a;
  }
  function checkStep(step) {
    clearErrs(step); var first = null, done = {};
    [].forEach.call(step.querySelectorAll('input,select,textarea'), function (f) {
      if (!f.name || f.name === 'website' || !visible(f) || done[f.name]) return;
      var msg = '';
      if (f.type === 'radio' || (f.type === 'checkbox' && f.dataset.group)) {
        done[f.name] = 1;
        var any = step.querySelector('[name="' + f.name + '"]:checked');
        var need = f.type === 'radio' ? step.querySelector('[name="' + f.name + '"][required]') : f.closest('[data-min]');
        if (need && !any) msg = f.type === 'radio' ? 'Please choose one.' : 'Please choose at least one.';
      } else if (f.type === 'checkbox') {
        if (f.required && !f.checked) msg = f.dataset.msg || 'Please tick this box to continue.';
      } else if (f.type === 'file') {
        var file = f.files && f.files[0];
        if (f.required && !file) msg = 'Please add a photo or PDF.';
        else if (file) {
          var ext = (file.name.split('.').pop() || '').toLowerCase();
          var FL = C.files || { types: ['image/jpeg', 'image/png', 'application/pdf'], ext: ['jpg', 'jpeg', 'png', 'pdf'], max_bytes: 5242880 };
          if ((FL.types.indexOf(file.type) < 0) && FL.ext.indexOf(ext) < 0) msg = 'Please use a JPG, PNG or PDF file.';
          else if (file.size > FL.max_bytes) msg = 'This file is too big. Please use one under 5 MB.';
        }
      } else {
        var v = (f.value || '').trim(), ri = f.dataset.reqIf, req = f.required;
        if (ri) { var kv = ri.split('='); var o = form.querySelector('[name="' + kv[0] + '"]:checked'); if (o && o.value === kv[1]) req = true; }
        if (req && !v) msg = f.dataset.msg || 'Please fill this in.';
        else if (v && f.type === 'tel' && v.replace(/\D/g, '').replace(/^1(?=\d{10}$)/, '').length !== 10) msg = 'Please enter a 10-digit phone number, like 469-555-0123.';
        else if (v && f.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) msg = 'Please check the email address.';
        else if (v && f.dataset.zip && !/^\d{5}(-\d{4})?$/.test(v)) msg = 'Please enter a 5-digit ZIP code.';
        else if (v && f.dataset.minage) { var a = age(v); if (a < 0 || a > 120) msg = 'Please check the date.'; else if (a < +f.dataset.minage) msg = 'Sorry, you must be ' + f.dataset.minage + ' or older.'; }
        else if (v && f.dataset.fullname && v.split(/\s+/).length < 2) msg = 'Please type your first and last name.';
      }
      if (msg) { setErr(f, msg); if (!first) first = f; }
    });
    if (first) { first.focus(); first.scrollIntoView({ block: 'center', behavior: 'smooth' }); return false; }
    return true;
  }

  form.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.classList.contains('mf-next')) { e.preventDefault(); if (checkStep(steps[cur])) show(cur + 1); }
    if (b.classList.contains('mf-back')) { e.preventDefault(); clearErrs(steps[cur]); show(cur - 1); }
  });
  form.addEventListener('input', function (e) { var b = e.target.closest('.bad'); if (b) { b.classList.remove('bad'); var m = b.querySelector('.mf-err'); if (m) m.remove(); } });

  function signer(d) { // typed signature; forms without a separate signature line use the full name; complaints may be anonymous
    var s = form.querySelector('[name="sig_name"]');
    var v = (s ? s.value : (d.full_name || d.name || '')).trim();
    return v || 'Anonymous';
  }
  function plain(el) { // readable text of the exact wording shown, keeping list items and headings apart
    var c = el.cloneNode(true);
    [].forEach.call(c.querySelectorAll('li,p,h3,h2,tr'), function (b) { b.insertAdjacentText('afterbegin', b.tagName === 'LI' ? '• ' : ''); b.insertAdjacentText('beforeend', '\n'); });
    return c.textContent.split('\n').map(function (l) { return l.replace(/\s+/g, ' ').trim(); }).filter(Boolean).join('\n');
  }
  function readFile(f) {
    return new Promise(function (ok, no) { var r = new FileReader(); r.onload = function () { ok(String(r.result).split(',')[1] || ''); }; r.onerror = no; r.readAsDataURL(f); });
  }

  function collect() {
    var data = {}, files = [], jobs = [];
    [].forEach.call(form.querySelectorAll('input,select,textarea'), function (f) {
      if (!f.name || f.name === 'website' || f.name === 'sig_name' || f.name === 'sig_agree') return;
      if (!visible(f)) return;
      if (f.type === 'file') {
        var file = f.files && f.files[0];
        if (file) jobs.push(readFile(file).then(function (b64) { files.push({ name: f.name + '.' + (file.name.split('.').pop() || 'bin').toLowerCase(), type: file.type || 'application/octet-stream', base64: b64 }); }));
        return;
      }
      if (f.type === 'radio') { if (f.checked) data[f.name] = f.value; return; }
      if (f.type === 'checkbox') {
        if (f.dataset.group) { data[f.name] = data[f.name] || []; if (f.checked) data[f.name].push(f.value); }
        else data[f.name] = f.checked;
        return;
      }
      data[f.name] = (f.value || '').trim();
    });
    data.signed_date = dateTxt;
    data.signed_at = new Date().toISOString();
    var sa = form.querySelector('[name="sig_agree"]'); if (sa) data.sig_agree = sa.checked;
    var u18 = form.querySelector('[data-under18]');
    if (u18) { data.under_18 = !u18.checked; if (!data.under_18) data.guardian_name = ''; }
    data.page = location.pathname.split('/').pop();
    return Promise.all(jobs).then(function () { return { data: data, files: files }; });
  }

  var send = form.querySelector('.mf-send'), status = document.getElementById('mfStatus');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!checkStep(steps[cur])) return;
    if (status) { status.hidden = true; status.innerHTML = ''; }
    send.disabled = true; var label = send.textContent; send.textContent = 'Sending…';
    collect().then(function (c) {
      var body = {
        form_type: form.dataset.formType,
        data: c.data,
        signer_name: signer(c.data),
        agreement_version: C.agreement_version,
        consent_text: [].map.call(form.querySelectorAll('[data-consent]'), plain).join('\n\n'),
        website: (form.querySelector('[name="website"]') || {}).value || ''
      };
      var ctl = window.AbortController ? new AbortController() : null;
      var t = setTimeout(function () { if (ctl) ctl.abort(); }, C.timeout_ms || 45000);
      return fetch(C.endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body), signal: ctl ? ctl.signal : undefined, credentials: 'omit', referrerPolicy: 'no-referrer' })
        .then(function (r) { clearTimeout(t); if (!r.ok) throw new Error('http'); return r.json().catch(function () { return {}; }); });
    }).then(function (j) {
      var ref = ''; (C.reference_keys || []).some(function (k) { if (j && j[k] != null && j[k] !== '') { ref = String(j[k]); return true; } return false; });
      form.reset(); form.hidden = true;
      var ty = document.getElementById('mfThanks'); ty.hidden = false;
      var rf = document.getElementById('mfRef');
      if (ref) rf.textContent = ref; else document.getElementById('mfRefWrap').hidden = true;
      var pb = document.querySelector('.mf-progress'); if (pb) pb.hidden = true;
      window.scrollTo({ top: 0, behavior: 'smooth' }); var h = ty.querySelector('h2'); if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
    }).catch(function () {
      send.disabled = false; send.textContent = label;
      if (status) {
        status.hidden = false;
        status.innerHTML = '<b>Sorry, we couldn’t send your form.</b> Please try again, or call us at <a href="tel:' + C.help_tel + '">' + C.help_phone + '</a> and we will help you.';
        status.scrollIntoView({ block: 'center', behavior: 'smooth' });
      }
    });
  });

  show(0, true);
})();
