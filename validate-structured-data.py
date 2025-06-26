#!/usr/bin/env python3
"""
Validate structured data in HTML files after fixes.
"""

import os
import json
import re
from pathlib import Path

def extract_json_ld_blocks(content):
    """Extract all JSON-LD blocks from HTML content."""
    pattern = r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>'
    matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
    return matches

def validate_json_ld(json_string):
    """Validate JSON-LD and check for common issues."""
    try:
        data = json.loads(json_string)
        issues = []
        
        # Check if it's a list (multiple schemas) or single schema
        schemas = data if isinstance(data, list) else [data]
        
        for schema in schemas:
            if not isinstance(schema, dict):
                continue
                
            # Check LocalBusiness requirements
            if schema.get('@type') == 'LocalBusiness':
                # Required fields
                if 'name' not in schema:
                    issues.append("Missing 'name' in LocalBusiness")
                if 'address' not in schema:
                    issues.append("Missing 'address' in LocalBusiness")
                if 'telephone' not in schema:
                    issues.append("Missing 'telephone' in LocalBusiness")
                
                # Check address structure
                if 'address' in schema:
                    addr = schema['address']
                    if isinstance(addr, dict):
                        if 'streetAddress' not in addr:
                            issues.append("Missing 'streetAddress' in address")
                        if 'postalCode' not in addr:
                            issues.append("Missing 'postalCode' in address")
                        if 'addressRegion' not in addr:
                            issues.append("Missing 'addressRegion' in address")
                        if 'addressCountry' in addr and addr['addressCountry'] == 'Greece':
                            issues.append("addressCountry should be 'GR' not 'Greece'")
                
                # Check optional but recommended fields
                if 'email' not in schema:
                    issues.append("Missing 'email' (recommended)")
                if 'logo' not in schema and 'image' not in schema:
                    issues.append("Missing 'logo' or 'image' (recommended)")
                if 'priceRange' in schema and schema['priceRange'] == '€€€':
                    issues.append("priceRange '€€€' should be '€€'")
                    
        return True, issues
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {str(e)}"]

def check_file(filepath):
    """Check a single HTML file for structured data issues."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return None, [f"Error reading file: {str(e)}"]
    
    json_blocks = extract_json_ld_blocks(content)
    if not json_blocks:
        return None, ["No JSON-LD structured data found"]
    
    all_issues = []
    valid_count = 0
    
    for i, block in enumerate(json_blocks):
        block = block.strip()
        valid, issues = validate_json_ld(block)
        if valid:
            valid_count += 1
        if issues:
            all_issues.extend([f"Block {i+1}: {issue}" for issue in issues])
    
    # Check for duplicates
    if len(json_blocks) > 1:
        # Simple duplicate check based on cleaned content
        cleaned_blocks = [re.sub(r'\s+', ' ', block.strip()) for block in json_blocks]
        if len(cleaned_blocks) != len(set(cleaned_blocks)):
            all_issues.append("Duplicate JSON-LD blocks detected")
    
    return valid_count, all_issues

def main():
    """Main function to validate all HTML files."""
    base_dir = Path('/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece')
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip certain directories
        if any(skip in root for skip in ['node_modules', '.git', 'temp-clone', 'backup']):
            continue
            
        for file in files:
            if file.endswith('.html') and not file.startswith('index-'):
                filepath = os.path.join(root, file)
                html_files.append(filepath)
    
    print(f"Checking {len(html_files)} HTML files for structured data...\n")
    
    files_with_issues = 0
    total_issues = 0
    files_without_data = 0
    
    for filepath in sorted(html_files):
        valid_count, issues = check_file(filepath)
        
        if valid_count is None:
            # No structured data
            files_without_data += 1
        elif issues:
            files_with_issues += 1
            total_issues += len(issues)
            print(f"\n❌ {filepath}")
            for issue in issues[:5]:  # Show first 5 issues
                print(f"   - {issue}")
            if len(issues) > 5:
                print(f"   ... and {len(issues) - 5} more issues")
    
    print(f"\n" + "="*60)
    print(f"Summary:")
    print(f"- Total files checked: {len(html_files)}")
    print(f"- Files without structured data: {files_without_data}")
    print(f"- Files with issues: {files_with_issues}")
    print(f"- Total issues found: {total_issues}")
    print(f"- Files with valid structured data: {len(html_files) - files_without_data - files_with_issues}")

if __name__ == '__main__':
    main()