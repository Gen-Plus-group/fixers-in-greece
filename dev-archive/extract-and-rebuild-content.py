#!/usr/bin/env python3
"""
Script to extract content from original minified files and rebuild with modern Tailwind layouts
"""

import re
import html
from pathlib import Path

def extract_content_from_minified(file_path):
    """Extract meaningful content from minified HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title from meta tag
        title_match = re.search(r'<title>([^<]+)</title>', content)
        title = title_match.group(1) if title_match else "Page Title"
        
        # Extract description from meta tag
        desc_match = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', content)
        description = desc_match.group(1) if desc_match else "Page description"
        
        # Extract main content between wpb_wrapper tags
        content_patterns = [
            r'<div class="wpb_wrapper[^"]*"[^>]*>(.*?)</div>',
            r'<h[1-6][^>]*>([^<]+)</h[1-6]>',
            r'<p[^>]*>([^<]+)</p>',
            r'<li[^>]*>([^<]+)</li>',
            r'<strong>([^<]+)</strong>',
            r'<a[^>]*href="([^"]*)"[^>]*>([^<]+)</a>'
        ]
        
        extracted_content = []
        
        # Look for text content in various patterns
        text_matches = re.findall(r'>([^<]{20,})<', content)
        for match in text_matches:
            clean_text = html.unescape(match.strip())
            if clean_text and len(clean_text) > 20 and not clean_text.startswith('var '):
                extracted_content.append(clean_text)
        
        return {
            'title': html.unescape(title),
            'description': html.unescape(description),
            'content': extracted_content[:10]  # Limit to first 10 meaningful pieces
        }
        
    except Exception as e:
        print(f"Error extracting from {file_path}: {e}")
        return None

def create_content_based_page(page_key, extracted_data):
    """Create a page with extracted content"""
    
    # Page-specific configurations
    page_configs = {
        'filming-in-vietnam': {
            'hero_title': 'Filming in Vietnam',
            'hero_subtitle': 'Your complete guide to successful film production in Vietnam',
            'current_page': 'FILMING IN VIETNAM'
        },
        'portfolio': {
            'hero_title': 'Our Portfolio',
            'hero_subtitle': 'Showcasing successful international productions filmed in Vietnam',
            'current_page': 'PORTFOLIO'
        },
        'clients': {
            'hero_title': 'Our Clients',
            'hero_subtitle': 'Trusted by leading international broadcasters and production companies worldwide',
            'current_page': 'CLIENTS'
        },
        'contact': {
            'hero_title': 'Contact Us',
            'hero_subtitle': 'Ready to start your Vietnam production? Get in touch for a personalized quote',
            'current_page': 'CONTACT'
        }
    }
    
    config = page_configs.get(page_key, {
        'hero_title': 'Page Title',
        'hero_subtitle': 'Page subtitle',
        'current_page': 'PAGE'
    })
    
    # Determine active menu states
    services_active = page_key in ['location-scouting-vietnam', 'film-permits-vietnam']
    current_active = config['current_page']
    
    html_content = f'''<!DOCTYPE html>
<html lang="en-US" itemscope itemtype="http://schema.org/WebPage">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- SEO Meta Tags -->
    <title>{extracted_data['title']}</title>
    <meta name="description" content="{extracted_data['description']}">
    <meta name="geo.region" content="VN">
    <meta name="geo.placename" content="Vietnam">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="/{page_key}/">
    
    <!-- Favicon -->
    <link rel="icon" sizes="32x32" href="/wp-content/uploads/2024/09/favicon-32x32-1.png">
    <link rel="shortcut icon" href="/wp-content/uploads/2024/09/favicon-32x32-1.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/wp-content/uploads/2024/09/apple-touch-icon.png">
    
    <!-- Tailwind CSS -->
    <link href="/dist/output.css" rel="stylesheet">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    
    <!-- Custom Styles -->
    <style>
        .page-hero-bg {{
            background-image: url('/wp-content/uploads/2015/10/VIETNAM-services.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
    </style>
</head>

<body class="bg-vietnam-darker text-white font-sans">
    <!-- Skip to Content -->
    <a href="#main-content" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 bg-vietnam-orange text-black px-4 py-2 rounded-md z-50">
        Skip to Main Content
    </a>

    <!-- Top Bar -->
    <div class="bg-vietnam-dark border-b border-gray-700 text-sm">
        <div class="container mx-auto px-4 py-3">
            <div class="flex flex-col md:flex-row md:justify-end items-center space-y-2 md:space-y-0 md:space-x-6 text-center md:text-right">
                <div class="flex items-center space-x-2">
                    <span class="text-vietnam-orange">📞</span>
                    <span>+44 (0) 20 8549 2259</span>
                </div>
                <div class="flex items-center space-x-2">
                    <span class="text-vietnam-orange">✉️</span>
                    <span>info@needafixer.com</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Header -->
    <header class="bg-vietnam-dark border-b border-gray-700 sticky top-0 z-40 backdrop-blur-sm bg-opacity-95">
        <div class="container mx-auto px-4">
            <div class="flex items-center justify-between py-4">
                <!-- Logo -->
                <div class="flex-shrink-0">
                    <a href="/" class="block">
                        <img src="/wp-content/uploads/2016/10/needafixer-vietnam.png" 
                             alt="Fixers in Vietnam" 
                             class="h-12 w-auto">
                    </a>
                </div>

                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center space-x-8" aria-label="Main navigation">
                    <a href="/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">HOME</a>
                    <a href="/about-us/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">ABOUT US</a>
                    <div class="relative group">
                        <a href="/film-production-services/" class="{'text-vietnam-orange font-medium' if services_active else 'text-vietnam-gray'} hover:text-vietnam-orange transition-colors duration-200 flex items-center">
                            SERVICES
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="absolute top-full left-0 mt-2 w-56 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/equipment-rental-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Equipment Rental</a>
                            <a href="/location-scouting-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Location Scouting</a>
                            <a href="/film-permits-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Film Permits</a>
                        </div>
                    </div>
                    <a href="/filming-in-vietnam/" class="{'text-vietnam-orange font-medium' if current_active == 'FILMING IN VIETNAM' else 'text-vietnam-gray'} hover:text-vietnam-orange transition-colors duration-200">FILMING IN VIETNAM</a>
                    <a href="/portfolio/" class="{'text-vietnam-orange font-medium' if current_active == 'PORTFOLIO' else 'text-vietnam-gray'} hover:text-vietnam-orange transition-colors duration-200">PORTFOLIO</a>
                    <a href="/clients/" class="{'text-vietnam-orange font-medium' if current_active == 'CLIENTS' else 'text-vietnam-gray'} hover:text-vietnam-orange transition-colors duration-200">CLIENTS</a>
                    <a href="/contact/" class="{'text-vietnam-orange font-medium' if current_active == 'CONTACT' else 'text-vietnam-gray'} hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
                </nav>

                <!-- Mobile Menu Button -->
                <button class="lg:hidden flex items-center px-3 py-2 border border-gray-600 rounded text-vietnam-gray hover:text-white hover:border-white" 
                        id="mobile-menu-button" 
                        aria-label="Toggle mobile menu"
                        aria-expanded="false">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>

            <!-- Mobile Navigation -->
            <nav class="lg:hidden hidden" id="mobile-menu" aria-label="Mobile navigation">
                <div class="px-2 pt-2 pb-3 space-y-1 border-t border-gray-700">
                    <a href="/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">HOME</a>
                    <a href="/about-us/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">ABOUT US</a>
                    <a href="/film-production-services/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">SERVICES</a>
                    <a href="/equipment-rental-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Equipment Rental</a>
                    <a href="/location-scouting-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Location Scouting</a>
                    <a href="/film-permits-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Permits</a>
                    <a href="/filming-in-vietnam/" class="block px-3 py-2 {'text-vietnam-orange font-medium' if current_active == 'FILMING IN VIETNAM' else 'text-vietnam-gray'} hover:text-vietnam-orange transition-colors duration-200">FILMING IN VIETNAM</a>
                    <a href="/portfolio/" class="block px-3 py-2 {'text-vietnam-orange font-medium' if current_active == 'PORTFOLIO' else 'text-vietnam-gray'} hover:text-vietnam-orange transition-colors duration-200">PORTFOLIO</a>
                    <a href="/clients/" class="block px-3 py-2 {'text-vietnam-orange font-medium' if current_active == 'CLIENTS' else 'text-vietnam-gray'} hover:text-vietnam-orange transition-colors duration-200">CLIENTS</a>
                    <a href="/contact/" class="block px-3 py-2 {'text-vietnam-orange font-medium' if current_active == 'CONTACT' else 'text-vietnam-gray'} hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
                </div>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main id="main-content">
        <!-- Hero Section -->
        <section class="page-hero-bg relative py-20 md:py-32">
            <div class="absolute inset-0 bg-black bg-opacity-60"></div>
            <div class="relative z-10 container mx-auto px-4 text-center">
                <h1 class="text-4xl md:text-6xl font-bold text-vietnam-orange mb-4">
                    {config['hero_title']}
                </h1>
                <p class="text-xl text-gray-200 max-w-2xl mx-auto">
                    {config['hero_subtitle']}
                </p>
            </div>
        </section>

        <!-- Page Content -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="max-w-4xl mx-auto">
                    <!-- Extracted Content -->
                    <div class="prose prose-lg max-w-none">'''
    
    # Add extracted content
    for i, content_piece in enumerate(extracted_data['content']):
        if len(content_piece.strip()) > 30:  # Only meaningful content
            if i == 0:
                html_content += f'''
                        <h2 class="text-3xl font-bold text-vietnam-orange mb-6">{content_piece}</h2>'''
            else:
                html_content += f'''
                        <p class="text-lg text-gray-300 mb-6 leading-relaxed">{content_piece}</p>'''
    
    # Add call to action
    html_content += '''
                        <div class="mt-12 text-center">
                            <a href="/contact/" class="inline-block bg-vietnam-orange text-black px-8 py-3 rounded-md font-semibold hover:bg-yellow-500 transition-colors duration-200">
                                Contact Us for More Information
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>'''
    
    return html_content

def main():
    """Extract content and rebuild pages"""
    pages_to_rebuild = [
        'filming-in-vietnam',
        'portfolio', 
        'clients',
        'contact'
    ]
    
    print("🔄 Extracting content and rebuilding pages with modern layouts...")
    print("=" * 70)
    
    for page_key in pages_to_rebuild:
        try:
            backup_file = Path(page_key) / 'index-original-backup.html'
            current_file = Path(page_key) / 'index.html'
            
            if backup_file.exists():
                print(f"📖 Extracting content from {backup_file}")
                extracted_data = extract_content_from_minified(backup_file)
                
                if extracted_data:
                    print(f"✅ Extracted: {extracted_data['title']}")
                    
                    # Create new page with extracted content
                    html_content = create_content_based_page(page_key, extracted_data)
                    
                    # Add footer and JavaScript (common to all pages)
                    footer_js = '''
    <!-- Footer Call-to-Action -->
    <section class="bg-gray-800 border-t border-gray-700 py-8">
        <div class="container mx-auto px-4">
            <div class="md:flex md:items-center md:justify-between">
                <div class="md:flex-grow text-center md:text-left">
                    <p class="text-xl text-gray-300 mb-4 md:mb-0">
                        Ready to shoot? We'd love to help and are just a click away! All enquiries will be answered within 24 hours!
                    </p>
                </div>
                <div class="text-center md:text-right">
                    <a href="/contact/" 
                       class="inline-block bg-vietnam-red text-white px-8 py-3 rounded-md font-semibold hover:bg-red-600 transition-colors duration-200">
                        Contact us
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-vietnam-dark border-t border-gray-700 py-12">
        <div class="container mx-auto px-4">
            <div class="grid md:grid-cols-3 gap-8">
                <!-- Company Info -->
                <div>
                    <img src="/wp-content/uploads/2016/10/needafixer-vietnam.png" 
                         alt="Fixers in Vietnam" 
                         class="h-12 w-auto mb-4">
                    <p class="text-gray-400 text-sm leading-relaxed">
                        Professional filming services in Vietnam for international productions. 
                        Expert fixers, location scouting, equipment rental, permits & crew.
                    </p>
                </div>
                
                <!-- Quick Links -->
                <div>
                    <h3 class="text-white font-semibold mb-4">Quick Links</h3>
                    <ul class="space-y-2">
                        <li><a href="/about-us/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">About Us</a></li>
                        <li><a href="/film-production-services/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Services</a></li>
                        <li><a href="/filming-in-vietnam/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Filming in Vietnam</a></li>
                        <li><a href="/portfolio/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Portfolio</a></li>
                        <li><a href="/contact/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Contact</a></li>
                    </ul>
                </div>
                
                <!-- Contact Info -->
                <div>
                    <h3 class="text-white font-semibold mb-4">Contact Info</h3>
                    <div class="space-y-2 text-gray-400 text-sm">
                        <div class="flex items-center space-x-2">
                            <span class="text-vietnam-orange">📞</span>
                            <span>+44 (0) 20 8549 2259</span>
                        </div>
                        <div class="flex items-center space-x-2">
                            <span class="text-vietnam-orange">✉️</span>
                            <span>info@needafixer.com</span>
                        </div>
                        <div class="flex items-center space-x-2">
                            <span class="text-vietnam-orange">🌐</span>
                            <span>needafixer.com</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="border-t border-gray-700 mt-8 pt-8 text-center">
                <p class="text-gray-400 text-sm">
                    © 2024 Fixers in Vietnam. All rights reserved. | Professional filming services throughout Vietnam.
                </p>
            </div>
        </div>
    </footer>

    <!-- JavaScript -->
    <script>
        // Mobile menu functionality
        document.getElementById('mobile-menu-button').addEventListener('click', function() {
            const mobileMenu = document.getElementById('mobile-menu');
            const isHidden = mobileMenu.classList.contains('hidden');
            
            if (isHidden) {
                mobileMenu.classList.remove('hidden');
                this.setAttribute('aria-expanded', 'true');
            } else {
                mobileMenu.classList.add('hidden');
                this.setAttribute('aria-expanded', 'false');
            }
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            const mobileMenu = document.getElementById('mobile-menu');
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            
            if (!mobileMenu.contains(event.target) && !mobileMenuButton.contains(event.target)) {
                mobileMenu.classList.add('hidden');
                mobileMenuButton.setAttribute('aria-expanded', 'false');
            }
        });
    </script>
</body>
</html>'''
                    
                    complete_html = html_content + footer_js
                    
                    # Write the new file
                    with open(current_file, 'w', encoding='utf-8') as f:
                        f.write(complete_html)
                    
                    print(f"✅ Rebuilt {page_key} with extracted content")
                else:
                    print(f"❌ Could not extract content from {page_key}")
            else:
                print(f"⚠️  Backup file not found for {page_key}")
                
        except Exception as e:
            print(f"❌ Error processing {page_key}: {e}")
    
    print("=" * 70)
    print("🎉 Content extraction and rebuilding complete!")

if __name__ == "__main__":
    main()
