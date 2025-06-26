#!/usr/bin/env python3
"""
Fix structured data markup errors in HTML files.
This script identifies and fixes common schema.org markup issues.
"""

import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup
import html

def find_json_ld_scripts(soup):
    """Find all JSON-LD script tags in the HTML."""
    return soup.find_all('script', type='application/ld+json')

def validate_json_ld(script_content):
    """Validate JSON-LD content and return parsed JSON if valid."""
    try:
        # Remove any HTML entities
        content = html.unescape(script_content.strip())
        return json.loads(content)
    except json.JSONDecodeError as e:
        return None, str(e)

def fix_local_business_schema(data):
    """Fix common LocalBusiness schema issues."""
    fixed = False
    
    # Handle @graph structure
    if '@graph' in data:
        for item in data['@graph']:
            if fix_local_business_schema(item):
                fixed = True
        return fixed
    
    # Check if this is a LocalBusiness type
    schema_type = data.get('@type', '')
    if isinstance(schema_type, list):
        is_local_business = 'LocalBusiness' in schema_type
    else:
        is_local_business = schema_type == 'LocalBusiness'
    
    if not is_local_business:
        return False
    
    # Ensure required properties
    if 'name' not in data:
        data['name'] = 'Fixers in Greece'
        fixed = True
    
    # Fix address
    if 'address' not in data or not isinstance(data.get('address'), dict):
        data['address'] = {
            "@type": "PostalAddress",
            "streetAddress": "Professional filming services throughout Greece",
            "addressLocality": "Athens",
            "addressRegion": "Attica", 
            "postalCode": "10431",
            "addressCountry": "GR"
        }
        fixed = True
    else:
        address = data['address']
        if 'streetAddress' not in address:
            address['streetAddress'] = "Professional filming services throughout Greece"
            fixed = True
        if 'postalCode' not in address:
            address['postalCode'] = "10431"
            fixed = True
        if 'addressRegion' not in address:
            address['addressRegion'] = "Attica"
            fixed = True
        if address.get('addressCountry') == 'Greece':
            address['addressCountry'] = 'GR'
            fixed = True
    
    # Fix telephone
    if 'telephone' not in data:
        data['telephone'] = '+30 210 6821895'
        fixed = True
    
    # Add email if missing
    if 'email' not in data:
        data['email'] = 'greece@needafixer.com'
        fixed = True
    
    # Fix priceRange format
    if 'priceRange' in data:
        if data['priceRange'] in ['€€€', '$$$', '€€€€']:
            data['priceRange'] = '€€'
            fixed = True
    
    # Add logo/image if missing
    if 'logo' not in data and 'image' not in data:
        data['logo'] = {
            "@type": "ImageObject",
            "url": "https://www.fixersingreece.gr/assets/images/needafixer-greece-white.png",
            "width": 184,
            "height": 63
        }
        fixed = True
    
    # Fix URL
    if 'url' in data:
        if data['url'] == 'https://www.fixersingreece.gr':
            data['url'] = 'https://www.fixersingreece.gr/'
            fixed = True
    
    # Add @id for better linking
    if '@id' not in data:
        data['@id'] = 'https://www.fixersingreece.gr/#organization'
        fixed = True
    
    return fixed

def fix_breadcrumb_schema(data):
    """Fix BreadcrumbList schema issues."""
    fixed = False
    
    if data.get('@type') != 'BreadcrumbList':
        return False
    
    if 'itemListElement' in data:
        for item in data['itemListElement']:
            if 'item' in item and isinstance(item['item'], str):
                # Ensure URLs end with slash
                if not item['item'].endswith('/'):
                    item['item'] += '/'
                    fixed = True
    
    return fixed

def remove_duplicate_schemas(soup):
    """Remove duplicate JSON-LD scripts with identical content."""
    scripts = find_json_ld_scripts(soup)
    seen_content = set()
    removed = 0
    
    for script in scripts:
        content = script.string
        if content:
            content_stripped = content.strip()
            if content_stripped in seen_content:
                script.decompose()
                removed += 1
            else:
                seen_content.add(content_stripped)
    
    return removed

def process_html_file(filepath):
    """Process a single HTML file to fix structured data issues."""
    print(f"\nProcessing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    changes_made = False
    
    # First, remove duplicate schemas
    duplicates_removed = remove_duplicate_schemas(soup)
    if duplicates_removed > 0:
        print(f"  - Removed {duplicates_removed} duplicate schema(s)")
        changes_made = True
    
    # Process remaining schemas
    scripts = find_json_ld_scripts(soup)
    
    for script in scripts:
        if script.string:
            result = validate_json_ld(script.string)
            
            if isinstance(result, tuple) and result[0] is None:
                print(f"  - JSON parsing error: {result[1]}")
                continue
            
            data = result
            schema_fixed = False
            
            # Apply fixes based on schema type
            if fix_local_business_schema(data):
                schema_fixed = True
                print(f"  - Fixed LocalBusiness schema")
            
            if fix_breadcrumb_schema(data):
                schema_fixed = True
                print(f"  - Fixed BreadcrumbList schema")
            
            if schema_fixed:
                # Update the script content with fixed data
                script.string = json.dumps(data, indent=4, ensure_ascii=False)
                changes_made = True
    
    # Save the file if changes were made
    if changes_made:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"  ✓ Saved changes to {filepath}")
    else:
        print(f"  - No changes needed")
    
    return changes_made

def main():
    """Main function to process all HTML files."""
    base_dir = Path('/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece')
    
    # Find all HTML files with structured data
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip certain directories
        if any(skip in root for skip in ['node_modules', '.git', 'temp-clone']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                # Quick check if file contains structured data
                with open(filepath, 'r', encoding='utf-8') as f:
                    if 'application/ld+json' in f.read():
                        html_files.append(filepath)
    
    print(f"Found {len(html_files)} HTML files with structured data")
    
    fixed_files = 0
    for filepath in html_files:
        if process_html_file(filepath):
            fixed_files += 1
    
    print(f"\n✅ Fixed structured data in {fixed_files} files")

if __name__ == '__main__':
    main()