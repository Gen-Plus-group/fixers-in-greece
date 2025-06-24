/**
 * Inline Component Loader - A simpler approach
 * This directly inserts the header and footer HTML without fetch
 */

// Add mega menu styles dynamically
const megaMenuStyles = `
<style>
/* Mega Menu Styles */
.mega-menu {
    position: absolute;
    top: calc(100% + 12px);
    left: 50%;
    transform: translateX(-50%) translateY(-10px);
    width: 100vw;
    max-width: 1400px;
    min-width: 1200px;
    background: #1a1a1a;
    border-top: 2px solid #f9a531;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
    z-index: 50;
    margin-top: 8px;
}

.mega-menu-trigger:hover .mega-menu {
    opacity: 1;
    visibility: visible;
    transform: translateX(-50%) translateY(0);
}

.mega-menu-column {
    border-right: 1px solid #333;
    min-width: 0;
}

.mega-menu-column:last-child {
    border-right: none;
}

.mega-menu-content {
    max-width: 1400px;
    margin: 0 auto;
    padding: 1.5rem 1rem;
}

/* Mega Menu Typography */
.mega-menu h3 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
}

.mega-menu h4 {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #f9a531;
}

.mega-menu a {
    font-size: 0.875rem;
    line-height: 1.5;
    padding: 0.25rem 0;
    display: block;
    transition: all 0.2s ease;
}

.mega-menu a:hover {
    color: #f9a531;
    padding-left: 0.25rem;
}

.mega-menu ul {
    margin-top: 0.5rem;
}

.mega-menu li {
    margin-bottom: 0.5rem;
}

/* Ensure mega menu doesn't get clipped */
.mega-menu-trigger {
    position: static;
}

/* Navigation container needs to allow overflow for mega menu */
nav {
    position: relative;
    overflow: visible;
}

/* Mobile Menu Styles */
@media (max-width: 1024px) {
    .mega-menu {
        display: none;
    }
}
</style>
`;

