#!/usr/bin/env python3
"""
Script to bulk update navigation on all remaining pages
"""

import os
import re

def update_navigation_in_file(file_path):
    """Update navigation in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update desktop navigation
        desktop_old = r'(\s*<a href="/hire-film-producer/"[^>]*>Hire Film Producer</a>)\s*</div>'
        desktop_new = '''\\1
                            <a href="/hire-line-producer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Line Producer</a>
                            <a href="/hire-fixer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Fixer</a>
                            <a href="/hire-dop/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire DOP</a>
                            <a href="/hire-location-manager/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Location Manager</a>
                        </div>'''
        
        content = re.sub(desktop_old, desktop_new, content)
        
        # Update mobile navigation
        mobile_old = r'(\s*<a href="/hire-film-producer/"[^>]*>Hire Film Producer</a>)\s*</div>'
        mobile_new = '''\\1
                            <a href="/hire-line-producer/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Line Producer</a>
                            <a href="/hire-fixer/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Fixer</a>
                            <a href="/hire-dop/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire DOP</a>
                            <a href="/hire-location-manager/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Location Manager</a>
                        </div>'''
        
        content = re.sub(mobile_old, mobile_new, content)
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} - Navigation updated")
        return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Update navigation on all pages"""
    print("🚀 Bulk updating navigation...")
    
    # Get all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == 'index.html' and 'hire-' not in root:
                html_files.append(os.path.join(root, file))
    
    # Remove the main index.html as we already updated it
    html_files = [f for f in html_files if f != './index.html']
    
    success_count = 0
    for file_path in html_files:
        if update_navigation_in_file(file_path):
            success_count += 1
    
    print(f"\n📊 Updated {success_count}/{len(html_files)} files")

if __name__ == "__main__":
    main()
