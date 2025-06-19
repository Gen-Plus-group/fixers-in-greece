#!/usr/bin/env python3
"""
Script to update mobile navigation across all pages with collapsible submenus
"""

import os
import re

def get_mobile_navigation_html():
    """Return the new mobile navigation HTML with collapsible submenus"""
    return '''            <!-- Mobile Navigation -->
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
                        </div>
                    </div>
                    
                    <!-- Documentaries Dropdown -->
                    <div class="mobile-dropdown">
                        <button class="mobile-dropdown-toggle w-full flex items-center justify-between px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200" 
                                data-target="documentaries-submenu"
                                aria-expanded="false">
                            <span>DOCUMENTARIES</span>
                            <svg class="mobile-dropdown-icon h-4 w-4 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div id="documentaries-submenu" class="mobile-submenu hidden pl-4 space-y-1">
                            <a href="/documentary-filming-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Documentary Services</a>
                            <a href="/commercial-video-production-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Commercial Production</a>
                            <a href="/news-filming-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">News & Current Affairs</a>
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

def get_mobile_navigation_javascript():
    """Return the JavaScript for mobile navigation functionality"""
    return '''        // Mobile menu main toggle
        document.getElementById('mobile-menu-button').addEventListener('click', function() {
            const mobileMenu = document.getElementById('mobile-menu');
            const isHidden = mobileMenu.classList.contains('hidden');

            if (isHidden) {
                mobileMenu.classList.remove('hidden');
                this.setAttribute('aria-expanded', 'true');
            } else {
                mobileMenu.classList.add('hidden');
                this.setAttribute('aria-expanded', 'false');
                // Close all submenus when main menu closes
                closeAllMobileSubmenus();
            }
        });

        // Mobile dropdown functionality
        function initializeMobileDropdowns() {
            const dropdownToggles = document.querySelectorAll('.mobile-dropdown-toggle');
            
            dropdownToggles.forEach(function(toggle) {
                toggle.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    const targetId = this.getAttribute('data-target');
                    const submenu = document.getElementById(targetId);
                    const icon = this.querySelector('.mobile-dropdown-icon');
                    const isExpanded = this.getAttribute('aria-expanded') === 'true';
                    
                    // Close other submenus
                    closeAllMobileSubmenus(targetId);
                    
                    if (isExpanded) {
                        // Close this submenu
                        submenu.classList.add('hidden');
                        this.setAttribute('aria-expanded', 'false');
                        icon.style.transform = 'rotate(0deg)';
                    } else {
                        // Open this submenu
                        submenu.classList.remove('hidden');
                        this.setAttribute('aria-expanded', 'true');
                        icon.style.transform = 'rotate(180deg)';
                    }
                });
            });
        }

        function closeAllMobileSubmenus(exceptId) {
            const allSubmenus = document.querySelectorAll('.mobile-submenu');
            const allToggles = document.querySelectorAll('.mobile-dropdown-toggle');
            const allIcons = document.querySelectorAll('.mobile-dropdown-icon');
            
            allSubmenus.forEach(function(submenu) {
                if (!exceptId || submenu.id !== exceptId) {
                    submenu.classList.add('hidden');
                }
            });
            
            allToggles.forEach(function(toggle) {
                if (!exceptId || toggle.getAttribute('data-target') !== exceptId) {
                    toggle.setAttribute('aria-expanded', 'false');
                }
            });
            
            allIcons.forEach(function(icon) {
                const toggle = icon.closest('.mobile-dropdown-toggle');
                if (!exceptId || toggle.getAttribute('data-target') !== exceptId) {
                    icon.style.transform = 'rotate(0deg)';
                }
            });
        }

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            const mobileMenu = document.getElementById('mobile-menu');
            const mobileMenuButton = document.getElementById('mobile-menu-button');

            if (!mobileMenu.contains(event.target) && !mobileMenuButton.contains(event.target)) {
                mobileMenu.classList.add('hidden');
                mobileMenuButton.setAttribute('aria-expanded', 'false');
                closeAllMobileSubmenus();
            }
        });

        // Initialize mobile dropdowns when DOM is loaded
        document.addEventListener('DOMContentLoaded', function() {
            initializeMobileDropdowns();
        });'''

def apply_current_page_highlighting(nav_html, current_page):
    """Apply highlighting for current page in mobile navigation"""
    highlighting_rules = {
        'vietnam-filming-locations': ('LOCATIONS', 'All Locations'),
        'ho-chi-minh-city-filming': ('LOCATIONS', 'Ho Chi Minh City'),
        'hanoi-film-production': ('LOCATIONS', 'Hanoi'),
        'documentary-filming-vietnam': ('DOCUMENTARIES', 'Documentary Services'),
        'commercial-video-production-vietnam': ('DOCUMENTARIES', 'Commercial Production'),
        'news-filming-vietnam': ('DOCUMENTARIES', 'News & Current Affairs'),
        'film-production-services': ('SERVICES', 'All Services'),
        'equipment-rental-vietnam': ('SERVICES', 'Equipment Rental'),
        'location-scouting-vietnam': ('SERVICES', 'Location Scouting'),
        'film-permits-vietnam': ('SERVICES', 'Film Permits'),
        'vietnam-film-crew': ('SERVICES', 'Film Crew'),
        'drone-filming-vietnam': ('SERVICES', 'Drone Filming'),
    }
    
    if current_page == 'index.html' or current_page == '':
        nav_html = nav_html.replace(
            'href="/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange',
            'href="/" class="block px-3 py-2 text-vietnam-orange font-medium hover:text-white'
        )
    elif current_page in highlighting_rules:
        section, item = highlighting_rules[current_page]
        
        # Highlight main section button
        if section == 'SERVICES':
            nav_html = nav_html.replace(
                '<span>SERVICES</span>',
                '<span class="text-vietnam-orange font-medium">SERVICES</span>'
            )
        elif section == 'DOCUMENTARIES':
            nav_html = nav_html.replace(
                '<span>DOCUMENTARIES</span>',
                '<span class="text-vietnam-orange font-medium">DOCUMENTARIES</span>'
            )
        elif section == 'LOCATIONS':
            nav_html = nav_html.replace(
                '<span>LOCATIONS</span>',
                '<span class="text-vietnam-orange font-medium">LOCATIONS</span>'
            )
        
        # Highlight specific item
        if item:
            nav_html = nav_html.replace(
                f'>{item}</a>',
                f' class="text-vietnam-orange font-medium">{item}</a>'
            )
    
    return nav_html

def update_mobile_navigation_in_file(file_path):
    """Update mobile navigation in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip homepage as it's already updated
        if file_path == 'index.html':
            print(f"ℹ️  {file_path} - Already updated (homepage)")
            return True
        
        # Determine current page
        current_page = file_path.replace('/index.html', '').replace('./', '')
        
        # Get mobile navigation HTML and apply highlighting
        mobile_nav_html = get_mobile_navigation_html()
        mobile_nav_html = apply_current_page_highlighting(mobile_nav_html, current_page)
        
        # Replace mobile navigation HTML
        mobile_nav_pattern = r'<!-- Mobile Navigation -->.*?</nav>'
        content = re.sub(mobile_nav_pattern, mobile_nav_html, content, flags=re.DOTALL)
        
        # Update JavaScript for mobile menu
        mobile_js = get_mobile_navigation_javascript()
        
        # Find and replace the mobile menu JavaScript
        js_pattern = r'document\.getElementById\(\'mobile-menu-button\'\)\.addEventListener.*?}\);'
        if re.search(js_pattern, content, re.DOTALL):
            content = re.sub(js_pattern, mobile_js, content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} - Mobile navigation updated")
        return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Update mobile navigation on all pages except homepage"""
    print("🚀 Updating mobile navigation with collapsible submenus...")
    
    # List of HTML files (excluding homepage which is already updated)
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
        'hanoi-film-production/index.html'
    ]
    
    success_count = 0
    total_count = len(html_files)
    
    for file_path in html_files:
        if os.path.exists(file_path):
            if update_mobile_navigation_in_file(file_path):
                success_count += 1
        else:
            print(f"⚠️  {file_path} - File not found")
    
    print(f"\\n📊 Results: {success_count}/{total_count} files updated successfully")
    print("\\n🎉 Mobile navigation update complete!")
    print("\\n📱 Features added:")
    print("   • Collapsible submenus for SERVICES, DOCUMENTARIES, LOCATIONS")
    print("   • Touch-friendly dropdown toggles with animated icons")
    print("   • Proper current page highlighting")
    print("   • Smooth animations and transitions")

if __name__ == "__main__":
    main()
