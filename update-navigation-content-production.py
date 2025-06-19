#!/usr/bin/env python3
"""
Update navigation.html to add Content Production megamenu
"""

import re

def update_navigation():
    # Read the current navigation file
    with open('components/navigation.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define the Content Production megamenu HTML
    content_production_menu = '''    <!-- Content Production Mega Menu -->
    <div class="relative mega-menu-trigger">
        <a href="/content-production/" class="text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200 flex items-center" data-nav="contentproduction">
            CONTENT PRODUCTION
            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
            </svg>
        </a>
        <div class="mega-menu">
            <div class="mega-menu-content">
                <div class="text-center mb-8">
                    <h3 class="text-vietnam-orange">Content Production Services</h3>
                    <p class="text-gray-400 text-base">TV, film, commercial, and digital content production</p>
                </div>
                <div class="grid grid-cols-3 gap-10">
                    <!-- Column 1: TV & Film -->
                    <div class="mega-menu-column">
                        <h4>TV & Film Production</h4>
                        <ul>
                            <li><a href="/content-production/tv-shows-broadcast-series/" class="text-gray-300">TV Shows & Broadcast Series</a></li>
                            <li><a href="/content-production/feature-films/" class="text-gray-300">Feature Films</a></li>
                            <li><a href="/content-production/drama-series/" class="text-gray-300">Drama Series</a></li>
                            <li><a href="/content-production/documentaries-docuseries/" class="text-gray-300">Documentaries & Docuseries</a></li>
                            <li><a href="/content-production/narrative-films-web-series/" class="text-gray-300">Narrative Films & Web Series</a></li>
                            <li><a href="/content-production/competition-reality-shows/" class="text-gray-300">Competition & Reality Shows</a></li>
                        </ul>
                    </div>

                    <!-- Column 2: Commercial & Corporate -->
                    <div class="mega-menu-column">
                        <h4>Commercial & Corporate</h4>
                        <ul>
                            <li><a href="/content-production/commercials-advertising/" class="text-gray-300">Commercials & Advertising</a></li>
                            <li><a href="/content-production/corporate-videos/" class="text-gray-300">Corporate Videos</a></li>
                            <li><a href="/content-production/social-media-content/" class="text-gray-300">Social Media Content</a></li>
                            <li><a href="/content-production/live-events-brand-activations/" class="text-gray-300">Live Events & Brand Activations</a></li>
                            <li><a href="/content-production/educational-explainer-videos/" class="text-gray-300">Educational & eLearning Videos</a></li>
                            <li><a href="/content-production/talk-shows-panel-shows/" class="text-gray-300">Talk Shows & Panel Shows</a></li>
                        </ul>
                    </div>

                    <!-- Column 3: Lifestyle & Creative -->
                    <div class="mega-menu-column">
                        <h4>Lifestyle & Creative</h4>
                        <ul>
                            <li><a href="/content-production/music-videos/" class="text-gray-300">Music Videos</a></li>
                            <li><a href="/content-production/fashion-videos/" class="text-gray-300">Fashion Videos</a></li>
                            <li><a href="/content-production/travel-lifestyle-marketing/" class="text-gray-300">Travel & Lifestyle Marketing</a></li>
                            <li><a href="/content-production/hotel-videos-reels/" class="text-gray-300">Hotel Videos & Reels</a></li>
                            <li><a href="/content-production/cookery-shows-food-content/" class="text-gray-300">Cookery Shows & Food Content</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

'''
    
    # Define the mobile Content Production menu
    mobile_content_production_menu = '''        <!-- Content Production Menu -->
        <div class="mobile-mega-menu border-b border-gray-700">
            <button class="mobile-mega-toggle w-full flex items-center justify-between px-4 py-3 text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200"
                    data-target="contentproduction-mega"
                    aria-expanded="false">
                <span class="font-medium">CONTENT PRODUCTION</span>
                <svg class="mobile-mega-icon h-3 w-3 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                </svg>
            </button>

            <div id="contentproduction-mega" class="mobile-mega-submenu hidden bg-gray-800">
                <div class="p-3">
                    <a href="/content-production/" class="block px-3 py-2 text-sm text-vietnam-orange hover:text-white hover:bg-gray-700 rounded transition-colors duration-200 mb-3">
                        All Content Production Services
                    </a>

                    <!-- TV & Film Category -->
                    <div class="mobile-category mb-2">
                        <button class="mobile-category-toggle w-full flex items-center justify-between px-3 py-2 text-sm text-gray-300 hover:text-vietnam-orange hover:bg-gray-700 rounded transition-colors duration-200"
                                data-target="tv-film-submenu"
                                aria-expanded="false">
                            <span>TV & Film Production</span>
                            <svg class="mobile-category-icon h-2 w-2 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div id="tv-film-submenu" class="mobile-category-submenu hidden pl-4 mt-1 space-y-1">
                            <a href="/content-production/tv-shows-broadcast-series/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">TV Shows & Broadcast Series</a>
                            <a href="/content-production/feature-films/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Feature Films</a>
                            <a href="/content-production/drama-series/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Drama Series</a>
                            <a href="/content-production/documentaries-docuseries/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Documentaries & Docuseries</a>
                            <a href="/content-production/narrative-films-web-series/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Narrative Films & Web Series</a>
                            <a href="/content-production/competition-reality-shows/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Competition & Reality Shows</a>
                        </div>
                    </div>

                    <!-- Commercial & Corporate Category -->
                    <div class="mobile-category mb-2">
                        <button class="mobile-category-toggle w-full flex items-center justify-between px-3 py-2 text-sm text-gray-300 hover:text-vietnam-orange hover:bg-gray-700 rounded transition-colors duration-200"
                                data-target="commercial-corporate-submenu"
                                aria-expanded="false">
                            <span>Commercial & Corporate</span>
                            <svg class="mobile-category-icon h-2 w-2 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div id="commercial-corporate-submenu" class="mobile-category-submenu hidden pl-4 mt-1 space-y-1">
                            <a href="/content-production/commercials-advertising/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Commercials & Advertising</a>
                            <a href="/content-production/corporate-videos/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Corporate Videos</a>
                            <a href="/content-production/social-media-content/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Social Media Content</a>
                            <a href="/content-production/live-events-brand-activations/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Live Events & Brand Activations</a>
                            <a href="/content-production/educational-explainer-videos/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Educational & eLearning Videos</a>
                            <a href="/content-production/talk-shows-panel-shows/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Talk Shows & Panel Shows</a>
                        </div>
                    </div>

                    <!-- Lifestyle & Creative Category -->
                    <div class="mobile-category mb-2">
                        <button class="mobile-category-toggle w-full flex items-center justify-between px-3 py-2 text-sm text-gray-300 hover:text-vietnam-orange hover:bg-gray-700 rounded transition-colors duration-200"
                                data-target="lifestyle-creative-submenu"
                                aria-expanded="false">
                            <span>Lifestyle & Creative</span>
                            <svg class="mobile-category-icon h-2 w-2 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div id="lifestyle-creative-submenu" class="mobile-category-submenu hidden pl-4 mt-1 space-y-1">
                            <a href="/content-production/music-videos/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Music Videos</a>
                            <a href="/content-production/fashion-videos/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Fashion Videos</a>
                            <a href="/content-production/travel-lifestyle-marketing/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Travel & Lifestyle Marketing</a>
                            <a href="/content-production/hotel-videos-reels/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Hotel Videos & Reels</a>
                            <a href="/content-production/cookery-shows-food-content/" class="block px-3 py-1 text-xs text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Cookery Shows & Food Content</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

'''
    
    # Find where to insert Content Production in desktop nav (after Post-Production)
    post_production_pattern = r'(<!-- Post-Production Services Mega Menu -->.*?</div>\s*</div>\s*\n)'
    match = re.search(post_production_pattern, content, re.DOTALL)
    
    if match:
        # Insert after Post-Production menu
        insert_pos = match.end()
        content = content[:insert_pos] + '\n' + content_production_menu + content[insert_pos:]
        print("✅ Added Content Production to desktop navigation")
    else:
        print("❌ Could not find Post-Production menu in desktop navigation")
    
    # Find where to insert Content Production in mobile nav (after Post-Production)
    mobile_post_production_pattern = r'(<!-- Post-Production Menu -->.*?</div>\s*</div>\s*\n)'
    match = re.search(mobile_post_production_pattern, content, re.DOTALL)
    
    if match:
        # Insert after Post-Production mobile menu
        insert_pos = match.end()
        content = content[:insert_pos] + '\n' + mobile_content_production_menu + content[insert_pos:]
        print("✅ Added Content Production to mobile navigation")
    else:
        print("❌ Could not find Post-Production in mobile navigation")
    
    # Update component loader to recognize content-production pages
    component_loader_addition = '''
        // Check for content production pages (main and sub-pages)
        if (cleanPath.startsWith('content-production')) {
            return 'contentproduction';
        }
'''
    
    # Write the updated navigation file
    with open('components/navigation.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Navigation updated successfully!")
    
    # Update component loader
    with open('js/component-loader.js', 'r', encoding='utf-8') as f:
        loader_content = f.read()
    
    # Add content production check after production services check
    production_check = "// Check for production services pages (main and sub-pages)\n        if (cleanPath.startsWith('production-services')) {\n            return 'production';\n        }"
    
    if production_check in loader_content:
        loader_content = loader_content.replace(
            production_check,
            production_check + '\n' + component_loader_addition
        )
        
        with open('js/component-loader.js', 'w', encoding='utf-8') as f:
            f.write(loader_content)
        print("✅ Component loader updated!")

if __name__ == "__main__":
    update_navigation()