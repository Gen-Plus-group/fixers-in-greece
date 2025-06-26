<?php
/**
 * Contact Form Handler for Fixers in Greece
 * Optimized Backend with Security, Performance & Logging
 * Sends formatted emails to greece@needafixer.com
 */

/ Start session for rate limiting
session_start();

/ Enhanced security headers
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: DENY');
header('X-XSS-Protection: 1; mode=block');
header('Referrer-Policy: strict-origin-when-cross-origin');
header('Content-Security-Policy: default-src \'self\'');

/ Rate limiting (max 3 submissions per hour per IP)
$ip = $_SERVER['REMOTE_ADDR'];
$current_time = time();
$rate_limit_key = 'contact_form_' . md5($ip);

if (!isset($_SESSION[$rate_limit_key])) {
    $_SESSION[$rate_limit_key] = [];
}

/ Clean old submissions (older than 1 hour)
$_SESSION[$rate_limit_key] = array_filter($_SESSION[$rate_limit_key], function($timestamp) use ($current_time) {
    return ($current_time - $timestamp) < 3600;
});

/ Check rate limit
if (count($_SESSION[$rate_limit_key]) >= 3) {
    http_response_code(429);
    header('Content-Type: application/json');
    echo json_encode([
        'success' => false, 
        'message' => 'Too many requests. Please wait before submitting again.'
    ]);
    exit;
}

/ Only allow POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    die('Method not allowed');
}

/ Configuration
$to_email = 'greece@needafixer.com';
$from_email = 'noreply@fixersinGreece.com';
$subject_prefix = '[Fixers Greece] New Production Enquiry';

/ Function to sanitize input
function sanitize_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

/ Function to validate email
function validate_email($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}

/ Collect and sanitize form data
$first_name = sanitize_input($_POST['first-name'] ?? '');
$last_name = sanitize_input($_POST['last-name'] ?? '');
$email = sanitize_input($_POST['email'] ?? '');
$company = sanitize_input($_POST['company'] ?? '');
$phone = sanitize_input($_POST['phone'] ?? '');
$project_type = sanitize_input($_POST['project-type'] ?? '');
$services = $_POST['services'] ?? [];
$shoot_dates = sanitize_input($_POST['shoot-dates'] ?? '');
$budget = sanitize_input($_POST['budget'] ?? '');
$message = sanitize_input($_POST['message'] ?? '');

/ Validation
$errors = [];

if (empty($first_name)) {
    $errors[] = 'First name is required';
}

if (empty($last_name)) {
    $errors[] = 'Last name is required';
}

if (empty($email)) {
    $errors[] = 'Email is required';
} elseif (!validate_email($email)) {
    $errors[] = 'Invalid email format';
}

if (empty($project_type)) {
    $errors[] = 'Project type is required';
}

if (empty($message)) {
    $errors[] = 'Project details are required';
}

/ If there are validation errors, return them
if (!empty($errors)) {
    http_response_code(400);
    header('Content-Type: application/json');
    echo json_encode(['success' => false, 'errors' => $errors]);
    exit;
}

/ Process services array
$services_text = '';
if (!empty($services)) {
    $service_labels = [
        'location-scouting' => 'Location Scouting',
        'equipment-rental' => 'Equipment Rental',
        'permits' => 'Film Permits',
        'crew' => 'Local Crew',
        'drone-filming' => 'Drone Filming',
        'documentary' => 'Documentary Services',
        'commercial-production' => 'Commercial Production',
        'corporate-video' => 'Corporate Video',
        'music-video' => 'Music Video Production',
        'event-filming' => 'Event Filming',
        'live-streaming' => 'Live Streaming',
        'news-filming' => 'News & Current Affairs',
        'post-production' => 'Post-Production',
        'translation' => 'Translation Services',
        'casting' => 'Casting Services',
        'equipment-transport' => 'Equipment Transport',
        'full-production' => 'Full Production Support'
    ];
    
    $selected_services = [];
    foreach ($services as $service) {
        if (isset($service_labels[$service])) {
            $selected_services[] = $service_labels[$service];
        }
    }
    $services_text = implode(', ', $selected_services);
} else {
    $services_text = 'Not specified';
}

/ Format budget
$budget_labels = [
    'under-10k' => 'Under $10,000',
    '10k-25k' => '$10,000 - $25,000',
    '25k-50k' => '$25,000 - $50,000',
    '50k-100k' => '$50,000 - $100,000',
    'over-100k' => 'Over $100,000',
    'discuss' => 'Prefer to Discuss'
];
$budget_text = isset($budget_labels[$budget]) ? $budget_labels[$budget] : 'Not specified';

