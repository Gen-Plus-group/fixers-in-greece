#!/usr/bin/env python3
"""
Create Content Production Services pages for Fixers in Vietnam website
"""

import os
import re

# Define page directories and their corresponding SEO content
PAGE_DIRS = {
    "TV Shows & Broadcast Series": "tv-shows-broadcast-series",
    "Feature Films": "feature-films",
    "Drama Series": "drama-series",
    "Commercials & Advertising Campaigns": "commercials-advertising",
    "Corporate Videos & Internal Communications": "corporate-videos",
    "Documentaries & Docuseries": "documentaries-docuseries",
    "Social Media Content & Influencer Videos": "social-media-content",
    "Narrative Films & Web Series": "narrative-films-web-series",
    "Music Videos": "music-videos",
    "Fashion Videos": "fashion-videos",
    "Travel, Lifestyle & Destination Marketing": "travel-lifestyle-marketing",
    "Hotel Videos & Reels": "hotel-videos-reels",
    "Cookery Shows & Food Content": "cookery-shows-food-content",
    "Talk Shows & Panel Shows": "talk-shows-panel-shows",
    "Competition & Reality Shows": "competition-reality-shows",
    "Live Events & Brand Activations": "live-events-brand-activations",
    "Educational, Explainer & eLearning Videos": "educational-explainer-videos"
}

# SEO Keywords for each service
SEO_KEYWORDS = {
    "TV Shows & Broadcast Series": "tv show production company, television series filming services, scripted tv production crew, unscripted tv filming, drama tv show production, live-to-tape studio filming, multi-camera tv show crew, episodic series filming, reality tv production services, broadcast production company, studio set crew, entertainment show filming, international tv logistics, tv show post-production",
    "Feature Films": "feature film production company, film production services, full-length film crew, cinematic film production, international film co-production, indie feature film support, theatrical release production, script-to-screen services",
    "Drama Series": "drama series production services, episodic drama filming, streaming series crew hire, scripted series production, drama show cinematography, production support for drama shows",
    "Commercials & Advertising Campaigns": "tv commercial production company, commercial video production services, branded content agency, online ad video production, campaign video services, promo video production, viral ad creators, product launch videos",
    "Corporate Videos & Internal Communications": "corporate video production, company profile video, internal communication videos, executive interview filming, business case studies, b2b video content, training video production",
    "Documentaries & Docuseries": "documentary film production, docuseries video crew, social impact film production, ngo video content, biographical documentaries, cinematic docu storytelling",
    "Social Media Content & Influencer Videos": "social media video production, influencer video creators, tiktok & reels production, vertical content editing, viral social video agency",
    "Narrative Films & Web Series": "narrative film production, indie film production crew, short film video team, web series filming services, script-to-screen production, low-budget film crew hire",
    "Music Videos": "music video production, artist video crew, live music filming, concert visuals, creative music video director, music performance shoot",
    "Fashion Videos": "fashion video production, runway filming, fashion campaign video, editorial lookbook filming, bts fashion content creators",
    "Travel, Lifestyle & Destination Marketing": "travel video production, lifestyle video production, destination marketing films, tourism video services, cultural travel content, destination branding agency",
    "Hotel Videos & Reels": "hotel video production, hotel reels agency, hospitality promo videos, luxury hotel content, social media reels for resorts",
    "Cookery Shows & Food Content": "cooking show production, recipe video filming, celebrity chef video content, branded food videos, tabletop filming services, culinary TV content",
    "Talk Shows & Panel Shows": "talk show production, panel show filming, live studio audience filming, multi-camera talk show services, late-night tv production",
    "Competition & Reality Shows": "reality tv filming, competition show crew, game show production, unscripted tv support, reality show logistics, reality series filming",
    "Live Events & Brand Activations": "brand activation video production, experiential marketing video, product launch events, event recap videos, branded live experience filming",
    "Educational, Explainer & eLearning Videos": "explainer video agency, educational video services, elearning content production, corporate training video production, instructional design videos"
}

