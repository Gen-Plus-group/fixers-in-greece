#!/usr/bin/env python3
"""
Script to update navigation menus across all pages to include new Film Director and Film Producer pages
"""

import os
import re

def update_navigation_in_file(file_path):
    """Update navigation in a single HTML file to include new pages"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine current page for highlighting
        current_page = file_path.replace('/index.html', '').replace('./', '')
        if current_page == 'index.html':
            current_page = 'index'
        
        # Update desktop navigation - Services dropdown
        desktop_services_old = r'(<a href="/post-production-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Post-Production Services</a>)\s*</div>'
        
        # Determine highlighting for new pages
        director_class = 'text-vietnam-orange hover:text-white' if current_page == 'hire-film-director' else 'text-vietnam-gray hover:text-vietnam-orange'
        producer_class = 'text-vietnam-orange hover:text-white' if current_page == 'hire-film-producer' else 'text-vietnam-gray hover:text-vietnam-orange'
        
        desktop_services_new = f'''\\1
                            <a href="/hire-film-director/" class="block px-4 py-3 text-sm {director_class} hover:bg-gray-800 transition-colors duration-200">Hire Film Director</a>
                            <a href="/hire-film-producer/" class="block px-4 py-3 text-sm {producer_class} hover:bg-gray-800 transition-colors duration-200">Hire Film Producer</a>
                        </div>'''
        
        if re.search(desktop_services_old, content):
            content = re.sub(desktop_services_old, desktop_services_new, content)
        else:
            print(f"⚠️  {file_path} - Desktop services dropdown pattern not found")
            return False
        
        # Update mobile navigation - Services dropdown
        mobile_services_old = r'(<a href="/post-production-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Post-Production Services</a>)\s*</div>'
        
        # Mobile highlighting
        mobile_director_class = 'text-vietnam-orange hover:text-white' if current_page == 'hire-film-director' else 'text-vietnam-gray hover:text-vietnam-orange'
        mobile_producer_class = 'text-vietnam-orange hover:text-white' if current_page == 'hire-film-producer' else 'text-vietnam-gray hover:text-vietnam-orange'
        
        mobile_services_new = f'''\\1
                            <a href="/hire-film-director/" class="block px-3 py-2 text-sm {mobile_director_class} transition-colors duration-200">Hire Film Director</a>
                            <a href="/hire-film-producer/" class="block px-3 py-2 text-sm {mobile_producer_class} transition-colors duration-200">Hire Film Producer</a>
                        </div>'''
        
        if re.search(mobile_services_old, content):
            content = re.sub(mobile_services_old, mobile_services_new, content)
        else:
            print(f"⚠️  {file_path} - Mobile services dropdown pattern not found")
            return False
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} - Navigation updated with new pages")
        return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Update navigation on all HTML pages to include new Film Director and Producer pages"""
    print("🚀 Updating navigation across all pages to include new Film Director and Producer pages...")
    
    # List of all HTML files to update
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
        print("🎉 All navigation menus have been successfully updated with new pages!")
    else:
        print(f"⚠️  {total_count - success_count} files had issues and may need manual review")

if __name__ == "__main__":
    main()