document.addEventListener('DOMContentLoaded', function() {
    // Inject mega menu styles
    document.head.insertAdjacentHTML('beforeend', megaMenuStyles);
    // Header HTML
    const headerHTML = `
    <!-- Top Bar -->
    <div class="bg-greece-dark border-b border-gray-700 text-sm">
        <div class="container mx-auto px-4 py-3">
            <div class="flex flex-col md:flex-row md:justify-end items-center space-y-2 md:space-y-0 md:space-x-6 text-center md:text-right">
                <div class="flex items-center space-x-2">
                    <span class="text-greece-blue">📞</span>
                    <a href="tel:+442085492259" class="text-gray-300 hover:text-greece-blue transition-colors">+30 211 1983 725</a>
                </div>
                <div class="flex items-center space-x-2">
                    <span class="text-greece-blue">✉️</span>
                    <a href="mailto:greece@needafixer.com" class="text-gray-300 hover:text-greece-blue transition-colors">greece@needafixer.com</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Header -->
    <header class="bg-greece-dark border-b border-gray-800 sticky top-0 z-50">
        <div class="container mx-auto px-4">
            <div class="flex items-center justify-between h-20 py-4">
                <!-- Logo -->
                <div class="flex-shrink-0">
                    <a href="/" class="flex items-center">
                        <img src="/assets/images/needafixer-greece-white.png" 
                             alt="NEEDaFIXER" 
                             class="h-12 w-auto">
                    </a>
                </div>

                <!-- Desktop Navigation -->
                <nav id="desktop-nav" class="hidden lg:flex items-center space-x-4">
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
                    <img src="/assets/images/needafixer-greece-white.png" 
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
    <footer class="bg-gray-900 border-t border-gray-800 py-12">
        <div class="container mx-auto px-4">
            <div class="grid md:grid-cols-4 gap-8">
                <!-- Company Info -->
                <div>
                    <img src="/assets/images/needafixer-greece-white.png" 
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
                        <li><a href="/" class="text-gray-400 hover:text-greece-blue transition-colors">Home</a></li>
                        <li><a href="/about-us/" class="text-gray-400 hover:text-greece-blue transition-colors">About Us</a></li>
                        <li><a href="/film-production-services/" class="text-gray-400 hover:text-greece-blue transition-colors">Services</a></li>
                        <li><a href="/filming-in-greece/" class="text-gray-400 hover:text-greece-blue transition-colors">Filming in Greece</a></li>
                        <li><a href="/portfolio/" class="text-gray-400 hover:text-greece-blue transition-colors">Portfolio</a></li>
                        <li><a href="/contact/" class="text-gray-400 hover:text-greece-blue transition-colors">Contact</a></li>
                    </ul>
                </div>
                
                <!-- Services -->
                <div>
                    <h3 class="text-white font-semibold mb-4">Our Services</h3>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/pre-production-services/" class="text-gray-400 hover:text-greece-blue transition-colors">Pre-Production</a></li>
                        <li><a href="/production-services/" class="text-gray-400 hover:text-greece-blue transition-colors">Production</a></li>
                        <li><a href="/post-production-services/" class="text-gray-400 hover:text-greece-blue transition-colors">Post-Production</a></li>
                        <li><a href="/film-crew/" class="text-gray-400 hover:text-greece-blue transition-colors">Film Crew</a></li>
                        <li><a href="/content-production/" class="text-gray-400 hover:text-greece-blue transition-colors">Content Production</a></li>
                    </ul>
                </div>
                
                <!-- Contact Info -->
                <div>
                    <h3 class="text-white font-semibold mb-4">Contact Us</h3>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-start">
                            <svg class="w-4 h-4 text-gray-500 mt-0.5 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                            </svg>
                            <div class="text-gray-400">
                                <a href="tel:+442085492259" class="hover:text-greece-blue transition-colors">+30 211 1983 725</a>
                            </div>
                        </li>
                        <li class="flex items-start">
                            <svg class="w-4 h-4 text-gray-500 mt-0.5 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                            </svg>
                            <div class="text-gray-400">
                                <a href="mailto:greece@needafixer.com" class="hover:text-greece-blue transition-colors">greece@needafixer.com</a>
                            </div>
                        </li>
                        <li class="flex items-start">
                            <svg class="w-4 h-4 text-gray-500 mt-0.5 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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
            <div class="mt-8 pt-8 border-t border-gray-800 text-center text-sm text-gray-400">
                <p>&copy; 2010-2025 NEEDaFIXER. All rights reserved. | 
                    <a href="/privacy-policy/" class="hover:text-greece-blue transition-colors">Privacy Policy</a> | 
                    <a href="/terms-of-service/" class="hover:text-greece-blue transition-colors">Terms of Service</a>
                </p>
            </div>
        </div>
    </footer>
    `;

    // Desktop navigation HTML with mega menus
    const navigationHTML = `
        <a href="/" class="text-sm text-greece-gray hover:text-greece-blue transition-colors duration-200" data-nav="home">HOME</a>
        <a href="/about-us/" class="text-sm text-greece-gray hover:text-greece-blue transition-colors duration-200" data-nav="about">ABOUT US</a>

        <!-- Pre-Production Mega Menu -->
        <div class="relative mega-menu-trigger">
            <a href="/pre-production-services/" class="text-sm text-greece-gray hover:text-greece-blue transition-colors duration-200 flex items-center" data-nav="preproduction">
                PRE-PRODUCTION
                <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                </svg>
            </a>
            <div class="mega-menu">
                <div class="mega-menu-content">
                    <div class="text-center mb-8">
                        <h3 class="text-greece-blue">Pre-Production Services</h3>
                        <p class="text-gray-400 text-base">Planning, creative development, logistics</p>
                    </div>
                    <div class="grid grid-cols-6 gap-10">
                        <!-- Creative & Development -->
                        <div class="mega-menu-column">
                            <h4>Creative & Development</h4>
                            <ul>
                                <li><a href="/pre-production-services/scriptwriting/" class="text-gray-300">Scriptwriting</a></li>
                                <li><a href="/pre-production-services/script-consultation/" class="text-gray-300">Script Consultation</a></li>
                                <li><a href="/pre-production-services/storyboarding/" class="text-gray-300">Storyboarding</a></li>
                                <li><a href="/pre-production-services/concept-development/" class="text-gray-300">Concept Development</a></li>
                                <li><a href="/pre-production-services/creative-direction/" class="text-gray-300">Creative Direction</a></li>
                                <li><a href="/pre-production-services/moodboard-creation/" class="text-gray-300">Moodboards</a></li>
                                <li><a href="/pre-production-services/pitch-deck-design/" class="text-gray-300">Pitch Decks</a></li>
                            </ul>
                        </div>

                        <!-- Casting & Talent -->
                        <div class="mega-menu-column">
                            <h4>Casting & Talent</h4>
                            <ul>
                                <li><a href="/pre-production-services/casting-services/" class="text-gray-300">Casting Services</a></li>
                                <li><a href="/pre-production-services/voiceover-casting/" class="text-gray-300">Voiceover Casting</a></li>
                                <li><a href="/pre-production-services/talent-coordination/" class="text-gray-300">Talent Coordination</a></li>
                                <li><a href="/pre-production-services/union-talent-management/" class="text-gray-300">Union Management</a></li>
                            </ul>
                        </div>

                        <!-- Location & Permits -->
                        <div class="mega-menu-column">
                            <h4>Location & Permits</h4>
                            <ul>
                                <li><a href="/pre-production-services/location-scouting-services/" class="text-gray-300">Location Scouting</a></li>
                                <li><a href="/pre-production-services/location-management/" class="text-gray-300">Location Management</a></li>
                                <li><a href="/pre-production-services/film-permit-acquisition/" class="text-gray-300">Permit Acquisition</a></li>
                                <li><a href="/pre-production-services/site-surveys/" class="text-gray-300">Site Surveys</a></li>
                                <li><a href="/pre-production-services/production-insurance/" class="text-gray-300">Production Insurance</a></li>
                            </ul>
                        </div>

                        <!-- Budgeting & Scheduling -->
                        <div class="mega-menu-column">
                            <h4>Budgeting & Scheduling</h4>
                            <ul>
                                <li><a href="/pre-production-services/production-budgeting/" class="text-gray-300">Production Budgeting</a></li>
                                <li><a href="/pre-production-services/cost-estimation/" class="text-gray-300">Cost Estimation</a></li>
                                <li><a href="/pre-production-services/production-scheduling/" class="text-gray-300">Production Scheduling</a></li>
                                <li><a href="/pre-production-services/call-sheets/" class="text-gray-300">Call Sheets</a></li>
                            </ul>
                        </div>

                        <!-- Crew & Logistics -->
                        <div class="mega-menu-column">
                            <h4>Crew & Logistics</h4>
                            <ul>
                                <li><a href="/pre-production-services/line-producing-services/" class="text-gray-300">Line Producing</a></li>
                                <li><a href="/pre-production-services/crew-hiring/" class="text-gray-300">Crew Hiring</a></li>
                                <li><a href="/pre-production-services/fixer-services-local/" class="text-gray-300">Local Fixers</a></li>
                                <li><a href="/pre-production-services/travel-logistics/" class="text-gray-300">Travel Logistics</a></li>
                                <li><a href="/pre-production-services/equipment-planning/" class="text-gray-300">Equipment Planning</a></li>
                                <li><a href="/pre-production-services/catering-services/" class="text-gray-300">Catering Services</a></li>
                            </ul>
                        </div>

                        <!-- Legal & Administrative -->
                        <div class="mega-menu-column">
                            <h4>Legal & Administrative</h4>
                            <ul>
                                <li><a href="/pre-production-services/contract-management/" class="text-gray-300">Contract Management</a></li>
                                <li><a href="/pre-production-services/talent-releases/" class="text-gray-300">Talent Releases</a></li>
                                <li><a href="/pre-production-services/location-agreements/" class="text-gray-300">Location Agreements</a></li>
                                <li><a href="/pre-production-services/licensing-rights/" class="text-gray-300">Licensing & Rights</a></li>
                                <li><a href="/pre-production-services/covid-compliance/" class="text-gray-300">COVID Compliance</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Production Services Mega Menu -->
        <div class="relative mega-menu-trigger">
            <a href="/production-services/" class="text-sm text-greece-gray hover:text-greece-blue transition-colors duration-200 flex items-center" data-nav="production">
                PRODUCTION
                <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                </svg>
            </a>
            <div class="mega-menu">
                <div class="mega-menu-content">
                    <div class="text-center mb-8">
                        <h3 class="text-greece-blue">Production Services</h3>
                        <p class="text-gray-400 text-base">On-set filming and technical execution</p>
                    </div>
                    <div class="grid grid-cols-6 gap-10">
                        <!-- Camera & Cinematography -->
                        <div class="mega-menu-column">
                            <h4>Camera & Cinematography</h4>
                            <ul>
                                <li><a href="/production-services/camera-cinematography/dp-services/" class="text-gray-300">DP Services</a></li>
                                <li><a href="/production-services/camera-cinematography/multi-camera-shoots/" class="text-gray-300">Multi-Camera Shoots</a></li>
                                <li><a href="/production-services/camera-cinematography/steadicam-gimbal-operation/" class="text-gray-300">Steadicam & Gimbal</a></li>
                                <li><a href="/production-services/camera-cinematography/drone-videography/" class="text-gray-300">Drone Videography</a></li>
                                <li><a href="/production-services/camera-cinematography/underwater-filming/" class="text-gray-300">Underwater Filming</a></li>
                                <li><a href="/production-services/camera-cinematography/timelapse-hyperlapse/" class="text-gray-300">Time-lapse & Hyperlapse</a></li>
                            </ul>
                        </div>

                        <!-- Lighting & Grip -->
                        <div class="mega-menu-column">
                            <h4>Lighting & Grip</h4>
                            <ul>
                                <li><a href="/production-services/lighting-grip/gaffer-lighting-team/" class="text-gray-300">Gaffer & Lighting Team</a></li>
                                <li><a href="/production-services/lighting-grip/grip-equipment-services/" class="text-gray-300">Grip Services</a></li>
                                <li><a href="/production-services/lighting-grip/led-lighting-systems/" class="text-gray-300">LED Lighting Systems</a></li>
                                <li><a href="/production-services/lighting-grip/portable-power-solutions/" class="text-gray-300">Portable Power Solutions</a></li>
                            </ul>
                        </div>

                        <!-- Sound & Audio -->
                        <div class="mega-menu-column">
                            <h4>Sound & Audio</h4>
                            <ul>
                                <li><a href="/production-services/sound-audio/location-sound-services/" class="text-gray-300">Location Sound Services</a></li>
                                <li><a href="/production-services/sound-audio/boom-operators/" class="text-gray-300">Boom Operators</a></li>
                                <li><a href="/production-services/sound-audio/wireless-audio-systems/" class="text-gray-300">Wireless Audio Systems</a></li>
                                <li><a href="/production-services/sound-audio/sound-recordist-team/" class="text-gray-300">Sound Recordist Team</a></li>
                                <li><a href="/production-services/sound-audio/post-production-audio/" class="text-gray-300">Post-Production Audio</a></li>
                            </ul>
                        </div>

                        <!-- Production Equipment -->
                        <div class="mega-menu-column">
                            <h4>Production Equipment</h4>
                            <ul>
                                <li><a href="/production-services/production-equipment/camera-equipment-rental/" class="text-gray-300">Camera Equipment</a></li>
                                <li><a href="/production-services/production-equipment/communication-systems/" class="text-gray-300">Communication Systems</a></li>
                                <li><a href="/production-services/production-equipment/lighting-equipment-rental/" class="text-gray-300">Lighting Equipment</a></li>
                                <li><a href="/production-services/production-equipment/power-distribution-systems/" class="text-gray-300">Power Distribution</a></li>
                                <li><a href="/production-services/production-equipment/data-management-systems/" class="text-gray-300">Data Management</a></li>
                                <li><a href="/production-services/production-equipment/monitor-video-village-setups/" class="text-gray-300">Monitor & Video Village</a></li>
                            </ul>
                        </div>

                        <!-- Production Team -->
                        <div class="mega-menu-column">
                            <h4>Production Team</h4>
                            <ul>
                                <li><a href="/production-services/production-team/line-producers/" class="text-gray-300">Line Producers</a></li>
                                <li><a href="/production-services/production-team/assistant-directors/" class="text-gray-300">Assistant Directors</a></li>
                                <li><a href="/production-services/production-team/production-coordinators/" class="text-gray-300">Production Coordinators</a></li>
                                <li><a href="/production-services/production-team/production-assistants/" class="text-gray-300">Production Assistants</a></li>
                                <li><a href="/production-services/production-team/locations-managers/" class="text-gray-300">Location Managers</a></li>
                                <li><a href="/production-services/production-team/casting-directors/" class="text-gray-300">Casting Directors</a></li>
                                <li><a href="/production-services/production-team/script-supervisors/" class="text-gray-300">Script Supervisors</a></li>
                                <li><a href="/production-services/production-team/makeup-artists/" class="text-gray-300">Makeup Artists</a></li>
                            </ul>
                        </div>

                        <!-- Specialized Filming -->
                        <div class="mega-menu-column">
                            <h4>Specialized Filming</h4>
                            <ul>
                                <li><a href="/production-services/specialized-filming/aerial-drone-services/" class="text-gray-300">Aerial Drone Services</a></li>
                                <li><a href="/production-services/specialized-filming/high-speed-filming/" class="text-gray-300">High-Speed Filming</a></li>
                                <li><a href="/production-services/specialized-filming/multi-camera-setups/" class="text-gray-300">Multi-Camera Setups</a></li>
                                <li><a href="/production-services/specialized-filming/timelapse-hyperlapse/" class="text-gray-300">Timelapse & Hyperlapse</a></li>
                                <li><a href="/production-services/specialized-filming/underwater-filming/" class="text-gray-300">Underwater Filming</a></li>
                                <li><a href="/production-services/specialized-filming/virtual-reality-filming/" class="text-gray-300">Virtual Reality Filming</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Post-Production Services Mega Menu -->
        <div class="relative mega-menu-trigger" style="position: relative;" onmouseover="this.querySelector('.mega-menu').style.opacity='1'; this.querySelector('.mega-menu').style.visibility='visible'; this.querySelector('.mega-menu').style.transform='translateX(-50%) translateY(0)';" onmouseout="this.querySelector('.mega-menu').style.opacity='0'; this.querySelector('.mega-menu').style.visibility='hidden'; this.querySelector('.mega-menu').style.transform='translateX(-50%) translateY(-10px)';">
            <a href="/post-production-services/" class="text-sm text-greece-gray hover:text-greece-blue transition-colors duration-200 flex items-center" data-nav="postproduction">
                POST-PRODUCTION
                <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                </svg>
            </a>
            <div class="mega-menu" style="position: absolute; top: calc(100% + 12px); left: 50%; transform: translateX(-50%) translateY(-10px); width: 100vw; max-width: 1400px; min-width: 1200px; background: #1a1a1a; border-top: 2px solid #f9a531; box-shadow: 0 10px 25px rgba(0,0,0,0.3); opacity: 0; visibility: hidden; transition: all 0.3s ease; z-index: 50; margin-top: 8px;">
                <div class="mega-menu-content" style="max-width: 1400px; margin: 0 auto; padding: 30px 40px;">
                    <div class="text-center mb-8">
                        <h3 class="text-greece-blue" style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.75rem;">Post-Production Services</h3>
                        <p class="text-gray-400 text-base">Editing, color, VFX, audio, and delivery</p>
                    </div>
                    <div class="grid grid-cols-5 gap-10" style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 2.5rem;">
                        <!-- Editing & Assembly -->
                        <div class="mega-menu-column" style="border-right: 1px solid #333; padding-right: 2rem;">
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">Editing & Assembly</h4>
                            <ul>
                                <li><a href="/post-production-services/editing-assembly/video-editing/" class="text-gray-300">Video Editing</a></li>
                                <li><a href="/post-production-services/editing-assembly/rough-cut-final-cut/" class="text-gray-300">Rough Cut to Final Cut</a></li>
                                <li><a href="/post-production-services/editing-assembly/narrative-documentary-editing/" class="text-gray-300">Narrative & Documentary</a></li>
                                <li><a href="/post-production-services/editing-assembly/multi-cam-sync-editing/" class="text-gray-300">Multi-Cam Sync Editing</a></li>
                                <li><a href="/post-production-services/editing-assembly/interview-dialogue-editing/" class="text-gray-300">Interview & Dialogue</a></li>
                            </ul>
                        </div>

                        <!-- Color & Visual Finishing -->
                        <div class="mega-menu-column" style="border-right: 1px solid #333; padding-right: 2rem;">
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">Color & Visual Finishing</h4>
                            <ul>
                                <li><a href="/post-production-services/color-visual-finishing/color-correction/" class="text-gray-300">Color Correction</a></li>
                                <li><a href="/post-production-services/color-visual-finishing/color-grading/" class="text-gray-300">Color Grading</a></li>
                                <li><a href="/post-production-services/color-visual-finishing/online-conform-qc/" class="text-gray-300">Online Conform & QC</a></li>
                                <li><a href="/post-production-services/color-visual-finishing/look-development/" class="text-gray-300">Look Development</a></li>
                            </ul>
                        </div>

                        <!-- Motion & VFX -->
                        <div class="mega-menu-column" style="border-right: 1px solid #333; padding-right: 2rem;">
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">Motion & VFX</h4>
                            <ul>
                                <li><a href="/post-production-services/motion-vfx/motion-graphics/" class="text-gray-300">Motion Graphics</a></li>
                                <li><a href="/post-production-services/motion-vfx/visual-effects-compositing/" class="text-gray-300">VFX Compositing</a></li>
                                <li><a href="/post-production-services/motion-vfx/cgi-3d-animation/" class="text-gray-300">CGI & 3D Animation</a></li>
                                <li><a href="/post-production-services/motion-vfx/title-design-credits/" class="text-gray-300">Title Design & Credits</a></li>
                                <li><a href="/post-production-services/motion-vfx/matte-painting-environments/" class="text-gray-300">Matte Painting</a></li>
                                <li><a href="/post-production-services/motion-vfx/rotoscoping-cleanup/" class="text-gray-300">Rotoscoping & Cleanup</a></li>
                            </ul>
                        </div>

                        <!-- Audio Post -->
                        <div class="mega-menu-column" style="border-right: 1px solid #333; padding-right: 2rem;">
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">Audio Post</h4>
                            <ul>
                                <li><a href="/post-production-services/audio-post/sound-design/" class="text-gray-300">Sound Design</a></li>
                                <li><a href="/post-production-services/audio-post/foley-recording/" class="text-gray-300">Foley Recording</a></li>
                                <li><a href="/post-production-services/audio-post/dialogue-editing-adr/" class="text-gray-300">Dialogue & ADR</a></li>
                                <li><a href="/post-production-services/audio-post/music-composition-scoring/" class="text-gray-300">Music & Scoring</a></li>
                                <li><a href="/post-production-services/audio-post/audio-mixing-mastering/" class="text-gray-300">Mixing & Mastering</a></li>
                                <li><a href="/post-production-services/audio-post/5-1-surround-mixing/" class="text-gray-300">5.1 Surround Mixing</a></li>
                                <li><a href="/post-production-services/audio-post/audio-restoration/" class="text-gray-300">Audio Restoration</a></li>
                            </ul>
                        </div>

                        <!-- Delivery & Output -->
                        <div class="mega-menu-column">
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">Delivery & Output</h4>
                            <ul>
                                <li><a href="/post-production-services/delivery-output/digital-cinema-package-dcp/" class="text-gray-300">DCP Creation</a></li>
                                <li><a href="/post-production-services/delivery-output/broadcast-delivery/" class="text-gray-300">Broadcast Delivery</a></li>
                                <li><a href="/post-production-services/delivery-output/streaming-platform-delivery/" class="text-gray-300">Streaming Platforms</a></li>
                                <li><a href="/post-production-services/delivery-output/archival-preservation/" class="text-gray-300">Archival & Preservation</a></li>
                                <li><a href="/post-production-services/delivery-output/format-conversion-encoding/" class="text-gray-300">Format Conversion</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Content Production Mega Menu -->
        <div class="relative mega-menu-trigger" style="position: relative;" onmouseover="this.querySelector('.mega-menu').style.opacity='1'; this.querySelector('.mega-menu').style.visibility='visible'; this.querySelector('.mega-menu').style.transform='translateX(-50%) translateY(0)';" onmouseout="this.querySelector('.mega-menu').style.opacity='0'; this.querySelector('.mega-menu').style.visibility='hidden'; this.querySelector('.mega-menu').style.transform='translateX(-50%) translateY(-10px)';">
            <a href="/content-production/" class="text-sm text-greece-gray hover:text-greece-blue transition-colors duration-200 flex items-center" data-nav="contentproduction">
                CONTENT PRODUCTION
                <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                </svg>
            </a>
            <div class="mega-menu" style="position: absolute; top: calc(100% + 12px); left: 50%; transform: translateX(-50%) translateY(-10px); width: 100vw; max-width: 1400px; min-width: 1200px; background: #1a1a1a; border-top: 2px solid #f9a531; box-shadow: 0 10px 25px rgba(0,0,0,0.3); opacity: 0; visibility: hidden; transition: all 0.3s ease; z-index: 50; margin-top: 8px;">
                <div class="mega-menu-content" style="max-width: 1400px; margin: 0 auto; padding: 30px 40px;">
                    <div class="text-center mb-8">
                        <h3 class="text-greece-blue" style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.75rem;">Content Production Services</h3>
                        <p class="text-gray-400 text-base">TV, film, commercial, and digital content production</p>
                    </div>
                    <div class="grid grid-cols-3 gap-10" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.5rem;">
                        <!-- Column 1: TV & Film -->
                        <div class="mega-menu-column" style="border-right: 1px solid #333; padding-right: 2rem;">
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">TV & Film Production</h4>
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
                        <div class="mega-menu-column" style="border-right: 1px solid #333; padding-right: 2rem;">
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">Commercial & Corporate</h4>
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
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">Lifestyle & Creative</h4>
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

        <!-- Film Crew Services Mega Menu -->
        <div class="relative mega-menu-trigger" style="position: relative;" onmouseover="this.querySelector('.mega-menu').style.opacity='1'; this.querySelector('.mega-menu').style.visibility='visible'; this.querySelector('.mega-menu').style.transform='translateX(-50%) translateY(0)';" onmouseout="this.querySelector('.mega-menu').style.opacity='0'; this.querySelector('.mega-menu').style.visibility='hidden'; this.querySelector('.mega-menu').style.transform='translateX(-50%) translateY(-10px)';">
            <a href="/film-crew/" class="text-sm text-greece-gray hover:text-greece-blue transition-colors duration-200 flex items-center" data-nav="filmcrew">
                FILM CREW
                <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                </svg>
            </a>
            <div class="mega-menu" style="position: absolute; top: calc(100% + 12px); left: 50%; transform: translateX(-50%) translateY(-10px); width: 100vw; max-width: 1400px; min-width: 1200px; background: #1a1a1a; border-top: 2px solid #f9a531; box-shadow: 0 10px 25px rgba(0,0,0,0.3); opacity: 0; visibility: hidden; transition: all 0.3s ease; z-index: 50; margin-top: 8px;">
                <div class="mega-menu-content" style="max-width: 1400px; margin: 0 auto; padding: 30px 40px;">
                    <div class="text-center mb-8">
                        <h3 class="text-greece-blue" style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.75rem;">Film Crew Services</h3>
                        <p class="text-gray-400 text-base">Production services by role type</p>
                    </div>
                    <div class="grid grid-cols-3 gap-10" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.5rem;">
                        <!-- Creative Roles -->
                        <div class="mega-menu-column" style="border-right: 1px solid #333; padding-right: 2rem;">
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">Creative Roles</h4>
                            <ul>
                                <li><a href="/film-crew/creative-roles/director/" class="text-gray-300">Director</a></li>
                                <li><a href="/film-crew/creative-roles/creative-producer/" class="text-gray-300">Creative Producer</a></li>
                                <li><a href="/film-crew/creative-roles/scriptwriter/" class="text-gray-300">Scriptwriter</a></li>
                                <li><a href="/film-crew/creative-roles/storyboard-artist/" class="text-gray-300">Storyboard Artist</a></li>
                                <li><a href="/film-crew/creative-roles/content-creator/" class="text-gray-300">Content Creator</a></li>
                                <li><a href="/film-crew/creative-roles/editor/" class="text-gray-300">Editor</a></li>
                                <li><a href="/film-crew/creative-roles/motion-graphics-designer/" class="text-gray-300">Motion Graphics Designer</a></li>
                                <li><a href="/film-crew/creative-roles/colorist/" class="text-gray-300">Colorist</a></li>
                            </ul>
                        </div>

                        <!-- Technical Roles -->
                        <div class="mega-menu-column" style="border-right: 1px solid #333; padding-right: 2rem;">
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">Technical Roles</h4>
                            <ul>
                                <li><a href="/film-crew/technical-roles/director-of-photography/" class="text-gray-300">Director of Photography</a></li>
                                <li><a href="/film-crew/technical-roles/film-maker/" class="text-gray-300">Film Maker</a></li>
                                <li><a href="/film-crew/technical-roles/videographer/" class="text-gray-300">Videographer</a></li>
                                <li><a href="/film-crew/technical-roles/content-creator-tech/" class="text-gray-300">Content Creator</a></li>
                                <li><a href="/film-crew/technical-roles/camera-operator/" class="text-gray-300">Camera Operator</a></li>
                                <li><a href="/film-crew/technical-roles/drone-operator/" class="text-gray-300">Drone Operator</a></li>
                                <li><a href="/film-crew/technical-roles/sound-mixer/" class="text-gray-300">Sound Mixer</a></li>
                                <li><a href="/film-crew/technical-roles/lighting-technician/" class="text-gray-300">Lighting Technician</a></li>
                                <li><a href="/film-crew/technical-roles/vfx-artist/" class="text-gray-300">VFX Artist</a></li>
                                <li><a href="/film-crew/technical-roles/cgi-artist/" class="text-gray-300">CGI Artist</a></li>
                                <li><a href="/film-crew/technical-roles/dit-data-technician/" class="text-gray-300">DIT (Data Technician)</a></li>
                                <li><a href="/film-crew/technical-roles/gaffer-grip/" class="text-gray-300">Gaffer / Grip</a></li>
                            </ul>
                        </div>

                        <!-- Support Roles -->
                        <div class="mega-menu-column">
                            <h4 style="font-size: 14px; font-weight: 600; text-transform: uppercase; color: #f9a531; margin-bottom: 12px;">Support Roles</h4>
                            <ul>
                                <li><a href="/film-crew/support-roles/fixer/" class="text-gray-300">Fixer</a></li>
                                <li><a href="/film-crew/support-roles/line-producer/" class="text-gray-300">Line Producer</a></li>
                                <li><a href="/film-crew/support-roles/production-manager/" class="text-gray-300">Production Manager</a></li>
                                <li><a href="/film-crew/support-roles/location-scout/" class="text-gray-300">Location Scout</a></li>
                                <li><a href="/film-crew/support-roles/runner-set-pa/" class="text-gray-300">Runner / Set PA</a></li>
                                <li><a href="/film-crew/support-roles/catering-logistics/" class="text-gray-300">Catering / Logistics</a></li>
                                <li><a href="/film-crew/support-roles/travel-coordinator/" class="text-gray-300">Travel Coordinator</a></li>
                                <li><a href="/film-crew/support-roles/post-production-supervisor/" class="text-gray-300">Post-Production Supervisor</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <a href="/filming-in-greece/" class="text-sm text-greece-gray hover:text-greece-blue transition-colors duration-200" data-nav="filming">FILMING IN GREECE</a>
        <a href="/portfolio/" class="text-sm text-greece-gray hover:text-greece-blue transition-colors duration-200" data-nav="portfolio">PORTFOLIO</a>
        <a href="/contact/" class="text-sm text-greece-gray hover:text-greece-blue transition-colors duration-200" data-nav="contact">CONTACT</a>
    `;

    // Mobile navigation HTML with proper structure (simplified for now)
    const mobileNavigationHTML = `
        <div class="space-y-0">
            <!-- Level 1: Main Navigation Items -->
            <a href="/" class="block px-4 py-3 text-greece-gray hover:text-greece-blue hover:bg-gray-800 transition-colors duration-200 border-b border-gray-700" data-nav="home">
                <span class="font-medium">HOME</span>
            </a>

            <a href="/about-us/" class="block px-4 py-3 text-greece-gray hover:text-greece-blue hover:bg-gray-800 transition-colors duration-200 border-b border-gray-700" data-nav="about">
                <span class="font-medium">ABOUT US</span>
            </a>

            <a href="/pre-production-services/" class="block px-4 py-3 text-greece-gray hover:text-greece-blue hover:bg-gray-800 transition-colors duration-200 border-b border-gray-700">
                <span class="font-medium">PRE-PRODUCTION</span>
            </a>

            <a href="/production-services/" class="block px-4 py-3 text-greece-gray hover:text-greece-blue hover:bg-gray-800 transition-colors duration-200 border-b border-gray-700">
                <span class="font-medium">PRODUCTION</span>
            </a>

            <a href="/post-production-services/" class="block px-4 py-3 text-greece-gray hover:text-greece-blue hover:bg-gray-800 transition-colors duration-200 border-b border-gray-700">
                <span class="font-medium">POST-PRODUCTION</span>
            </a>

            <a href="/content-production/" class="block px-4 py-3 text-greece-gray hover:text-greece-blue hover:bg-gray-800 transition-colors duration-200 border-b border-gray-700">
                <span class="font-medium">CONTENT PRODUCTION</span>
            </a>

            <a href="/film-crew/" class="block px-4 py-3 text-greece-gray hover:text-greece-blue hover:bg-gray-800 transition-colors duration-200 border-b border-gray-700">
                <span class="font-medium">FILM CREW</span>
            </a>

            <a href="/filming-in-greece/" class="block px-4 py-3 text-greece-gray hover:text-greece-blue hover:bg-gray-800 transition-colors duration-200 border-b border-gray-700" data-nav="filming">
                <span class="font-medium">FILMING IN GREECE</span>
            </a>

            <a href="/portfolio/" class="block px-4 py-3 text-greece-gray hover:text-greece-blue hover:bg-gray-800 transition-colors duration-200 border-b border-gray-700" data-nav="portfolio">
                <span class="font-medium">PORTFOLIO</span>
            </a>

            <a href="/contact/" class="block px-4 py-3 text-greece-gray hover:text-greece-blue hover:bg-gray-800 transition-colors duration-200 border-b border-gray-700" data-nav="contact">
                <span class="font-medium">CONTACT</span>
            </a>
        </div>
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
    
    // Dispatch custom event when components are loaded
    document.dispatchEvent(new CustomEvent('componentsLoaded'));
});