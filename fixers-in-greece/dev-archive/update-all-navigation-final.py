#!/usr/bin/env python3
"""
Script to update all navigation menus to include all 6 new pages
"""

import os
import re

def update_navigation_in_file(file_path):
    """Update navigation in a single HTML file to include all new pages"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine current page for highlighting
        current_page = file_path.replace('/index.html', '').replace('./', '')
        if current_page == 'index.html':
            current_page = 'index'
        
        # Define all new pages with their highlighting
        new_pages = [
            ('hire-film-director', 'Hire Film Director'),
            ('hire-film-producer', 'Hire Film Producer'),
            ('hire-line-producer', 'Hire Line Producer'),
            ('hire-fixer', 'Hire Fixer'),
            ('hire-dop', 'Hire DOP'),
            ('hire-location-manager', 'Hire Location Manager')
        ]
        
        # Build new navigation links
        desktop_new_links = ""
        mobile_new_links = ""
        
        for page_slug, page_title in new_pages:
            desktop_class = 'text-vietnam-orange hover:text-white' if current_page == page_slug else 'text-vietnam-gray hover:text-vietnam-orange'
            mobile_class = 'text-vietnam-orange hover:text-white' if current_page == page_slug else 'text-vietnam-gray hover:text-vietnam-orange'
            
            desktop_new_links += f'                            <a href="/{page_slug}/" class="block px-4 py-3 text-sm {desktop_class} hover:bg-gray-800 transition-colors duration-200">{page_title}</a>\n'
            mobile_new_links += f'                            <a href="/{page_slug}/" class="block px-3 py-2 text-sm {mobile_class} transition-colors duration-200">{page_title}</a>\n'
        
        # Update desktop navigation - Services dropdown
        desktop_pattern = r'(<a href="/post-production-vietnam/"[^>]*>Post-Production Services</a>)\s*</div>'
        desktop_replacement = f'\\1\n{desktop_new_links.rstrip()}\n                        </div>'
        
        if re.search(desktop_pattern, content):
            content = re.sub(desktop_pattern, desktop_replacement, content)
        else:
            print(f"⚠️  {file_path} - Desktop services dropdown pattern not found")
            return False
        
        # Update mobile navigation - Services dropdown  
        mobile_pattern = r'(<a href="/post-production-vietnam/"[^>]*>Post-Production Services</a>)\s*</div>'
        mobile_replacement = f'\\1\n{mobile_new_links.rstrip()}\n                        </div>'
        
        if re.search(mobile_pattern, content):
            content = re.sub(mobile_pattern, mobile_replacement, content)
        else:
            print(f"⚠️  {file_path} - Mobile services dropdown pattern not found")
            return False
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} - Navigation updated with all new pages")
        return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Update navigation on all HTML pages to include all new pages"""
    print("🚀 Updating navigation across all pages to include all 6 new pages...")
    
    # List of all HTML files to update (excluding the new pages themselves)
    html_files = [
        'index.html',  # Homepage
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
        'translation-services-vietnam/index.html'
    ]
    
    success_count = 0
    total_count = len(html_files)
    
    for file_path in html_files:
        if os.path.exists(file_path):
            if update_navigation_in_file(file_path):
                success_count += 1
        else:
            print(f"⚠️  {file_path} - File not found")
    
    print(f"\n📊 Navigation update completed: {success_count}/{total_count} files updated")
    
    if success_count == total_count:
        print("🎉 All navigation menus have been successfully updated with all new pages!")
    else:
        print(f"⚠️  {total_count - success_count} files had issues and may need manual review")

if __name__ == "__main__":
    main()