# CTA Text for each service
CTA_TEXT = {
    "TV Shows & Broadcast Series": "Explore Full-Service TV Show Production Services",
    "Feature Films": "Find Your Feature Film Production Service Company",
    "Drama Series": "Get Production Support for Your Drama Series",
    "Commercials & Advertising Campaigns": "Find your High-Impact Commercial Video Producer",
    "Corporate Videos & Internal Communications": "Corporate Video Services for Business Impact",
    "Documentaries & Docuseries": "Tell Powerful Stories with Documentary Production Services",
    "Social Media Content & Influencer Videos": "Create Engaging Social Media Videos",
    "Narrative Films & Web Series": "Produce Your Narrative Film or Web Series",
    "Music Videos": "Bring Your Music Video to Life",
    "Fashion Videos": "Create Beautiful Fashion Content",
    "Travel, Lifestyle & Destination Marketing": "Capture Stunning Travel & Lifestyle Visuals",
    "Hotel Videos & Reels": "Promote Your Hotel with Video",
    "Cookery Shows & Food Content": "Produce Engaging Food & Cookery Content",
    "Talk Shows & Panel Shows": "Book Studio + Crew for Talk or Panel Shows",
    "Competition & Reality Shows": "Launch Your Reality or Competition Format",
    "Live Events & Brand Activations": "Capture Your Live Event or Activation",
    "Educational, Explainer & eLearning Videos": "Create Professional Educational Videos"
}

# Service descriptions
SERVICE_DESCRIPTIONS = {
    "TV Shows & Broadcast Series": "From scripted dramas to unscripted reality shows, talk shows to game shows, our comprehensive TV production services handle everything from pre-production through post. We specialize in multi-camera setups, live-to-tape recordings, and episodic content for both traditional broadcast and streaming platforms.",
    "Feature Films": "Complete feature film production services for studio-backed and independent productions. Our experienced crews support international co-productions, theatrical releases, and streaming platform features with full script-to-screen capabilities.",
    "Drama Series": "Expert production services for scripted episodic content. Whether for traditional TV or streaming platforms, we provide specialized crews experienced in drama production, from period pieces to contemporary series.",
    "Commercials & Advertising Campaigns": "High-impact commercial production for TV, digital, and social media campaigns. We create branded content that drives engagement, from product launches to viral marketing campaigns.",
    "Corporate Videos & Internal Communications": "Professional corporate video production services including company profiles, internal communications, training videos, and B2B content that effectively communicates your business message.",
    "Documentaries & Docuseries": "Compelling documentary production for long-form films, docuseries, and social impact storytelling. We specialize in cinematic documentary techniques for NGOs, biographical films, and investigative series.",
    "Social Media Content & Influencer Videos": "Dynamic content creation for all social platforms including Instagram Reels, TikTok, YouTube Shorts, and influencer collaborations. We understand vertical video formats and viral content strategies.",
    "Narrative Films & Web Series": "Complete production services for short films, indie projects, and web-first scripted series. We support creative storytelling with flexible crews for projects of all sizes.",
    "Music Videos": "Creative music video production for artists, bands, and labels. From performance shoots to conceptual narratives, we bring musical visions to life with innovative cinematography.",
    "Fashion Videos": "Sophisticated fashion video production including runway shows, campaign videos, lookbooks, and behind-the-scenes content that captures the essence of fashion brands.",
    "Travel, Lifestyle & Destination Marketing": "Stunning travel and lifestyle content production for tourism boards, destinations, and lifestyle brands. We create compelling visual stories that inspire and engage audiences.",
    "Hotel Videos & Reels": "Professional hospitality video production showcasing resorts, hotels, and amenities. We create engaging content for websites and social media that drives bookings.",
    "Cookery Shows & Food Content": "Appetizing food content production from cooking shows to branded recipe videos. Our specialized tabletop filming and culinary production expertise brings food stories to life.",
    "Talk Shows & Panel Shows": "Complete talk show and panel production services with multi-camera capabilities, studio setups, and live audience management for engaging conversational content.",
    "Competition & Reality Shows": "Dynamic production services for reality TV, competition formats, and game shows. We handle the complex logistics of unscripted content with experienced crews.",
    "Live Events & Brand Activations": "Real-time event coverage and brand activation video production. We capture the energy of live experiences, from product launches to experiential marketing campaigns.",
    "Educational, Explainer & eLearning Videos": "Clear, engaging educational content production including explainer videos, eLearning modules, and training materials that effectively communicate complex information."
}

