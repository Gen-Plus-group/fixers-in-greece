#!/usr/bin/env python3
"""
Update all portfolio pages to include a cache-busting version parameter in the CSS link.
"""

import os
import re
from datetime import datetime

def update_css_link_with_version(file_path):
    """Add version parameter to CSS link for cache busting"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Current CSS link pattern
        old_pattern = r'<link href="/portfolio-spacing-fix\.css" rel="stylesheet">'
        
        # New CSS link with version parameter (using current timestamp)
        version = datetime.now().strftime("%Y%m%d%H%M")
        new_link = f'<link href="/portfolio-spacing-fix.css?v={version}" rel="stylesheet">'
        
        # Check for the link (case insensitive search)
        if '<link href="/portfolio-spacing-fix.css" rel="stylesheet">' in content:
            updated_content = content.replace('<link href="/portfolio-spacing-fix.css" rel="stylesheet">', new_link)
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            
            print(f"✓ Updated CSS link in {file_path}")
            return True
        else:
            print(f"- CSS link not found in {file_path}")
            return False
            
    except Exception as e:
        print(f"✗ Error updating {file_path}: {str(e)}")
        return False

def main():
    """Update all portfolio pages with versioned CSS link"""
    
    portfolio_dir = "portfolio-item"
    updated_count = 0
    
    if not os.path.exists(portfolio_dir):
        print(f"Portfolio directory '{portfolio_dir}' not found!")
        return
    
    # Get all portfolio subdirectories
    portfolio_items = []
    for item in os.listdir(portfolio_dir):
        item_path = os.path.join(portfolio_dir, item)
        if os.path.isdir(item_path):
            index_file = os.path.join(item_path, "index.html")
            if os.path.exists(index_file):
                portfolio_items.append(index_file)
    
    print(f"Found {len(portfolio_items)} portfolio pages to update...")
    print("-" * 50)
    
    for file_path in portfolio_items:
        if update_css_link_with_version(file_path):
            updated_count += 1
    
    print("-" * 50)
    print(f"Updated {updated_count} out of {len(portfolio_items)} portfolio pages")

if __name__ == "__main__":
    main()