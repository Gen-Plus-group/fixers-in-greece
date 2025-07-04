/**
 * Dynamic Component Loader for Fixers in Greece Website
 * Loads header, navigation, and footer components dynamically
 */

class ComponentLoader {
    constructor() {
        this.components = {
            header: '/components/header.html',
            navigation: '/components/navigation.html',
            footer: '/components/footer.html'
        };
        this.currentPage = this.getCurrentPage();
        this.cache = new Map();
    }

    /**
     * Get current page identifier for navigation highlighting
     */
    getCurrentPage() {
        const path = window.location.pathname;

        // Remove trailing slash and leading slash
        const cleanPath = path.replace(/^\/+|\/+$/g, '');

        // Check for pre-production services pages (main and sub-pages)
        if (cleanPath.startsWith('pre-production-services')) {
            return 'preproduction';
        }

        // Check for production services pages (main and sub-pages)
        if (cleanPath.startsWith('production-services')) {
            return 'production';
        }

        // Check for content production pages (main and sub-pages)
        if (cleanPath.startsWith('content-production')) {
            return 'contentproduction';
        }

        // Check for filming-in-greece pages (main and sub-pages)
        if (cleanPath.startsWith('filming-in-greece')) {
            return 'filming';
        }

        // Map paths to page identifiers
        const pageMap = {
            '': 'home',
            'index.html': 'home',
            'about-us': 'about',
            'contact': 'contact',
            'film-production-services': 'services',
            'equipment-rental-Greece': 'services',
            'location-scouting-Greece': 'services',
            'film-permits-Greece': 'services',
            'Greece-film-crew': 'services',
            'drone-filming-Greece': 'services',
            'corporate-video-Greece': 'services',
            'equipment-transport-Greece': 'services',
            'translation-services-Greece': 'services',
            'casting-services-Greece': 'services',
            'post-production-Greece': 'services',
            'hire-film-director': 'services',
            'hire-film-producer': 'services',
            'hire-line-producer': 'services',
            'hire-fixer': 'services',
            'hire-dop': 'services',
            'hire-location-manager': 'services',
            'filming-in-Greece': 'filming',
            'portfolio': 'portfolio',
            'clients': 'clients'
        };

        return pageMap[cleanPath] || 'other';
    }

    /**
     * Load a component from cache or fetch from server
     */
    async loadComponent(componentName) {
        if (this.cache.has(componentName)) {
            return this.cache.get(componentName);
        }

        try {
            const response = await fetch(this.components[componentName]);
            if (!response.ok) {
                throw new Error(`Failed to load ${componentName}: ${response.status}`);
            }
            
            const html = await response.text();
            this.cache.set(componentName, html);
            return html;
        } catch (error) {
            console.error(`Error loading ${componentName}:`, error);
            return null;
        }
    }

    /**
     * Load and inject header component
     */
    async loadHeader() {
        const headerContainer = document.getElementById('header-container');
        if (!headerContainer) return;

        const headerHtml = await this.loadComponent('header');
        if (headerHtml) {
            headerContainer.innerHTML = headerHtml;

            // Load mobile menu CSS dynamically
            this.loadMobileMenuCSS();

            console.log('✅ Header loaded successfully');
        }
    }

    /**
     * Load mobile menu CSS dynamically
     */
    loadMobileMenuCSS() {
        // Check if mobile menu CSS is already loaded
        if (document.querySelector('link[href="/mobile-menu.css"]')) {
            return;
        }

        // Create and inject mobile menu CSS link
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = '/mobile-menu.css';
        link.type = 'text/css';

        // Add to document head
        document.head.appendChild(link);

        // Also ensure dark theme CSS is loaded for compatibility
        this.loadDarkThemeCSS();

        console.log('✅ Mobile menu CSS loaded dynamically');
    }

    /**
     * Load dark theme CSS if not already present
     */
    loadDarkThemeCSS() {
        // Check if dark theme CSS is already loaded
        if (document.querySelector('link[href="/dark-theme.css"]')) {
            return;
        }

        // Create and inject dark theme CSS link
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = '/dark-theme.css';
        link.type = 'text/css';

        // Add to document head
        document.head.appendChild(link);

        console.log('✅ Dark theme CSS loaded dynamically');
    }

    /**
     * Load and inject navigation components
     */
    async loadNavigation() {
        const navigationHtml = await this.loadComponent('navigation');
        if (!navigationHtml) return;

        // Extract desktop and mobile navigation
        const parser = new DOMParser();
        const doc = parser.parseFromString(navigationHtml, 'text/html');
        
        const desktopNav = doc.getElementById('desktop-navigation');
        const mobileNav = doc.getElementById('mobile-navigation');

        // Inject desktop navigation
        const desktopContainer = document.getElementById('desktop-nav');
        if (desktopContainer && desktopNav) {
            desktopContainer.innerHTML = desktopNav.innerHTML;
        }

        // Inject mobile navigation
        const mobileContainer = document.getElementById('mobile-navigation-content');
        if (mobileContainer && mobileNav) {
            mobileContainer.innerHTML = mobileNav.innerHTML;
        }

        // Apply current page highlighting
        this.highlightCurrentPage();
        
        // Initialize mobile menu functionality
        this.initializeMobileMenu();
        
        console.log('✅ Navigation loaded successfully');
    }