def create_service_grid_items(service_name, all_services):
    """Generate related service grid items"""
    items = []
    # Get 3 related services (excluding the current one)
    related_services = [s for s in all_services if s != service_name][:3]
    
    for related in related_services:
        dir_name = PAGE_DIRS[related]
        items.append(f'''
                        <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6 hover:border-vietnam-orange transition-all duration-200 group">
                            <h3 class="text-xl font-bold text-vietnam-orange mb-3 group-hover:text-yellow-400 transition-colors">
                                {related}
                            </h3>
                            <p class="text-gray-300 mb-4 text-sm">
                                Professional {related.lower()} production services with experienced crews and cutting-edge equipment.
                            </p>
                            <a href="/content-production/{dir_name}/" 
                               class="inline-flex items-center text-vietnam-orange hover:text-yellow-400 transition-colors duration-200 font-medium">
                                Learn More
                                <svg class="ml-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                                </svg>
                            </a>
                        </div>''')
    
    return '\n'.join(items)

def create_page_content(service_name):
    """Create the HTML content for a service page"""
    dir_name = PAGE_DIRS[service_name]
    keywords = SEO_KEYWORDS[service_name]
    cta_text = CTA_TEXT[service_name]
    description = SERVICE_DESCRIPTIONS[service_name]
    
    # Generate title without special characters for SEO
    clean_title = service_name.replace('&', 'and')
    
    # Get all services for the related services grid
    all_services = list(PAGE_DIRS.keys())
    service_grid = create_service_grid_items(service_name, all_services)
    
    html_content = f'''<!DOCTYPE html>
<html lang="en-US" itemscope itemtype="http://schema.org/WebPage">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- SEO Meta Tags -->
    <title>{clean_title} Production | Professional Video Services | NEEDaFIXER</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="NEEDaFIXER">
    
    <!-- Geographic Meta Tags -->
    <meta name="geo.region" content="VN">
    <meta name="geo.placename" content="Vietnam">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:locale" content="en_US">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{clean_title} Production | Professional Video Services">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="/content-production/{dir_name}/">
    <meta property="og:site_name" content="NEEDaFIXER">
    <meta property="og:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{clean_title} Production Services">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="/content-production/{dir_name}/">
    
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
    </style>
</head>

<body class="bg-vietnam-darker text-white font-sans">
    <!-- Skip to Content -->
    <a href="#main-content" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 bg-vietnam-orange text-black px-4 py-2 rounded-md z-50">
        Skip to Main Content
    </a>

    <!-- Dynamic Header Container -->
    <div id="header-container">
        <!-- Header will be loaded here dynamically -->
    </div>

    <!-- Main Content -->
    <main id="main-content">
        <!-- Hero Section -->
        <section class="page-hero-bg relative py-20 md:py-32">
            <div class="absolute inset-0 bg-black bg-opacity-60"></div>
            <div class="relative z-10 container mx-auto px-4 text-center">
                <h1 class="text-4xl md:text-6xl font-bold text-vietnam-orange mb-4">
                    {service_name}
                </h1>
                <p class="text-xl text-gray-200 max-w-3xl mx-auto">
                    {description}
                </p>
            </div>
        </section>

        <!-- Service Details Section -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="max-w-4xl mx-auto">
                    <!-- Service Overview -->
                    <div class="mb-12">
                        <h2 class="text-3xl font-bold text-vietnam-orange mb-6">Professional {service_name} Production</h2>
                        <div class="prose prose-lg text-gray-300">
                            <p class="mb-6">
                                Our {service_name.lower()} production services combine creative excellence with technical expertise to deliver content that engages audiences and achieves your objectives. With experienced crews and state-of-the-art equipment, we handle projects of all scales throughout Vietnam and Southeast Asia.
                            </p>
                            <p class="mb-6">
                                From concept development through final delivery, our comprehensive production services ensure your vision is realized with the highest production values. We understand the unique requirements of {service_name.lower()} and bring specialized expertise to every project.
                            </p>
                        </div>
                    </div>

                    <!-- Key Services -->
                    <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-8 mb-12">
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-6">Our {service_name} Services Include:</h3>
                        <div class="grid md:grid-cols-2 gap-4">
                            <ul class="space-y-3">
                                <li class="flex items-start">
                                    <svg class="h-6 w-6 text-vietnam-orange mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                    <span>Creative concept development</span>
                                </li>
                                <li class="flex items-start">
                                    <svg class="h-6 w-6 text-vietnam-orange mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                    <span>Pre-production planning</span>
                                </li>
                                <li class="flex items-start">
                                    <svg class="h-6 w-6 text-vietnam-orange mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                    <span>Professional crew and equipment</span>
                                </li>
                                <li class="flex items-start">
                                    <svg class="h-6 w-6 text-vietnam-orange mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                    <span>Location scouting and permits</span>
                                </li>
                            </ul>
                            <ul class="space-y-3">
                                <li class="flex items-start">
                                    <svg class="h-6 w-6 text-vietnam-orange mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                    <span>Multi-camera production</span>
                                </li>
                                <li class="flex items-start">
                                    <svg class="h-6 w-6 text-vietnam-orange mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                    <span>Post-production services</span>
                                </li>
                                <li class="flex items-start">
                                    <svg class="h-6 w-6 text-vietnam-orange mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                    <span>Color grading and sound design</span>
                                </li>
                                <li class="flex items-start">
                                    <svg class="h-6 w-6 text-vietnam-orange mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                    <span>Final delivery in any format</span>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <!-- Why Choose Us -->
                    <div class="mb-12">
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-6">Why Choose Our {service_name} Production Services?</h3>
                        <div class="grid md:grid-cols-3 gap-6">
                            <div class="text-center">
                                <div class="bg-vietnam-orange text-black rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                                    <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </div>
                                <h4 class="text-lg font-semibold mb-2">Experienced Teams</h4>
                                <p class="text-gray-400">Specialized crews with extensive {service_name.lower()} production experience</p>
                            </div>
                            <div class="text-center">
                                <div class="bg-vietnam-orange text-black rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                                    <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                                    </svg>
                                </div>
                                <h4 class="text-lg font-semibold mb-2">Latest Technology</h4>
                                <p class="text-gray-400">State-of-the-art equipment for superior production quality</p>
                            </div>
                            <div class="text-center">
                                <div class="bg-vietnam-orange text-black rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                                    <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </div>
                                <h4 class="text-lg font-semibold mb-2">On-Time Delivery</h4>
                                <p class="text-gray-400">Reliable production schedules that meet your deadlines</p>
                            </div>
                        </div>
                    </div>

                    <!-- Related Services -->
                    <div class="mb-12">
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-6">Related Content Production Services</h3>
                        <div class="grid md:grid-cols-3 gap-6">
                            {service_grid}
                        </div>
                    </div>

                    <!-- CTA Section -->
                    <div class="bg-gradient-to-r from-vietnam-orange to-yellow-500 rounded-lg p-8 text-center">
                        <h3 class="text-2xl font-bold text-black mb-4">
                            Ready to Start Your {service_name} Project?
                        </h3>
                        <p class="text-black mb-6 text-lg">
                            Let's discuss how our production expertise can bring your vision to life.
                        </p>
                        <a href="/contact/" 
                           class="inline-block bg-black text-white px-8 py-3 rounded-md font-semibold hover:bg-gray-800 transition-colors duration-200">
                            {cta_text}
                        </a>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Dynamic Footer Container -->
    <div id="footer-container">
        <!-- Footer will be loaded here dynamically -->
    </div>

    <!-- Component Loader Script -->
    <script src="/js/component-loader.js"></script>
</body>
</html>'''
    
    return html_content

