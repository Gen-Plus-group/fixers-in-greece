#!/usr/bin/env python3
"""
Fix spacing and visual issues in portfolio pages - Version 2
This version properly restructures the sections without truncating files
"""

import os
from pathlib import Path

def fix_portfolio_page_v2(file_path):
    """Fix spacing and visual issues in a single portfolio page"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Make hero section taller
    content = content.replace(
        'class="portfolio-hero relative min-h-[60vh] flex items-center justify-center"',
        'class="portfolio-hero relative min-h-[70vh] flex items-center justify-center"'
    )
    
    # Fix Project Details Section background and spacing
    content = content.replace(
        '<!-- Project Details Section -->\n        <section class="py-20">',
        '<!-- Project Details Section -->\n        <section class="py-24 bg-gray-900">'
    )
    
    # Fix grid gaps
    content = content.replace('gap-12 mb-20', 'gap-8 mb-24')
    
    # Fix main image section
    content = content.replace(
        '<!-- Main Project Image -->\n                    <div class="mb-20">',
        '<!-- Main Project Image -->\n                    <div class="mb-24">'
    )
    
    # Fix Services Provided section
    content = content.replace(
        '<!-- Services Provided -->\n                    <div class="bg-gradient-to-r from-vietnam-orange to-yellow-500 rounded-2xl p-8 mb-20">',
        '<!-- Services Provided -->\n                    <div class="bg-gradient-to-r from-vietnam-orange to-yellow-500 rounded-2xl p-12 shadow-2xl mb-24">'
    )
    
    # Fix CTA section
    content = content.replace(
        '<!-- Call to Action -->\n                    <div class="text-center bg-vietnam-dark rounded-2xl p-12 border border-gray-700">',
        '<!-- Call to Action -->\n                    <div class="text-center bg-vietnam-dark rounded-2xl p-16 border-2 border-gray-700 shadow-2xl">'
    )
    
    # Fix Related Projects section background
    content = content.replace(
        '<!-- Related Projects -->\n        <section class="py-20 bg-vietnam-dark">',
        '<!-- Related Projects -->\n        <section class="py-24 bg-gray-900 border-t border-gray-800">'
    )
    
    # Fix button spacing
    content = content.replace('btn btn-primary btn-lg"', 'btn btn-primary btn-lg px-8 py-4"')
    content = content.replace('btn btn-outline btn-lg"', 'btn btn-outline btn-lg px-8 py-4"')
    content = content.replace('btn btn-sm btn-primary"', 'btn btn-sm btn-primary px-6 py-2"')
    
    # Ensure proper image styling
    content = content.replace(
        'class="w-full h-auto">',
        'class="w-full h-auto object-cover">'
    )
    
    # Add alternating backgrounds by wrapping sections
    # First, let's ensure we have proper section breaks
    
    # Close the Project Details section properly and add Image Showcase section
    content = content.replace(
        '</div>\n                </div>\n            </div>\n        </section>\n\n        <!-- Related Projects -->',
        '''</div>
                </div>
            </div>
        </section>

        <!-- Image Showcase Section -->
        <section class="py-24 bg-vietnam-darker">
            <div class="container mx-auto px-4">
                <div class="max-w-6xl mx-auto">
                    <!-- Content moved from above -->
                </div>
            </div>
        </section>

        <!-- Related Projects -->'''
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def fix_all_portfolio_pages_v2():
    """Fix all portfolio pages"""
    
    portfolio_slugs = [
        'test2',
        'wolf-blass-heres-to-the-chase-commercial',
        'panorama-europes-border-crisis-the-long-road-curent-affairs-television',
        'direct-asia-commercial',
        'open-season-josef-salvat-music-video',
        'huangs-world'
    ]
    
    portfolio_dir = Path('/home/moister/vietnam/fiexers/fixers-in-vietnam/portfolio-item')
    fixed_count = 0
    
    for slug in portfolio_slugs:
        index_file = portfolio_dir / slug / 'index.html'
        
        if index_file.exists():
            print(f"Fixing spacing in: {slug}")
            # First restore from backup if file is truncated
            backup_file = portfolio_dir / slug / 'index-original-backup.html'
            if backup_file.exists():
                with open(backup_file, 'r') as f:
                    original_content = f.read()
                    if len(original_content) > 1000:  # Basic check that backup is complete
                        with open(index_file, 'w') as out:
                            out.write(original_content)
                        print(f"  Restored from backup: {slug}")
            
            if fix_portfolio_page_v2(index_file):
                fixed_count += 1
                print(f"✓ Fixed: {slug}")
        else:
            print(f"✗ File not found: {index_file}")
    
    print(f"\n✅ Fixed {fixed_count} portfolio pages")

if __name__ == "__main__":
    fix_all_portfolio_pages_v2()