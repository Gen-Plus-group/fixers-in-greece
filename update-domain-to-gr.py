#!/usr/bin/env python3
"""
Update all domain references from fixersingreece.com to www.fixersingreece.gr
"""

import os
import re
from pathlib import Path

def update_domain_in_file(file_path):
    """Update domain references in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Track if we made any changes
        original_content = content
        
        # Replace various forms of the old domain
        replacements = [
            # Standard URLs
            ('https://fixersingreece.com/', 'https://www.fixersingreece.gr/'),
            ('http://fixersingreece.com/', 'https://www.fixersingreece.gr/'),
            ('https://www.fixersingreece.com/', 'https://www.fixersingreece.gr/'),
            ('http://www.fixersingreece.com/', 'https://www.fixersingreece.gr/'),
            
            # Mixed case variants
            ('https://fixersinGreece.com/', 'https://www.fixersingreece.gr/'),
            ('http://fixersinGreece.com/', 'https://www.fixersingreece.gr/'),
            
            # Without trailing slash
            ('https://fixersingreece.com"', 'https://www.fixersingreece.gr"'),
            ('http://fixersingreece.com"', 'https://www.fixersingreece.gr"'),
            ('https://fixersinGreece.com"', 'https://www.fixersingreece.gr"'),
            
            # Domain only references
            ('fixersingreece.com/', 'www.fixersingreece.gr/'),
            ('fixersinGreece.com/', 'www.fixersingreece.gr/'),
            ('www.fixersingreece.com/', 'www.fixersingreece.gr/'),
            ('www.fixersinGreece.com/', 'www.fixersingreece.gr/'),
            
            # Email domain references (keeping these as is for now)
            # ('noreply@fixersinGreece.com', 'noreply@fixersingreece.gr'),
            # ('noreply@fixersingreece.com', 'noreply@fixersingreece.gr'),
        ]
        
        for old_domain, new_domain in replacements:
            content = content.replace(old_domain, new_domain)
        
        # If content changed, write it back
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def update_all_files():
    """Update domain references in all relevant files."""
    updated_files = []
    
    # Define file patterns to update
    patterns = ['*.html', '*.xml', '*.json', '*.md', '*.txt', '*.php', '*.js']
    
    # Get the current directory
    base_dir = Path('.')
    
    # Process each file type
    for pattern in patterns:
        for file_path in base_dir.rglob(pattern):
            # Skip node_modules and other directories we don't want to modify
            if any(skip in str(file_path) for skip in ['node_modules', '.git', 'wordpress-backup']):
                continue
            
            if update_domain_in_file(file_path):
                updated_files.append(str(file_path))
                print(f"Updated: {file_path}")
    
    return updated_files

def main():
    """Main function."""
    print("Starting domain update from fixersingreece.com to www.fixersingreece.gr...")
    
    updated_files = update_all_files()
    
    print(f"\nDomain update complete!")
    print(f"Total files updated: {len(updated_files)}")
    
    if updated_files:
        print("\nUpdated files:")
        for file in sorted(updated_files):
            print(f"  - {file}")

if __name__ == "__main__":
    main()