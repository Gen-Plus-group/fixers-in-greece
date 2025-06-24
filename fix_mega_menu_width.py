#!/usr/bin/env python3
"""
Fix mega menu width issues causing horizontal overflow
"""

import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def fix_mega_menu_in_file(file_path):
    """Fix mega menu width issues in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove min-width: 100% from mega menu inline styles
        content = re.sub(r'min-width:\s*100%;?', '', content)
        
        # Fix mega menu width declarations - ensure it doesn't exceed viewport
        content = re.sub(
            r'(\.mega-menu[^{]*\{[^}]*?)width:\s*\d+vw;?\s*max-width:\s*\d+px',
            r'\1width: min(90vw, 1200px)',
            content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        # Fix inline style mega menus
        content = re.sub(
            r'style="([^"]*?)position:\s*absolute;[^"]*?width:\s*100%;[^"]*?min-width:\s*100%;([^"]*?)"',
            r'style="\1position: absolute;\2width: min(90vw, 1200px);"',
            content
        )
        
        # Another pattern for inline styles
        content = re.sub(
            r'(<div[^>]+class="[^"]*mega-menu[^"]*"[^>]+style="[^"]*?)width:\s*100%;[^"]*?max-width:\s*1400px;[^"]*?min-width:\s*100%;([^"]*?")',
            r'\1width: min(90vw, 1200px); max-width: 1200px;\2',
            content
        )
        
        # Fix mega-menu-content max-width if it's too large
        content = re.sub(
            r'(\.mega-menu-content[^{]*\{[^}]*?)max-width:\s*1400px',
            r'\1max-width: 1200px',
            content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        # Add overflow-x: hidden to mega-menu class if not present
        if '.mega-menu' in content and 'overflow-x: hidden' not in content:
            content = re.sub(
                r'(\.mega-menu[^{]*\{[^}]*?)(})',
                r'\1overflow-x: hidden;\2',
                content,
                flags=re.MULTILINE | re.DOTALL
            )
        
        # Write back if changes were made
        if content != original_content:
            # Create backup
            backup_dir = os.path.join(os.path.dirname(file_path), 'megamenu_backup')
            os.makedirs(backup_dir, exist_ok=True)
            backup_file = os.path.join(backup_dir, f"{os.path.basename(file_path)}.{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak")
            
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return file_path, True
        
        return file_path, False
        
    except Exception as e:
        return file_path, False

def main():
    """Main function to fix mega menu width issues"""
    print("Fixing mega menu width issues...")
    
    # Files to fix
    files_to_fix = [
        'components/navigation.html',
        'css/layout.css',
        'src/input.css'
    ]
    
    # Also find all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in root or 'backup' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    all_files = files_to_fix + html_files
    
    fixed_count = 0
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fix_mega_menu_in_file, file_path): file_path for file_path in all_files}
        
        for future in as_completed(futures):
            file_path, was_fixed = future.result()
            if was_fixed:
                fixed_count += 1
                print(f"✓ Fixed: {file_path}")
    
    print(f"\n✅ Fixed {fixed_count} files")
    
    # Add specific CSS fixes
    print("\nAdding CSS fixes to layout.css...")
    
    css_fixes = """
/* Mega menu overflow fixes */
.mega-menu {
    overflow-x: hidden !important;
    max-width: min(90vw, 1200px) !important;
}

.mega-menu-content {
    overflow-x: hidden !important;
}

/* Prevent any absolute positioned element from causing overflow */
[style*="position: absolute"] {
    max-width: 100vw !important;
}
"""
    
    if os.path.exists('css/layout.css'):
        with open('css/layout.css', 'a', encoding='utf-8') as f:
            f.write(css_fixes)
        print("✓ Added CSS overflow fixes")

if __name__ == "__main__":
    main()