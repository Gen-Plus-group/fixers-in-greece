#!/usr/bin/env python3
"""
Fix all potential horizontal scrolling issues across the website
"""

import os
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def find_width_issues(content):
    """Find potential width issues in HTML/CSS content"""
    issues = []
    
    # Check for problematic width declarations
    patterns = [
        (r'width:\s*100vw', 'width: 100vw found'),
        (r'min-width:\s*\d+px', 'min-width with fixed pixels found'),
        (r'width:\s*\d{4,}px', 'large fixed width found'),
        (r'left:\s*-\d+px', 'negative left positioning found'),
        (r'right:\s*-\d+px', 'negative right positioning found'),
        (r'margin-left:\s*-\d+px', 'negative margin-left found'),
        (r'margin-right:\s*-\d+px', 'negative margin-right found'),
        (r'translate-x-\d+', 'translate-x with large value found'),
    ]
    
    for pattern, desc in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append(desc)
    
    return issues

def fix_html_file(file_path):
    """Fix width issues in HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Add overflow-x-hidden to body if not present
        body_pattern = r'<body([^>]*?)>'
        body_match = re.search(body_pattern, content)
        
        if body_match:
            body_tag = body_match.group(0)
            body_attrs = body_match.group(1)
            
            # Check if overflow-x-hidden is already present
            if 'overflow-x-hidden' not in body_attrs:
                # Check if there's a class attribute
                if 'class=' in body_attrs:
                    # Add to existing class
                    content = content.replace(body_tag, 
                        body_tag.replace('class="', 'class="overflow-x-hidden '))
                else:
                    # Add new class attribute
                    new_body = '<body class="overflow-x-hidden"' + body_attrs + '>'
                    content = content.replace(body_tag, new_body)
        
        # Fix any width: 100vw declarations in inline styles
        content = re.sub(r'width:\s*100vw', 'width: 100%', content)
        
        # Fix large min-width values
        content = re.sub(r'min-width:\s*(\d{4,})px', r'max-width: \1px', content)
        
        # Add max-width constraint to containers
        content = re.sub(r'class="([^"]*container[^"]*)"', 
                        lambda m: f'class="{m.group(1)} max-w-full"' if 'max-w-' not in m.group(1) else m.group(0), 
                        content)
        
        # Fix negative margins that might cause overflow
        content = re.sub(r'margin-left:\s*-(\d{3,})px', r'margin-left: -\1px; overflow-x: hidden', content)
        content = re.sub(r'margin-right:\s*-(\d{3,})px', r'margin-right: -\1px; overflow-x: hidden', content)
        
        # Add viewport meta tag if missing
        if '<meta name="viewport"' not in content:
            viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5">'
            content = content.replace('</head>', f'    {viewport_meta}\n</head>')
        
        # Write back if changes were made
        if content != original_content:
            # Create backup
            backup_dir = os.path.join(os.path.dirname(file_path), 'width_fix_backup')
            os.makedirs(backup_dir, exist_ok=True)
            backup_file = os.path.join(backup_dir, f"{os.path.basename(file_path)}.{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak")
            
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Find issues for reporting
            issues = find_width_issues(original_content)
            
            return file_path, True, issues
        
        return file_path, False, []
        
    except Exception as e:
        return file_path, False, [f"Error: {str(e)}"]

def fix_css_file(file_path):
    """Fix width issues in CSS file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix width: 100vw declarations
        content = re.sub(r'width:\s*100vw', 'width: 100%', content)
        
        # Fix large min-width values
        content = re.sub(r'min-width:\s*(\d{4,})px', r'max-width: \1px', content)
        
        # Add global overflow fixes if not present
        if '/* Global overflow fix */' not in content:
            overflow_fix = """
/* Global overflow fix for horizontal scrolling */
html, body {
  overflow-x: hidden;
  max-width: 100%;
}

* {
  max-width: 100%;
}

.container, .max-w-7xl, .max-w-6xl, .max-w-5xl {
  max-width: min(100%, var(--max-width, 1400px));
  margin-left: auto;
  margin-right: auto;
  padding-left: 1rem;
  padding-right: 1rem;
}

/* Fix for any elements that might overflow */
img, video, iframe, embed, object {
  max-width: 100%;
  height: auto;
}

/* Fix for tables */
table {
  max-width: 100%;
  overflow-x: auto;
  display: block;
}

/* Fix for code blocks */
pre, code {
  max-width: 100%;
  overflow-x: auto;
}
"""
            content = overflow_fix + content
        
        # Write back if changes were made
        if content != original_content:
            # Create backup
            backup_dir = os.path.join(os.path.dirname(file_path), 'width_fix_backup')
            os.makedirs(backup_dir, exist_ok=True)
            backup_file = os.path.join(backup_dir, f"{os.path.basename(file_path)}.{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak")
            
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return file_path, True, ["CSS overflow fixes added"]
        
        return file_path, False, []
        
    except Exception as e:
        return file_path, False, [f"Error: {str(e)}"]

