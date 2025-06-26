#!/usr/bin/env python3
"""
Script to fix alignment issues in all portfolio item pages.
Applies the new CSS classes and structure for consistent alignment.
"""

import os
import re
import glob

def find_portfolio_items():
    """Find all portfolio item HTML files."""
    pattern = "/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/portfolio-item/*/index.html"
    return glob.glob(pattern)

def read_file(filepath):
    """Read file content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_css_link(content):
    """Add the portfolio alignment CSS link."""
    # Check if the link already exists
    if 'portfolio-alignment-fix.css' in content:
        return content
    
    # Find the Tailwind CSS link and add our fix after it
    pattern = r'(<!-- Tailwind CSS -->\s*<link href="/dist/output\.css\?v=\d+" rel="stylesheet">)'
    replacement = r'\1\n    \n    <!-- Portfolio Alignment Fix -->\n    <link href="/portfolio-alignment-fix.css?v=20250626" rel="stylesheet">'
    
    return re.sub(pattern, replacement, content)

def fix_hero_section(content):
    """Fix hero section structure."""
    # Pattern for existing hero section
    pattern = r'<!-- Hero Section -->\s*<section class="portfolio-hero[^"]*"[^>]*>\s*<div class="container[^"]*"[^>]*>\s*<div class="max-w-4xl">\s*(?:<!-- Title -->)?\s*<h1 class="[^"]*"[^>]*>\s*([^<]+)\s*</h1>\s*(?:<!-- Subtitle -->)?\s*<p class="[^"]*"[^>]*>\s*([^<]+)\s*</p>\s*</div>\s*</div>\s*</section>'
    
    def hero_replacement(match):
        title = match.group(1).strip()
        subtitle = match.group(2).strip()
        
        return f'''<!-- Hero Section -->
        <section class="portfolio-hero relative">
            <div class="portfolio-container relative z-10">
                <div class="max-w-4xl">
                    <h1 class="text-6xl md:text-8xl font-bold text-white mb-8">
                        {title}
                    </h1>
                    <p class="text-xl md:text-2xl text-gray-300 leading-relaxed mb-12">
                        {subtitle}
                    </p>
                </div>
            </div>
        </section>'''
    
    return re.sub(pattern, hero_replacement, content, flags=re.DOTALL)

def fix_project_details(content):
    """Fix project details grid structure."""
    # Complex pattern to match the project details section
    pattern = r'<!-- Project Details Section -->\s*<section class="[^"]*"[^>]*>\s*<div class="[^"]*"[^>]*>\s*<div class="[^"]*"[^>]*>\s*(.*?)\s*</div>\s*</div>\s*</section>'
    
    def details_replacement(match):
        # Extract the grid content and parse it
        grid_content = match.group(1)
        
        # Extract individual items
        item_pattern = r'<div class="[^"]*"[^>]*>\s*<h3[^>]*>([^<]+)</h3>\s*<p class="[^"]*"[^>]*>([^<]+)</p>\s*</div>'
        items = re.findall(item_pattern, grid_content)
        
        if not items:
            return match.group(0)  # Return original if parsing fails
        
        # Build new structure
        new_items = []
        for label, value in items:
            # Determine text color class
            color_class = "text-greece-blue" if "Fixers in Greece" in value or any(client in value.lower() for client in ["nike", "abaton", "canaves"]) else "text-white"
            
            new_items.append(f'''                    <div class="portfolio-detail-item">
                        <h3>{label.strip()}</h3>
                        <p class="{color_class}">{value.strip()}</p>
                    </div>''')
        
        return f'''<!-- Project Details Section -->
        <section class="portfolio-section bg-greece-dark border-y border-gray-800">
            <div class="portfolio-container">
                <div class="portfolio-details-grid">
{chr(10).join(new_items)}
                </div>
            </div>
        </section>'''
    
    return re.sub(pattern, details_replacement, content, flags=re.DOTALL)

def fix_video_section(content):
    """Fix video section structure."""
    pattern = r'<!-- Video Section -->\s*<section class="[^"]*"[^>]*>\s*<div class="[^"]*"[^>]*>\s*<div class="[^"]*"[^>]*>\s*(.*?)\s*</div>\s*</div>\s*</section>'
    
    def video_replacement(match):
        video_content = match.group(1)
        return f'''<!-- Video Section -->
        <section class="portfolio-section portfolio-video-section">
            <div class="portfolio-container">
                <div class="max-w-5xl mx-auto">
                    {video_content}
                </div>
            </div>
        </section>'''
    
    return re.sub(pattern, video_replacement, content, flags=re.DOTALL)

def fix_cta_section(content):
    """Fix call-to-action section structure."""
    pattern = r'<!-- Call to Action -->\s*<section class="[^"]*"[^>]*>\s*<div class="[^"]*"[^>]*>\s*<div class="[^"]*"[^>]*>\s*(.*?)\s*</div>\s*</div>\s*</section>'
    
    def cta_replacement(match):
        cta_content = match.group(1)
        return f'''<!-- Call to Action -->
        <section class="portfolio-section">
            <div class="portfolio-container">
                <div class="portfolio-cta">
                    {cta_content}
                </div>
            </div>
        </section>'''
    
    return re.sub(pattern, cta_replacement, content, flags=re.DOTALL)

def fix_navigation_section(content):
    """Fix navigation section structure."""
    pattern = r'<!-- Navigation -->\s*<section class="[^"]*"[^>]*>\s*<div class="[^"]*"[^>]*>\s*(.*?)\s*</div>\s*</section>'
    
    def nav_replacement(match):
        nav_content = match.group(1)
        return f'''<!-- Navigation -->
        <section class="portfolio-navigation">
            <div class="container">
                {nav_content}
            </div>
        </section>'''
    
    return re.sub(pattern, nav_replacement, content, flags=re.DOTALL)

def process_file(filepath):
    """Process a single portfolio file."""
    print(f"Processing: {filepath}")
    
    content = read_file(filepath)
    
    # Apply all fixes
    content = fix_css_link(content)
    content = fix_hero_section(content)
    content = fix_project_details(content)
    content = fix_video_section(content)
    content = fix_cta_section(content)
    content = fix_navigation_section(content)
    
    write_file(filepath, content)
    print(f"✓ Fixed: {filepath}")

def main():
    """Main function."""
    portfolio_files = find_portfolio_items()
    
    print(f"Found {len(portfolio_files)} portfolio items to process:")
    for filepath in portfolio_files:
        print(f"  - {os.path.basename(os.path.dirname(filepath))}")
    
    print("\nStarting fixes...")
    
    for filepath in portfolio_files:
        try:
            process_file(filepath)
        except Exception as e:
            print(f"✗ Error processing {filepath}: {e}")
    
    print("\nPortfolio alignment fixes completed!")

if __name__ == "__main__":
    main()