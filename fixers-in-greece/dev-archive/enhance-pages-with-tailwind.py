#!/usr/bin/env python3
"""
Script to enhance pages with basic Tailwind CSS classes
"""

import os
import re
from pathlib import Path

def enhance_page_styling(file_path):
    """Add basic Tailwind styling to improve page appearance"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add dark background to body if not present
        if 'bg-vietnam-darker' not in content and 'bg-' not in content:
            content = re.sub(r'<body([^>]*)>', r'<body\1 class="bg-vietnam-darker text-white font-sans">', content)
        
        # Enhance container classes
        content = re.sub(r'class="container"', 'class="container mx-auto px-4"', content)
        
        # Add responsive padding to main content areas
        content = re.sub(r'<div class="wpb_wrapper">', '<div class="wpb_wrapper p-4 md:p-8">', content)
        
        # Enhance headings with Vietnam orange color
        content = re.sub(r'<h1([^>]*)>', r'<h1\1 class="text-3xl md:text-5xl font-bold text-vietnam-orange mb-6">', content)
        content = re.sub(r'<h2([^>]*)>', r'<h2\1 class="text-2xl md:text-3xl font-bold text-vietnam-orange mb-4">', content)
        content = re.sub(r'<h3([^>]*)>', r'<h3\1 class="text-xl md:text-2xl font-semibold text-vietnam-orange mb-3">', content)
        
        # Enhance paragraphs
        content = re.sub(r'<p([^>]*)>', r'<p\1 class="text-gray-300 leading-relaxed mb-4">', content)
        
        # Enhance links
        content = re.sub(r'<a([^>]*href[^>]*)>', r'<a\1 class="text-vietnam-orange hover:text-yellow-400 transition-colors duration-200">', content)
        
        # Enhance buttons
        content = re.sub(r'<button([^>]*)>', r'<button\1 class="bg-vietnam-orange text-black px-6 py-3 rounded-md font-semibold hover:bg-yellow-500 transition-colors duration-200">', content)
        
        # Add responsive classes to images
        content = re.sub(r'<img([^>]*)>', r'<img\1 class="max-w-full h-auto rounded-lg shadow-lg">', content)
        
        # Enhance form elements
        content = re.sub(r'<input([^>]*type="text"[^>]*)>', r'<input\1 class="w-full px-3 py-2 bg-vietnam-dark border border-gray-600 rounded-md text-white focus:border-vietnam-orange focus:outline-none">', content)
        content = re.sub(r'<input([^>]*type="email"[^>]*)>', r'<input\1 class="w-full px-3 py-2 bg-vietnam-dark border border-gray-600 rounded-md text-white focus:border-vietnam-orange focus:outline-none">', content)
        content = re.sub(r'<textarea([^>]*)>', r'<textarea\1 class="w-full px-3 py-2 bg-vietnam-dark border border-gray-600 rounded-md text-white focus:border-vietnam-orange focus:outline-none resize-y">', content)
        
        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Enhanced {file_path} with Tailwind styling")
        return True
        
    except Exception as e:
        print(f"❌ Error enhancing {file_path}: {e}")
        return False

def main():
    """Main function to enhance all pages"""
    # List of directories to enhance
    directories = [
        'clients',
        'contact', 
        'equipment-rental-vietnam',
        'film-permits-vietnam',
        'filming-in-vietnam',
        'location-scouting-vietnam',
        'portfolio'
    ]
    
    enhanced_count = 0
    total_count = 0
    
    print("🎨 Enhancing pages with Tailwind CSS styling...")
    print("=" * 50)
    
    for directory in directories:
        index_file = Path(directory) / 'index.html'
        if index_file.exists():
            total_count += 1
            if enhance_page_styling(index_file):
                enhanced_count += 1
        else:
            print(f"⚠️  {index_file} not found")
    
    print("=" * 50)
    print(f"📊 Summary: {enhanced_count}/{total_count} pages enhanced successfully")
    
    if enhanced_count == total_count:
        print("🎉 All pages now have enhanced Tailwind styling!")
    else:
        print("⚠️  Some pages may need manual review")

if __name__ == "__main__":
    main()