def create_content_production_main_page():
    """Create the main content production category page"""
    
    # Generate service grid for main page
    service_items = []
    for service_name, dir_name in PAGE_DIRS.items():
        keywords = SEO_KEYWORDS[service_name]
        short_desc = keywords.split(',')[0]
        
        service_items.append(f'''
                        <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-6 hover:border-vietnam-orange transition-all duration-200 group hover:transform hover:scale-105">
                            <h3 class="text-xl font-bold text-vietnam-orange mb-3 group-hover:text-yellow-400 transition-colors">
                                {service_name}
                            </h3>
                            <p class="text-gray-300 mb-4 text-sm">
                                Professional {short_desc} with experienced crews and cutting-edge equipment.
                            </p>
                            <a href="/content-production/{dir_name}/" 
                               class="inline-flex items-center text-vietnam-orange hover:text-yellow-400 transition-colors duration-200 font-medium">
                                Learn More
                                <svg class="ml-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                                </svg>
                            </a>
                        </div>''')
    
    services_grid = '\n'.join(service_items)
    
    html_content = f'''<!DOCTYPE html>
<html lang="en-US" itemscope itemtype="http://schema.org/WebPage">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- SEO Meta Tags -->
    <title>Content Production Services | TV, Film, Commercial & Digital | NEEDaFIXER</title>
    <meta name="description" content="Comprehensive content production services including TV shows, feature films, commercials, corporate videos, documentaries, social media content, and more. Professional crews and equipment throughout Vietnam.">
    <meta name="keywords" content="content production services, tv production company, film production services, commercial video production, corporate video production, documentary production, social media video production, Vietnam production services">
    <meta name="author" content="NEEDaFIXER">
    
    <!-- Geographic Meta Tags -->
    <meta name="geo.region" content="VN">
    <meta name="geo.placename" content="Vietnam">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:locale" content="en_US">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Content Production Services | Professional Video Production">
    <meta property="og:description" content="Complete content production services for TV, film, commercial, and digital projects. Expert crews and cutting-edge equipment.">
    <meta property="og:url" content="/content-production/">
    <meta property="og:site_name" content="NEEDaFIXER">
    <meta property="og:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="Content Production Services">
    <meta name="twitter:description" content="Professional content production for TV, film, commercial, and digital projects.">
    <meta name="twitter:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="/content-production/">
    
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
    </style>
</head>

<body class="bg-vietnam-darker text-white font-sans">
    <!-- Skip to Content -->
    <a href="#main-content" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 bg-vietnam-orange text-black px-4 py-2 rounded-md z-50">
        Skip to Main Content
    </a>

    <!-- Dynamic Header Container -->
    <div id="header-container">
        <!-- Header will be loaded here dynamically -->
    </div>

    <!-- Main Content -->
    <main id="main-content">
        <!-- Hero Section -->
        <section class="page-hero-bg relative py-20 md:py-32">
            <div class="absolute inset-0 bg-black bg-opacity-60"></div>
            <div class="relative z-10 container mx-auto px-4 text-center">
                <h1 class="text-4xl md:text-6xl font-bold text-vietnam-orange mb-4">
                    Content Production Services
                </h1>
                <p class="text-xl text-gray-200 max-w-3xl mx-auto">
                    Comprehensive production services for TV, film, commercial, and digital content. From concept to delivery, we bring your vision to life with professional crews and state-of-the-art equipment.
                </p>
            </div>
        </section>

        <!-- Introduction Section -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="max-w-4xl mx-auto text-center mb-12">
                    <h2 class="text-3xl font-bold text-vietnam-orange mb-6">Full-Service Content Production</h2>
                    <p class="text-lg text-gray-300 mb-6">
                        Whether you're producing a TV series, feature film, commercial campaign, or digital content, our comprehensive production services cover every aspect of your project. With experienced crews, cutting-edge equipment, and deep local knowledge, we ensure smooth, efficient productions that deliver exceptional results.
                    </p>
                    <p class="text-lg text-gray-300">
                        From scripted dramas to unscripted reality shows, from viral social media content to cinematic documentaries, we have the expertise and resources to handle productions of any scale throughout Vietnam and Southeast Asia.
                    </p>
                </div>

                <!-- Services Grid -->
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
                    {services_grid}
                </div>

                <!-- Why Choose Us Section -->
                <div class="bg-vietnam-dark border border-gray-700 rounded-lg p-8 mb-12">
                    <h3 class="text-2xl font-bold text-vietnam-orange mb-6 text-center">Why Choose Our Content Production Services?</h3>
                    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                        <div class="text-center">
                            <div class="bg-vietnam-orange text-black rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                                <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"></path>
                                </svg>
                            </div>
                            <h4 class="text-lg font-semibold mb-2">17+ Content Types</h4>
                            <p class="text-gray-400 text-sm">From TV shows to social media, we produce all content formats</p>
                        </div>
                        <div class="text-center">
                            <div class="bg-vietnam-orange text-black rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                                <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
                                </svg>
                            </div>
                            <h4 class="text-lg font-semibold mb-2">Expert Crews</h4>
                            <p class="text-gray-400 text-sm">Specialized teams for each production type</p>
                        </div>
                        <div class="text-center">
                            <div class="bg-vietnam-orange text-black rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                                <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                </svg>
                            </div>
                            <h4 class="text-lg font-semibold mb-2">End-to-End Service</h4>
                            <p class="text-gray-400 text-sm">From concept development to final delivery</p>
                        </div>
                        <div class="text-center">
                            <div class="bg-vietnam-orange text-black rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                                <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                </svg>
                            </div>
                            <h4 class="text-lg font-semibold mb-2">Vietnam & Beyond</h4>
                            <p class="text-gray-400 text-sm">Local expertise with international standards</p>
                        </div>
                    </div>
                </div>

                <!-- CTA Section -->
                <div class="bg-gradient-to-r from-vietnam-orange to-yellow-500 rounded-lg p-8 text-center max-w-4xl mx-auto">
                    <h3 class="text-2xl font-bold text-black mb-4">
                        Ready to Create Exceptional Content?
                    </h3>
                    <p class="text-black mb-6 text-lg">
                        Whatever your content production needs, we have the expertise and resources to deliver outstanding results.
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 justify-center">
                        <a href="/contact/" 
                           class="inline-block bg-black text-white px-8 py-3 rounded-md font-semibold hover:bg-gray-800 transition-colors duration-200">
                            Start Your Project
                        </a>
                        <a href="tel:+442085492259" 
                           class="inline-block bg-white text-black px-8 py-3 rounded-md font-semibold hover:bg-gray-100 transition-colors duration-200">
                            Call +44 (0) 20 8549 2259
                        </a>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Dynamic Footer Container -->
    <div id="footer-container">
        <!-- Footer will be loaded here dynamically -->
    </div>

    <!-- Component Loader Script -->
    <script src="/js/component-loader.js"></script>
</body>
</html>'''
    
    return html_content

def main():
    # Create content-production directory
    base_dir = "content-production"
    os.makedirs(base_dir, exist_ok=True)
    
    # Create main content production page
    main_page_content = create_content_production_main_page()
    with open(os.path.join(base_dir, "index.html"), 'w', encoding='utf-8') as f:
        f.write(main_page_content)
    print("Created main content production page")
    
    # Create individual service pages
    for service_name, dir_name in PAGE_DIRS.items():
        # Create service directory
        service_dir = os.path.join(base_dir, dir_name)
        os.makedirs(service_dir, exist_ok=True)
        
        # Create service page
        page_content = create_page_content(service_name)
        with open(os.path.join(service_dir, "index.html"), 'w', encoding='utf-8') as f:
            f.write(page_content)
        
        print(f"Created {service_name} page")
    
    print(f"\n✅ Successfully created {len(PAGE_DIRS) + 1} content production pages!")

if __name__ == "__main__":
    main()