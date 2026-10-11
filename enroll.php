<?php
// Enrollment form handler for maasinspiration.org (GoDaddy cPanel). Emails submissions to $TO below.
$TO = 'aslamhemani@gmail.com';   // TEMPORARY: switch to hello@maasinspiration.org once that mailbox exists
$FROM = 'no-reply@maasinspiration.org';   // must be an address on this domain for deliverability
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: /programs.html'); exit; }
if (!empty($_POST['website'])) { header('Location: /thank-you.html'); exit; }   // honeypot: bots fill it
$clean = function($v){ $v = is_array($v) ? implode(', ', $v) : (string)$v; return trim(str_replace(["\r","\n"], ' ', substr($v, 0, 2000))); };
$form = $clean($_POST['form'] ?? 'Enrollment');
$allowed = ["Maa's Place enrollment", 'Blooming Star Village interest list', 'Volunteer sign-up'];
if (!in_array($form, $allowed, true)) { http_response_code(400); exit('Bad request'); }
if ($form === 'Volunteer sign-up' && (empty($_POST['programs']) || empty($_POST['agree_code_of_conduct']) || empty($_POST['age_18_or_guardian']))) { http_response_code(400); exit('Please choose a program and tick the required boxes.'); }
if ($form === 'Volunteer sign-up') { foreach (['photo_consent'=>'No'] as $k=>$d) if (!isset($_POST[$k])) $_POST[$k] = $d; }
$lines = [];
foreach ($_POST as $k => $v) { if (in_array($k, ['website','form'], true)) continue;
  $lines[] = ucwords(str_replace('_',' ', preg_replace('/[^a-z0-9_]/i','',$k))) . ': ' . $clean($v); }
if (count(array_filter($lines, fn($l) => !preg_match('/:\s*$/', $l))) < 2) { http_response_code(400); exit('Please fill out the form.'); }
$email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);
$headers = "From: MAA's Inspiration Website <$FROM>\r\nContent-Type: text/plain; charset=UTF-8\r\n" . ($email ? "Reply-To: $email\r\n" : '');
$body = "New submission: $form\nReceived: " . date('Y-m-d H:i') . "\n\n" . implode("\n", $lines) . "\n";
$ok = mail($TO, "New $form" . (!empty($_POST['full_name']) ? ' – ' . $clean($_POST['full_name']) : ''), $body, $headers, "-f$FROM");
header('Location: /thank-you.html' . ($ok ? '' : '?error=1')); exit;
