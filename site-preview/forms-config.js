/* Maa's Inspiration online forms – ONE place for the backend contract.
   Change the endpoint or version here; no other file needs editing.
   Never put keys, passcodes or personal data in this file. */
window.MAAS_FORMS_CONFIG = {
  endpoint: "https://csfydwvxzuidvtumjxcv.supabase.co/functions/v1/public-forms",
  agreement_version: "v3-2026-10-19",
  timeout_ms: 45000,
  help_phone: "(469) 270-8156",
  help_tel: "+14692708156",
  timezone: "America/Chicago",
  /* form_type values the backend accepts */
  form_types: ["meals_recipient", "bloom_fee_agreement", "bloom_rights_ack", "bloom_grievance", "driver_agreement", "volunteer_sms_consent", "maas_place_enrollment", "volunteer_signup"],
  /* Request body sent as JSON (POST, Content-Type: application/json):
     { form_type, data:{...fields}, signer_name, agreement_version, consent_text,
       (no form uploads files; there is no files field),
       website: "" (hidden honeypot; bots fill it) }
     Expected reply: 2xx JSON with a reference number in one of:
     reference | reference_number | ref | id  */
  reference_keys: ["reference", "reference_number", "ref", "id"]
};
