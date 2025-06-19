#!/usr/bin/env python3
"""
Script to create all pre-production service pages with comprehensive content
"""

import os

# Define all pre-production services with their details
PREPRODUCTION_SERVICES = {
    # Creative & Development
    'scriptwriting': {
        'title': 'Professional Scriptwriting Services | Expert Screenwriters | NEEDaFIXER',
        'meta_desc': 'Professional scriptwriting services for films, TV, commercials, and digital content. Expert screenwriters worldwide.',
        'h1': 'Professional Scriptwriting Services',
        'tagline': 'Expert screenwriters for films, TV, commercials, and digital content worldwide.',
        'category': 'Creative & Development'
    },
    'script-consultation': {
        'title': 'Script Consultation & Polishing Services | Expert Script Doctors | NEEDaFIXER',
        'meta_desc': 'Professional script consultation and polishing services. Expert script doctors to refine your screenplay.',
        'h1': 'Script Consultation & Polishing Services',
        'tagline': 'Expert script doctors to refine, polish, and perfect your screenplay.',
        'category': 'Creative & Development'
    },
    'storyboarding': {
        'title': 'Professional Storyboarding Services | Visual Storytelling | NEEDaFIXER',
        'meta_desc': 'Professional storyboarding services for films, commercials, and digital content. Expert visual storytelling.',
        'h1': 'Professional Storyboarding Services',
        'tagline': 'Expert visual storytelling through detailed storyboards for all production types.',
        'category': 'Creative & Development'
    },
    'concept-development': {
        'title': 'Concept Development Services | Creative Ideation | NEEDaFIXER',
        'meta_desc': 'Professional concept development services for films, commercials, and digital content. Creative ideation experts.',
        'h1': 'Concept Development Services',
        'tagline': 'Creative ideation and concept development for compelling visual narratives.',
        'category': 'Creative & Development'
    },
    'creative-direction': {
        'title': 'Creative Direction Services | Artistic Vision | NEEDaFIXER',
        'meta_desc': 'Professional creative direction services for films, commercials, and digital content. Artistic vision experts.',
        'h1': 'Creative Direction Services',
        'tagline': 'Artistic vision and creative leadership for exceptional visual storytelling.',
        'category': 'Creative & Development'
    },
    'moodboard-creation': {
        'title': 'Moodboard & Lookbook Creation | Visual Style Guides | NEEDaFIXER',
        'meta_desc': 'Professional moodboard and lookbook creation services. Visual style guides for productions.',
        'h1': 'Moodboard & Lookbook Creation',
        'tagline': 'Visual style guides and aesthetic direction for your production.',
        'category': 'Creative & Development'
    },
    'pitch-deck-design': {
        'title': 'Pitch Deck & Treatment Design | Presentation Services | NEEDaFIXER',
        'meta_desc': 'Professional pitch deck and treatment design services. Compelling presentations for your projects.',
        'h1': 'Pitch Deck & Treatment Design',
        'tagline': 'Compelling presentations and treatments to secure funding and partnerships.',
        'category': 'Creative & Development'
    },
    
    # Casting & Talent
    'casting-services': {
        'title': 'Casting Services | Actors, Models, Extras | NEEDaFIXER',
        'meta_desc': 'Professional casting services for actors, models, and extras. Global talent casting for all productions.',
        'h1': 'Casting Services',
        'tagline': 'Professional casting for actors, models, and extras across all production types.',
        'category': 'Casting & Talent'
    },
    'voiceover-casting': {
        'title': 'Voiceover Casting Services | Professional Voice Talent | NEEDaFIXER',
        'meta_desc': 'Professional voiceover casting services. Expert voice talent for commercials, films, and digital content.',
        'h1': 'Voiceover Casting Services',
        'tagline': 'Expert voice talent casting for commercials, films, and digital content.',
        'category': 'Casting & Talent'
    },
    'talent-coordination': {
        'title': 'Talent Coordination Services | Artist Management | NEEDaFIXER',
        'meta_desc': 'Professional talent coordination services. Expert artist management for productions worldwide.',
        'h1': 'Talent Coordination Services',
        'tagline': 'Expert coordination and management of talent throughout production.',
        'category': 'Casting & Talent'
    },
    'union-talent-management': {
        'title': 'Union & Non-Union Talent Management | Professional Services | NEEDaFIXER',
        'meta_desc': 'Professional union and non-union talent management services. Expert handling of talent agreements.',
        'h1': 'Union & Non-Union Talent Management',
        'tagline': 'Expert management of union and non-union talent agreements and coordination.',
        'category': 'Casting & Talent'
    },
    
    # Location & Permits
    'location-scouting-services': {
        'title': 'Location Scouting Services | Perfect Filming Locations | NEEDaFIXER',
        'meta_desc': 'Professional location scouting services. Find perfect filming locations worldwide for your production.',
        'h1': 'Location Scouting Services',
        'tagline': 'Find perfect filming locations worldwide for your production needs.',
        'category': 'Location & Permits'
    },
    'location-management': {
        'title': 'Location Management Services | On-Site Coordination | NEEDaFIXER',
        'meta_desc': 'Professional location management services. Expert on-site coordination for filming locations.',
        'h1': 'Location Management Services',
        'tagline': 'Expert on-site coordination and management of filming locations.',
        'category': 'Location & Permits'
    },
    'film-permit-acquisition': {
        'title': 'Film Permit Acquisition | Licensing Services | NEEDaFIXER',
        'meta_desc': 'Professional film permit acquisition services. Expert licensing and permit handling worldwide.',
        'h1': 'Film Permit Acquisition',
        'tagline': 'Expert acquisition of filming permits and licenses worldwide.',
        'category': 'Location & Permits'
    },
    'site-surveys': {
        'title': 'Site Surveys & Tech Scouting | Location Assessment | NEEDaFIXER',
        'meta_desc': 'Professional site surveys and tech scouting services. Comprehensive location assessment for productions.',
        'h1': 'Site Surveys & Tech Scouting',
        'tagline': 'Comprehensive technical assessment and surveying of filming locations.',
        'category': 'Location & Permits'
    },
    'production-insurance': {
        'title': 'Production Insurance Services | Coverage Solutions | NEEDaFIXER',
        'meta_desc': 'Professional production insurance services. Comprehensive coverage solutions for film productions.',
        'h1': 'Production Insurance Services',
        'tagline': 'Comprehensive insurance coverage and risk management for productions.',
        'category': 'Location & Permits'
    },

    # Budgeting & Scheduling
    'production-budgeting': {
        'title': 'Production Budgeting Services | Cost Management | NEEDaFIXER',
        'meta_desc': 'Professional production budgeting services. Expert cost management and financial planning.',
        'h1': 'Production Budgeting Services',
        'tagline': 'Expert financial planning and budget management for productions.',
        'category': 'Budgeting & Scheduling'
    },
    'cost-estimation': {
        'title': 'Cost Estimation Services | Budget Planning | NEEDaFIXER',
        'meta_desc': 'Professional cost estimation services. Accurate budget planning and cost analysis.',
        'h1': 'Cost Estimation Services',
        'tagline': 'Accurate cost analysis and budget estimation for all production types.',
        'category': 'Budgeting & Scheduling'
    },
    'production-scheduling': {
        'title': 'Production Scheduling Services | Timeline Management | NEEDaFIXER',
        'meta_desc': 'Professional production scheduling services. Expert timeline management and coordination.',
        'h1': 'Production Scheduling Services',
        'tagline': 'Expert timeline management and production coordination services.',
        'category': 'Budgeting & Scheduling'
    },
    'call-sheets': {
        'title': 'Call Sheets & Shooting Schedules | Production Coordination | NEEDaFIXER',
        'meta_desc': 'Professional call sheet and shooting schedule services. Expert production coordination.',
        'h1': 'Call Sheets & Shooting Schedules',
        'tagline': 'Professional call sheets and detailed shooting schedule coordination.',
        'category': 'Budgeting & Scheduling'
    },

    # Crew & Logistics
    'line-producing-services': {
        'title': 'Line Producing Services | Production Management | NEEDaFIXER',
        'meta_desc': 'Professional line producing services. Expert production management and coordination.',
        'h1': 'Line Producing Services',
        'tagline': 'Expert production management and line producing for all project types.',
        'category': 'Crew & Logistics'
    },
    'crew-hiring': {
        'title': 'Crew Hiring & Coordination | Professional Film Crew | NEEDaFIXER',
        'meta_desc': 'Professional crew hiring and coordination services. Expert film crew recruitment worldwide.',
        'h1': 'Crew Hiring & Coordination',
        'tagline': 'Professional film crew recruitment and coordination worldwide.',
        'category': 'Crew & Logistics'
    },
    'fixer-services-local': {
        'title': 'Local Fixer Services | Production Support | NEEDaFIXER',
        'meta_desc': 'Professional local fixer services. Expert production support and local coordination.',
        'h1': 'Local Fixer Services',
        'tagline': 'Expert local production support and coordination services worldwide.',
        'category': 'Crew & Logistics'
    },
    'travel-logistics': {
        'title': 'Travel & Accommodation Logistics | Production Travel | NEEDaFIXER',
        'meta_desc': 'Professional travel and accommodation logistics. Expert coordination for production travel.',
        'h1': 'Travel & Accommodation Logistics',
        'tagline': 'Expert coordination of travel and accommodation for productions.',
        'category': 'Crew & Logistics'
    },
    'equipment-planning': {
        'title': 'Equipment Planning Services | Production Gear | NEEDaFIXER',
        'meta_desc': 'Professional equipment planning services. Expert coordination of production gear and technology.',
        'h1': 'Equipment Planning Services',
        'tagline': 'Expert planning and coordination of production equipment and technology.',
        'category': 'Crew & Logistics'
    },
    'catering-services': {
        'title': 'Catering & On-Set Services | Production Catering | NEEDaFIXER',
        'meta_desc': 'Professional catering and on-set services. Expert coordination of production catering.',
        'h1': 'Catering & On-Set Services',
        'tagline': 'Professional catering and on-set service coordination for productions.',
        'category': 'Crew & Logistics'
    },

    # Legal & Administrative
    'contract-management': {
        'title': 'Contract Management Services | Legal Documentation | NEEDaFIXER',
        'meta_desc': 'Professional contract management services. Expert handling of legal documentation.',
        'h1': 'Contract Management Services',
        'tagline': 'Expert management of contracts and legal documentation for productions.',
        'category': 'Legal & Administrative'
    },
    'talent-releases': {
        'title': 'Talent Releases & Agreements | Legal Documentation | NEEDaFIXER',
        'meta_desc': 'Professional talent release and agreement services. Expert legal documentation handling.',
        'h1': 'Talent Releases & Agreements',
        'tagline': 'Professional handling of talent releases and legal agreements.',
        'category': 'Legal & Administrative'
    },
    'location-agreements': {
        'title': 'Location Agreements & Contracts | Legal Services | NEEDaFIXER',
        'meta_desc': 'Professional location agreement and contract services. Expert legal documentation.',
        'h1': 'Location Agreements & Contracts',
        'tagline': 'Expert handling of location agreements and legal contracts.',
        'category': 'Legal & Administrative'
    },
    'licensing-rights': {
        'title': 'Licensing & Rights Management | Intellectual Property | NEEDaFIXER',
        'meta_desc': 'Professional licensing and rights management services. Expert intellectual property handling.',
        'h1': 'Licensing & Rights Management',
        'tagline': 'Expert management of licensing and intellectual property rights.',
        'category': 'Legal & Administrative'
    },
    'covid-compliance': {
        'title': 'COVID-19 Compliance & Protocols | Safety Services | NEEDaFIXER',
        'meta_desc': 'Professional COVID-19 compliance and protocol services. Expert safety coordination.',
        'h1': 'COVID-19 Compliance & Protocols',
        'tagline': 'Expert COVID-19 safety protocols and compliance coordination.',
        'category': 'Legal & Administrative'
    }
}

