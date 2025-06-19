#!/usr/bin/env python3
"""
Script to improve mega menu visual appearance with better spacing and typography
"""

import os
import re

def get_improved_mega_menu_styles():
    """Return the improved mega menu CSS styles with better spacing and typography"""
    return '''        /* Mega Menu Styles */
        .mega-menu {
            position: absolute;
            top: calc(100% + 12px); /* Add 12px breathing space from navigation */
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
            margin-top: 8px; /* Additional top margin for visual separation */
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
            padding: 1.5rem 1rem; /* Increased padding for better spacing */
        }
        
        /* Mega Menu Typography Improvements */
        .mega-menu h3 {
            font-size: 1.5rem; /* Larger main title */
            font-weight: 700;
            margin-bottom: 0.75rem;
        }
        
        .mega-menu h4 {
            font-size: 1rem; /* Increased from text-sm to text-base */
            font-weight: 600;
            margin-bottom: 1rem;
            color: #ff6b35;
        }
        
        .mega-menu a {
            font-size: 0.875rem; /* Increased from text-xs to text-sm */
            line-height: 1.5;
            padding: 0.25rem 0;
            display: block;
            transition: all 0.2s ease;
        }
        
        .mega-menu a:hover {
            color: #ff6b35;
            padding-left: 0.25rem;
        }
        
        .mega-menu ul {
            margin-top: 0.5rem;
        }
        
        .mega-menu li {
            margin-bottom: 0.5rem; /* Better spacing between links */
        }
        
        /* Ensure mega menu doesn't get clipped */
        .mega-menu-trigger {
            position: static;
        }
        
        /* Navigation container needs to allow overflow for mega menu */
        nav {
            position: relative;
            overflow: visible;
        }
        
        /* Responsive mega menu */
        @media (max-width: 1024px) {
            .mega-menu {
                display: none; /* Hide on mobile/tablet - use mobile menu instead */
            }
        }'''

def improve_mega_menu_html_structure(content):
    """Improve the mega menu HTML structure with better spacing and typography"""
    
    # Update main mega menu container
    content = re.sub(
        r'<div class="mega-menu-content py-8">',
        '<div class="mega-menu-content">',
        content
    )
    
    # Update main title section
    content = re.sub(
        r'<div class="text-center mb-6">\s*<h3 class="text-xl font-bold text-vietnam-orange">Pre-Production Services</h3>\s*<p class="text-gray-400 text-sm">Planning, creative development, logistics</p>\s*</div>',
        '''<div class="text-center mb-8">
                                    <h3 class="text-vietnam-orange">Pre-Production Services</h3>
                                    <p class="text-gray-400 text-base">Planning, creative development, logistics</p>
                                </div>''',
        content,
        flags=re.DOTALL
    )
    
    # Update grid spacing
    content = re.sub(
        r'<div class="grid grid-cols-6 gap-8">',
        '<div class="grid grid-cols-6 gap-10">',
        content
    )
    
    # Update column headers - remove inline classes
    content = re.sub(
        r'<h4 class="text-vietnam-orange font-semibold mb-3 text-sm">([^<]+)</h4>',
        r'<h4>\1</h4>',
        content
    )
    
    # Update list containers - remove inline classes
    content = re.sub(
        r'<ul class="space-y-2">',
        '<ul>',
        content
    )
    
    # Update links - remove inline classes except text color
    content = re.sub(
        r'<a href="([^"]+)" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">([^<]+)</a>',
        r'<a href="\1" class="text-gray-300">\2</a>',
        content
    )
    
    return content

def improve_page_mega_menu_visuals(file_path):
    """Improve mega menu visuals on a single page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if this page doesn't have mega menu
        if 'mega-menu' not in content:
            return True
        
        # Update mega menu CSS styles with improved spacing and typography
        old_styles_pattern = r'/\* Mega Menu Styles \*/.*?(?=\n\s*(?:/\*|\.service-card|</style>))'
        improved_styles = get_improved_mega_menu_styles()
        content = re.sub(old_styles_pattern, improved_styles, content, flags=re.DOTALL)
        
        # Improve HTML structure
        content = improve_mega_menu_html_structure(content)
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ Error improving {file_path}: {e}")
        return False

def main():
    """Improve mega menu visuals across all pages"""
    print("🚀 Improving mega menu visual appearance with better spacing and typography...")
    
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
        if improve_page_mega_menu_visuals(file_path):
            print(f"✅ Improved mega menu visuals in {file_path}")
            success_count += 1
    
    print(f"\n📊 Improved mega menu visuals in {success_count}/{len(html_files)} pages")
    print("🎉 Mega menu visual improvements completed!")

if __name__ == "__main__":
    main()