/ Format project type
$project_type_labels = [
    'documentary' => 'Documentary',
    'commercial' => 'Commercial Production',
    'news' => 'News/Current Affairs',
    'corporate' => 'Corporate Video',
    'music-video' => 'Music Video',
    'event' => 'Event Filming',
    'live-streaming' => 'Live Streaming',
    'feature' => 'Feature Film',
    'other' => 'Other'
];
$project_type_text = isset($project_type_labels[$project_type]) ? $project_type_labels[$project_type] : $project_type;

/ Create email subject
$subject = $subject_prefix . ' - ' . $project_type_text . ' from ' . $first_name . ' ' . $last_name;

/ Create HTML email content
$html_message = '
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>New Production Enquiry</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .header { background-color: #f9a531; color: #000; padding: 20px; text-align: center; }
        .content { padding: 20px; }
        .section { margin-bottom: 20px; }
        .label { font-weight: bold; color: #f9a531; }
        .value { margin-left: 10px; }
        .message-box { background-color: #f5f5f5; padding: 15px; border-left: 4px solid #f9a531; margin: 15px 0; }
        .footer { background-color: #2d3748; color: #fff; padding: 15px; text-align: center; font-size: 12px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎬 New Production Enquiry</h1>
        <p>Fixers in Greece - Professional Film Production Services</p>
    </div>
    
    <div class="content">
        <div class="section">
            <h2 style="color: #f9a531; border-bottom: 2px solid #f9a531; padding-bottom: 5px;">Contact Information</h2>
            <p><span class="label">Name:</span><span class="value">' . $first_name . ' ' . $last_name . '</span></p>
            <p><span class="label">Email:</span><span class="value"><a href="mailto:' . $email . '">' . $email . '</a></span></p>
            ' . (!empty($company) ? '<p><span class="label">Company:</span><span class="value">' . $company . '</span></p>' : '') . '
            ' . (!empty($phone) ? '<p><span class="label">Phone:</span><span class="value"><a href="tel:' . $phone . '">' . $phone . '</a></span></p>' : '') . '
        </div>
        
        <div class="section">
            <h2 style="color: #f9a531; border-bottom: 2px solid #f9a531; padding-bottom: 5px;">Project Details</h2>
            <p><span class="label">Project Type:</span><span class="value">' . $project_type_text . '</span></p>
            <p><span class="label">Services Needed:</span><span class="value">' . $services_text . '</span></p>
            ' . (!empty($shoot_dates) ? '<p><span class="label">Planned Shoot Dates:</span><span class="value">' . $shoot_dates . '</span></p>' : '') . '
            <p><span class="label">Budget Range:</span><span class="value">' . $budget_text . '</span></p>
        </div>
        
        <div class="section">
            <h2 style="color: #f9a531; border-bottom: 2px solid #f9a531; padding-bottom: 5px;">Project Description</h2>
            <div class="message-box">
                ' . nl2br($message) . '
            </div>
        </div>
        
        <div class="section">
            <h2 style="color: #f9a531; border-bottom: 2px solid #f9a531; padding-bottom: 5px;">Next Steps</h2>
            <ul>
                <li>Respond to this enquiry within 24 hours</li>
                <li>Prepare detailed quote based on requirements</li>
                <li>Schedule consultation call if needed</li>
                <li>Send follow-up information about Greece filming</li>
            </ul>
        </div>
    </div>
    
    <div class="footer">
        <p>This enquiry was submitted through the Fixers in Greece website contact form.</p>
        <p>Timestamp: ' . date('Y-m-d H:i:s T') . '</p>
        <p>IP Address: ' . $_SERVER['REMOTE_ADDR'] . '</p>
    </div>
</body>
</html>';

/ Create plain text version
$text_message = "NEW PRODUCTION ENQUIRY - Fixers in Greece\n";
$text_message .= "==========================================\n\n";
$text_message .= "CONTACT INFORMATION:\n";
$text_message .= "Name: " . $first_name . " " . $last_name . "\n";
$text_message .= "Email: " . $email . "\n";
if (!empty($company)) $text_message .= "Company: " . $company . "\n";
if (!empty($phone)) $text_message .= "Phone: " . $phone . "\n";
$text_message .= "\nPROJECT DETAILS:\n";
$text_message .= "Project Type: " . $project_type_text . "\n";
$text_message .= "Services Needed: " . $services_text . "\n";
if (!empty($shoot_dates)) $text_message .= "Planned Shoot Dates: " . $shoot_dates . "\n";
$text_message .= "Budget Range: " . $budget_text . "\n";
$text_message .= "\nPROJECT DESCRIPTION:\n";
$text_message .= $message . "\n";
$text_message .= "\n==========================================\n";
$text_message .= "Submitted: " . date('Y-m-d H:i:s T') . "\n";
$text_message .= "IP Address: " . $_SERVER['REMOTE_ADDR'] . "\n";

/ Email headers
$headers = [
    'MIME-Version: 1.0',
    'Content-Type: text/html; charset=UTF-8',
    'From: Fixers Greece Website <' . $from_email . '>',
    'Reply-To: ' . $email,
    'X-Mailer: PHP/' . phpversion(),
    'X-Priority: 1',
    'Importance: High'
];

/ Logging function
function log_submission($data, $status) {
    $log_entry = [
        'timestamp' => date('Y-m-d H:i:s T'),
        'ip' => $_SERVER['REMOTE_ADDR'],
        'user_agent' => $_SERVER['HTTP_USER_AGENT'] ?? 'Unknown',
        'status' => $status,
        'email' => $data['email'] ?? 'Unknown',
        'project_type' => $data['project_type'] ?? 'Unknown',
        'company' => $data['company'] ?? 'None'
    ];
    
    $log_line = json_encode($log_entry) . "\n";
    error_log($log_line, 3, __DIR__ . '/logs/contact_submissions.log');
}

/ Create logs directory if it doesn't exist
$log_dir = __DIR__ . '/logs';
if (!file_exists($log_dir)) {
    mkdir($log_dir, 0755, true);
}

/ Send email with error handling
$mail_sent = false;
try {
    $mail_sent = mail($to_email, $subject, $html_message, implode("\r\n", $headers));
    if ($mail_sent) {
        log_submission($_POST, 'success');
        / Add to rate limiting counter
        $_SESSION[$rate_limit_key][] = $current_time;
    } else {
        log_submission($_POST, 'mail_failed');
        error_log("Failed to send email for enquiry from: " . $email);
    }
} catch (Exception $e) {
    log_submission($_POST, 'error');
    error_log("Email sending exception: " . $e->getMessage());
}

/ Send auto-reply to customer
$auto_reply_subject = 'Thank you for contacting Fixers in Greece';
$auto_reply_message = '
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Thank you for your enquiry</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .header { background-color: #f9a531; color: #000; padding: 20px; text-align: center; }
        .content { padding: 20px; }
        .footer { background-color: #2d3748; color: #fff; padding: 15px; text-align: center; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎬 Thank You for Your Enquiry!</h1>
        <p>Fixers in Greece - Professional Film Production Services</p>
    </div>
    
    <div class="content">
        <p>Dear ' . $first_name . ',</p>
        
        <p>Thank you for contacting Fixers in Greece regarding your <strong>' . $project_type_text . '</strong> project.</p>
        
        <p>We have received your enquiry and our team will respond within <strong>24 hours</strong> with:</p>
        <ul>
            <li>Detailed quote for your requirements</li>
            <li>Information about filming in Greece</li>
            <li>Next steps for your production</li>
        </ul>
        
        <p>For urgent matters, please call us directly at <strong><a href="tel:+302106821895">+30 210 6821895</a></strong>.</p>
        
        <p>We look forward to helping make your Greece production a success!</p>
        
        <p>Best regards,<br>
        <strong>The Fixers in Greece Team</strong></p>
    </div>
    
    <div class="footer">
        <p>Fixers in Greece | Professional Film Production Services</p>
        <p>Email: greece@needafixer.com | Phone: <a href="tel:+302106821895">+30 210 6821895</a></p>
        <p>Website: www.fixersinGreece.com</p>
    </div>
</body>
</html>';

$auto_reply_headers = [
    'MIME-Version: 1.0',
    'Content-Type: text/html; charset=UTF-8',
    'From: Fixers Greece <' . $from_email . '>',
    'X-Mailer: PHP/' . phpversion()
];

/ Send auto-reply
$auto_reply_sent = mail($email, $auto_reply_subject, $auto_reply_message, implode("\r\n", $auto_reply_headers));

/ Return response
header('Content-Type: application/json');

if ($mail_sent) {
    echo json_encode([
        'success' => true,
        'message' => 'Thank you for your enquiry! We will respond within 24 hours.',
        'auto_reply_sent' => $auto_reply_sent
    ]);
} else {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'message' => 'Sorry, there was an error sending your message. Please try again or contact us directly.'
    ]);
}
?>
