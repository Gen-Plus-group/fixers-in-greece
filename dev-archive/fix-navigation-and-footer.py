#!/usr/bin/env python3
"""
Script to fix navigation inconsistencies and apply enhanced footer to all pages
"""

import os
import re

def get_enhanced_footer():
    """Return the enhanced footer HTML"""
    return '''    <!-- Footer -->
    <footer class="bg-vietnam-dark border-t border-gray-700 py-12">
        <div class="container mx-auto px-4">
            <div class="grid md:grid-cols-4 gap-8">
                <!-- Company Info -->
                <div>
                    <img src="/wp-content/uploads/2016/10/needafixer-vietnam.png" 
                         alt="NEEDaFIXER" 
                         class="h-12 w-auto mb-4">
                    <p class="text-gray-400 text-sm leading-relaxed">
                        Global film production services connecting you with expert directors, producers, and crew in 100+ countries.
                    </p>
                </div>
                
                <!-- Talent Services -->
                <div>
                    <h3 class="text-white font-semibold mb-4">Talent Services</h3>
                    <ul class="space-y-2">
                        <li><a href="/hire-film-director/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Hire Film Director</a></li>
                        <li><a href="/hire-film-producer/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Hire Film Producer</a></li>
                        <li><a href="/hire-line-producer/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Hire Line Producer</a></li>
                        <li><a href="/hire-dop/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Hire DOP</a></li>
                        <li><a href="/hire-fixer/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Hire Fixer</a></li>
                        <li><a href="/hire-location-manager/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Hire Location Manager</a></li>
                    </ul>
                </div>
                
                <!-- Production Services -->
                <div>
                    <h3 class="text-white font-semibold mb-4">Production Services</h3>
                    <ul class="space-y-2">
                        <li><a href="/film-production-services/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">All Services</a></li>
                        <li><a href="/equipment-rental-vietnam/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Equipment Rental</a></li>
                        <li><a href="/location-scouting-vietnam/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Location Scouting</a></li>
                        <li><a href="/film-permits-vietnam/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Film Permits</a></li>
                        <li><a href="/vietnam-film-crew/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Film Crew</a></li>
                        <li><a href="/post-production-vietnam/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Post-Production</a></li>
                    </ul>
                </div>
                
                <!-- Company & Contact -->
                <div>
                    <h3 class="text-white font-semibold mb-4">Company</h3>
                    <ul class="space-y-2 mb-4">
                        <li><a href="/about-us/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">About Us</a></li>
                        <li><a href="/filming-in-vietnam/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Filming in Vietnam</a></li>
                        <li><a href="/portfolio/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Portfolio</a></li>
                        <li><a href="/contact/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Contact</a></li>
                    </ul>
                    <div class="space-y-2 text-gray-400 text-sm">
                        <div class="flex items-center space-x-2">
                            <span class="text-vietnam-orange">📞</span>
                            <span>+44 (0) 20 8549 2259</span>
                        </div>
                        <div class="flex items-center space-x-2">
                            <span class="text-vietnam-orange">✉️</span>
                            <span>enquiries@needafixer.com</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="border-t border-gray-700 mt-8 pt-8 text-center">
                <p class="text-gray-400 text-sm">
                    © 2024 NEEDaFIXER. All rights reserved. | Global film production services and talent management.
                </p>
            </div>
        </div>
    </footer>'''

def get_standard_desktop_navigation():
    """Return the standard desktop navigation HTML"""
    return '''                        <div class="absolute top-full left-0 mt-2 w-56 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
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
                            <a href="/hire-film-director/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Film Director</a>
                            <a href="/hire-film-producer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Film Producer</a>
                            <a href="/hire-line-producer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Line Producer</a>
                            <a href="/hire-fixer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Fixer</a>
                            <a href="/hire-dop/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire DOP</a>
                            <a href="/hire-location-manager/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Location Manager</a>
                        </div>'''

def get_standard_mobile_navigation():
    """Return the standard mobile navigation HTML"""
    return '''                        <div id="services-submenu" class="mobile-submenu hidden pl-4 space-y-1">
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
                            <a href="/hire-film-director/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Film Director</a>
                            <a href="/hire-film-producer/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Film Producer</a>
                            <a href="/hire-line-producer/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Line Producer</a>
                            <a href="/hire-fixer/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Fixer</a>
                            <a href="/hire-dop/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire DOP</a>
                            <a href="/hire-location-manager/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Location Manager</a>
                        </div>'''

def update_page_navigation_and_footer(file_path, current_page):
    """Update navigation and footer for a single page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update desktop navigation with current page highlighting
        desktop_nav = get_standard_desktop_navigation()
        if current_page:
            desktop_nav = desktop_nav.replace(
                f'<a href="/{current_page}/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">',
                f'<a href="/{current_page}/" class="block px-4 py-3 text-sm text-vietnam-orange hover:text-white hover:bg-gray-800 transition-colors duration-200">'
            )
        
        # Update mobile navigation with current page highlighting
        mobile_nav = get_standard_mobile_navigation()
        if current_page:
            mobile_nav = mobile_nav.replace(
                f'<a href="/{current_page}/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">',
                f'<a href="/{current_page}/" class="block px-3 py-2 text-sm text-vietnam-orange hover:text-white transition-colors duration-200">'
            )
        
        # Replace desktop navigation
        desktop_pattern = r'<div class="absolute top-full left-0 mt-2 w-56 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">.*?</div>'
        content = re.sub(desktop_pattern, desktop_nav, content, flags=re.DOTALL)
        
        # Replace mobile navigation
        mobile_pattern = r'<div id="services-submenu" class="mobile-submenu hidden pl-4 space-y-1">.*?</div>'
        content = re.sub(mobile_pattern, mobile_nav, content, flags=re.DOTALL)
        
        # Replace footer
        footer_pattern = r'<!-- Footer -->.*?</footer>'
        content = re.sub(footer_pattern, get_enhanced_footer(), content, flags=re.DOTALL)
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} - Updated navigation and footer")
        return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Update all pages with consistent navigation and enhanced footer"""
    print("🚀 Fixing navigation inconsistencies and applying enhanced footer...")
    
    # Define pages and their current page identifiers
    pages = [
        ('index.html', None),
        ('hire-film-producer/index.html', 'hire-film-producer'),
        ('hire-line-producer/index.html', 'hire-line-producer'),
        ('hire-fixer/index.html', 'hire-fixer'),
        ('hire-dop/index.html', 'hire-dop'),
        ('hire-location-manager/index.html', 'hire-location-manager'),
    ]
    
    success_count = 0
    for file_path, current_page in pages:
        if os.path.exists(file_path):
            if update_page_navigation_and_footer(file_path, current_page):
                success_count += 1
        else:
            print(f"⚠️  {file_path} - File not found")
    
    print(f"\n📊 Updated {success_count}/{len(pages)} pages")
    print("🎉 Navigation and footer updates completed!")

if __name__ == "__main__":
    main()
