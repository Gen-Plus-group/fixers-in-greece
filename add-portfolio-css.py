#!/usr/bin/env python3
"""
Add custom CSS to portfolio pages to improve spacing
"""

import os
from pathlib import Path

def add_css_to_portfolio_page(file_path):
    """Add custom CSS link to a portfolio page"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if CSS is already added
    if 'portfolio-spacing-fix.css' in content:
        print(f"  CSS already added to: {file_path}")
        return False
    
    # Add the CSS link after the main stylesheet
    css_link = '<link href="/portfolio-spacing-fix.css" rel="stylesheet">'
    
    # Find a good place to insert it - after the Total theme stylesheet
    insert_after = '<link href="/wp-content/themes/Total/style.css" rel="stylesheet">'
    
    if insert_after in content:
        content = content.replace(
            insert_after,
            f'{insert_after}\n{css_link}'
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    else:
        print(f"  Warning: Could not find insertion point in {file_path}")
        return False

def add_css_to_all_portfolio_pages():
    """Add CSS to all portfolio pages"""
    
    portfolio_slugs = [
        'test2',
        'wolf-blass-heres-to-the-chase-commercial',
        'panorama-europes-border-crisis-the-long-road-curent-affairs-television',
        'direct-asia-commercial',
        'open-season-josef-salvat-music-video',
        'huangs-world'
    ]
    
    portfolio_dir = Path('/home/moister/vietnam/fiexers/fixers-in-vietnam/portfolio-item')
    updated_count = 0
    
    for slug in portfolio_slugs:
        index_file = portfolio_dir / slug / 'index.html'
        
        if index_file.exists():
            print(f"Processing: {slug}")
            if add_css_to_portfolio_page(index_file):
                updated_count += 1
                print(f"✓ Updated: {slug}")
        else:
            print(f"✗ File not found: {index_file}")
    
    print(f"\n✅ Updated {updated_count} portfolio pages with spacing CSS")

if __name__ == "__main__":
    add_css_to_all_portfolio_pages()