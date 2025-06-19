#!/usr/bin/env python3
"""
Script to apply Tailwind CSS to all pages by updating their CSS links
"""

import os
import re
from pathlib import Path

def update_page_css(file_path):
    """Update a single HTML file to use Tailwind CSS"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it's already using Tailwind
        if '/dist/output.css' in content:
            print(f"✅ {file_path} already using Tailwind CSS")
            return True
            
        # Add Google Fonts if not present
        if 'fonts.googleapis.com' not in content:
            # Find the head section and add Google Fonts
            head_pattern = r'(<head[^>]*>)'
            if re.search(head_pattern, content):
                google_fonts = '''<link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">'''
                content = re.sub(head_pattern, r'\1' + google_fonts, content)
        
        # Add Tailwind CSS link
        # Look for existing stylesheet links and add Tailwind after them
        stylesheet_pattern = r'(<link[^>]*rel=["\']stylesheet["\'][^>]*>)'
        stylesheets = re.findall(stylesheet_pattern, content)
        
        if stylesheets:
            # Add Tailwind CSS after the last stylesheet
            last_stylesheet = stylesheets[-1]
            tailwind_link = '<link href="/dist/output.css" rel="stylesheet">'
            content = content.replace(last_stylesheet, last_stylesheet + tailwind_link)
        else:
            # If no stylesheets found, add to head
            head_pattern = r'(</head>)'
            if re.search(head_pattern, content):
                tailwind_link = '<link href="/dist/output.css" rel="stylesheet">'
                content = re.sub(head_pattern, tailwind_link + r'\1', content)
        
        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated {file_path} with Tailwind CSS")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update all pages"""
    # List of directories to update
    directories = [
        'clients',
        'contact', 
        'equipment-rental-vietnam',
        'film-permits-vietnam',
        'filming-in-vietnam',
        'location-scouting-vietnam',
        'portfolio'
    ]
    
    updated_count = 0
    total_count = 0
    
    print("🚀 Applying Tailwind CSS to all pages...")
    print("=" * 50)
    
    for directory in directories:
        index_file = Path(directory) / 'index.html'
        if index_file.exists():
            total_count += 1
            if update_page_css(index_file):
                updated_count += 1
        else:
            print(f"⚠️  {index_file} not found")
    
    print("=" * 50)
    print(f"📊 Summary: {updated_count}/{total_count} pages updated successfully")
    
    if updated_count == total_count:
        print("🎉 All pages now have Tailwind CSS!")
    else:
        print("⚠️  Some pages may need manual review")

if __name__ == "__main__":
    main()
