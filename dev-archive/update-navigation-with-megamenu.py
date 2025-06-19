#!/usr/bin/env python3
"""
Script to update navigation across all existing pages to include Pre-Production mega menu
"""

import os
import re

def get_updated_desktop_navigation():
    """Return updated desktop navigation with Pre-Production mega menu"""
    return '''                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center space-x-8" aria-label="Main navigation">
                    <a href="/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">HOME</a>
                    <a href="/about-us/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">ABOUT US</a>
                    
                    <!-- Pre-Production Mega Menu -->
                    <div class="relative mega-menu-trigger">
                        <a href="/pre-production-services/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200 flex items-center">
                            PRE-PRODUCTION
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="mega-menu">
                            <div class="container mx-auto px-4 py-8">
                                <div class="text-center mb-6">
                                    <h3 class="text-xl font-bold text-vietnam-orange">Pre-Production Services</h3>
                                    <p class="text-gray-400 text-sm">Planning, creative development, logistics</p>
                                </div>
                                <div class="grid grid-cols-6 gap-6">
                                    <!-- Creative & Development -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Creative & Development</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/scriptwriting/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Scriptwriting</a></li>
                                            <li><a href="/pre-production-services/script-consultation/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Script Consultation</a></li>
                                            <li><a href="/pre-production-services/storyboarding/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Storyboarding</a></li>
                                            <li><a href="/pre-production-services/concept-development/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Concept Development</a></li>
                                            <li><a href="/pre-production-services/creative-direction/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Creative Direction</a></li>
                                            <li><a href="/pre-production-services/moodboard-creation/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Moodboards</a></li>
                                            <li><a href="/pre-production-services/pitch-deck-design/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Pitch Decks</a></li>
                                        </ul>
                                    </div>
                                    
                                    <!-- Casting & Talent -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Casting & Talent</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/casting-services/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Casting Services</a></li>
                                            <li><a href="/pre-production-services/voiceover-casting/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Voiceover Casting</a></li>
                                            <li><a href="/pre-production-services/talent-coordination/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Talent Coordination</a></li>
                                            <li><a href="/pre-production-services/union-talent-management/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Union Management</a></li>
                                        </ul>
                                    </div>
                                    
                                    <!-- Location & Permits -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Location & Permits</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/location-scouting-services/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Location Scouting</a></li>
                                            <li><a href="/pre-production-services/location-management/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Location Management</a></li>
                                            <li><a href="/pre-production-services/film-permit-acquisition/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Permit Acquisition</a></li>
                                            <li><a href="/pre-production-services/site-surveys/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Site Surveys</a></li>
                                            <li><a href="/pre-production-services/production-insurance/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Production Insurance</a></li>
                                        </ul>
                                    </div>
                                    
                                    <!-- Budgeting & Scheduling -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Budgeting & Scheduling</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/production-budgeting/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Production Budgeting</a></li>
                                            <li><a href="/pre-production-services/cost-estimation/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Cost Estimation</a></li>
                                            <li><a href="/pre-production-services/production-scheduling/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Production Scheduling</a></li>
                                            <li><a href="/pre-production-services/call-sheets/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Call Sheets</a></li>
                                        </ul>
                                    </div>
                                    
                                    <!-- Crew & Logistics -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Crew & Logistics</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/line-producing-services/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Line Producing</a></li>
                                            <li><a href="/pre-production-services/crew-hiring/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Crew Hiring</a></li>
                                            <li><a href="/pre-production-services/fixer-services-local/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Local Fixers</a></li>
                                            <li><a href="/pre-production-services/travel-logistics/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Travel Logistics</a></li>
                                            <li><a href="/pre-production-services/equipment-planning/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Equipment Planning</a></li>
                                            <li><a href="/pre-production-services/catering-services/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Catering Services</a></li>
                                        </ul>
                                    </div>
                                    
                                    <!-- Legal & Administrative -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Legal & Administrative</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/contract-management/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Contract Management</a></li>
                                            <li><a href="/pre-production-services/talent-releases/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Talent Releases</a></li>
                                            <li><a href="/pre-production-services/location-agreements/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Location Agreements</a></li>
                                            <li><a href="/pre-production-services/licensing-rights/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Licensing & Rights</a></li>
                                            <li><a href="/pre-production-services/covid-compliance/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">COVID Compliance</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
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
                            <a href="/hire-film-director/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Film Director</a>
                            <a href="/hire-film-producer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Film Producer</a>
                            <a href="/hire-line-producer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Line Producer</a>
                            <a href="/hire-fixer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Fixer</a>
                            <a href="/hire-dop/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire DOP</a>
                            <a href="/hire-location-manager/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Location Manager</a>
                        </div>
                    </div>
                    <a href="/filming-in-vietnam/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">FILMING IN VIETNAM</a>
                    <a href="/portfolio/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">PORTFOLIO</a>
                    <a href="/contact/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
                </nav>'''

