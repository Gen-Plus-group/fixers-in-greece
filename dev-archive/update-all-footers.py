#!/usr/bin/env python3
"""
Script to update footers on all pages across the website
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

def update_footer_in_file(file_path):
    """Update footer in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace footer
        footer_pattern = r'<!-- Footer -->.*?</footer>'
        content = re.sub(footer_pattern, get_enhanced_footer(), content, flags=re.DOTALL)
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} - Footer updated")
        return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Update footers on all HTML pages"""
    print("🚀 Updating enhanced footer across all pages...")
    
    # Get all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == 'index.html':
                html_files.append(os.path.join(root, file))
    
    success_count = 0
    for file_path in html_files:
        if update_footer_in_file(file_path):
            success_count += 1
    
    print(f"\n📊 Updated {success_count}/{len(html_files)} files")
    print("🎉 All footers have been updated with enhanced design!")

if __name__ == "__main__":
    main()
