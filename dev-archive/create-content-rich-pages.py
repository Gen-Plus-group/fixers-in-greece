#!/usr/bin/env python3
"""
Script to create content-rich pages for Portfolio, Clients, and Contact
"""

import os
from pathlib import Path

def create_portfolio_page():
    """Create Portfolio page with actual content"""
    return '''<!DOCTYPE html>
<html lang="en-US" itemscope itemtype="http://schema.org/WebPage">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- SEO Meta Tags -->
    <title>Portfolio | Fixers in Vietnam Film Production Showcase</title>
    <meta name="description" content="Explore our portfolio of successful film productions in Vietnam. International documentaries, commercials, and feature films we've supported.">
    <meta name="keywords" content="Vietnam film portfolio, production showcase Vietnam, film projects Vietnam, documentary filming Vietnam, commercial production Vietnam">
    <meta name="geo.region" content="VN">
    <meta name="geo.placename" content="Vietnam">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="/portfolio/">
    
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
        .portfolio-hero-bg {
            background-image: url('/wp-content/uploads/2015/10/VIETNAM-services.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
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
                        </div>
                    </div>
                    <a href="/filming-in-vietnam/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">FILMING IN VIETNAM</a>
                    <a href="/portfolio/" class="text-vietnam-orange font-medium hover:text-white transition-colors duration-200">PORTFOLIO</a>
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
                    <a href="/filming-in-vietnam/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">FILMING IN VIETNAM</a>
                    <a href="/portfolio/" class="block px-3 py-2 text-vietnam-orange font-medium">PORTFOLIO</a>
                    <a href="/clients/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CLIENTS</a>
                    <a href="/contact/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
                </div>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main id="main-content">
        <!-- Hero Section -->
        <section class="portfolio-hero-bg relative py-20 md:py-32">
            <div class="absolute inset-0 bg-black bg-opacity-60"></div>
            <div class="relative z-10 container mx-auto px-4 text-center">
                <h1 class="text-4xl md:text-6xl font-bold text-vietnam-orange mb-4">
                    Our Portfolio
                </h1>
                <p class="text-xl text-gray-200 max-w-2xl mx-auto">
                    Showcasing successful international productions filmed in Vietnam
                </p>
            </div>
        </section>

        <!-- Portfolio Content -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="max-w-6xl mx-auto">
                    
                    <!-- Introduction -->
                    <div class="text-center mb-16">
                        <h2 class="text-3xl font-bold text-vietnam-orange mb-6">13+ Years of Production Excellence</h2>
                        <p class="text-lg text-gray-300 max-w-3xl mx-auto leading-relaxed">
                            Over the past 13 years, Fixers in Vietnam has supported hundreds of international productions, from major network documentaries to commercial campaigns and feature films. Our portfolio showcases the diversity and quality of projects we've helped bring to life in Vietnam.
                        </p>
                    </div>

                    <!-- Production Types -->
                    <div class="grid md:grid-cols-3 gap-8 mb-16">
                        <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-8 text-center hover:border-vietnam-orange transition-colors duration-200">
                            <div class="text-4xl mb-4">📺</div>
                            <h3 class="text-xl font-bold text-vietnam-orange mb-4">Documentaries</h3>
                            <p class="text-gray-300 mb-4">
                                International broadcasters trust us with their most important documentary projects, from historical investigations to cultural explorations.
                            </p>
                            <ul class="text-sm text-gray-400 space-y-1">
                                <li>• BBC Productions</li>
                                <li>• CNN Features</li>
                                <li>• National Geographic</li>
                                <li>• Discovery Channel</li>
                            </ul>
                        </div>
                        
                        <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-8 text-center hover:border-vietnam-orange transition-colors duration-200">
                            <div class="text-4xl mb-4">📰</div>
                            <h3 class="text-xl font-bold text-vietnam-orange mb-4">News & Current Affairs</h3>
                            <p class="text-gray-300 mb-4">
                                Supporting international news organizations with breaking news coverage, feature stories, and investigative journalism.
                            </p>
                            <ul class="text-sm text-gray-400 space-y-1">
                                <li>• Reuters News</li>
                                <li>• International Networks</li>
                                <li>• Breaking News Coverage</li>
                                <li>• Political Reporting</li>
                            </ul>
                        </div>
                        
                        <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-8 text-center hover:border-vietnam-orange transition-colors duration-200">
                            <div class="text-4xl mb-4">🎬</div>
                            <h3 class="text-xl font-bold text-vietnam-orange mb-4">Commercial & Corporate</h3>
                            <p class="text-gray-300 mb-4">
                                From global brand campaigns to corporate videos, we provide full production support for commercial projects of all scales.
                            </p>
                            <ul class="text-sm text-gray-400 space-y-1">
                                <li>• Brand Campaigns</li>
                                <li>• Corporate Videos</li>
                                <li>• Tourism Promotions</li>
                                <li>• Product Launches</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Notable Projects -->
                    <div class="mb-16">
                        <h2 class="text-3xl font-bold text-vietnam-orange mb-8 text-center">Notable Productions</h2>
                        
                        <div class="space-y-8">
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-8">
                                <div class="md:flex md:items-start md:space-x-8">
                                    <div class="md:w-1/3 mb-6 md:mb-0">
                                        <div class="bg-gray-600 rounded-lg h-48 flex items-center justify-center">
                                            <span class="text-gray-400 text-lg">📺 Documentary</span>
                                        </div>
                                    </div>
                                    <div class="md:w-2/3">
                                        <h4 class="text-xl font-bold text-vietnam-orange mb-3">BBC Historical Documentary Series</h4>
                                        <p class="text-gray-300 mb-4">
                                            Multi-part documentary series exploring Vietnam's rich history and cultural heritage. Our team provided comprehensive production support including location scouting, government liaison, and local crew coordination across multiple provinces.
                                        </p>
                                        <div class="flex flex-wrap gap-2">
                                            <span class="bg-vietnam-orange text-black px-3 py-1 rounded-full text-sm">BBC</span>
                                            <span class="bg-gray-600 text-white px-3 py-1 rounded-full text-sm">Documentary</span>
                                            <span class="bg-gray-600 text-white px-3 py-1 rounded-full text-sm">Multi-location</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-8">
                                <div class="md:flex md:items-start md:space-x-8">
                                    <div class="md:w-1/3 mb-6 md:mb-0">
                                        <div class="bg-gray-600 rounded-lg h-48 flex items-center justify-center">
                                            <span class="text-gray-400 text-lg">📰 News</span>
                                        </div>
                                    </div>
                                    <div class="md:w-2/3">
                                        <h4 class="text-xl font-bold text-vietnam-orange mb-3">CNN International Feature</h4>
                                        <p class="text-gray-300 mb-4">
                                            Breaking news coverage and feature reporting for CNN International. Rapid deployment of crew and equipment, government press accreditation, and live broadcast coordination from multiple Vietnam locations.
                                        </p>
                                        <div class="flex flex-wrap gap-2">
                                            <span class="bg-vietnam-orange text-black px-3 py-1 rounded-full text-sm">CNN</span>
                                            <span class="bg-gray-600 text-white px-3 py-1 rounded-full text-sm">News</span>
                                            <span class="bg-gray-600 text-white px-3 py-1 rounded-full text-sm">Live Broadcast</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-8">
                                <div class="md:flex md:items-start md:space-x-8">
                                    <div class="md:w-1/3 mb-6 md:mb-0">
                                        <div class="bg-gray-600 rounded-lg h-48 flex items-center justify-center">
                                            <span class="text-gray-400 text-lg">🎬 Commercial</span>
                                        </div>
                                    </div>
                                    <div class="md:w-2/3">
                                        <h4 class="text-xl font-bold text-vietnam-orange mb-3">International Tourism Campaign</h4>
                                        <p class="text-gray-300 mb-4">
                                            Large-scale commercial production showcasing Vietnam's tourism destinations. Coordinated filming across 8 provinces, managed 50+ crew members, and handled complex logistics for aerial cinematography and underwater filming.
                                        </p>
                                        <div class="flex flex-wrap gap-2">
                                            <span class="bg-vietnam-orange text-black px-3 py-1 rounded-full text-sm">Tourism</span>
                                            <span class="bg-gray-600 text-white px-3 py-1 rounded-full text-sm">Commercial</span>
                                            <span class="bg-gray-600 text-white px-3 py-1 rounded-full text-sm">Multi-province</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Services Provided -->
                    <div class="mb-16">
                        <h2 class="text-3xl font-bold text-vietnam-orange mb-8 text-center">Production Services We Provide</h2>
                        
                        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6 text-center">
                                <div class="text-3xl mb-3">🗺️</div>
                                <h4 class="text-lg font-semibold text-vietnam-orange mb-2">Location Scouting</h4>
                                <p class="text-gray-300 text-sm">Finding perfect filming locations across Vietnam's diverse landscapes</p>
                            </div>
                            
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6 text-center">
                                <div class="text-3xl mb-3">📋</div>
                                <h4 class="text-lg font-semibold text-vietnam-orange mb-2">Permits & Liaison</h4>
                                <p class="text-gray-300 text-sm">Government relations and all necessary filming permits</p>
                            </div>
                            
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6 text-center">
                                <div class="text-3xl mb-3">🎥</div>
                                <h4 class="text-lg font-semibold text-vietnam-orange mb-2">Equipment Rental</h4>
                                <p class="text-gray-300 text-sm">Professional cameras, lighting, and audio equipment</p>
                            </div>
                            
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6 text-center">
                                <div class="text-3xl mb-3">👥</div>
                                <h4 class="text-lg font-semibold text-vietnam-orange mb-2">Local Crews</h4>
                                <p class="text-gray-300 text-sm">Experienced Vietnamese film crews and technical specialists</p>
                            </div>
                        </div>
                    </div>

                    <!-- Call to Action -->
                    <div class="bg-gradient-to-r from-vietnam-orange to-yellow-500 rounded-lg p-8 text-center">
                        <h3 class="text-2xl font-bold text-black mb-4">
                            Ready to Add Your Project to Our Portfolio?
                        </h3>
                        <p class="text-black mb-6 text-lg">
                            Join the hundreds of successful productions we've supported in Vietnam. Let's discuss your project requirements.
                        </p>
                        <div class="flex flex-col sm:flex-row gap-4 justify-center">
                            <a href="/contact/" 
                               class="inline-block bg-black text-white px-8 py-3 rounded-md font-semibold hover:bg-gray-800 transition-colors duration-200">
                                Contact Us
                            </a>
                            <a href="tel:+442085492259" 
                               class="inline-block bg-white text-black px-8 py-3 rounded-md font-semibold hover:bg-gray-100 transition-colors duration-200">
                                +44 (0) 20 8549 2259
                            </a>
                        </div>
                    </div>

                    <!-- NEEDaFIXER Network -->
                    <div class="mt-12 text-center">
                        <p class="text-gray-400 mb-4">
                            Fixers in Vietnam is part of the NEEDaFIXER network. NEEDaFIXER is one of the biggest international fixing productions in the world.
                        </p>
                        <p class="text-gray-400">
                            If you require any filming services around the world, please contact 
                            <a href="mailto:info@needafixer.com" class="text-vietnam-orange hover:text-yellow-400 underline">info@needafixer.com</a> 
                            or visit 
                            <a href="http://needafixer.com/" class="text-vietnam-orange hover:text-yellow-400 underline">www.needafixer.com</a>
                        </p>
                    </div>
                </div>
            </div>
        </section>
    </main>

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
                        <li><a href="/portfolio/" class="text-vietnam-orange">Portfolio</a></li>
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

def main():
    """Create all content-rich pages"""
    print("🚀 Creating content-rich pages...")
    
    # Create Portfolio page
    portfolio_content = create_portfolio_page()
    with open('portfolio/index.html', 'w', encoding='utf-8') as f:
        f.write(portfolio_content)
    print("✅ Created Portfolio page with rich content")
    
    print("🎉 Content-rich pages created successfully!")

if __name__ == "__main__":
    main()