def create_page_content(service_key, service_data):
    """Create HTML content for a pre-production service page"""
    
    current_page_path = f'/pre-production-services/{service_key}/'
    
    return f'''<!DOCTYPE html>
<html lang="en-US" itemscope itemtype="http://schema.org/WebPage">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- SEO Meta Tags -->
    <title>{service_data['title']}</title>
    <meta name="description" content="{service_data['meta_desc']}">
    <meta name="keywords" content="{service_key.replace('-', ' ')}, pre-production services, film production, {service_data['category'].lower()}">
    <meta name="author" content="NEEDaFIXER">
    
    <!-- Geographic Meta Tags -->
    <meta name="geo.region" content="GLOBAL">
    <meta name="geo.placename" content="Worldwide">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:locale" content="en_US">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{service_data['title']}">
    <meta property="og:description" content="{service_data['meta_desc']}">
    <meta property="og:url" content="{current_page_path}">
    <meta property="og:site_name" content="NEEDaFIXER">
    <meta property="og:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="{current_page_path}">
    
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
            background-image: url('/wp-content/uploads/2015/10/VIETNAM-home-main-banner.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        
        /* Mega Menu Styles */
        .mega-menu {{
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: #1a1a1a;
            border-top: 2px solid #ff6b35;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            opacity: 0;
            visibility: hidden;
            transform: translateY(-10px);
            transition: all 0.3s ease;
            z-index: 50;
        }}
        
        .mega-menu-trigger:hover .mega-menu {{
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }}
        
        .mega-menu-column {{
            border-right: 1px solid #333;
        }}
        
        .mega-menu-column:last-child {{
            border-right: none;
        }}
    </style>
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "{service_data['h1']}",
        "description": "{service_data['meta_desc']}",
        "provider": {{
            "@type": "Organization",
            "name": "NEEDaFIXER",
            "url": "https://needafixer.com/"
        }},
        "serviceType": "{service_data['category']}",
        "areaServed": "Worldwide"
    }}
    </script>
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
    <header class="bg-vietnam-dark border-b border-gray-700 sticky top-0 z-40">
        <div class="container mx-auto px-4">
            <div class="flex items-center justify-between h-20">
                <!-- Logo -->
                <div class="flex-shrink-0">
                    <a href="/" class="flex items-center">
                        <img src="/wp-content/uploads/2016/10/needafixer-vietnam.png"
                             alt="NEEDaFIXER"
                             class="h-12 w-auto">
                    </a>
                </div>

                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center space-x-8" aria-label="Main navigation">
                    <a href="/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">HOME</a>
                    <a href="/about-us/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">ABOUT US</a>

                    <!-- Pre-Production Mega Menu -->
                    <div class="relative mega-menu-trigger">
                        <a href="/pre-production-services/" class="text-vietnam-orange hover:text-white transition-colors duration-200 flex items-center">
                            PRE-PRODUCTION
                            <svg class="ml-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="mega-menu">
                            <div class="container mx-auto px-4 py-8">
                                <div class="text-center mb-6">
                                    <h3 class="text-xl font-bold text-vietnam-orange">Pre-Production Services</h3>
                                    <p class="text-gray-400 text-sm">Planning, creative development, logistics</p>
                                </div>
                                <div class="grid grid-cols-6 gap-6">
                                    <!-- Creative & Development -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Creative & Development</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/scriptwriting/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Scriptwriting</a></li>
                                            <li><a href="/pre-production-services/script-consultation/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Script Consultation</a></li>
                                            <li><a href="/pre-production-services/storyboarding/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Storyboarding</a></li>
                                            <li><a href="/pre-production-services/concept-development/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Concept Development</a></li>
                                            <li><a href="/pre-production-services/creative-direction/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Creative Direction</a></li>
                                            <li><a href="/pre-production-services/moodboard-creation/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Moodboards</a></li>
                                            <li><a href="/pre-production-services/pitch-deck-design/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Pitch Decks</a></li>
                                        </ul>
                                    </div>

                                    <!-- Casting & Talent -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Casting & Talent</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/casting-services/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Casting Services</a></li>
                                            <li><a href="/pre-production-services/voiceover-casting/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Voiceover Casting</a></li>
                                            <li><a href="/pre-production-services/talent-coordination/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Talent Coordination</a></li>
                                            <li><a href="/pre-production-services/union-talent-management/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Union Management</a></li>
                                        </ul>
                                    </div>

                                    <!-- Location & Permits -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Location & Permits</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/location-scouting-services/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Location Scouting</a></li>
                                            <li><a href="/pre-production-services/location-management/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Location Management</a></li>
                                            <li><a href="/pre-production-services/film-permit-acquisition/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Permit Acquisition</a></li>
                                            <li><a href="/pre-production-services/site-surveys/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Site Surveys</a></li>
                                            <li><a href="/pre-production-services/production-insurance/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Production Insurance</a></li>
                                        </ul>
                                    </div>

                                    <!-- Budgeting & Scheduling -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Budgeting & Scheduling</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/production-budgeting/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Production Budgeting</a></li>
                                            <li><a href="/pre-production-services/cost-estimation/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Cost Estimation</a></li>
                                            <li><a href="/pre-production-services/production-scheduling/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Production Scheduling</a></li>
                                            <li><a href="/pre-production-services/call-sheets/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Call Sheets</a></li>
                                        </ul>
                                    </div>

                                    <!-- Crew & Logistics -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Crew & Logistics</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/line-producing-services/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Line Producing</a></li>
                                            <li><a href="/pre-production-services/crew-hiring/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Crew Hiring</a></li>
                                            <li><a href="/pre-production-services/fixer-services-local/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Local Fixers</a></li>
                                            <li><a href="/pre-production-services/travel-logistics/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Travel Logistics</a></li>
                                            <li><a href="/pre-production-services/equipment-planning/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Equipment Planning</a></li>
                                            <li><a href="/pre-production-services/catering-services/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Catering Services</a></li>
                                        </ul>
                                    </div>

                                    <!-- Legal & Administrative -->
                                    <div class="mega-menu-column">
                                        <h4 class="text-vietnam-orange font-semibold mb-3 text-sm">Legal & Administrative</h4>
                                        <ul class="space-y-2">
                                            <li><a href="/pre-production-services/contract-management/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Contract Management</a></li>
                                            <li><a href="/pre-production-services/talent-releases/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Talent Releases</a></li>
                                            <li><a href="/pre-production-services/location-agreements/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Location Agreements</a></li>
                                            <li><a href="/pre-production-services/licensing-rights/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">Licensing & Rights</a></li>
                                            <li><a href="/pre-production-services/covid-compliance/" class="text-gray-300 hover:text-vietnam-orange text-xs transition-colors">COVID Compliance</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

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
                            <a href="/corporate-video-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Corporate Video</a>
                            <a href="/equipment-transport-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Equipment Transport</a>
                            <a href="/translation-services-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Translation Services</a>
                            <a href="/casting-services-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Casting Services</a>
                            <a href="/post-production-vietnam/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Post-Production Services</a>
                            <a href="/hire-film-director/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Film Director</a>
                            <a href="/hire-film-producer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Film Producer</a>
                            <a href="/hire-line-producer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Line Producer</a>
                            <a href="/hire-fixer/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Fixer</a>
                            <a href="/hire-dop/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire DOP</a>
                            <a href="/hire-location-manager/" class="block px-4 py-3 text-sm text-vietnam-gray hover:text-vietnam-orange hover:bg-gray-800 transition-colors duration-200">Hire Location Manager</a>
                        </div>
                    </div>
                    <a href="/filming-in-vietnam/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">FILMING IN VIETNAM</a>
                    <a href="/portfolio/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">PORTFOLIO</a>
                    <a href="/contact/" class="text-vietnam-gray hover:text-vietnam-orange transition-colors duration-200">CONTACT</a>
                </nav>'''

def main():
    """Create all pre-production service pages"""
    print("🚀 Creating pre-production service pages...")
    
    created_count = 0
    for service_key, service_data in PREPRODUCTION_SERVICES.items():
        try:
            page_content = create_page_content(service_key, service_data)
            
            # Create the page file
            page_path = f'pre-production-services/{service_key}/index.html'
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(page_content)
            
            print(f"✅ Created {page_path}")
            created_count += 1
            
        except Exception as e:
            print(f"❌ Error creating {service_key}: {e}")
    
    print(f"\n📊 Created {created_count}/{len(PREPRODUCTION_SERVICES)} pages")
    print("🎉 Pre-production pages creation completed!")

if __name__ == "__main__":
    main()
