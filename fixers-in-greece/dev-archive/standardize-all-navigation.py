#!/usr/bin/env python3
"""
Script to standardize navigation menus across all pages to match the homepage
"""

import os
import re

def get_homepage_navigation_templates():
    """Extract navigation templates from homepage"""
    
    desktop_nav = '''                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center space-x-8" aria-label="Main navigation">
                    <a href="/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">HOME</a>
                    <a href="/about-us/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">ABOUT US</a>
                    <div class="relative group">
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
                            <a href="/corporate-video-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Corporate Video</a>
                            <a href="/equipment-transport-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Equipment Transport</a>
                            <a href="/translation-services-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Translation Services</a>
                            <a href="/casting-services-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Casting Services</a>
                            <a href="/post-production-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Post-Production Services</a>
                        </div>
                    </div>
                    <div class="relative group">
                        <a href="/documentary-filming-vietnam/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200 flex items-center">
                            MEDIA PRODUCTION
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="absolute top-full left-0 mt-2 w-64 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/documentary-filming-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Documentary Services</a>
                            <a href="/commercial-video-production-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Commercial Production</a>
                            <a href="/news-filming-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">News & Current Affairs</a>
                            <a href="/music-video-production-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Music Video Production</a>
                            <a href="/event-filming-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Event Filming</a>
                            <a href="/live-streaming-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Live Streaming</a>
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
                            <a href="/ho-chi-minh-city-filming/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Ho Chi Minh City</a>
                            <a href="/hanoi-film-production/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hanoi</a>
                        </div>
                    </div>
                    <a href="/filming-in-vietnam/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">FILMING GUIDE</a>
                    <a href="/portfolio/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">PORTFOLIO</a>
                    <a href="/clients/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CLIENTS</a>
                    <a href="/contact/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
                </nav>'''

    mobile_nav = '''            <!-- Mobile Navigation -->
            <nav class="lg:hidden hidden" id="mobile-menu" aria-label="Mobile navigation">
                <div class="px-2 pt-2 pb-3 space-y-1 border-t border-gray-700">
                    <a href="/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">HOME</a>
                    <a href="/about-us/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">ABOUT US</a>

                    <!-- Services Dropdown -->
                    <div class="mobile-dropdown">
                        <button class="mobile-dropdown-toggle w-full flex items-center justify-between px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200"
                                data-target="services-submenu"
                                aria-expanded="false">
                            <span>SERVICES</span>
                            <svg class="mobile-dropdown-icon h-4 w-4 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div id="services-submenu" class="mobile-submenu hidden pl-4 space-y-1">
                            <a href="/film-production-services/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">All Services</a>
                            <a href="/equipment-rental-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Equipment Rental</a>
                            <a href="/location-scouting-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Location Scouting</a>
                            <a href="/film-permits-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Permits</a>
                            <a href="/vietnam-film-crew/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Crew</a>
                            <a href="/drone-filming-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Drone Filming</a>
                            <a href="/corporate-video-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Corporate Video</a>
                            <a href="/equipment-transport-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Equipment Transport</a>
                            <a href="/translation-services-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Translation Services</a>
                            <a href="/casting-services-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Casting Services</a>
                            <a href="/post-production-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Post-Production Services</a>
                        </div>
                    </div>

                    <!-- Documentaries Dropdown -->
                    <div class="mobile-dropdown">
                        <button class="mobile-dropdown-toggle w-full flex items-center justify-between px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200"
                                data-target="documentaries-submenu"
                                aria-expanded="false">
                            <span>MEDIA PRODUCTION</span>
                            <svg class="mobile-dropdown-icon h-4 w-4 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div id="documentaries-submenu" class="mobile-submenu hidden pl-4 space-y-1">
                            <a href="/documentary-filming-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Documentary Services</a>
                            <a href="/commercial-video-production-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Commercial Production</a>
                            <a href="/news-filming-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">News & Current Affairs</a>
                            <a href="/music-video-production-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Music Video Production</a>
                            <a href="/event-filming-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Event Filming</a>
                            <a href="/live-streaming-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Live Streaming</a>
                        </div>
                    </div>

                    <!-- Locations Dropdown -->
                    <div class="mobile-dropdown">
                        <button class="mobile-dropdown-toggle w-full flex items-center justify-between px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200"
                                data-target="locations-submenu"
                                aria-expanded="false">
                            <span>LOCATIONS</span>
                            <svg class="mobile-dropdown-icon h-4 w-4 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div id="locations-submenu" class="mobile-submenu hidden pl-4 space-y-1">
                            <a href="/vietnam-filming-locations/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">All Locations</a>
                            <a href="/ho-chi-minh-city-filming/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Ho Chi Minh City</a>
                            <a href="/hanoi-film-production/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hanoi</a>
                        </div>
                    </div>

                    <a href="/filming-in-vietnam/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">FILMING GUIDE</a>
                    <a href="/portfolio/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">PORTFOLIO</a>
                    <a href="/clients/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CLIENTS</a>
                    <a href="/contact/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
                </div>
            </nav>'''

    return desktop_nav, mobile_nav

