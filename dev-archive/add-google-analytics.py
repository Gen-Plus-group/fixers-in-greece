#!/usr/bin/env python3
"""
Script to add Google Analytics tracking code to all HTML pages
"""

import os
import re
from pathlib import Path

# Google Analytics tracking code
GA_CODE = '''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-FD4LC3V4DB"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-FD4LC3V4DB');
    </script>
    '''

def add_ga_to_file(file_path):
    """Add Google Analytics code to a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if GA code already exists
        if 'G-FD4LC3V4DB' in content:
            print(f"✅ {file_path} - Already has Google Analytics")
            return True
        
        # Find the best place to insert GA code (before </head>)
        if '</head>' in content:
            # Insert before closing head tag
            content = content.replace('</head>', f'{GA_CODE}\n</head>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ {file_path} - Added Google Analytics")
            return True
        else:
            print(f"❌ {file_path} - No </head> tag found")
            return False
            
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Add Google Analytics to all HTML pages"""
    print("🚀 Adding Google Analytics to all HTML pages...")
    
    # List of HTML files to update
    html_files = [
        # Service pages
        'equipment-rental-vietnam/index.html',
        'location-scouting-vietnam/index.html',
        'film-permits-vietnam/index.html',
        'filming-in-vietnam/index.html',
        
        # Main pages
        'portfolio/index.html',
        'clients/index.html',
        
        # Thank you and utility pages
        'thank-you.html',
        'form-success.html',
        
        # Test pages
        'test-contact-form.html',
        'form-enhancement-test.html',
        'thank-you-test.html'
    ]
    
    success_count = 0
    total_count = len(html_files)
    
    for file_path in html_files:
        if os.path.exists(file_path):
            if add_ga_to_file(file_path):
                success_count += 1
        else:
            print(f"⚠️  {file_path} - File not found")
    
    print(f"\n📊 Results: {success_count}/{total_count} files updated successfully")
    
    # Also add enhanced tracking to contact form
    print("\n🎯 Adding enhanced tracking to contact form...")
    add_form_tracking()
    
    print("\n🎉 Google Analytics installation complete!")

def add_form_tracking():
    """Add enhanced form tracking to contact page"""
    contact_file = 'contact/index.html'
    
    if not os.path.exists(contact_file):
        print(f"❌ {contact_file} not found")
        return
    
    try:
        with open(contact_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if enhanced tracking is already added
        if 'form_submission' in content:
            print(f"✅ {contact_file} - Already has enhanced form tracking")
            return
        
        # Add form submission tracking to the form submission handler
        tracking_code = '''
                    // Track form submission for analytics
                    if (typeof gtag !== 'undefined') {
                        gtag('event', 'form_submission', {
                            'event_category': 'Contact',
                            'event_label': 'Production Enquiry',
                            'value': 1
                        });
                    }'''
        
        # Find the form submission section and add tracking
        if 'Show loading state' in content:
            content = content.replace(
                '// Show loading state',
                f'{tracking_code}\n                    \n                    // Show loading state'
            )
            
            with open(contact_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ {contact_file} - Added enhanced form tracking")
        else:
            print(f"⚠️  {contact_file} - Could not find form submission section")
            
    except Exception as e:
        print(f"❌ {contact_file} - Error adding form tracking: {e}")

if __name__ == "__main__":
    main()