    /**
     * Load and inject footer component
     */
    async loadFooter() {
        const footerContainer = document.getElementById('footer-container');
        if (!footerContainer) return;

        const footerHtml = await this.loadComponent('footer');
        if (footerHtml) {
            footerContainer.innerHTML = footerHtml;
            console.log('✅ Footer loaded successfully');
        }
    }

    /**
     * Highlight current page in navigation
     */
    highlightCurrentPage() {
        // Remove existing highlights
        document.querySelectorAll('[data-nav]').forEach(link => {
            link.classList.remove('text-greece-blue', 'font-medium');
            link.classList.add('text-greece-gray');
        });

        // Add highlight to current page
        const currentLinks = document.querySelectorAll(`[data-nav="${this.currentPage}"]`);
        currentLinks.forEach(link => {
            link.classList.remove('text-greece-gray');
            link.classList.add('text-greece-blue', 'font-medium');
        });
    }

    /**
     * Initialize mobile menu functionality
     */
    initializeMobileMenu() {
        // Mobile menu main toggle
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileMenuClose = document.getElementById('mobile-menu-close');
        const mobileMenuBackdrop = document.getElementById('mobile-menu-backdrop');
        const mobileMenuIcon = document.getElementById('mobile-menu-icon');

        // Open mobile menu
        if (mobileMenuButton && mobileMenuOverlay && mobileMenu) {
            mobileMenuButton.addEventListener('click', () => {
                this.openMobileMenu();
            });
        }

        // Close mobile menu
        if (mobileMenuClose) {
            mobileMenuClose.addEventListener('click', () => {
                this.closeMobileMenu();
            });
        }

        // Close mobile menu when clicking backdrop
        if (mobileMenuBackdrop) {
            mobileMenuBackdrop.addEventListener('click', () => {
                this.closeMobileMenu();
            });
        }

        // Initialize 3-level mobile menu functionality
        this.initializeMobileMegaMenus();
        this.initializeMobileCategoryMenus();

        // Close mobile menu on escape key
        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape' && !mobileMenuOverlay.classList.contains('hidden')) {
                this.closeMobileMenu();
            }
        });
    }

    /**
     * Open mobile menu
     */
    openMobileMenu() {
        const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenuIcon = document.getElementById('mobile-menu-icon');

        if (mobileMenuOverlay && mobileMenu) {
            // Show overlay
            mobileMenuOverlay.classList.remove('hidden');

            // Animate menu in
            setTimeout(() => {
                mobileMenu.classList.remove('translate-x-full');
            }, 10);

            // Update button state
            if (mobileMenuButton) {
                mobileMenuButton.setAttribute('aria-expanded', 'true');
            }

            // Change hamburger to X
            if (mobileMenuIcon) {
                mobileMenuIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>';
            }

            // Prevent body scroll
            document.body.style.overflow = 'hidden';
        }
    }

    /**
     * Close mobile menu
     */
    closeMobileMenu() {
        const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenuIcon = document.getElementById('mobile-menu-icon');

        if (mobileMenuOverlay && mobileMenu) {
            // Animate menu out
            mobileMenu.classList.add('translate-x-full');

            // Hide overlay after animation
            setTimeout(() => {
                mobileMenuOverlay.classList.add('hidden');
            }, 300);

            // Update button state
            if (mobileMenuButton) {
                mobileMenuButton.setAttribute('aria-expanded', 'false');
            }

            // Change X back to hamburger
            if (mobileMenuIcon) {
                mobileMenuIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>';
            }

            // Restore body scroll
            document.body.style.overflow = '';

            // Close all submenus
            this.closeAllMobileSubmenus();
        }
    }

    /**
     * Initialize mobile mega menus (Level 2)
     */
    initializeMobileMegaMenus() {
        const megaToggles = document.querySelectorAll('.mobile-mega-toggle');

        megaToggles.forEach(toggle => {
            toggle.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                const targetId = toggle.getAttribute('data-target');
                const submenu = document.getElementById(targetId);
                const icon = toggle.querySelector('.mobile-mega-icon');
                const isExpanded = toggle.getAttribute('aria-expanded') === 'true';

                // Close other mega menus
                this.closeAllMobileMegaMenus(targetId);

                if (isExpanded) {
                    // Close this mega menu
                    submenu.classList.add('hidden');
                    toggle.setAttribute('aria-expanded', 'false');
                    icon.style.transform = 'rotate(0deg)';
                } else {
                    // Open this mega menu
                    submenu.classList.remove('hidden');
                    toggle.setAttribute('aria-expanded', 'true');
                    icon.style.transform = 'rotate(180deg)';
                }
            });
        });
    }

    /**
     * Initialize mobile category menus (Level 3)
     */
    initializeMobileCategoryMenus() {
        const categoryToggles = document.querySelectorAll('.mobile-category-toggle');

        categoryToggles.forEach(toggle => {
            toggle.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                const targetId = toggle.getAttribute('data-target');
                const submenu = document.getElementById(targetId);
                const icon = toggle.querySelector('.mobile-category-icon');
                const isExpanded = toggle.getAttribute('aria-expanded') === 'true';

                if (isExpanded) {
                    // Close this category menu
                    submenu.classList.add('hidden');
                    toggle.setAttribute('aria-expanded', 'false');
                    icon.style.transform = 'rotate(0deg)';
                } else {
                    // Open this category menu
                    submenu.classList.remove('hidden');
                    toggle.setAttribute('aria-expanded', 'true');
                    icon.style.transform = 'rotate(180deg)';
                }
            });
        });
    }

    /**
     * Close all mobile mega menus
     */
    closeAllMobileMegaMenus(exceptId) {
        const allMegaMenus = document.querySelectorAll('.mobile-mega-submenu');
        const allMegaToggles = document.querySelectorAll('.mobile-mega-toggle');
        const allMegaIcons = document.querySelectorAll('.mobile-mega-icon');

        allMegaMenus.forEach(submenu => {
            if (!exceptId || submenu.id !== exceptId) {
                submenu.classList.add('hidden');
            }
        });

        allMegaToggles.forEach(toggle => {
            if (!exceptId || toggle.getAttribute('data-target') !== exceptId) {
                toggle.setAttribute('aria-expanded', 'false');
            }
        });

        allMegaIcons.forEach(icon => {
            const toggle = icon.closest('.mobile-mega-toggle');
            if (!exceptId || toggle.getAttribute('data-target') !== exceptId) {
                icon.style.transform = 'rotate(0deg)';
            }
        });

        // Also close all category menus when closing mega menus
        this.closeAllMobileCategoryMenus();
    }

    /**
     * Close all mobile category menus
     */
    closeAllMobileCategoryMenus() {
        const allCategoryMenus = document.querySelectorAll('.mobile-category-submenu');
        const allCategoryToggles = document.querySelectorAll('.mobile-category-toggle');
        const allCategoryIcons = document.querySelectorAll('.mobile-category-icon');

        allCategoryMenus.forEach(submenu => {
            submenu.classList.add('hidden');
        });

        allCategoryToggles.forEach(toggle => {
            toggle.setAttribute('aria-expanded', 'false');
        });

        allCategoryIcons.forEach(icon => {
            icon.style.transform = 'rotate(0deg)';
        });
    }

    /**
     * Close all mobile submenus (legacy support)
     */
    closeAllMobileSubmenus() {
        this.closeAllMobileMegaMenus();
        this.closeAllMobileCategoryMenus();
    }

    /**
     * Load all components
     */
    async loadAllComponents() {
        console.log('🚀 Loading dynamic components...');

        try {
            // Load header first, then navigation (which depends on header), then footer
            await this.loadHeader();
            console.log('✅ Header loaded, now loading navigation...');

            await this.loadNavigation();
            console.log('✅ Navigation loaded, now loading footer...');

            await this.loadFooter();
            console.log('✅ Footer loaded');

            console.log('🎉 All components loaded successfully!');

            // Dispatch custom event when components are loaded
            document.dispatchEvent(new CustomEvent('componentsLoaded'));

        } catch (error) {
            console.error('❌ Error loading components:', error);
            // Try to reload components once more if there was an error
            setTimeout(() => {
                console.log('🔄 Retrying component loading...');
                this.loadAllComponents();
            }, 1000);
        }
    }
}

// Initialize component loader when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    console.log('🔧 DOM Content Loaded - Initializing Component Loader...');
    const loader = new ComponentLoader();
    loader.loadAllComponents();
});

// Fallback initialization if DOMContentLoaded has already fired
if (document.readyState === 'loading') {
    // DOM is still loading, DOMContentLoaded will fire
    console.log('📄 DOM is still loading, waiting for DOMContentLoaded...');
} else {
    // DOM has already loaded
    console.log('⚡ DOM already loaded, initializing components immediately...');
    const loader = new ComponentLoader();
    loader.loadAllComponents();
}

// Export for potential external use
window.ComponentLoader = ComponentLoader;
