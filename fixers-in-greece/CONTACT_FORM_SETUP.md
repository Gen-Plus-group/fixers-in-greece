# Contact Form Setup Guide - Fixers in Greece

## Overview
The contact form has been set up to send nicely formatted emails to `enquiries@needafixer.com`. There are multiple implementation options depending on your hosting environment.

## 🎯 Current Implementation

### Primary Solution: PHP Handler
- **File**: `contact-form-handler.php`
- **Sends to**: `enquiries@needafixer.com`
- **Features**:
  - Formatted HTML emails with Greece branding
  - Auto-reply to customers
  - Form validation and security
  - Professional email templates

### Form Features
- ✅ **Required field validation**
- ✅ **Email format validation**
- ✅ **Project type selection**
- ✅ **Service checkboxes**
- ✅ **Budget range selection**
- ✅ **Professional email formatting**
- ✅ **Auto-reply to customers**
- ✅ **Security headers and sanitization**

## 🚀 Setup Instructions

### Option 1: PHP Server (Recommended)
If your hosting supports PHP:

1. **Upload the PHP handler**:
   ```bash
   # Upload contact-form-handler.php to your web root
   ```

2. **Test the form**:
   - Visit `/test-contact-form.html` to test functionality
   - Check if emails are received at `enquiries@needafixer.com`

3. **Configure email settings** (if needed):
   ```php
   / In contact-form-handler.php, update these if needed:
   $to_email = 'enquiries@needafixer.com';
   $from_email = 'noreply@fixersinGreece.com';
   ```

### Option 2: Formspree (No PHP Required)
If PHP is not available, use Formspree:

1. **Sign up at [Formspree.io](https://formspree.io)**

2. **Create a new form** and get your form ID

3. **Update the contact form**:
   ```html
   <!-- Change the form action in contact/index.html -->
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```

4. **Add Formspree configuration**:
   ```html
   <!-- Add these hidden fields to the form -->
   <input type="hidden" name="_subject" value="New Production Enquiry - Fixers Greece">
   <input type="hidden" name="_replyto" value="enquiries@needafixer.com">
   <input type="hidden" name="_next" value="/thank-you.html">
   ```

### Option 3: Netlify Forms (Netlify Hosting)
If hosted on Netlify:

1. **Add netlify attribute to form**:
   ```html
   <form netlify name="contact" action="/contact/" method="POST">
   ```

2. **Add hidden form-name field**:
   ```html
   <input type="hidden" name="form-name" value="contact">
   ```

3. **Configure notifications** in Netlify dashboard

### Option 4: EmailJS (Client-side)
For client-side email sending:

1. **Sign up at [EmailJS.com](https://www.emailjs.com)**

2. **Create email service and template**

3. **Include EmailJS script**:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
   ```

4. **Update configuration** in `contact-form-alternative.js`

## 📧 Email Template Features

### Main Notification Email
Sent to `enquiries@needafixer.com`:
- **Professional HTML formatting** with Greece branding
- **Complete contact information** (name, email, phone, company)
- **Project details** (type, services needed, budget, dates)
- **Formatted message** with proper line breaks
- **Timestamp and IP address** for tracking
- **Next steps checklist** for follow-up

### Auto-Reply Email
Sent to customer:
- **Thank you message** with Greece branding
- **24-hour response commitment**
- **Emergency contact information**
- **Professional signature**

## 🔧 Testing

### Test the Form
1. Visit `/test-contact-form.html`
2. Fill out the test form
3. Check for:
   - Email received at `enquiries@needafixer.com`
   - Auto-reply sent to test email
   - Proper formatting and branding

### Troubleshooting
- **PHP errors**: Check server error logs
- **Email not sending**: Verify server mail configuration
- **Form not submitting**: Check browser console for JavaScript errors

## 🎨 Email Template Preview

### Main Notification
```
🎬 NEW PRODUCTION ENQUIRY
Fixers in Greece - Professional Film Production Services

CONTACT INFORMATION:
Name: John Smith
Email: john@example.com
Company: ABC Productions
Phone: +1 234 567 8900

PROJECT DETAILS:
Project Type: Documentary
Services Needed: Location Scouting, Equipment Rental
Planned Shoot Dates: March 2024
Budget Range: $25,000 - $50,000

PROJECT DESCRIPTION:
We're planning a documentary about Greeceese culture...

NEXT STEPS:
• Respond to this enquiry within 24 hours
• Prepare detailed quote based on requirements
• Schedule consultation call if needed
• Send follow-up information about Greece filming
```

### Auto-Reply
```
🎬 THANK YOU FOR YOUR ENQUIRY!
Fixers in Greece - Professional Film Production Services

Dear John,

Thank you for contacting Fixers in Greece regarding your Documentary project.

We have received your enquiry and our team will respond within 24 hours with:
• Detailed quote for your requirements
• Information about filming in Greece
• Next steps for your production

For urgent matters, please call us directly at +44 (0) 20 8549 2259.

Best regards,
The Fixers in Greece Team
```

## 🔒 Security Features

- **Input sanitization** to prevent XSS attacks
- **Email validation** to prevent spam
- **Rate limiting** (can be added if needed)
- **CSRF protection** (can be enhanced)
- **Security headers** to prevent common attacks

## 📱 Mobile Optimization

- **Responsive form design** works on all devices
- **Touch-friendly inputs** for mobile users
- **Proper keyboard types** for email/phone fields
- **Accessible labels** and error messages

## 🎯 Next Steps

1. **Choose your preferred setup method** (PHP recommended)
2. **Test the form thoroughly** with real email addresses
3. **Monitor email delivery** and response times
4. **Consider adding** additional features like file uploads if needed

The contact form is now professional, secure, and ready to handle production enquiries with properly formatted emails sent to `enquiries@needafixer.com`!
