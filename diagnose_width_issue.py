#!/usr/bin/env python3
"""
Diagnose horizontal scrolling issues
"""

import os
import re
from pathlib import Path

def check_file_for_issues(file_path):
    """Check a single file for potential width issues"""
    issues = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for various potential issues
        patterns = [
            (r'min-width:\s*\d{4,}px', 'Large min-width found'),
            (r'width:\s*\d{4,}px', 'Large fixed width found'),
            (r'width:\s*100vw(?!;?\s*max-width)', '100vw without max-width constraint'),
            (r'margin-left:\s*-\d{3,}px', 'Large negative margin-left'),
            (r'margin-right:\s*-\d{3,}px', 'Large negative margin-right'),
            (r'left:\s*-\d{3,}px', 'Large negative left position'),
            (r'right:\s*-\d{3,}px', 'Large negative right position'),
            (r'translateX\(-?\d{3,}', 'Large translateX value'),
            (r'padding-left:\s*\d{3,}px', 'Large padding-left'),
            (r'padding-right:\s*\d{3,}px', 'Large padding-right'),
            (r'\.mega-menu[^{]*\{[^}]*width:\s*\d+px', 'Mega menu with fixed width'),
            (r'position:\s*absolute[^}]*width:\s*\d{4,}px', 'Absolute positioned element with large width'),
            (r'class="[^"]*w-\[\d{4,}px\]', 'Tailwind arbitrary width class'),
        ]
        
        for pattern, desc in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.MULTILINE | re.DOTALL)
            if matches:
                for match in matches:
                    issues.append(f"{desc}: {match}")
        
        # Check for missing overflow-x-hidden on body
        body_match = re.search(r'<body([^>]*?)>', content)
        if body_match and 'overflow-x-hidden' not in body_match.group(1):
            issues.append("Body tag missing overflow-x-hidden class")
        
        # Check for elements that might overflow
        overflow_elements = [
            (r'<table[^>]*>', 'Table without responsive wrapper'),
            (r'<pre[^>]*>', 'Pre tag that might overflow'),
            (r'<code[^>]*>[^<]{200,}', 'Long code block'),
        ]
        
        for pattern, desc in overflow_elements:
            if re.search(pattern, content):
                issues.append(desc)
        
        return issues
        
    except Exception as e:
        return [f"Error reading file: {str(e)}"]

def main():
    """Main function to diagnose width issues"""
    print("Diagnosing horizontal scrolling issues...")
    print("=" * 60)
    
    # Check key files
    key_files = [
        'index.html',
        'css/layout.css',
        'css/base.css',
        'css/components.css',
        'dist/output.css',
        'components/header.html',
        'components/navigation.html'
    ]
    
    issues_found = {}
    
    # Check key files first
    for file_path in key_files:
        if os.path.exists(file_path):
            issues = check_file_for_issues(file_path)
            if issues:
                issues_found[file_path] = issues
    
    # Check a sample of HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in root or 'backup' in root:
            continue
        for file in files:
            if file.endswith('.html') and not file.endswith('-backup.html'):
                html_files.append(os.path.join(root, file))
    
    # Check first 10 HTML files
    for file_path in html_files[:10]:
        issues = check_file_for_issues(file_path)
        if issues:
            issues_found[file_path] = issues
    
    # Report findings
    if issues_found:
        print("\n🔍 Potential Issues Found:")
        print("=" * 60)
        for file_path, issues in issues_found.items():
            print(f"\n📄 {file_path}:")
            for issue in issues:
                print(f"   ⚠️  {issue}")
    else:
        print("\n✅ No obvious width issues found in checked files.")
    
    # Check CSS for global overflow settings
    print("\n\n🔍 Checking CSS for overflow fixes...")
    print("=" * 60)
    
    css_files = ['css/base.css', 'src/input.css', 'dist/output.css']
    for css_file in css_files:
        if os.path.exists(css_file):
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            has_html_overflow = 'html' in content and 'overflow-x: hidden' in content
            has_body_overflow = 'body' in content and 'overflow-x: hidden' in content
            
            print(f"\n{css_file}:")
            print(f"  - HTML overflow-x: hidden: {'✅ Yes' if has_html_overflow else '❌ No'}")
            print(f"  - Body overflow-x: hidden: {'✅ Yes' if has_body_overflow else '❌ No'}")
    
    # Suggest fixes
    print("\n\n💡 Recommended Fixes:")
    print("=" * 60)
    print("1. Ensure all HTML files have <body class='overflow-x-hidden'>")
    print("2. Add to base CSS:")
    print("   html, body { overflow-x: hidden; max-width: 100%; }")
    print("3. Check for elements with fixed widths > 1200px")
    print("4. Wrap tables in responsive containers")
    print("5. Use max-width instead of width for large elements")

if __name__ == "__main__":
    main()