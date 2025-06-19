#!/usr/bin/env python3
"""
Script to fix mega menu width issues across all pages
"""

import os
import re

def get_fixed_mega_menu_styles():
    """Return the fixed mega menu CSS styles"""
    return '''        /* Mega Menu Styles */
        .mega-menu {
            position: fixed;
            top: 100px; /* Adjust based on header height */
            left: 0;
            right: 0;
            width: 100vw;
            background: #1a1a1a;
            border-top: 2px solid #ff6b35;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            opacity: 0;
            visibility: hidden;
            transform: translateY(-10px);
            transition: all 0.3s ease;
            z-index: 50;
        }
        
        .mega-menu-trigger:hover .mega-menu {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }
        
        .mega-menu-column {
            border-right: 1px solid #333;
            min-width: 0; /* Allow columns to shrink */
        }
        
        .mega-menu-column:last-child {
            border-right: none;
        }
        
        .mega-menu-content {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        /* Responsive mega menu */
        @media (max-width: 1024px) {
            .mega-menu {
                display: none; /* Hide on mobile/tablet - use mobile menu instead */
            }
        }'''

def fix_mega_menu_html_structure(content):
    """Fix the mega menu HTML structure to use the new wrapper"""
    # Replace the mega menu container structure
    old_pattern = r'<div class="mega-menu">\s*<div class="container mx-auto px-4 py-8">\s*<div class="text-center mb-6">\s*<h3 class="text-xl font-bold text-vietnam-orange">Pre-Production Services</h3>\s*<p class="text-gray-400 text-sm">Planning, creative development, logistics</p>\s*</div>\s*<div class="grid grid-cols-6 gap-6">'
    
    new_structure = '''<div class="mega-menu">
                            <div class="mega-menu-content py-8">
                                <div class="text-center mb-6">
                                    <h3 class="text-xl font-bold text-vietnam-orange">Pre-Production Services</h3>
                                    <p class="text-gray-400 text-sm">Planning, creative development, logistics</p>
                                </div>
                                <div class="grid grid-cols-6 gap-8">'''
    
    content = re.sub(old_pattern, new_structure, content, flags=re.DOTALL)
    
    # Also handle simpler pattern matching
    content = content.replace(
        '<div class="container mx-auto px-4 py-8">',
        '<div class="mega-menu-content py-8">'
    )
    
    content = content.replace(
        '<div class="grid grid-cols-6 gap-6">',
        '<div class="grid grid-cols-6 gap-8">'
    )
    
    return content

def fix_page_mega_menu(file_path):
    """Fix mega menu width issues on a single page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if this page doesn't have mega menu
        if 'mega-menu' not in content:
            return True
        
        # Update mega menu CSS styles
        old_styles_pattern = r'/\* Mega Menu Styles \*/.*?(?=\n\s*(?:/\*|\.service-card|</style>))'
        fixed_styles = get_fixed_mega_menu_styles()
        content = re.sub(old_styles_pattern, fixed_styles, content, flags=re.DOTALL)
        
        # Fix HTML structure
        content = fix_mega_menu_html_structure(content)
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
        return False

def main():
    """Fix mega menu width issues across all pages"""
    print("🚀 Fixing mega menu width issues across all pages...")
    
    # Get all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == 'index.html':
                html_files.append(os.path.join(root, file))
    
    success_count = 0
    updated_count = 0
    
    for file_path in html_files:
        # Check if file has mega menu before processing
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'mega-menu' in content:
                if fix_page_mega_menu(file_path):
                    print(f"✅ Fixed mega menu in {file_path}")
                    updated_count += 1
                success_count += 1
            else:
                success_count += 1
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")
    
    print(f"\n📊 Processed {success_count}/{len(html_files)} pages")
    print(f"📊 Updated mega menu in {updated_count} pages")
    print("🎉 Mega menu width fixes completed!")

if __name__ == "__main__":
    main()
