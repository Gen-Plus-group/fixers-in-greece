#!/usr/bin/env python3
"""
Script to complete pre-production service pages with full content
"""

import os
import re

def get_mobile_navigation():
    """Return mobile navigation HTML"""
    return '''
                <!-- Mobile Menu Button -->
                <button id="mobile-menu-button"
                        class="lg:hidden flex items-center px-3 py-2 border border-gray-600 rounded text-gray-400 hover:text-white hover:border-white"
                        aria-expanded="false"
                        aria-controls="mobile-menu"
                        aria-label="Toggle navigation menu">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
        </div>

        <!-- Mobile Navigation Menu -->
        <div id="mobile-menu" class="lg:hidden hidden bg-vietnam-dark border-t border-gray-700">
            <div class="px-4 py-4 space-y-2">
                <a href="/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">HOME</a>
                <a href="/about-us/" class="block px-3 py-2 text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">ABOUT US</a>

                <!-- Pre-Production Mobile Menu -->
                <div>
                    <button class="mobile-dropdown-toggle w-full flex items-center justify-between px-3 py-2 text-vietnam-orange hover:text-white transition-colors duration-200"
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
        </div>
    </header>'''

def get_main_content_template(service_data):
    """Return main content template"""
    return f'''
    <!-- Main Content -->
    <main id="main-content">
        <!-- Hero Section -->
        <section class="page-hero-bg relative py-24 md:py-32">
            <div class="absolute inset-0 bg-black bg-opacity-60"></div>
            <div class="container mx-auto px-4 relative z-10">
                <div class="text-center">
                    <h1 class="text-4xl md:text-6xl font-bold text-white mb-6">
                        {service_data['h1']}
                    </h1>
                    <p class="text-xl md:text-2xl text-gray-200 max-w-4xl mx-auto">
                        {service_data['tagline']}
                    </p>
                </div>
            </div>
        </section>

        <!-- Introduction Section -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-vietnam-orange mb-6">
                        Expert {service_data['category']} Services
                    </h2>
                    <p class="text-xl text-gray-300 max-w-4xl mx-auto mb-8">
                        Professional {service_data['h1'].lower()} services for films, commercials, TV series, and digital content. Our expert team delivers exceptional results for productions worldwide.
                    </p>
                </div>

                <div class="grid md:grid-cols-2 gap-12 mb-16">
                    <div>
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-4">Professional Excellence</h3>
                        <p class="text-gray-300 leading-relaxed mb-6">
                            Our {service_data['category'].lower()} specialists bring years of industry experience and proven expertise to every project. We understand the unique requirements of different production types and deliver tailored solutions that meet your specific needs.
                        </p>
                        <p class="text-gray-300 leading-relaxed">
                            From independent films to major studio productions, our team has the skills and resources to handle projects of any scale and complexity, ensuring professional results that exceed expectations.
                        </p>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-4">Global Reach & Support</h3>
                        <p class="text-gray-300 leading-relaxed mb-6">
                            With our worldwide network of professionals, we provide comprehensive {service_data['category'].lower()} services across multiple countries and regions. Our global presence ensures consistent quality and reliable support wherever your production takes you.
                        </p>
                        <p class="text-gray-300 leading-relaxed">
                            Our experienced team coordinates seamlessly across time zones and cultures, providing the local expertise and international standards that modern productions demand.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Services Section -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="max-w-6xl mx-auto">
                    <!-- Why Choose NEEDaFIXER -->
                    <div class="mb-16">
                        <h2 class="text-3xl font-bold text-vietnam-orange mb-8 text-center">Why Choose NEEDaFIXER</h2>
                        <div class="grid md:grid-cols-2 gap-8">
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6 hover:border-vietnam-orange transition-colors duration-200">
                                <div class="text-3xl mb-4">✅</div>
                                <h3 class="text-xl font-semibold text-vietnam-orange mb-3">Proven Expertise</h3>
                                <p class="text-gray-300">Industry-leading professionals with extensive experience across all production types and budgets.</p>
                            </div>
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6 hover:border-vietnam-orange transition-colors duration-200">
                                <div class="text-3xl mb-4">🌍</div>
                                <h3 class="text-xl font-semibold text-vietnam-orange mb-3">Global Network</h3>
                                <p class="text-gray-300">Worldwide coverage with local expertise and international quality standards.</p>
                            </div>
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6 hover:border-vietnam-orange transition-colors duration-200">
                                <div class="text-3xl mb-4">⚡</div>
                                <h3 class="text-xl font-semibold text-vietnam-orange mb-3">Fast Response</h3>
                                <p class="text-gray-300">Quick turnaround times with 24-48 hour response for urgent projects.</p>
                            </div>
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6 hover:border-vietnam-orange transition-colors duration-200">
                                <div class="text-3xl mb-4">💼</div>
                                <h3 class="text-xl font-semibold text-vietnam-orange mb-3">Full Service</h3>
                                <p class="text-gray-300">Comprehensive solutions from concept to completion with ongoing support.</p>
                            </div>
                        </div>
                    </div>

                    <!-- How It Works -->
                    <div class="mb-16">
                        <h2 class="text-3xl font-bold text-vietnam-orange mb-8 text-center">How It Works</h2>
                        <div class="grid md:grid-cols-4 gap-6">
                            <div class="text-center">
                                <div class="bg-vietnam-orange text-black rounded-full w-12 h-12 flex items-center justify-center text-xl font-bold mx-auto mb-4">1</div>
                                <h3 class="text-lg font-semibold text-vietnam-orange mb-2">Consultation</h3>
                                <p class="text-gray-300">Discuss your project requirements and objectives.</p>
                            </div>
                            <div class="text-center">
                                <div class="bg-vietnam-orange text-black rounded-full w-12 h-12 flex items-center justify-center text-xl font-bold mx-auto mb-4">2</div>
                                <h3 class="text-lg font-semibold text-vietnam-orange mb-2">Planning</h3>
                                <p class="text-gray-300">Develop customized solutions for your needs.</p>
                            </div>
                            <div class="text-center">
                                <div class="bg-vietnam-orange text-black rounded-full w-12 h-12 flex items-center justify-center text-xl font-bold mx-auto mb-4">3</div>
                                <h3 class="text-lg font-semibold text-vietnam-orange mb-2">Execution</h3>
                                <p class="text-gray-300">Professional delivery with quality assurance.</p>
                            </div>
                            <div class="text-center">
                                <div class="bg-vietnam-orange text-black rounded-full w-12 h-12 flex items-center justify-center text-xl font-bold mx-auto mb-4">4</div>
                                <h3 class="text-lg font-semibold text-vietnam-orange mb-2">Support</h3>
                                <p class="text-gray-300">Ongoing assistance and project coordination.</p>
                            </div>
                        </div>
                    </div>

                    <!-- Testimonials -->
                    <div class="mb-16">
                        <h2 class="text-3xl font-bold text-vietnam-orange mb-8 text-center">Client Testimonials</h2>
                        <div class="grid md:grid-cols-3 gap-6">
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6">
                                <div class="text-vietnam-orange text-4xl mb-4">"</div>
                                <p class="text-gray-300 mb-4 italic">Exceptional service and professional results.</p>
                                <p class="text-vietnam-orange font-semibold">— Sarah M.</p>
                            </div>
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6">
                                <div class="text-vietnam-orange text-4xl mb-4">"</div>
                                <p class="text-gray-300 mb-4 italic">Delivered exactly what we needed on time.</p>
                                <p class="text-vietnam-orange font-semibold">— David L.</p>
                            </div>
                            <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6">
                                <div class="text-vietnam-orange text-4xl mb-4">"</div>
                                <p class="text-gray-300 mb-4 italic">Outstanding expertise and global reach.</p>
                                <p class="text-vietnam-orange font-semibold">— Maria R.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

def get_enhanced_footer():
    """Return enhanced footer HTML"""
    return '''
        <!-- FAQ Section -->
        <section class="py-16 bg-vietnam-dark">
            <div class="container mx-auto px-4">
                <div class="max-w-4xl mx-auto">
                    <h2 class="text-3xl font-bold text-vietnam-orange mb-8 text-center">Frequently Asked Questions</h2>
                    <div class="space-y-6">
                        <div class="bg-vietnam-darker border border-gray-700 rounded-lg p-6">
                            <h3 class="text-xl font-semibold text-vietnam-orange mb-3">How quickly can you start?</h3>
                            <p class="text-gray-300">We can typically begin within 24-48 hours of project confirmation, depending on scope and requirements.</p>
                        </div>
                        <div class="bg-vietnam-darker border border-gray-700 rounded-lg p-6">
                            <h3 class="text-xl font-semibold text-vietnam-orange mb-3">What's included in your services?</h3>
                            <p class="text-gray-300">Comprehensive solutions including consultation, planning, execution, and ongoing support throughout your project.</p>
                        </div>
                        <div class="bg-vietnam-darker border border-gray-700 rounded-lg p-6">
                            <h3 class="text-xl font-semibold text-vietnam-orange mb-3">Do you work internationally?</h3>
                            <p class="text-gray-300">Yes, we provide services worldwide with local expertise and international quality standards.</p>
                        </div>
                        <div class="bg-vietnam-darker border border-gray-700 rounded-lg p-6">
                            <h3 class="text-xl font-semibold text-vietnam-orange mb-3">How do you ensure quality?</h3>
                            <p class="text-gray-300">Our experienced professionals follow industry best practices with rigorous quality control and client feedback integration.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Call to Action -->
        <section class="py-16 bg-gradient-to-r from-vietnam-orange to-yellow-500">
            <div class="container mx-auto px-4 text-center">
                <h2 class="text-3xl md:text-4xl font-bold text-black mb-6">
                    Ready to Get Started?
                </h2>
                <p class="text-xl text-black mb-8 max-w-3xl mx-auto">
                    Contact us today to discuss your project requirements and discover how our expert services can bring your vision to life.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">
                    <a href="/contact/" class="inline-block bg-black text-vietnam-orange px-8 py-3 rounded-md font-semibold hover:bg-gray-800 transition-colors duration-200">
                        Get Started Today
                    </a>
                    <a href="tel:+442085492259" class="inline-block border-2 border-black text-black px-8 py-3 rounded-md font-semibold hover:bg-black hover:text-vietnam-orange transition-colors duration-200">
                        Call +44 20 8549 2259
                    </a>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
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
                        <li><a href="/pre-production-services/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Pre-Production</a></li>
                        <li><a href="/equipment-rental-vietnam/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Equipment Rental</a></li>
                        <li><a href="/location-scouting-vietnam/" class="text-gray-400 hover:text-vietnam-orange transition-colors duration-200">Location Scouting</a></li>
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
    </footer>

    <!-- Mobile Menu JavaScript -->
    <script>
        // Mobile menu main toggle
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
        });
    </script>
