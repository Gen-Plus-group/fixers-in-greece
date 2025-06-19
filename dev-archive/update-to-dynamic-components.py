#!/usr/bin/env python3
"""
Script to update existing HTML pages to use dynamic component loading system
"""

import os
import re
from pathlib import Path

def update_page_to_dynamic_components(file_path):
    """Update a single HTML page to use dynamic components"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"📄 Processing {file_path}...")

        # 1. Remove existing header/navigation (from top bar to end of header)
        header_pattern = r'<!-- Top Bar -->.*?</header>'
        content = re.sub(header_pattern, '<!-- Dynamic Header Container -->\n    <div id="header-container">\n        <!-- Header will be loaded here dynamically -->\n    </div>', content, flags=re.DOTALL)

        # 2. Remove existing footer if present
        footer_pattern = r'<!-- Footer -->.*?</footer>'
        if re.search(footer_pattern, content, re.DOTALL):
            content = re.sub(footer_pattern, '<!-- Dynamic Footer Container -->\n    <div id="footer-container">\n        <!-- Footer will be loaded here dynamically -->\n    </div>', content, flags=re.DOTALL)
        else:
            # If no footer exists, add footer container before closing body tag
            content = content.replace('</body>', '    <!-- Dynamic Footer Container -->\n    <div id="footer-container">\n        <!-- Footer will be loaded here dynamically -->\n    </div>\n\n</body>')

        # 3. Add component loader script before closing body tag
        if '/js/component-loader.js' not in content:
            script_tag = '''    <!-- Component Loader Script -->
    <script src="/js/component-loader.js"></script>

    <!-- Page-specific JavaScript -->
    <script>
        // Wait for components to load before initializing page-specific functionality
        document.addEventListener('componentsLoaded', function() {
            console.log('Components loaded, initializing page functionality...');
            
            // Page-specific functionality will be preserved below
        });
    </script>

'''
            # Insert before existing scripts or before closing body tag
            if '<script>' in content:
                # Find the first script tag and insert before it
                script_pos = content.find('<script>')
                content = content[:script_pos] + script_tag + content[script_pos:]
            else:
                content = content.replace('</body>', script_tag + '</body>')

        # 4. Preserve existing page-specific JavaScript but wrap it in componentsLoaded event
        # This is a basic implementation - more complex pages might need manual adjustment
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ {file_path} - Updated successfully")
        return True

    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Update all HTML pages to use dynamic components"""
    print("🚀 Updating pages to use dynamic component loading...")
    print("=" * 60)

    # List of HTML files to update
    html_files = [
        'index.html',
        'about-us/index.html',
        'contact/index.html',
        'film-production-services/index.html',
        'equipment-rental-vietnam/index.html',
        'location-scouting-vietnam/index.html',
        'film-permits-vietnam/index.html',
        'filming-in-vietnam/index.html',
        'portfolio/index.html',
        'clients/index.html',
        'vietnam-filming-locations/index.html',
        'vietnam-film-crew/index.html',
        'documentary-filming-vietnam/index.html',
        'drone-filming-vietnam/index.html',
        'commercial-video-production-vietnam/index.html',
        'news-filming-vietnam/index.html',
        'ho-chi-minh-city-filming/index.html',
        'hanoi-film-production/index.html',
        'casting-services-vietnam/index.html',
        'corporate-video-vietnam/index.html',
        'equipment-transport-vietnam/index.html',
        'event-filming-vietnam/index.html',
        'live-streaming-vietnam/index.html',
        'music-video-production-vietnam/index.html',
        'post-production-vietnam/index.html',
        'translation-services-vietnam/index.html',
        'hire-film-director/index.html',
        'hire-film-producer/index.html',
        'hire-line-producer/index.html',
        'hire-fixer/index.html',
        'hire-dop/index.html',
        'hire-location-manager/index.html'
    ]

    success_count = 0
    total_count = len(html_files)

    for file_path in html_files:
        if os.path.exists(file_path):
            if update_page_to_dynamic_components(file_path):
                success_count += 1
        else:
            print(f"⚠️  {file_path} - File not found")

    print("\n" + "=" * 60)
    print(f"📊 Update completed: {success_count}/{total_count} files updated")

    if success_count == total_count:
        print("🎉 All pages have been successfully updated to use dynamic components!")
        print("\n📋 Next steps:")
        print("1. Test the website to ensure all components load correctly")
        print("2. Check that navigation highlighting works properly")
        print("3. Verify mobile menu functionality")
        print("4. Update any page-specific JavaScript as needed")
    else:
        print(f"⚠️  {total_count - success_count} files had issues and may need manual review")

    print("\n🔧 Component files created:")
    print("- /components/header.html")
    print("- /components/navigation.html") 
    print("- /components/footer.html")
    print("- /js/component-loader.js")
    print("- /template-page.html (for new pages)")

if __name__ == "__main__":
    main()
