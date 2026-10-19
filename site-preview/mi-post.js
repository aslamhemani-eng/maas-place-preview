/* Maa's Inspiration – small helper that sends simple forms (contact, Bloom Village inquiry,
   gift dedications) to the secure public-forms endpoint in forms-config.js.
   No email services, no keys, no personal data stored here. */
(function () {
  var C = window.MAAS_FORMS_CONFIG || {};
  var PH = C.help_phone || '(469) 270-8156', TEL = C.help_tel || '+14692708156';
  window.MI_FAIL_HTML = 'Sorry, we couldn’t send your message. Please try again, or call us at <a href="tel:' + TEL + '">' + PH + '</a>.';
  window.miPost = function (formType, data, signerName, website) {
    var ctl = window.AbortController ? new AbortController() : null;
    var t = ctl ? setTimeout(function () { ctl.abort(); }, C.timeout_ms || 45000) : null;
    data.page = location.pathname.split('/').pop();
    data.sent_at = new Date().toISOString();
    var body = { form_type: formType, data: data, signer_name: signerName || data.name || 'Anonymous',
      agreement_version: C.agreement_version, consent_text: '', website: website || '' };
    return fetch(C.endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body),
      signal: ctl ? ctl.signal : undefined, credentials: 'omit', referrerPolicy: 'no-referrer' })
      .then(function (r) {
        if (t) clearTimeout(t);
        return r.json().catch(function () { return {}; }).then(function (j) {
          if (!r.ok) throw new Error('HTTP ' + r.status);
          var ref = ''; (C.reference_keys || ['reference']).forEach(function (k) { if (!ref && j && j[k]) ref = String(j[k]); });
          return ref;
        });
      }, function (e) { if (t) clearTimeout(t); throw e; });
  };
  /* Wire a <form data-mi-type="contact|bloom_inquiry"> whose inputs are named after the data fields. */
  window.miWire = function (form, opts) {
    opts = opts || {};
    var type = form.getAttribute('data-mi-type'), btn = form.querySelector('[type="submit"]');
    var msg = form.querySelector('.mi-status');
    if (!msg) { msg = document.createElement('p'); msg.className = 'mi-status'; msg.setAttribute('role', 'alert'); msg.hidden = true; btn.parentNode.insertBefore(msg, btn); }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.reportValidity && !form.reportValidity()) return;
      var data = {}, hp = '';
      [].forEach.call(form.querySelectorAll('input,select,textarea'), function (f) {
        if (!f.name) return;
        if (f.name === 'website') { hp = f.value; return; }
        data[f.name] = f.type === 'checkbox' ? f.checked : (f.value || '').trim();
      });
      if (opts.prepare) data = opts.prepare(data);
      var label = btn.textContent; btn.disabled = true; btn.textContent = 'Sending…'; msg.hidden = true;
      window.miPost(type, data, data.name, hp).then(function (ref) {
        btn.disabled = false; btn.textContent = label;
        if (opts.done) return opts.done(ref, data);
        var ok = document.createElement('div'); ok.className = 'mi-ok'; ok.setAttribute('role', 'status'); ok.tabIndex = -1;
        ok.innerHTML = '<h3>Thank you!</h3><p>' + (opts.okText || 'We got your message and will get back to you soon.') + '</p>' + (ref ? '<p>Your reference number: <b>' + ref.replace(/[<>&"]/g, '') + '</b></p>' : '') + '<p>Questions? Call <a href="tel:' + TEL + '">' + PH + '</a>.</p>';
        form.parentNode.replaceChild(ok, form); ok.focus();
      }).catch(function () {
        btn.disabled = false; btn.textContent = label;
        msg.innerHTML = window.MI_FAIL_HTML; msg.hidden = false;
      });
    });
  };
  [].forEach.call(document.querySelectorAll('form[data-mi-type]'), function (f) { if (!f.hasAttribute('data-mi-manual')) window.miWire(f); });
  var st = document.createElement('style');
  st.textContent = '.mi-status{background:#fdecea;color:#7a1f16;border-radius:10px;padding:12px 14px;margin:8px 0;font-weight:600}.mi-status a{color:inherit}.mi-ok{background:#eef6ec;border:2px solid #8DA98A;border-radius:14px;padding:20px;color:#2E2438}.mi-ok h3{margin:0 0 6px}';
  document.head.appendChild(st);
})();