def get_updated_mobile_navigation():
    """Return updated mobile navigation with Pre-Production submenu"""
    return '''        <!-- Mobile Navigation Menu -->
        <div id="mobile-menu" class="lg:hidden hidden bg-vietnam-dark border-t border-gray-700">
            <div class="px-4 py-4 space-y-2">
                <a href="/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">HOME</a>
                <a href="/about-us/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">ABOUT US</a>
                
                <!-- Pre-Production Mobile Menu -->
                <div>
                    <button class="mobile-dropdown-toggle w-full flex items-center justify-between px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200"
                            data-target="preproduction-submenu"
                            aria-expanded="false">
                        PRE-PRODUCTION
                        <svg class="mobile-dropdown-icon h-4 w-4 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                        </svg>
                    </button>
                    <div id="preproduction-submenu" class="mobile-submenu hidden pl-4 space-y-1">
                        <a href="/pre-production-services/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">All Pre-Production</a>
                        <a href="/pre-production-services/scriptwriting/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Scriptwriting</a>
                        <a href="/pre-production-services/casting-services/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Casting Services</a>
                        <a href="/pre-production-services/location-scouting-services/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Location Scouting</a>
                        <a href="/pre-production-services/production-budgeting/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Production Budgeting</a>
                        <a href="/pre-production-services/line-producing-services/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Line Producing</a>
                        <a href="/pre-production-services/contract-management/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Contract Management</a>
                    </div>
                </div>
                
                <!-- Services Mobile Menu -->
                <div>
                    <button class="mobile-dropdown-toggle w-full flex items-center justify-between px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200"
                            data-target="services-submenu"
                            aria-expanded="false">
                        SERVICES
                        <svg class="mobile-dropdown-icon h-4 w-4 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                        </svg>
                    </button>
                    <div id="services-submenu" class="mobile-submenu hidden pl-4 space-y-1">
                        <a href="/film-production-services/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">All Services</a>
                        <a href="/equipment-rental-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Equipment Rental</a>
                        <a href="/location-scouting-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Location Scouting</a>
                        <a href="/film-permits-vietnam/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Permits</a>
                        <a href="/vietnam-film-crew/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Crew</a>
                        <a href="/hire-film-director/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Film Director</a>
                        <a href="/hire-film-producer/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Film Producer</a>
                        <a href="/hire-line-producer/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Line Producer</a>
                        <a href="/hire-fixer/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Fixer</a>
                        <a href="/hire-dop/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire DOP</a>
                        <a href="/hire-location-manager/" class="block px-3 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Hire Location Manager</a>
                    </div>
                </div>
                
                <a href="/filming-in-vietnam/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">FILMING IN VIETNAM</a>
                <a href="/portfolio/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">PORTFOLIO</a>
                <a href="/contact/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
            </div>
        </div>'''

def get_mega_menu_styles():
    """Return mega menu CSS styles"""
    return '''        /* Mega Menu Styles */
        .mega-menu {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: #1a1a1a;
            border-top: 2px solid #ff6b35;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            opacity: 0;
            visibility: hidden;
            transform: translateY(-10px);
            transition: all 0.3s ease;
            z-index: 50;
        }
        
        .mega-menu-trigger:hover .mega-menu {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }
        
        .mega-menu-column {
            border-right: 1px solid #333;
        }
        
        .mega-menu-column:last-child {
            border-right: none;
        }'''

def update_page_navigation(file_path):
    """Update navigation on a single page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add mega menu styles if not present
        if 'mega-menu' not in content:
            styles_pattern = r'(<!-- Custom Styles -->.*?<style>)(.*?)(</style>)'
            mega_styles = get_mega_menu_styles()
            content = re.sub(styles_pattern, rf'\1\2{mega_styles}\n        \3', content, flags=re.DOTALL)
        
        # Update desktop navigation
        desktop_pattern = r'<!-- Desktop Navigation -->.*?</nav>'
        content = re.sub(desktop_pattern, get_updated_desktop_navigation(), content, flags=re.DOTALL)
        
        # Update mobile navigation
        mobile_pattern = r'<!-- Mobile Navigation Menu -->.*?</div>\s*</div>'
        content = re.sub(mobile_pattern, get_updated_mobile_navigation(), content, flags=re.DOTALL)
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """Update navigation across all existing pages"""
    print("🚀 Updating navigation with Pre-Production mega menu...")
    
    # Get all HTML files except pre-production pages
    html_files = []
    for root, dirs, files in os.walk('.'):
        # Skip pre-production-services directory
        if 'pre-production-services' in root:
            continue
        for file in files:
            if file == 'index.html':
                html_files.append(os.path.join(root, file))
    
    success_count = 0
    for file_path in html_files:
        if update_page_navigation(file_path):
            print(f"✅ Updated {file_path}")
            success_count += 1
    
    print(f"\n📊 Updated {success_count}/{len(html_files)} pages")
    print("🎉 Navigation update completed!")

if __name__ == "__main__":
    main()
