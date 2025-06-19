#!/usr/bin/env python3
"""
Script to fix navigation consistency and create missing pages
"""

import os
import shutil

def create_missing_page(page_name, title, description, keywords):
    """Create a missing page with proper navigation"""
    
    # Create directory
    os.makedirs(page_name, exist_ok=True)
    
    # Determine if this page should be highlighted in navigation
    current_page_highlights = {
        'commercial-video-production-vietnam': ('DOCUMENTARIES', 'Commercial Production'),
        'news-filming-vietnam': ('DOCUMENTARIES', 'News & Current Affairs'),
        'ho-chi-minh-city-filming': ('LOCATIONS', 'Ho Chi Minh City'),
        'hanoi-film-production': ('LOCATIONS', 'Hanoi')
    }
    
    highlight_section, highlight_item = current_page_highlights.get(page_name, ('', ''))
    
    html_content = f'''<!DOCTYPE html>
<html lang="en-US" itemscope itemtype="http://schema.org/WebPage">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- SEO Meta Tags -->
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="geo.region" content="VN">
    <meta name="geo.placename" content="Vietnam">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="/{page_name}/">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="/{page_name}/">
    
    <!-- Favicon -->
    <link rel="icon" sizes="32x32" href="/wp-content/uploads/2024/09/favicon-32x32-1.png">
    <link rel="shortcut icon" href="/wp-content/uploads/2024/09/favicon-32x32-1.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/wp-content/uploads/2024/09/apple-touch-icon.png">
    
    <!-- Tailwind CSS -->
    <link href="/dist/output.css" rel="stylesheet">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-FD4LC3V4DB"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', 'G-FD4LC3V4DB');
    </script>
    
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
                    <span>enquiries@needafixer.com</span>
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
                        <a href="/documentary-filming-vietnam/" class="{'text-vietnam-orange hover:text-white' if highlight_section == 'DOCUMENTARIES' else 'text-vietnam-gray hover:text-vietnam-orange'} transition-colors duration-200 flex items-center">
                            DOCUMENTARIES
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="absolute top-full left-0 mt-2 w-64 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/documentary-filming-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Documentary Services</a>
                            <a href="/commercial-video-production-vietnam/" class="block px-4 py-3 text-sm {'text-vietnam-orange hover:text-white' if highlight_item == 'Commercial Production' else 'text-vietnam-gray hover:text-vietnam-orange'} hover:bg-gray-800 transition-colors duration-200">Commercial Production</a>
                            <a href="/news-filming-vietnam/" class="block px-4 py-3 text-sm {'text-vietnam-orange hover:text-white' if highlight_item == 'News & Current Affairs' else 'text-vietnam-gray hover:text-vietnam-orange'} hover:bg-gray-800 transition-colors duration-200">News & Current Affairs</a>
                        </div>
                    </div>
                    <div class="relative group">
                        <a href="/vietnam-filming-locations/" class="{'text-vietnam-orange hover:text-white' if highlight_section == 'LOCATIONS' else 'text-vietnam-gray hover:text-vietnam-orange'} transition-colors duration-200 flex items-center">
                            LOCATIONS
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="absolute top-full left-0 mt-2 w-64 bg-vietnam-dark border border-gray-700 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                            <a href="/vietnam-filming-locations/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">All Locations</a>
                            <a href="/ho-chi-minh-city-filming/" class="block px-4 py-3 text-sm {'text-vietnam-orange hover:text-white' if highlight_item == 'Ho Chi Minh City' else 'text-vietnam-gray hover:text-vietnam-orange'} hover:bg-gray-800 transition-colors duration-200">Ho Chi Minh City</a>
                            <a href="/hanoi-film-production/" class="block px-4 py-3 text-sm {'text-vietnam-orange hover:text-white' if highlight_item == 'Hanoi' else 'text-vietnam-gray hover:text-vietnam-orange'} hover:bg-gray-800 transition-colors duration-200">Hanoi</a>
                        </div>
                    </div>
                    <a href="/filming-in-vietnam/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">FILMING GUIDE</a>
                    <a href="/portfolio/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">PORTFOLIO</a>
                    <a href="/clients/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CLIENTS</a>
                    <a href="/contact/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
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
                    <a href="/vietnam-film-crew/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Film Crew</a>
                    <a href="/drone-filming-vietnam/" class="block px-6 py-2 text-sm text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">Drone Filming</a>
                    <a href="/documentary-filming-vietnam/" class="block px-3 py-2 {'text-vietnam-orange font-medium' if highlight_section == 'DOCUMENTARIES' else 'text-vietnam-gray hover:text-vietnam-orange'} transition-colors duration-200">DOCUMENTARIES</a>
                    <a href="/commercial-video-production-vietnam/" class="block px-6 py-2 text-sm {'text-vietnam-orange font-medium' if highlight_item == 'Commercial Production' else 'text-vietnam-gray hover:text-vietnam-orange'} transition-colors duration-200">Commercial Production</a>
                    <a href="/news-filming-vietnam/" class="block px-6 py-2 text-sm {'text-vietnam-orange font-medium' if highlight_item == 'News & Current Affairs' else 'text-vietnam-gray hover:text-vietnam-orange'} transition-colors duration-200">News & Current Affairs</a>
                    <a href="/vietnam-filming-locations/" class="block px-3 py-2 {'text-vietnam-orange font-medium' if highlight_section == 'LOCATIONS' else 'text-vietnam-gray hover:text-vietnam-orange'} transition-colors duration-200">LOCATIONS</a>
                    <a href="/ho-chi-minh-city-filming/" class="block px-6 py-2 text-sm {'text-vietnam-orange font-medium' if highlight_item == 'Ho Chi Minh City' else 'text-vietnam-gray hover:text-vietnam-orange'} transition-colors duration-200">Ho Chi Minh City</a>
                    <a href="/hanoi-film-production/" class="block px-6 py-2 text-sm {'text-vietnam-orange font-medium' if highlight_item == 'Hanoi' else 'text-vietnam-gray hover:text-vietnam-orange'} transition-colors duration-200">Hanoi</a>
                    <a href="/filming-in-vietnam/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">FILMING GUIDE</a>
                    <a href="/portfolio/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">PORTFOLIO</a>
                    <a href="/clients/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CLIENTS</a>
                    <a href="/contact/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
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
                <h1 class="text-4xl md:text-6xl font-bold text-vietnam-orange mb-6">
                    {title.split('|')[0].strip()}
                </h1>
                <p class="text-xl md:text-2xl text-gray-200 max-w-3xl mx-auto mb-8">
                    {description}
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">
                    <a href="#content" 
                       class="inline-block bg-vietnam-orange text-black px-8 py-3 rounded-md font-semibold hover:bg-yellow-500 transition-colors duration-200">
                        Learn More
                    </a>
                    <a href="/contact/" 
                       class="inline-block bg-transparent border-2 border-vietnam-orange text-vietnam-orange px-8 py-3 rounded-md font-semibold hover:bg-vietnam-orange hover:text-black transition-colors duration-200">
                        Get Quote
                    </a>
                </div>
            </div>
        </section>

        <!-- Coming Soon Content -->
        <section id="content" class="py-16">
            <div class="container mx-auto px-4">
                <div class="max-w-4xl mx-auto text-center">
                    <h2 class="text-3xl font-bold text-vietnam-orange mb-6">Coming Soon</h2>
                    <p class="text-lg text-gray-300 mb-8">
                        We're developing comprehensive content for this service. This page will include detailed information about our capabilities, pricing, and how we can help with your Vietnam production needs.
                    </p>
                    <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-8 mb-8">
                        <h3 class="text-xl font-bold text-vietnam-orange mb-4">What We're Preparing</h3>
                        <p class="text-gray-300">
                            Detailed service information, case studies, pricing guides, and comprehensive resources for your Vietnam filming project.
                        </p>
                    </div>
                    <a href="/contact/" class="inline-block bg-vietnam-orange text-black px-8 py-3 rounded-md font-semibold hover:bg-yellow-500 transition-colors duration-200">
                        Contact Us for More Information
                    </a>
                </div>
            </div>
        </section>
    </main>

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
                        <li><a href="/vietnam-filming-locations/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Filming Locations</a></li>
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
                            <span>enquiries@needafixer.com</span>
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
        document.getElementById('mobile-menu-button').addEventListener('click', function() {{
            const mobileMenu = document.getElementById('mobile-menu');
            const isHidden = mobileMenu.classList.contains('hidden');
            
            if (isHidden) {{
                mobileMenu.classList.remove('hidden');
                this.setAttribute('aria-expanded', 'true');
            }} else {{
                mobileMenu.classList.add('hidden');
                this.setAttribute('aria-expanded', 'false');
            }}
        }});

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {{
            const mobileMenu = document.getElementById('mobile-menu');
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            
            if (!mobileMenu.contains(event.target) && !mobileMenuButton.contains(event.target)) {{
                mobileMenu.classList.add('hidden');
                mobileMenuButton.setAttribute('aria-expanded', 'false');
            }}
        }});
    </script>
</body>
</html>'''
    
    with open(f'{page_name}/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Created {page_name}/index.html")

def main():
    """Create all missing pages"""
    print("🚀 Creating missing pages...")
    
    # Define missing pages
    missing_pages = [
        {
            'name': 'commercial-video-production-vietnam',
            'title': 'Commercial Video Production Vietnam | Professional Advertising Filming',
            'description': 'Professional commercial video production services in Vietnam. Expert filming for TV commercials, digital advertising, and brand videos with international production standards.',
            'keywords': 'commercial video production Vietnam, advertising filming Vietnam, brand video Vietnam, TV commercial Vietnam, product launch video Vietnam'
        },
        {
            'name': 'news-filming-vietnam',
            'title': 'News and Current Affairs Filming Vietnam | Breaking News Support',
            'description': 'Fast-turnaround news filming services in Vietnam. 24/7 support for breaking news, current affairs, and live broadcasting with experienced local crews.',
            'keywords': 'news filming Vietnam, current affairs production Vietnam, breaking news Vietnam, CNN Vietnam filming, Reuters Vietnam bureau, live broadcasting Vietnam'
        },
        {
            'name': 'ho-chi-minh-city-filming',
            'title': 'Ho Chi Minh City Filming Services | Saigon Video Production',
            'description': 'Professional filming services in Ho Chi Minh City (Saigon). Urban locations, modern skylines, and vibrant street life for your Vietnam production.',
            'keywords': 'Ho Chi Minh City filming, Saigon film production, HCMC video production, District 1 filming, Saigon street filming, urban Vietnam filming'
        },
        {
            'name': 'hanoi-film-production',
            'title': 'Hanoi Film Production Services | Capital City Filming Vietnam',
            'description': 'Professional film production services in Hanoi, Vietnam\'s capital. Historical locations, government filming, and cultural sites with expert local knowledge.',
            'keywords': 'Hanoi filming, Hanoi video production, capital city filming Vietnam, Old Quarter filming, government filming Hanoi, Hanoi documentary production'
        }
    ]
    
    for page in missing_pages:
        create_missing_page(page['name'], page['title'], page['description'], page['keywords'])
    
    print(f"\\n📊 Created {len(missing_pages)} missing pages")
    print("\\n🎉 All missing pages created successfully!")

if __name__ == "__main__":
    main()
