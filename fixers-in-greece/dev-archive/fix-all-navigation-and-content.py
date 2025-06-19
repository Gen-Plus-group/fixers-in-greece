#!/usr/bin/env python3
"""
Script to fix all navigation consistency and add content to coming soon pages
"""

import os
import re

def get_standard_navigation_template():
    """Return the standard navigation template"""
    return '''                <!-- Desktop Navigation -->
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
                        </div>
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
                            <a href="/commercial-video-production-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Commercial Production</a>
                            <a href="/news-filming-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">News & Current Affairs</a>
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

def get_standard_mobile_navigation():
    """Return the standard mobile navigation"""
    return '''            <!-- Mobile Navigation -->
            <nav class="lg:hidden hidden" id="mobile-menu" aria-label="Mobile navigation">
                <div class="px-2 pt-2 pb-3 space-y-1 border-t border-gray-700">
                    <a href="/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">HOME</a>
                    <a href="/about-us/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">ABOUT US</a>
                    <a href="/film-production-services/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">SERVICES</a>
                    <a href="/equipment-rental-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Equipment Rental</a>
                    <a href="/location-scouting-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Location Scouting</a>
                    <a href="/film-permits-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Permits</a>
                    <a href="/vietnam-film-crew/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Crew</a>
                    <a href="/drone-filming-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Drone Filming</a>
                    <a href="/documentary-filming-vietnam/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">DOCUMENTARIES</a>
                    <a href="/commercial-video-production-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Commercial Production</a>
                    <a href="/news-filming-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">News & Current Affairs</a>
                    <a href="/vietnam-filming-locations/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">LOCATIONS</a>
                    <a href="/ho-chi-minh-city-filming/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Ho Chi Minh City</a>
                    <a href="/hanoi-film-production/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hanoi</a>
                    <a href="/filming-in-vietnam/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">FILMING GUIDE</a>
                    <a href="/portfolio/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">PORTFOLIO</a>
                    <a href="/clients/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CLIENTS</a>
                    <a href="/contact/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
                </div>
            </nav>'''

def apply_current_page_highlighting(nav_content, current_page):
    """Apply highlighting for current page"""
    # Define page highlighting rules
    highlighting_rules = {
        'vietnam-filming-locations': ('LOCATIONS', 'All Locations'),
        'ho-chi-minh-city-filming': ('LOCATIONS', 'Ho Chi Minh City'),
        'hanoi-film-production': ('LOCATIONS', 'Hanoi'),
        'documentary-filming-vietnam': ('DOCUMENTARIES', 'Documentary Services'),
        'commercial-video-production-vietnam': ('DOCUMENTARIES', 'Commercial Production'),
        'news-filming-vietnam': ('DOCUMENTARIES', 'News & Current Affairs'),
        'film-production-services': ('SERVICES', ''),
        'equipment-rental-vietnam': ('SERVICES', 'Equipment Rental'),
        'location-scouting-vietnam': ('SERVICES', 'Location Scouting'),
        'film-permits-vietnam': ('SERVICES', 'Film Permits'),
        'vietnam-film-crew': ('SERVICES', 'Film Crew'),
        'drone-filming-vietnam': ('SERVICES', 'Drone Filming'),
    }
    
    if current_page in highlighting_rules:
        section, item = highlighting_rules[current_page]
        
        # Highlight main section
        if section == 'SERVICES':
            nav_content = nav_content.replace(
                'href="/film-production-services/" class="text-vietnam-gray hover:text-vietnam-orange',
                'href="/film-production-services/" class="text-vietnam-orange hover:text-white'
            )
        elif section == 'DOCUMENTARIES':
            nav_content = nav_content.replace(
                'href="/documentary-filming-vietnam/" class="text-vietnam-gray hover:text-vietnam-orange',
                'href="/documentary-filming-vietnam/" class="text-vietnam-orange hover:text-white'
            )
        elif section == 'LOCATIONS':
            nav_content = nav_content.replace(
                'href="/vietnam-filming-locations/" class="text-vietnam-gray hover:text-vietnam-orange',
                'href="/vietnam-filming-locations/" class="text-vietnam-orange hover:text-white'
            )
        
        # Highlight specific item
        if item:
            nav_content = nav_content.replace(
                f'>{item}</a>',
                f' class="text-vietnam-orange hover:text-white">{item}</a>'
            ).replace(
                'text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200"',
                'text-vietnam-orange hover:text-white hover:bg-gray-800 transition-colors duration-200"'
            )
    
    return nav_content

def fix_navigation_in_file(file_path):
    """Fix navigation in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine current page
        current_page = file_path.replace('/index.html', '').replace('./', '')
        if current_page == 'index.html':
            current_page = 'home'
        
        # Get standard navigation templates
        desktop_nav = get_standard_navigation_template()
        mobile_nav = get_standard_mobile_navigation()
        
        # Apply current page highlighting
        desktop_nav = apply_current_page_highlighting(desktop_nav, current_page)
        mobile_nav = apply_current_page_highlighting(mobile_nav, current_page)
        
        # Replace desktop navigation
        desktop_pattern = r'<!-- Desktop Navigation -->.*?</nav>'
        content = re.sub(desktop_pattern, desktop_nav, content, flags=re.DOTALL)
        
        # Replace mobile navigation
        mobile_pattern = r'<!-- Mobile Navigation -->.*?</nav>'
        content = re.sub(mobile_pattern, mobile_nav, content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} - Navigation fixed")
        return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def add_content_to_coming_soon_pages():
    """Add proper content to pages that say 'coming soon'"""
    
    # Define content for each page
    page_contents = {
        'drone-filming-vietnam': {
            'title': 'Professional Drone Services',
            'content': '''
        <!-- Drone Services -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-vietnam-orange mb-4">
                        Professional Drone Filming Services
                    </h2>
                    <p class="text-xl text-gray-300 max-w-3xl mx-auto">
                        Licensed UAV operators providing stunning aerial cinematography across Vietnam with proper permits and safety protocols.
                    </p>
                </div>

                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <!-- Professional Equipment -->
                    <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6">
                        <div class="text-4xl mb-4 text-center">🚁</div>
                        <h3 class="text-xl font-bold text-vietnam-orange mb-3 text-center">Professional Equipment</h3>
                        <ul class="text-gray-300 space-y-2 mb-4">
                            <li>• DJI Inspire 2 with X7 camera</li>
                            <li>• DJI Mavic 3 Cine</li>
                            <li>• 4K and 6K recording capabilities</li>
                            <li>• Professional gimbal stabilization</li>
                            <li>• Long-range transmission systems</li>
                        </ul>
                    </div>

                    <!-- Licensed Operators -->
                    <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6">
                        <div class="text-4xl mb-4 text-center">👨‍✈️</div>
                        <h3 class="text-xl font-bold text-vietnam-orange mb-3 text-center">Licensed Operators</h3>
                        <ul class="text-gray-300 space-y-2 mb-4">
                            <li>• Vietnam CAA certified pilots</li>
                            <li>• International flight experience</li>
                            <li>• Safety protocol training</li>
                            <li>• Insurance coverage included</li>
                            <li>• Emergency procedures certified</li>
                        </ul>
                    </div>

                    <!-- Permit Compliance -->
                    <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6">
                        <div class="text-4xl mb-4 text-center">📋</div>
                        <h3 class="text-xl font-bold text-vietnam-orange mb-3 text-center">Permit Compliance</h3>
                        <ul class="text-gray-300 space-y-2 mb-4">
                            <li>• CAA flight permit applications</li>
                            <li>• No-fly zone navigation</li>
                            <li>• Military coordination when required</li>
                            <li>• Location-specific permissions</li>
                            <li>• Real-time airspace monitoring</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>'''
        },
        
        'commercial-video-production-vietnam': {
            'title': 'Commercial Video Production',
            'content': '''
        <!-- Commercial Services -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-vietnam-orange mb-4">
                        Commercial Video Production Services
                    </h2>
                    <p class="text-xl text-gray-300 max-w-3xl mx-auto">
                        Professional commercial and advertising video production in Vietnam for international brands and agencies.
                    </p>
                </div>

                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <!-- TV Commercials -->
                    <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6">
                        <div class="text-4xl mb-4 text-center">📺</div>
                        <h3 class="text-xl font-bold text-vietnam-orange mb-3 text-center">TV Commercials</h3>
                        <ul class="text-gray-300 space-y-2 mb-4">
                            <li>• Broadcast quality production</li>
                            <li>• Multi-camera setups</li>
                            <li>• Professional lighting design</li>
                            <li>• Celebrity talent coordination</li>
                            <li>• Post-production services</li>
                        </ul>
                    </div>

                    <!-- Digital Advertising -->
                    <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6">
                        <div class="text-4xl mb-4 text-center">💻</div>
                        <h3 class="text-xl font-bold text-vietnam-orange mb-3 text-center">Digital Advertising</h3>
                        <ul class="text-gray-300 space-y-2 mb-4">
                            <li>• Social media content</li>
                            <li>• Online video campaigns</li>
                            <li>• Multiple format delivery</li>
                            <li>• Platform optimization</li>
                            <li>• Analytics integration</li>
                        </ul>
                    </div>

                    <!-- Brand Videos -->
                    <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6">
                        <div class="text-4xl mb-4 text-center">🏢</div>
                        <h3 class="text-xl font-bold text-vietnam-orange mb-3 text-center">Brand Videos</h3>
                        <ul class="text-gray-300 space-y-2 mb-4">
                            <li>• Corporate storytelling</li>
                            <li>• Product launches</li>
                            <li>• Company profiles</li>
                            <li>• Executive interviews</li>
                            <li>• Event coverage</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>'''
        }
    }
    
    for page_name, page_data in page_contents.items():
        file_path = f"{page_name}/index.html"
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace "Coming Soon" content
                coming_soon_pattern = r'<h2 class="text-3xl font-bold text-vietnam-orange mb-6">Coming Soon</h2>.*?</section>'
                if re.search(coming_soon_pattern, content, re.DOTALL):
                    content = re.sub(coming_soon_pattern, page_data['content'] + '\n        </section>', content, flags=re.DOTALL)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"✅ {file_path} - Content added")
                else:
                    print(f"ℹ️  {file_path} - No coming soon content found")
                    
            except Exception as e:
                print(f"❌ {file_path} - Error: {e}")

def main():
    """Fix all navigation and content issues"""
    print("🚀 Fixing all navigation and content issues...")
    
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
    
    print("\n📋 Fixing navigation consistency...")
    success_count = 0
    for file_path in html_files:
        if os.path.exists(file_path):
            if fix_navigation_in_file(file_path):
                success_count += 1
        else:
            print(f"⚠️  {file_path} - File not found")
    
    print(f"\n📊 Navigation: {success_count}/{len(html_files)} files fixed")
    
    print("\n📝 Adding content to coming soon pages...")
    add_content_to_coming_soon_pages()
    
    print("\n🎉 All fixes completed!")

if __name__ == "__main__":
    main()