def process_file(file_path):
    """Process a single file"""
    if file_path.endswith('.html'):
        return fix_html_file(file_path)
    elif file_path.endswith('.css'):
        return fix_css_file(file_path)
    return file_path, False, []

def main():
    """Main function to fix width issues across all files"""
    print("Fixing width issues across all files...")
    
    # Find all HTML and CSS files
    html_files = []
    css_files = []
    
    for root, dirs, files in os.walk('.'):
        # Skip node_modules and backup directories
        if 'node_modules' in root or 'backup' in root or '.git' in root:
            continue
        
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.html') and not file.endswith('-backup.html'):
                html_files.append(file_path)
            elif file.endswith('.css') and 'dist' not in root:
                css_files.append(file_path)
    
    # Process all files in parallel
    all_files = html_files + css_files
    print(f"Found {len(html_files)} HTML files and {len(css_files)} CSS files to check")
    
    fixed_count = 0
    issues_found = {}
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(process_file, file_path): file_path for file_path in all_files}
        
        for future in as_completed(futures):
            file_path, was_fixed, issues = future.result()
            if was_fixed:
                fixed_count += 1
                if issues:
                    issues_found[file_path] = issues
                print(f"✓ Fixed: {file_path}")
    
    # Create a comprehensive log
    log_content = f"""Width Issues Fix Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Files Processed: {len(all_files)}
Files Fixed: {fixed_count}

Issues Found and Fixed:
"""
    
    for file_path, issues in issues_found.items():
        log_content += f"\n{file_path}:\n"
        for issue in issues:
            log_content += f"  - {issue}\n"
    
    # Save log
    with open('width_fix_report.txt', 'w') as f:
        f.write(log_content)
    
    print(f"\n✅ Fixed {fixed_count} files")
    print(f"📄 Report saved to width_fix_report.txt")
    
    # Add specific fixes to src/input.css
    print("\nAdding global overflow fixes to src/input.css...")
    
    input_css_path = 'src/input.css'
    if os.path.exists(input_css_path):
        with open(input_css_path, 'r', encoding='utf-8') as f:
            input_css = f.read()
        
        if '/* Global overflow prevention */' not in input_css:
            overflow_layer = """
/* Global overflow prevention */
@layer base {
  html {
    @apply overflow-x-hidden;
  }
  
  body {
    @apply overflow-x-hidden relative;
    max-width: 100vw;
  }
  
  * {
    max-width: 100%;
  }
}

@layer utilities {
  .no-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
  
  .no-scrollbar::-webkit-scrollbar {
    display: none;
  }
}
"""
            # Add after the @tailwind directives
            input_css = input_css.replace('@tailwind utilities;', '@tailwind utilities;\n' + overflow_layer)
            
            with open(input_css_path, 'w', encoding='utf-8') as f:
                f.write(input_css)
            
            print("✓ Added global overflow fixes to src/input.css")

if __name__ == "__main__":
    main()