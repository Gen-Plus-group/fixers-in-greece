/**
 * Inline Component Loader - A simpler approach
 * This directly inserts the header and footer HTML without fetch
 */

document.addEventListener('DOMContentLoaded', function() {
    // Header HTML
    const headerHTML = `
    <!-- Header -->
    <header class="bg-greece-dark border-b border-gray-800 sticky top-0 z-50">
        <div class="container mx-auto px-4">
            <div class="flex items-center justify-between h-20">
                <!-- Logo -->
                <div class="flex-shrink-0">
                    <a href="/" class="flex items-center">
                        <img src="/assets/images/2016/10/needafixer-greece.png" 
                             alt="NEEDaFIXER" 
                             class="h-12 w-auto">
                    </a>
                </div>

                <!-- Desktop Navigation -->
                <nav id="desktop-nav" class="hidden lg:flex items-center space-x-8">
                    <!-- Navigation will be loaded here -->
                </nav>

                <!-- Mobile Menu Button -->
                <div class="lg:hidden">
                    <button id="mobile-menu-button" 
                            type="button" 
                            class="text-white hover:text-greece-blue transition-colors"
                            aria-label="Toggle mobile menu"
                            aria-expanded="false">
                        <svg id="mobile-menu-icon" class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </header>

    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu-overlay" class="fixed inset-0 z-[9999] hidden lg:hidden">
        <!-- Backdrop -->
        <div id="mobile-menu-backdrop" class="absolute inset-0 bg-black/50"></div>
        
        <!-- Mobile Menu Panel -->
        <div id="mobile-menu" class="absolute right-0 top-0 h-full w-full max-w-sm bg-greece-dark transform translate-x-full transition-transform duration-300 ease-in-out overflow-y-auto">
            <div class="p-4">
                <!-- Close Button -->
                <div class="flex items-center justify-between mb-8">
                    <img src="/assets/images/2016/10/needafixer-greece.png" 
                         alt="NEEDaFIXER" 
                         class="h-10 w-auto">
                    <button id="mobile-menu-close" 
                            type="button" 
                            class="text-white hover:text-greece-blue transition-colors"
                            aria-label="Close mobile menu">
                        <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>
                
                <!-- Mobile Navigation -->
                <nav id="mobile-navigation-content" class="space-y-1">
                    <!-- Mobile navigation will be loaded here -->
                </nav>
            </div>
        </div>
    </div>
    `;

    // Footer HTML
    const footerHTML = `
    <!-- Footer -->
    <footer class="bg-greece-blue border-t border-gray-700 py-12">
        <div class="container mx-auto px-4">
            <div class="grid md:grid-cols-4 gap-8">
                <!-- Company Info -->
                <div>
                    <img src="/assets/images/2016/10/needafixer-greece.png" 
                         alt="NEEDaFIXER" 
                         class="h-12 w-auto mb-4">
                    <p class="text-gray-400 text-sm leading-relaxed">
                        Global film production services connecting you with expert directors, producers, and crew in 100+ countries.
                    </p>
                </div>
                
                <!-- Main Navigation -->
                <div>
                    <h3 class="text-white font-semibold mb-4">Main Navigation</h3>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/" class="text-gray-400 hover:text-white transition-colors">Home</a></li>
                        <li><a href="/about-us/" class="text-gray-400 hover:text-white transition-colors">About Us</a></li>
                        <li><a href="/film-production-services/" class="text-gray-400 hover:text-white transition-colors">Services</a></li>
                        <li><a href="/filming-in-greece/" class="text-gray-400 hover:text-white transition-colors">Filming in Greece</a></li>
                        <li><a href="/portfolio/" class="text-gray-400 hover:text-white transition-colors">Portfolio</a></li>
                        <li><a href="/contact/" class="text-gray-400 hover:text-white transition-colors">Contact</a></li>
                    </ul>
                </div>
                
                <!-- Services -->
                <div>
                    <h3 class="text-white font-semibold mb-4">Our Services</h3>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/pre-production-services/" class="text-gray-400 hover:text-white transition-colors">Pre-Production</a></li>
                        <li><a href="/production-services/" class="text-gray-400 hover:text-white transition-colors">Production</a></li>
                        <li><a href="/post-production-services/" class="text-gray-400 hover:text-white transition-colors">Post-Production</a></li>
                        <li><a href="/film-crew/" class="text-gray-400 hover:text-white transition-colors">Film Crew</a></li>
                        <li><a href="/content-production/" class="text-gray-400 hover:text-white transition-colors">Content Production</a></li>
                    </ul>
                </div>
                
                <!-- Contact Info -->
                <div>
                    <h3 class="text-white font-semibold mb-4">Contact Us</h3>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-gray-400 mt-0.5 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                            </svg>
                            <div class="text-gray-400">
                                <a href="tel:+442085492259" class="hover:text-white transition-colors">+44 (0) 20 8549 2259</a>
                            </div>
                        </li>
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-gray-400 mt-0.5 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                            </svg>
                            <div class="text-gray-400">
                                <a href="mailto:enquiries@needafixer.com" class="hover:text-white transition-colors">enquiries@needafixer.com</a>
                            </div>
                        </li>
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-gray-400 mt-0.5 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                            </svg>
                            <div class="text-gray-400">
                                Athens, Greece
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
            
            <!-- Bottom Bar -->
            <div class="mt-8 pt-8 border-t border-gray-700 text-center text-sm text-gray-400">
                <p>&copy; 2010-2025 NEEDaFIXER. All rights reserved. | 
                    <a href="/privacy-policy/" class="hover:text-white transition-colors">Privacy Policy</a> | 
                    <a href="/terms-of-service/" class="hover:text-white transition-colors">Terms of Service</a>
                </p>
            </div>
        </div>
    </footer>
    `;

    // Simple navigation HTML
    const navigationHTML = `
        <a href="/" class="text-sm text-gray-300 hover:text-greece-blue transition-colors">HOME</a>
        <a href="/about-us/" class="text-sm text-gray-300 hover:text-greece-blue transition-colors">ABOUT US</a>
        <a href="/film-production-services/" class="text-sm text-gray-300 hover:text-greece-blue transition-colors">SERVICES</a>
        <a href="/filming-in-greece/" class="text-sm text-gray-300 hover:text-greece-blue transition-colors">FILMING IN GREECE</a>
        <a href="/portfolio/" class="text-sm text-gray-300 hover:text-greece-blue transition-colors">PORTFOLIO</a>
        <a href="/clients/" class="text-sm text-gray-300 hover:text-greece-blue transition-colors">CLIENTS</a>
        <a href="/contact/" class="text-sm text-gray-300 hover:text-greece-blue transition-colors">CONTACT</a>
    `;

    // Mobile navigation HTML
    const mobileNavigationHTML = `
        <a href="/" class="block py-3 text-white hover:text-greece-blue transition-colors">HOME</a>
        <a href="/about-us/" class="block py-3 text-white hover:text-greece-blue transition-colors">ABOUT US</a>
        <a href="/film-production-services/" class="block py-3 text-white hover:text-greece-blue transition-colors">SERVICES</a>
        <a href="/filming-in-greece/" class="block py-3 text-white hover:text-greece-blue transition-colors">FILMING IN GREECE</a>
        <a href="/portfolio/" class="block py-3 text-white hover:text-greece-blue transition-colors">PORTFOLIO</a>
        <a href="/clients/" class="block py-3 text-white hover:text-greece-blue transition-colors">CLIENTS</a>
        <a href="/contact/" class="block py-3 text-white hover:text-greece-blue transition-colors">CONTACT</a>
    `;

    // Insert components
    const headerContainer = document.getElementById('header-container');
    if (headerContainer) {
        headerContainer.innerHTML = headerHTML;
        
        // Insert navigation after header is loaded
        const desktopNav = document.getElementById('desktop-nav');
        if (desktopNav) {
            desktopNav.innerHTML = navigationHTML;
        }
        
        const mobileNav = document.getElementById('mobile-navigation-content');
        if (mobileNav) {
            mobileNav.innerHTML = mobileNavigationHTML;
        }
    }

    const footerContainer = document.getElementById('footer-container');
    if (footerContainer) {
        footerContainer.innerHTML = footerHTML;
    }

    // Initialize mobile menu functionality
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuClose = document.getElementById('mobile-menu-close');
    const mobileMenuBackdrop = document.getElementById('mobile-menu-backdrop');
    const mobileMenuIcon = document.getElementById('mobile-menu-icon');

    if (mobileMenuButton && mobileMenuOverlay && mobileMenu) {
        // Open menu
        mobileMenuButton.addEventListener('click', () => {
            mobileMenuOverlay.classList.remove('hidden');
            setTimeout(() => {
                mobileMenu.classList.remove('translate-x-full');
            }, 10);
            mobileMenuButton.setAttribute('aria-expanded', 'true');
            document.body.style.overflow = 'hidden';
        });

        // Close menu
        const closeMenu = () => {
            mobileMenu.classList.add('translate-x-full');
            setTimeout(() => {
                mobileMenuOverlay.classList.add('hidden');
            }, 300);
            mobileMenuButton.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        };

        if (mobileMenuClose) {
            mobileMenuClose.addEventListener('click', closeMenu);
        }
        if (mobileMenuBackdrop) {
            mobileMenuBackdrop.addEventListener('click', closeMenu);
        }
    }

    console.log('✅ Components loaded successfully!');
});