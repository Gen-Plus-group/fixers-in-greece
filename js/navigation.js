/**
 * Navigation JavaScript for Fixers in Greece
 * Handles mobile menu, dropdowns, and navigation interactions
 * Version: 1.0.37
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // Mobile menu elements
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuClose = document.getElementById('mobile-menu-close');
    const mobileMenuBackdrop = document.getElementById('mobile-menu-backdrop');
    
    // Mobile menu toggle functionality
    if (mobileMenuButton && mobileMenuOverlay && mobileMenu) {
        
        // Open mobile menu
        mobileMenuButton.addEventListener('click', function() {
            mobileMenuOverlay.classList.remove('hidden');
            // Force reflow
            mobileMenuOverlay.offsetHeight;
            mobileMenu.classList.remove('translate-x-full');
            mobileMenuButton.setAttribute('aria-expanded', 'true');
            document.body.style.overflow = 'hidden';
        });
        
        // Close mobile menu
        function closeMobileMenu() {
            mobileMenu.classList.add('translate-x-full');
            mobileMenuButton.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
            setTimeout(() => {
                mobileMenuOverlay.classList.add('hidden');
            }, 300);
        }
        
        // Close button
        if (mobileMenuClose) {
            mobileMenuClose.addEventListener('click', closeMobileMenu);
        }
        
        // Backdrop click
        if (mobileMenuBackdrop) {
            mobileMenuBackdrop.addEventListener('click', closeMobileMenu);
        }
        
        // Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && !mobileMenuOverlay.classList.contains('hidden')) {
                closeMobileMenu();
            }
        });
        
        // Close on window resize (desktop)
        window.addEventListener('resize', function() {
            if (window.innerWidth >= 1024) {
                closeMobileMenu();
            }
        });
    }
    
    // Dropdown menu functionality for desktop
    const dropdownTriggers = document.querySelectorAll('.dropdown-toggle, .mega-menu-trigger > a');
    const megaMenus = document.querySelectorAll('.mega-menu');
    
    // Handle dropdown hovers
    dropdownTriggers.forEach(trigger => {
        const parent = trigger.closest('.dropdown, .mega-menu-trigger');
        const menu = parent?.querySelector('.dropdown-menu, .mega-menu');
        
        if (parent && menu) {
            let hoverTimeout;
            
            parent.addEventListener('mouseenter', function() {
                clearTimeout(hoverTimeout);
                // Close other open menus
                megaMenus.forEach(otherMenu => {
                    if (otherMenu !== menu) {
                        otherMenu.style.opacity = '0';
                        otherMenu.style.visibility = 'hidden';
                    }
                });
                
                // Open this menu
                menu.style.opacity = '1';
                menu.style.visibility = 'visible';
            });
            
            parent.addEventListener('mouseleave', function() {
                hoverTimeout = setTimeout(() => {
                    menu.style.opacity = '0';
                    menu.style.visibility = 'hidden';
                }, 150);
            });
        }
    });
    
    // Mobile submenu functionality
    const mobileSubmenuToggles = document.querySelectorAll('.mobile-submenu-toggle');
    
    mobileSubmenuToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            const submenu = this.nextElementSibling;
            const arrow = this.querySelector('.arrow');
            
            if (submenu) {
                const isOpen = submenu.style.display === 'block';
                
                if (isOpen) {
                    submenu.style.display = 'none';
                    if (arrow) arrow.style.transform = 'rotate(0deg)';
                } else {
                    submenu.style.display = 'block';
                    if (arrow) arrow.style.transform = 'rotate(180deg)';
                }
            }
        });
    });
    
    // Active page highlighting
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a[href]');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (href !== '/' && currentPath.startsWith(href))) {
            link.classList.add('active');
        }
    });
    
    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const offsetTop = target.offsetTop - 80; // Account for fixed header
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Header scroll behavior
    const header = document.querySelector('header, .site-header');
    if (header) {
        let lastScrollTop = 0;
        let isScrolling = false;
        
        window.addEventListener('scroll', function() {
            if (!isScrolling) {
                window.requestAnimationFrame(function() {
                    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                    
                    if (scrollTop > lastScrollTop && scrollTop > 100) {
                        // Scrolling down
                        header.style.transform = 'translateY(-100%)';
                    } else {
                        // Scrolling up
                        header.style.transform = 'translateY(0)';
                    }
                    
                    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
                    isScrolling = false;
                });
                isScrolling = true;
            }
        });
    }
    
    // Focus trap for mobile menu accessibility
    function trapFocus(element) {
        const focusableElements = element.querySelectorAll(
            'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];
        
        element.addEventListener('keydown', function(e) {
            if (e.key === 'Tab') {
                if (e.shiftKey) {
                    if (document.activeElement === firstElement) {
                        lastElement.focus();
                        e.preventDefault();
                    }
                } else {
                    if (document.activeElement === lastElement) {
                        firstElement.focus();
                        e.preventDefault();
                    }
                }
            }
        });
    }
    
    if (mobileMenu) {
        trapFocus(mobileMenu);
    }
    
    console.log('Navigation JavaScript loaded successfully');
});