def apply_current_page_highlighting(nav_content, current_page):
    """Apply highlighting for current page"""
    # Define page highlighting rules
    highlighting_rules = {
        'about-us': ('ABOUT US', ''),
        'contact': ('CONTACT', ''),
        'portfolio': ('PORTFOLIO', ''),
        'clients': ('CLIENTS', ''),
        'filming-in-vietnam': ('FILMING GUIDE', ''),
        'film-production-services': ('SERVICES', ''),
        'equipment-rental-vietnam': ('SERVICES', 'Equipment Rental'),
        'location-scouting-vietnam': ('SERVICES', 'Location Scouting'),
        'film-permits-vietnam': ('SERVICES', 'Film Permits'),
        'vietnam-film-crew': ('SERVICES', 'Film Crew'),
        'drone-filming-vietnam': ('SERVICES', 'Drone Filming'),
        'corporate-video-vietnam': ('SERVICES', 'Corporate Video'),
        'equipment-transport-vietnam': ('SERVICES', 'Equipment Transport'),
        'translation-services-vietnam': ('SERVICES', 'Translation Services'),
        'casting-services-vietnam': ('SERVICES', 'Casting Services'),
        'post-production-vietnam': ('SERVICES', 'Post-Production Services'),
        'documentary-filming-vietnam': ('MEDIA PRODUCTION', 'Documentary Services'),
        'commercial-video-production-vietnam': ('MEDIA PRODUCTION', 'Commercial Production'),
        'news-filming-vietnam': ('MEDIA PRODUCTION', 'News & Current Affairs'),
        'music-video-production-vietnam': ('MEDIA PRODUCTION', 'Music Video Production'),
        'event-filming-vietnam': ('MEDIA PRODUCTION', 'Event Filming'),
        'live-streaming-vietnam': ('MEDIA PRODUCTION', 'Live Streaming'),
        'vietnam-filming-locations': ('LOCATIONS', 'All Locations'),
        'ho-chi-minh-city-filming': ('LOCATIONS', 'Ho Chi Minh City'),
        'hanoi-film-production': ('LOCATIONS', 'Hanoi'),
    }
    
    if current_page in highlighting_rules:
        section, item = highlighting_rules[current_page]
        
        # Highlight main section
        nav_content = nav_content.replace(
            f'>{section}</a>',
            f' class="text-vietnam-orange hover:text-white">{section}</a>'
        ).replace(
            f'>{section}</span>',
            f' class="text-vietnam-orange hover:text-white">{section}</span>'
        )
        
        # Highlight specific item
        if item:
            nav_content = nav_content.replace(
                f'>{item}</a>',
                f' class="text-vietnam-orange hover:text-white">{item}</a>'
            )
    
    # Special case for homepage
    if current_page == 'index' or current_page == '':
        nav_content = nav_content.replace(
            'href="/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange',
            'href="/" class="block px-3 py-2 text-vietnam-orange font-medium hover:text-white'
        )
    
    return nav_content

def standardize_navigation_in_file(file_path):
    """Standardize navigation in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Determine current page
        current_page = file_path.replace('/index.html', '').replace('./', '')
        if current_page == 'index.html':
            current_page = 'index'

        # Get standard navigation templates
        desktop_nav, mobile_nav = get_homepage_navigation_templates()

        # Apply current page highlighting
        desktop_nav = apply_current_page_highlighting(desktop_nav, current_page)
        mobile_nav = apply_current_page_highlighting(mobile_nav, current_page)

        # Replace desktop navigation
        desktop_pattern = r'<!-- Desktop Navigation -->.*?</nav>'
        if re.search(desktop_pattern, content, re.DOTALL):
            content = re.sub(desktop_pattern, desktop_nav, content, flags=re.DOTALL)
        else:
            print(f"⚠️  {file_path} - Desktop navigation pattern not found")
            return False

        # Replace mobile navigation
        mobile_pattern = r'<!-- Mobile Navigation -->.*?</nav>\s*</div>\s*</header>'
        if re.search(mobile_pattern, content, re.DOTALL):
            content = re.sub(mobile_pattern, mobile_nav + '\n        </div>\n    </header>', content, flags=re.DOTALL)
        else:
            print(f"⚠️  {file_path} - Mobile navigation pattern not found")
            return False

        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ {file_path} - Navigation standardized")
        return True

    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Standardize navigation on all HTML pages"""
    print("🚀 Standardizing navigation across all pages...")

    # List of all HTML files to update (excluding homepage)
    html_files = [
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
            if standardize_navigation_in_file(file_path):
                success_count += 1
        else:
            print(f"⚠️  {file_path} - File not found")

    print(f"\n📊 Navigation standardization completed: {success_count}/{total_count} files updated")

    if success_count == total_count:
        print("🎉 All navigation menus have been successfully standardized!")
    else:
        print(f"⚠️  {total_count - success_count} files had issues and may need manual review")

if __name__ == "__main__":
    main()
