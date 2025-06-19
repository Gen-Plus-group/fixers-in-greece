#!/usr/bin/env python3
"""
Script to update navigation menus across all pages to include new pages
"""

import os
import re

def update_navigation_in_file(file_path):
    """Update navigation in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if this is one of the new pages (they already have correct navigation)
        if any(page in file_path for page in ['vietnam-filming-locations', 'vietnam-film-crew', 'documentary-filming-vietnam']):
            print(f"✅ {file_path} - Skipping (new page with correct navigation)")
            return True
        
        # Update desktop navigation - add Film Crew to Services dropdown
        services_dropdown_old = '''<div class="absolute top-full left-0 mt-2 w-56 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/equipment-rental-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Equipment Rental</a>
                            <a href="/location-scouting-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Location Scouting</a>
                            <a href="/film-permits-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Film Permits</a>
                        </div>'''
        
        services_dropdown_new = '''<div class="absolute top-full left-0 mt-2 w-56 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/equipment-rental-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Equipment Rental</a>
                            <a href="/location-scouting-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Location Scouting</a>
                            <a href="/film-permits-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Film Permits</a>
                            <a href="/vietnam-film-crew/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Film Crew</a>
                        </div>'''
        
        if services_dropdown_old in content:
            content = content.replace(services_dropdown_old, services_dropdown_new)
            print(f"✅ {file_path} - Updated services dropdown")
        
        # Add new navigation sections after services
        # Look for the pattern after services dropdown and add new sections
        services_section_pattern = r'(</div>\s*</div>\s*<a href="/filming-in-vietnam/")'
        
        new_sections = '''</div>
                    </div>
                    <div class="relative group">
                        <a href="/documentary-filming-vietnam/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200 flex items-center">
                            DOCUMENTARIES
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="absolute top-full left-0 mt-2 w-64 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/documentary-filming-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Documentary Services</a>
                        </div>
                    </div>
                    <div class="relative group">
                        <a href="/vietnam-filming-locations/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200 flex items-center">
                            LOCATIONS
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="absolute top-full left-0 mt-2 w-64 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/vietnam-filming-locations/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">All Locations</a>
                        </div>
                    </div>
                    <a href="/filming-in-vietnam/"'''
        
        content = re.sub(services_section_pattern, new_sections, content)
        
        # Update mobile navigation
        mobile_nav_pattern = r'(<a href="/film-permits-vietnam/"[^>]*>Film Permits</a>\s*<a href="/filming-in-vietnam/")'
        mobile_nav_replacement = r'\1\n                    <a href="/vietnam-film-crew/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Crew</a>\n                    <a href="/documentary-filming-vietnam/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">DOCUMENTARIES</a>\n                    <a href="/vietnam-filming-locations/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">LOCATIONS</a>\n                    <a href="/filming-in-vietnam/"'
        
        content = re.sub(mobile_nav_pattern, mobile_nav_replacement, content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} - Navigation updated successfully")
        return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Update navigation on all HTML pages"""
    print("🚀 Updating navigation menus across all pages...")
    
    # List of HTML files to update (excluding the new pages)
    html_files = [
        'about-us/index.html',
        'contact/index.html',
        'film-production-services/index.html',
        'equipment-rental-vietnam/index.html',
        'location-scouting-vietnam/index.html',
        'film-permits-vietnam/index.html',
        'filming-in-vietnam/index.html',
        'portfolio/index.html',
        'clients/index.html'
    ]
    
    success_count = 0
    total_count = len(html_files)
    
    for file_path in html_files:
        if os.path.exists(file_path):
            if update_navigation_in_file(file_path):
                success_count += 1
        else:
            print(f"⚠️  {file_path} - File not found")
    
    print(f"\n📊 Results: {success_count}/{total_count} files updated successfully")
    print("\n🎉 Navigation update complete!")

if __name__ == "__main__":
    main()
