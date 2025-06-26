#!/usr/bin/env python3
"""
Fix structured data markup errors in HTML files.
This script identifies and fixes common schema.org markup issues.
"""

import os
import re
import json
from pathlib import Path

def extract_json_ld_blocks(content):
    """Extract all JSON-LD script blocks from HTML content."""
    pattern = r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>'
    matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
    return matches

def validate_and_parse_json(json_str):
    """Validate JSON-LD content and return parsed JSON if valid."""
    try:
        # Clean up the JSON string
        json_str = json_str.strip()
        return json.loads(json_str), None
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
    
    # Fix URL - ensure trailing slash
    if 'url' in data:
        url = data['url']
        if url == 'https://www.fixersingreece.gr':
            data['url'] = 'https://www.fixersingreece.gr/'
            fixed = True
        elif url.startswith('https://www.fixersingreece.gr') and not url.endswith('/') and '.' not in url.split('/')[-1]:
            data['url'] = url + '/'
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
                # Ensure URLs end with slash for directories
                url = item['item']
                if url.startswith('https://www.fixersingreece.gr') and not url.endswith('/') and '.' not in url.split('/')[-1]:
                    item['item'] = url + '/'
                    fixed = True
    
    return fixed

def fix_service_schema(data):
    """Fix Service schema issues."""
    fixed = False
    
    if data.get('@type') == 'Service' or (isinstance(data.get('@type'), list) and 'Service' in data.get('@type', [])):
        # Ensure provider reference
        if 'provider' not in data:
            data['provider'] = {"@id": "https://www.fixersingreece.gr/#organization"}
            fixed = True
        
        # Ensure areaServed
        if 'areaServed' not in data:
            data['areaServed'] = "Greece"
            fixed = True
    
    return fixed

def process_html_file(filepath):
    """Process a single HTML file to fix structured data issues."""
    print(f"\nProcessing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract JSON-LD blocks
    json_blocks = extract_json_ld_blocks(content)
    
    if not json_blocks:
        print(f"  - No JSON-LD structured data found")
        return False
    
    # Check for duplicates
    unique_blocks = []
    seen = set()
    
    for block in json_blocks:
        block_clean = block.strip()
        if block_clean not in seen:
            seen.add(block_clean)
            unique_blocks.append(block)
    
    if len(unique_blocks) < len(json_blocks):
        print(f"  - Found {len(json_blocks) - len(unique_blocks)} duplicate schema(s)")
    
    # Process each unique block
    new_content = content
    changes_made = False
    
    for i, block in enumerate(unique_blocks):
        data, error = validate_and_parse_json(block)
        
        if error:
            print(f"  - JSON parsing error in block {i+1}: {error}")
            continue
        
        schema_fixed = False
        
        # Apply fixes based on schema type
        if fix_local_business_schema(data):
            schema_fixed = True
            print(f"  - Fixed LocalBusiness schema in block {i+1}")
        
        if fix_breadcrumb_schema(data):
            schema_fixed = True
            print(f"  - Fixed BreadcrumbList schema in block {i+1}")
            
        if fix_service_schema(data):
            schema_fixed = True
            print(f"  - Fixed Service schema in block {i+1}")
        
        if schema_fixed:
            # Replace the old JSON with the fixed JSON
            new_json = json.dumps(data, indent=4, ensure_ascii=False)
            # Find and replace this specific block in the content
            old_script = f'<script type="application/ld+json">{block}</script>'
            new_script = f'<script type="application/ld+json">\n{new_json}\n</script>'
            new_content = new_content.replace(old_script, new_script, 1)
            changes_made = True
    
    # Remove duplicate script tags if any
    if len(unique_blocks) < len(json_blocks):
        # Remove duplicate occurrences
        for block in json_blocks:
            if json_blocks.count(block) > 1:
                # Keep only the first occurrence
                count = json_blocks.count(block) - 1
                for _ in range(count):
                    old_script = f'<script type="application/ld+json">{block}</script>'
                    # Remove one occurrence at a time
                    parts = new_content.split(old_script, 1)
                    if len(parts) > 1:
                        new_content = parts[0] + parts[1]
                        changes_made = True
    
    # Save the file if changes were made
    if changes_made:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
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
        if any(skip in root for skip in ['node_modules', '.git', 'temp-clone', 'backup']):
            continue
            
        for file in files:
            if file.endswith('.html') and not file.startswith('index-'):
                filepath = os.path.join(root, file)
                # Quick check if file contains structured data
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        if 'application/ld+json' in f.read():
                            html_files.append(filepath)
                except:
                    continue
    
    print(f"Found {len(html_files)} HTML files with structured data")
    
    fixed_files = 0
    for filepath in sorted(html_files):
        if process_html_file(filepath):
            fixed_files += 1
    
    print(f"\n✅ Fixed structured data in {fixed_files} files")

if __name__ == '__main__':
    main()