#!/usr/bin/env python3
"""
Script to fix HTML title tags that exceed 60 characters.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple
import html

def find_html_files(root_dir: str) -> List[Path]:
    """Find all HTML files, excluding backups and node_modules."""
    html_files = []
    root_path = Path(root_dir)
    
    for file_path in root_path.rglob('*.html'):
        # Skip files in backup, node_modules, and test directories
        path_str = str(file_path)
        if any(exclude in path_str for exclude in ['backup', 'node_modules', 'test-', 'debug-']):
            continue
        html_files.append(file_path)
    
    return html_files

def extract_title(content: str) -> Tuple[str, int, int]:
    """Extract title tag content and its position in the file."""
    # Look for <title> tags
    title_match = re.search(r'<title[^>]*?>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if title_match:
        title_content = html.unescape(title_match.group(1).strip())
        return title_content, title_match.start(), title_match.end()
    return None, -1, -1

def shorten_title(title: str) -> str:
    """Shorten title to be between 50-60 characters while keeping it meaningful."""
    if len(title) <= 60:
        return title
    
    # Common patterns to remove or shorten
    replacements = [
        # Remove redundant company name at the end
        (r'\s*[-|]\s*Fixers in Greece$', ''),
        (r'\s*[-|]\s*Fixers In Greece$', ''),
        (r'\s*[-|]\s*NEEDaFIXER$', ''),
        # Shorten location references
        (r'Professional\s+', ''),
        (r'Services\s+in\s+Greece', 'Services Greece'),
        (r'Services\s+Greece', 'Greece'),
        (r'Greece\s*[-|]\s*Athens', 'Greece'),
        (r'Athens\s+&\s+Islands', 'Greece'),
        (r'Greek\s+Islands', 'Greece'),
        # Remove redundant words
        (r'\s+and\s+', ' & '),
        (r'Production\s+Services', 'Production'),
        (r'Equipment\s+Rental', 'Equipment'),
        (r'Services\s+Services', 'Services'),
        # Shorten common phrases
        (r'Documentary\s+Filming', 'Documentary'),
        (r'Film\s+Production', 'Film'),
        (r'Location\s+Scouting', 'Locations'),
        (r'Coordination\s+Greece', 'Greece'),
        (r'Management\s+Greece', 'Greece'),
        # Remove less important suffixes
        (r'\s*[-|]\s*Greece\s+Film\s+Production$', ''),
        (r'\s*[-|]\s*Commercial\s+Production$', ''),
        (r'\s*[-|]\s*Reality\s+TV\s+Production$', ''),
        (r'\s*[-|]\s*Music\s+Video$', ''),
        (r'Production\s+Coordination', 'Coordination'),
        # Simplify service descriptions
        (r'Professional\s+Film\s+Crew', 'Film Crew'),
        (r'Professional\s+Services', 'Services'),
        (r'Complete\s+Production\s+Guide', 'Production Guide'),
        (r'Luxury\s+Commercial', 'Luxury'),
        (r'Resort\s+Commercial', 'Resort'),
        (r'Beach\s+Club\s+Commercial', 'Beach Club'),
        (r'Lifestyle\s+Commercial', 'Lifestyle'),
    ]
    
    shortened = title
    for pattern, replacement in replacements:
        shortened = re.sub(pattern, replacement, shortened, flags=re.IGNORECASE)
    
    # If still too long, try more aggressive shortening
    if len(shortened) > 60:
        # Remove everything after the second pipe or dash
        parts = re.split(r'\s*[|-]\s*', shortened)
        if len(parts) > 2:
            shortened = ' | '.join(parts[:2])
    
    # If still too long, truncate intelligently
    if len(shortened) > 60:
        # Try to cut at a word boundary before 60 chars
        if ' ' in shortened[:60]:
            shortened = shortened[:shortened.rfind(' ', 0, 60)]
        else:
            shortened = shortened[:57] + '...'
    
    return shortened.strip()

def process_file(file_path: Path, dry_run: bool = True) -> Tuple[bool, str, str]:
    """Process a single HTML file and fix long title tags."""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_title, start_pos, end_pos = extract_title(content)
        
        if not original_title:
            return False, "", ""
        
        if len(original_title) <= 60:
            return False, original_title, ""
        
        # Shorten the title
        new_title = shorten_title(original_title)
        
        if not dry_run and new_title != original_title:
            # Replace the title in the content
            title_tag_match = re.search(r'(<title[^>]*?>)(.*?)(</title>)', content, re.IGNORECASE | re.DOTALL)
            if title_tag_match:
                new_content = content[:title_tag_match.start(2)] + html.escape(new_title) + content[title_tag_match.end(2):]
                file_path.write_text(new_content, encoding='utf-8')
        
        return True, original_title, new_title
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, "", ""

def main():
    """Main function to process all HTML files."""
    root_dir = "/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece"
    html_files = find_html_files(root_dir)
    
    print(f"Found {len(html_files)} HTML files to process\n")
    
    # First, do a dry run to show what will be changed
    changes_needed = []
    
    for file_path in html_files:
        needs_fix, original, new = process_file(file_path, dry_run=True)
        if needs_fix:
            changes_needed.append((file_path, original, new))
    
    if not changes_needed:
        print("No title tags need fixing!")
        return
    
    print(f"Found {len(changes_needed)} title tags that need fixing:\n")
    
    for file_path, original, new in changes_needed:
        rel_path = file_path.relative_to(root_dir)
        print(f"File: {rel_path}")
        print(f"  Original ({len(original)} chars): {original}")
        print(f"  New ({len(new)} chars): {new}")
        print()
    
    # Automatically apply the changes
    print("\nApplying changes...")
    success_count = 0
    
    for file_path, _, _ in changes_needed:
        needs_fix, _, _ = process_file(file_path, dry_run=False)
        if needs_fix:
            success_count += 1
            print(f"✓ Fixed: {file_path.relative_to(root_dir)}")
    
    print(f"\nSuccessfully fixed {success_count} title tags!")

if __name__ == "__main__":
    main()