</body>
</html>'''

# Service data for completion
SERVICES_DATA = {
    'scriptwriting': {'h1': 'Professional Scriptwriting Services', 'tagline': 'Expert screenwriters for films, TV, commercials, and digital content worldwide.', 'category': 'Creative & Development'},
    'script-consultation': {'h1': 'Script Consultation & Polishing Services', 'tagline': 'Expert script doctors to refine, polish, and perfect your screenplay.', 'category': 'Creative & Development'},
    'storyboarding': {'h1': 'Professional Storyboarding Services', 'tagline': 'Expert visual storytelling through detailed storyboards for all production types.', 'category': 'Creative & Development'},
    'concept-development': {'h1': 'Concept Development Services', 'tagline': 'Creative ideation and concept development for compelling visual narratives.', 'category': 'Creative & Development'},
    'creative-direction': {'h1': 'Creative Direction Services', 'tagline': 'Artistic vision and creative leadership for exceptional visual storytelling.', 'category': 'Creative & Development'},
    'moodboard-creation': {'h1': 'Moodboard & Lookbook Creation', 'tagline': 'Visual style guides and aesthetic direction for your production.', 'category': 'Creative & Development'},
    'pitch-deck-design': {'h1': 'Pitch Deck & Treatment Design', 'tagline': 'Compelling presentations and treatments to secure funding and partnerships.', 'category': 'Creative & Development'},
    'casting-services': {'h1': 'Casting Services', 'tagline': 'Professional casting for actors, models, and extras across all production types.', 'category': 'Casting & Talent'},
    'voiceover-casting': {'h1': 'Voiceover Casting Services', 'tagline': 'Expert voice talent casting for commercials, films, and digital content.', 'category': 'Casting & Talent'},
    'talent-coordination': {'h1': 'Talent Coordination Services', 'tagline': 'Expert coordination and management of talent throughout production.', 'category': 'Casting & Talent'},
    'union-talent-management': {'h1': 'Union & Non-Union Talent Management', 'tagline': 'Expert management of union and non-union talent agreements and coordination.', 'category': 'Casting & Talent'},
    'location-scouting-services': {'h1': 'Location Scouting Services', 'tagline': 'Find perfect filming locations worldwide for your production needs.', 'category': 'Location & Permits'},
    'location-management': {'h1': 'Location Management Services', 'tagline': 'Expert on-site coordination and management of filming locations.', 'category': 'Location & Permits'},
    'film-permit-acquisition': {'h1': 'Film Permit Acquisition', 'tagline': 'Expert acquisition of filming permits and licenses worldwide.', 'category': 'Location & Permits'},
    'site-surveys': {'h1': 'Site Surveys & Tech Scouting', 'tagline': 'Comprehensive technical assessment and surveying of filming locations.', 'category': 'Location & Permits'},
    'production-insurance': {'h1': 'Production Insurance Services', 'tagline': 'Comprehensive insurance coverage and risk management for productions.', 'category': 'Location & Permits'},
    'production-budgeting': {'h1': 'Production Budgeting Services', 'tagline': 'Expert financial planning and budget management for productions.', 'category': 'Budgeting & Scheduling'},
    'cost-estimation': {'h1': 'Cost Estimation Services', 'tagline': 'Accurate cost analysis and budget estimation for all production types.', 'category': 'Budgeting & Scheduling'},
    'production-scheduling': {'h1': 'Production Scheduling Services', 'tagline': 'Expert timeline management and production coordination services.', 'category': 'Budgeting & Scheduling'},
    'call-sheets': {'h1': 'Call Sheets & Shooting Schedules', 'tagline': 'Professional call sheets and detailed shooting schedule coordination.', 'category': 'Budgeting & Scheduling'},
    'line-producing-services': {'h1': 'Line Producing Services', 'tagline': 'Expert production management and line producing for all project types.', 'category': 'Crew & Logistics'},
    'crew-hiring': {'h1': 'Crew Hiring & Coordination', 'tagline': 'Professional film crew recruitment and coordination worldwide.', 'category': 'Crew & Logistics'},
    'fixer-services-local': {'h1': 'Local Fixer Services', 'tagline': 'Expert local production support and coordination services worldwide.', 'category': 'Crew & Logistics'},
    'travel-logistics': {'h1': 'Travel & Accommodation Logistics', 'tagline': 'Expert coordination of travel and accommodation for productions.', 'category': 'Crew & Logistics'},
    'equipment-planning': {'h1': 'Equipment Planning Services', 'tagline': 'Expert planning and coordination of production equipment and technology.', 'category': 'Crew & Logistics'},
    'catering-services': {'h1': 'Catering & On-Set Services', 'tagline': 'Professional catering and on-set service coordination for productions.', 'category': 'Crew & Logistics'},
    'contract-management': {'h1': 'Contract Management Services', 'tagline': 'Expert management of contracts and legal documentation for productions.', 'category': 'Legal & Administrative'},
    'talent-releases': {'h1': 'Talent Releases & Agreements', 'tagline': 'Professional handling of talent releases and legal agreements.', 'category': 'Legal & Administrative'},
    'location-agreements': {'h1': 'Location Agreements & Contracts', 'tagline': 'Expert handling of location agreements and legal contracts.', 'category': 'Legal & Administrative'},
    'licensing-rights': {'h1': 'Licensing & Rights Management', 'tagline': 'Expert management of licensing and intellectual property rights.', 'category': 'Legal & Administrative'},
    'covid-compliance': {'h1': 'COVID-19 Compliance & Protocols', 'tagline': 'Expert COVID-19 safety protocols and compliance coordination.', 'category': 'Legal & Administrative'}
}

def complete_page(service_key, service_data):
    """Complete a pre-production service page with full content"""
    page_path = f'pre-production-services/{service_key}/index.html'

    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add mobile navigation after desktop navigation
        mobile_nav = get_mobile_navigation()
        content = content.replace('                </nav>', f'                </nav>{mobile_nav}')

        # Add main content after header
        main_content = get_main_content_template(service_data)
        content = content.replace('    </header>', f'    </header>{main_content}')

        # Add footer and JavaScript
        footer_js = get_enhanced_footer()
        content = content.replace('</body>\n</html>', footer_js)

        # Write completed content
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    except Exception as e:
        print(f"❌ Error completing {service_key}: {e}")
        return False

def main():
    """Complete all pre-production service pages"""
    print("🚀 Completing pre-production service pages...")

    completed_count = 0
    for service_key, service_data in SERVICES_DATA.items():
        if complete_page(service_key, service_data):
            print(f"✅ Completed {service_key}")
            completed_count += 1

    print(f"\n📊 Completed {completed_count}/{len(SERVICES_DATA)} pages")
    print("🎉 Pre-production pages completion finished!")

if __name__ == "__main__":
    main()