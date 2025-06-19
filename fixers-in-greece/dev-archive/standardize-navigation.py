#!/usr/bin/env python3
"""
Script to standardize navigation across all pages
"""

import os
import re

def get_standard_navigation():
    """Return the standard navigation HTML"""
    return {
        'desktop_services': '''<div class="relative group">
                        <a href="/film-production-services/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200 flex items-center">
                            SERVICES
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="absolute top-full left-0 mt-2 w-56 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/equipment-rental-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Equipment Rental</a>
                            <a href="/location-scouting-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Location Scouting</a>
                            <a href="/film-permits-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Film Permits</a>
                            <a href="/vietnam-film-crew/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Film Crew</a>
                            <a href="/drone-filming-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Drone Filming</a>
                        </div>
                    </div>''',
        
        'desktop_documentaries': '''<div class="relative group">
                        <a href="/documentary-filming-vietnam/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200 flex items-center">
                            DOCUMENTARIES
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="absolute top-full left-0 mt-2 w-64 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/documentary-filming-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Documentary Services</a>
                            <a href="/commercial-video-production-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Commercial Production</a>
                            <a href="/news-filming-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">News & Current Affairs</a>
                        </div>
                    </div>''',
        
        'desktop_locations': '''<div class="relative group">
                        <a href="/vietnam-filming-locations/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200 flex items-center">
                            LOCATIONS
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="absolute top-full left-0 mt-2 w-64 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/vietnam-filming-locations/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">All Locations</a>
                            <a href="/ho-chi-minh-city-filming/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Ho Chi Minh City</a>
                            <a href="/hanoi-film-production/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hanoi</a>
                        </div>
                    </div>''',
        
        'mobile_services': '''<a href="/film-production-services/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">SERVICES</a>
                    <a href="/equipment-rental-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Equipment Rental</a>
                    <a href="/location-scouting-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Location Scouting</a>
                    <a href="/film-permits-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Permits</a>
                    <a href="/vietnam-film-crew/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Crew</a>
                    <a href="/drone-filming-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Drone Filming</a>''',
        
        'mobile_documentaries': '''<a href="/documentary-filming-vietnam/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">DOCUMENTARIES</a>
                    <a href="/commercial-video-production-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Commercial Production</a>
                    <a href="/news-filming-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">News & Current Affairs</a>''',
        
        'mobile_locations': '''<a href="/vietnam-filming-locations/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">LOCATIONS</a>
                    <a href="/ho-chi-minh-city-filming/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Ho Chi Minh City</a>
                    <a href="/hanoi-film-production/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hanoi</a>'''
    }

def update_navigation_in_file(file_path):
    """Update navigation in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        nav_templates = get_standard_navigation()
        
        # Determine current page highlighting
        current_page = file_path.replace('/index.html', '').replace('./', '')
        
        # Update desktop navigation sections
        # Services section
        services_pattern = r'<div class="relative group">\s*<a href="/film-production-services/"[^>]*>.*?</div>\s*</div>'
        if re.search(services_pattern, content, re.DOTALL):
            # Highlight services if this is a service page
            services_nav = nav_templates['desktop_services']
            if current_page in ['film-production-services', 'equipment-rental-vietnam', 'location-scouting-vietnam', 'film-permits-vietnam', 'vietnam-film-crew', 'drone-filming-vietnam']:
                services_nav = services_nav.replace('text-vietnam-gray hover:text-vietnam-orange', 'text-vietnam-orange hover:text-white', 1)
                # Highlight specific service
                if current_page == 'equipment-rental-vietnam':
                    services_nav = services_nav.replace('Equipment Rental</a>', 'Equipment Rental</a>').replace('text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800', 'text-vietnam-orange hover:text-white hover:bg-gray-800', 1)
                elif current_page == 'location-scouting-vietnam':
                    services_nav = services_nav.replace('Location Scouting</a>', 'Location Scouting</a>').replace('text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800', 'text-vietnam-orange hover:text-white hover:bg-gray-800', 2)
                elif current_page == 'film-permits-vietnam':
                    services_nav = services_nav.replace('Film Permits</a>', 'Film Permits</a>').replace('text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800', 'text-vietnam-orange hover:text-white hover:bg-gray-800', 3)
                elif current_page == 'vietnam-film-crew':
                    services_nav = services_nav.replace('Film Crew</a>', 'Film Crew</a>').replace('text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800', 'text-vietnam-orange hover:text-white hover:bg-gray-800', 4)
                elif current_page == 'drone-filming-vietnam':
                    services_nav = services_nav.replace('Drone Filming</a>', 'Drone Filming</a>').replace('text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800', 'text-vietnam-orange hover:text-white hover:bg-gray-800', 5)
            
            content = re.sub(services_pattern, services_nav, content, flags=re.DOTALL)
        
        # Add documentaries section if not present
        if 'DOCUMENTARIES' not in content:
            # Find where to insert documentaries section (after services)
            services_end = content.find('</div>\n                    <a href="/filming-in-vietnam/"')
            if services_end != -1:
                docs_nav = nav_templates['desktop_documentaries']
                if current_page in ['documentary-filming-vietnam', 'commercial-video-production-vietnam', 'news-filming-vietnam']:
                    docs_nav = docs_nav.replace('text-vietnam-gray hover:text-vietnam-orange', 'text-vietnam-orange hover:text-white', 1)
                
                content = content[:services_end] + '</div>\n                    ' + docs_nav + '\n                    <a href="/filming-in-vietnam/"' + content[services_end + len('</div>\n                    <a href="/filming-in-vietnam/"'):]
        
        # Add locations section if not present
        if 'LOCATIONS' not in content:
            # Find where to insert locations section (after documentaries)
            docs_end = content.find('</div>\n                    <a href="/filming-in-vietnam/"')
            if docs_end != -1:
                locations_nav = nav_templates['desktop_locations']
                if current_page in ['vietnam-filming-locations', 'ho-chi-minh-city-filming', 'hanoi-film-production']:
                    locations_nav = locations_nav.replace('text-vietnam-gray hover:text-vietnam-orange', 'text-vietnam-orange hover:text-white', 1)
                
                content = content[:docs_end] + '</div>\n                    ' + locations_nav + '\n                    <a href="/filming-in-vietnam/"' + content[docs_end + len('</div>\n                    <a href="/filming-in-vietnam/"'):]
        
        # Update mobile navigation
        mobile_pattern = r'<a href="/film-production-services/"[^>]*>SERVICES</a>\s*<a href="/equipment-rental-vietnam/".*?<a href="/filming-in-vietnam/"'
        if re.search(mobile_pattern, content, re.DOTALL):
            mobile_nav = nav_templates['mobile_services'] + '\n                    ' + nav_templates['mobile_documentaries'] + '\n                    ' + nav_templates['mobile_locations'] + '\n                    <a href="/filming-in-vietnam/"'
            content = re.sub(mobile_pattern, mobile_nav, content, flags=re.DOTALL)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {file_path} - Navigation updated")
            return True
        else:
            print(f"ℹ️  {file_path} - No changes needed")
            return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Update navigation on all HTML pages"""
    print("🚀 Standardizing navigation across all pages...")
    
    # List of all HTML files
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
        'hanoi-film-production/index.html'
    ]
    
    success_count = 0
    total_count = len(html_files)
    
    for file_path in html_files:
        if os.path.exists(file_path):
            if update_navigation_in_file(file_path):
                success_count += 1
        else:
            print(f"⚠️  {file_path} - File not found")
    
    print(f"\n📊 Results: {success_count}/{total_count} files processed")
    print("\n🎉 Navigation standardization complete!")

if __name__ == "__main__":
    main()
