#!/usr/bin/env python3
"""
Script to fix mega menu positioning and width issues across all pages
"""

import os
import re

def get_improved_mega_menu_styles():
    """Return the improved mega menu CSS styles with better positioning"""
    return '''        /* Mega Menu Styles */
        .mega-menu {
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%) translateY(-10px);
            width: 100vw;
            max-width: 1400px;
            min-width: 1200px;
            background: #1a1a1a;
            border-top: 2px solid #ff6b35;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 50;
        }
        
        .mega-menu-trigger:hover .mega-menu {
            opacity: 1;
            visibility: visible;
            transform: translateX(-50%) translateY(0);
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
        }
        
        /* Ensure mega menu doesn't get clipped */
        .mega-menu-trigger {
            position: static;
        }
        
        /* Navigation container needs to allow overflow for mega menu */
        nav {
            position: relative;
            overflow: visible;
        }'''

def fix_page_mega_menu_positioning(file_path):
    """Fix mega menu positioning on a single page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if this page doesn't have mega menu
        if 'mega-menu' not in content:
            return True
        
        # Update mega menu CSS styles with improved positioning
        old_styles_pattern = r'/\* Mega Menu Styles \*/.*?(?=\n\s*(?:/\*|\.service-card|</style>))'
        improved_styles = get_improved_mega_menu_styles()
        content = re.sub(old_styles_pattern, improved_styles, content, flags=re.DOTALL)
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
        return False

def main():
    """Fix mega menu positioning across all pages"""
    print("🚀 Fixing mega menu positioning and width issues...")
    
    # Get all HTML files that have mega menu
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == 'index.html':
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if 'mega-menu' in content:
                        html_files.append(file_path)
                except:
                    continue
    
    success_count = 0
    
    for file_path in html_files:
        if fix_page_mega_menu_positioning(file_path):
            print(f"✅ Fixed mega menu positioning in {file_path}")
            success_count += 1
    
    print(f"\n📊 Updated mega menu positioning in {success_count}/{len(html_files)} pages")
    print("🎉 Mega menu positioning fixes completed!")

if __name__ == "__main__":
    main()
