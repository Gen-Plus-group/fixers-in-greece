/**
 * Alternative Contact Form Handler
 * This provides fallback options for form submission when PHP is not available
 */

/ Configuration for different form services
const FORM_SERVICES = {
    / Formspree (free tier available)
    formspree: {
        endpoint: 'https://formspree.io/f/YOUR_FORM_ID', / Replace with actual Formspree form ID
        method: 'POST',
        headers: {
            'Accept': 'application/json'
        }
    },
    
    / Netlify Forms (if hosted on Netlify)
    netlify: {
        endpoint: '/', / Same page with netlify form handling
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        addHiddenField: true / Netlify requires form-name field
    },
    
    / EmailJS (client-side email service)
    emailjs: {
        serviceId: 'YOUR_SERVICE_ID',
        templateId: 'YOUR_TEMPLATE_ID',
        publicKey: 'YOUR_PUBLIC_KEY'
    }
};

/ Current service configuration
const CURRENT_SERVICE = 'formspree'; / Change this to switch services

/**
 * Initialize alternative form handling
 */
function initAlternativeFormHandler() {
    const form = document.getElementById('contact-form');
    if (!form) return;
    
    / Add service-specific modifications
    if (CURRENT_SERVICE === 'netlify' && FORM_SERVICES.netlify.addHiddenField) {
        addNetlifyFormField(form);
    }
    
    / Override form submission
    form.addEventListener('submit', handleAlternativeSubmission);
}

/**
 * Add Netlify form field
 */
function addNetlifyFormField(form) {
    / Add netlify form attribute
    form.setAttribute('netlify', '');
    form.setAttribute('name', 'contact');
    
    / Add hidden form-name field
    const hiddenField = document.createElement('input');
    hiddenField.type = 'hidden';
    hiddenField.name = 'form-name';
    hiddenField.value = 'contact';
    form.appendChild(hiddenField);
}

/**
 * Handle form submission with alternative service
 */
async function handleAlternativeSubmission(e) {
    e.preventDefault();
    
    const form = e.target;
    const submitButton = form.querySelector('button[type="submit"]');
    const originalButtonText = submitButton.textContent;
    
    / Show loading state
    submitButton.disabled = true;
    submitButton.textContent = 'Sending...';
    submitButton.classList.add('opacity-75');
    
    try {
        let success = false;
        
        switch (CURRENT_SERVICE) {
            case 'formspree':
                success = await submitToFormspree(form);
                break;
            case 'netlify':
                success = await submitToNetlify(form);
                break;
            case 'emailjs':
                success = await submitToEmailJS(form);
                break;
            default:
                throw new Error('No form service configured');
        }
        
        if (success) {
            showMessage('Thank you for your enquiry! We will respond within 24 hours.', 'success');
            form.reset();
        } else {
            throw new Error('Form submission failed');
        }
        
    } catch (error) {
        console.error('Form submission error:', error);
        showMessage('There was an error sending your message. Please try again or contact us directly at greece@needafixer.com', 'error');
    } finally {
        / Reset button state
        submitButton.disabled = false;
        submitButton.textContent = originalButtonText;
        submitButton.classList.remove('opacity-75');
    }
}

/**
 * Submit to Formspree
 */
async function submitToFormspree(form) {
    const config = FORM_SERVICES.formspree;
    const formData = new FormData(form);
    
    / Add additional fields for better email formatting
    formData.append('_subject', `New Production Enquiry from ${formData.get('first-name')} ${formData.get('last-name')}`);
    formData.append('_replyto', formData.get('email'));
    formData.append('_format', 'plain'); / or 'html'
    
    const response = await fetch(config.endpoint, {
        method: config.method,
        body: formData,
        headers: config.headers
    });
    
    return response.ok;
}

/**
 * Submit to Netlify Forms
 */
async function submitToNetlify(form) {
    const config = FORM_SERVICES.netlify;
    const formData = new FormData(form);
    
    / Convert to URL encoded for Netlify
    const urlEncoded = new URLSearchParams();
    for (const [key, value] of formData) {
        urlEncoded.append(key, value);
    }
    
    const response = await fetch(config.endpoint, {
        method: config.method,
        body: urlEncoded,
        headers: config.headers
    });
    
    return response.ok;
}

/**
 * Submit using EmailJS
 */
async function submitToEmailJS(form) {
    / Check if EmailJS is loaded
    if (typeof emailjs === 'undefined') {
        console.error('EmailJS not loaded');
        return false;
    }
    
    const config = FORM_SERVICES.emailjs;
    const formData = new FormData(form);
    
    / Convert FormData to object
    const templateParams = {};
    for (const [key, value] of formData) {
        templateParams[key] = value;
    }
    
    / Add additional template parameters
    templateParams.to_email = 'greece@needafixer.com';
    templateParams.reply_to = templateParams.email;
    
    try {
        const response = await emailjs.send(
            config.serviceId,
            config.templateId,
            templateParams,
            config.publicKey
        );
        return response.status === 200;
    } catch (error) {
        console.error('EmailJS error:', error);
        return false;
    }
}

/**
 * Create formatted email content for services that support it
 */
function createFormattedEmailContent(formData) {
    const services = [];
    if (formData.getAll('services[]')) {
        formData.getAll('services[]').forEach(service => {
            services.push(service);
        });
    }
    
    return `
NEW PRODUCTION ENQUIRY - Fixers in Greece
==========================================

CONTACT INFORMATION:
Name: ${formData.get('first-name')} ${formData.get('last-name')}
Email: ${formData.get('email')}
Company: ${formData.get('company') || 'Not provided'}
Phone: ${formData.get('phone') || 'Not provided'}

PROJECT DETAILS:
Project Type: ${formData.get('project-type')}
Services Needed: ${services.join(', ') || 'Not specified'}
Planned Shoot Dates: ${formData.get('shoot-dates') || 'Not specified'}
Budget Range: ${formData.get('budget') || 'Not specified'}

PROJECT DESCRIPTION:
${formData.get('message')}

==========================================
Submitted: ${new Date().toLocaleString()}
    `.trim();
}

/**
 * Show message function (same as in main contact form)
 */
function showMessage(message, type) {
    / Remove existing messages
    const existingMessages = document.querySelectorAll('.form-message');
    existingMessages.forEach(msg => msg.remove());
    
    / Create message element
    const messageDiv = document.createElement('div');
    messageDiv.className = `form-message p-4 rounded-md mb-6 ${type === 'success' ? 'bg-green-600 text-white' : 'bg-red-600 text-white'}`;
    messageDiv.textContent = message;
    
    / Insert message before form
    const form = document.getElementById('contact-form');
    form.parentNode.insertBefore(messageDiv, form);
    
    / Auto-remove message after 10 seconds
    setTimeout(() => {
        messageDiv.remove();
    }, 10000);
    
    / Scroll to message
    messageDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

/ Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    / Check if PHP handler is available first
    fetch('/contact-form-handler.php', { method: 'HEAD' })
        .then(response => {
            if (!response.ok) {
                console.log('PHP handler not available, using alternative form service');
                initAlternativeFormHandler();
            }
        })
        .catch(() => {
            console.log('PHP handler not available, using alternative form service');
            initAlternativeFormHandler();
        });
});

/ Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initAlternativeFormHandler,
        FORM_SERVICES,
        showMessage
    };
}
