#!/usr/bin/env python3
"""
Fix spacing and visual issues in portfolio pages
"""

import os
from pathlib import Path

def fix_portfolio_page(file_path):
    """Fix spacing and visual issues in a single portfolio page"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix hero section - add proper min-height and spacing
    content = content.replace(
        'class="portfolio-hero relative min-h-[60vh] flex items-center justify-center"',
        'class="portfolio-hero relative min-h-[70vh] flex items-center justify-center"'
    )
    
    # Fix Project Details Section - add background and better spacing
    content = content.replace(
        '<!-- Project Details Section -->\n        <section class="py-20">',
        '<!-- Project Details Section -->\n        <section class="py-24 bg-gray-900">'
    )
    
    content = content.replace(
        '<!-- Project Details Section -->\n        <section class="py-20 bg-gray-900">',
        '<!-- Project Details Section -->\n        <section class="py-24 bg-gray-900">'
    )
    
    # Fix grid gaps
    content = content.replace('gap-12 mb-20', 'gap-8 mb-24')
    
    # Fix main image section - add background
    content = content.replace(
        '<!-- Main Project Image -->\n                    <div class="mb-20">',
        '<!-- Main Project Image -->\n                    <div class="mb-24">'
    )
    
    # Add section wrapper around image
    content = content.replace(
        '</section>\n\n        <!-- Related Projects -->',
        '</section>\n\n        <!-- Image Section -->\n        <section class="py-24 bg-vietnam-darker">\n            <div class="container mx-auto px-4">\n                <div class="max-w-6xl mx-auto">\n                    <!-- Main Project Image moved here -->\n                </div>\n            </div>\n        </section>\n\n        <!-- Related Projects -->'
    )
    
    # Fix Services Provided section spacing and background
    content = content.replace(
        '<!-- Services Provided -->\n                    <div class="bg-gradient-to-r from-vietnam-orange to-yellow-500 rounded-2xl p-8 mb-20">',
        '<!-- Services Provided -->\n                    <div class="bg-gradient-to-r from-vietnam-orange to-yellow-500 rounded-2xl p-12 shadow-2xl">'
    )
    
    # Fix CTA section
    content = content.replace(
        '<!-- Call to Action -->\n                    <div class="text-center bg-vietnam-dark rounded-2xl p-12 border border-gray-700">',
        '<!-- Call to Action -->\n                    <div class="text-center bg-vietnam-dark rounded-2xl p-16 border-2 border-gray-700 shadow-2xl">'
    )
    
    # Fix Related Projects section
    content = content.replace(
        '<!-- Related Projects -->\n        <section class="py-20 bg-vietnam-dark">',
        '<!-- Related Projects -->\n        <section class="py-24 bg-gray-900 border-t border-gray-800">'
    )
    
    # Better section organization - restructure the page
    lines = content.split('\n')
    new_lines = []
    image_section_lines = []
    services_section_lines = []
    cta_section_lines = []
    in_image_section = False
    in_services_section = False
    in_cta_section = False
    skip_lines = 0
    
    for i, line in enumerate(lines):
        if skip_lines > 0:
            skip_lines -= 1
            continue
            
        # Capture image section
        if '<!-- Main Project Image -->' in line:
            in_image_section = True
            image_section_lines = []
        
        if in_image_section:
            image_section_lines.append(line)
            if '</div>' in line and 'rounded-2xl overflow-hidden shadow-2xl' in lines[i-2]:
                in_image_section = False
                # Skip the next </div> that closes the image
                skip_lines = 1
            continue
        
        # Capture services section
        if '<!-- Services Provided -->' in line:
            in_services_section = True
            services_section_lines = []
        
        if in_services_section:
            services_section_lines.append(line)
            if '</div>' in line and 'Services Provided' in ' '.join(services_section_lines[-10:]):
                # Check if this is the closing div of services section
                next_lines = lines[i+1:i+5]
                if any('Call to Action' in l for l in next_lines):
                    in_services_section = False
            continue
        
        # Capture CTA section
        if '<!-- Call to Action -->' in line:
            in_cta_section = True
            cta_section_lines = []
        
        if in_cta_section:
            cta_section_lines.append(line)
            if '</div>' in line and 'View More Work' in ' '.join(cta_section_lines[-5:]):
                in_cta_section = False
                # Add sections in new order after project details
                new_lines.append('                </div>')
                new_lines.append('            </div>')
                new_lines.append('        </section>')
                new_lines.append('')
                
                # Add image section with proper wrapper
                new_lines.append('        <!-- Image Showcase Section -->')
                new_lines.append('        <section class="py-24 bg-vietnam-darker">')
                new_lines.append('            <div class="container mx-auto px-4">')
                new_lines.append('                <div class="max-w-6xl mx-auto">')
                new_lines.extend(image_section_lines)
                new_lines.append('                </div>')
                new_lines.append('            </div>')
                new_lines.append('        </section>')
                new_lines.append('')
                
                # Add services section with wrapper
                new_lines.append('        <!-- Services Section -->')
                new_lines.append('        <section class="py-24 bg-gray-900">')
                new_lines.append('            <div class="container mx-auto px-4">')
                new_lines.append('                <div class="max-w-6xl mx-auto">')
                new_lines.extend(services_section_lines)
                new_lines.append('                </div>')
                new_lines.append('            </div>')
                new_lines.append('        </section>')
                new_lines.append('')
                
                # Add CTA section with wrapper
                new_lines.append('        <!-- CTA Section -->')
                new_lines.append('        <section class="py-24 bg-vietnam-darker">')
                new_lines.append('            <div class="container mx-auto px-4">')
                new_lines.append('                <div class="max-w-6xl mx-auto">')
                new_lines.extend(cta_section_lines)
                new_lines.append('                </div>')
                new_lines.append('            </div>')
                new_lines.append('        </section>')
                continue
            continue
        
        new_lines.append(line)
    
    # Join and do final replacements
    content = '\n'.join(new_lines)
    
    # Fix button spacing
    content = content.replace('btn btn-primary btn-lg', 'btn btn-primary btn-lg px-8 py-4')
    content = content.replace('btn btn-outline btn-lg', 'btn btn-outline btn-lg px-8 py-4')
    content = content.replace('btn btn-sm btn-primary', 'btn btn-sm btn-primary px-6 py-2')
    
    # Ensure proper image styling
    content = content.replace(
        'class="w-full h-auto"',
        'class="w-full h-auto object-cover"'
    )
    
    # Fix any double sections
    content = content.replace('</section>\n\n        <!-- Image Section -->', '')
    content = content.replace('</section>\n        <!-- Image Section -->', '')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def fix_all_portfolio_pages():
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
            if fix_portfolio_page(index_file):
                fixed_count += 1
                print(f"✓ Fixed: {slug}")
        else:
            print(f"✗ File not found: {index_file}")
    
    print(f"\n✅ Fixed {fixed_count} portfolio pages")

if __name__ == "__main__":
    fix_all_portfolio_pages()