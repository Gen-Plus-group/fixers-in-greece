#!/usr/bin/env python3
"""
Script to create the remaining three pages: Fixer, DOP, and Location Manager
"""

import os

def create_fixer_page():
    """Create the Hire Fixer page"""
    content = '''<!DOCTYPE html>
<html lang="en-US" itemscope itemtype="http://schema.org/WebPage">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- SEO Meta Tags -->
    <title>Hire a Fixer | Global In-House & Vetted Local Experts | NEEDaFIXER</title>
    <meta name="description" content="NEEDaFIXER offers fixers globally with full production support in 100+ countries.">
    <meta name="keywords" content="hire fixer, local fixer, production fixer, film fixer, global fixer services">
    <meta name="author" content="NEEDaFIXER">
    
    <!-- Geographic Meta Tags -->
    <meta name="geo.region" content="GLOBAL">
    <meta name="geo.placename" content="Worldwide">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:locale" content="en_US">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Hire a Fixer | Global In-House & Vetted Local Experts | NEEDaFIXER">
    <meta property="og:description" content="NEEDaFIXER offers fixers globally with full production support in 100+ countries.">
    <meta property="og:url" content="/hire-fixer/">
    <meta property="og:site_name" content="NEEDaFIXER">
    <meta property="og:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="/hire-fixer/">
    
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
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-FD4LC3V4DB');
    </script>

    <!-- Custom Styles -->
    <style>
        .page-hero-bg {
            background-image: url('/wp-content/uploads/2015/10/VIETNAM-home-main-banner.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Fixer Hiring Services",
        "description": "Global fixer services providing local expertise, permits, crew, and production support in 100+ countries.",
        "provider": {
            "@type": "Organization",
            "name": "NEEDaFIXER",
            "url": "https://needafixer.com/"
        },
        "serviceType": "Fixer Services",
        "areaServed": "Worldwide"
    }
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
    </div>'''
    
    with open('hire-fixer/index.html', 'w', encoding='utf-8') as f:
        f.write(content)

def create_dop_page():
    """Create the Hire DOP page"""
    content = '''<!DOCTYPE html>
<html lang="en-US" itemscope itemtype="http://schema.org/WebPage">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- SEO Meta Tags -->
    <title>Hire a DOP | Global Cinematography Experts | NEEDaFIXER</title>
    <meta name="description" content="NEEDaFIXER provides expert DOPs globally for cinematic features, TV, commercials, and more.">
    <meta name="keywords" content="hire DOP, director of photography, cinematographer, camera operator, film DOP">
    <meta name="author" content="NEEDaFIXER">
    
    <!-- Geographic Meta Tags -->
    <meta name="geo.region" content="GLOBAL">
    <meta name="geo.placename" content="Worldwide">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:locale" content="en_US">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Hire a DOP | Global Cinematography Experts | NEEDaFIXER">
    <meta property="og:description" content="NEEDaFIXER provides expert DOPs globally for cinematic features, TV, commercials, and more.">
    <meta property="og:url" content="/hire-dop/">
    <meta property="og:site_name" content="NEEDaFIXER">
    <meta property="og:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="/hire-dop/">
    
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
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-FD4LC3V4DB');
    </script>

    <!-- Custom Styles -->
    <style>
        .page-hero-bg {
            background-image: url('/wp-content/uploads/2015/10/VIETNAM-home-main-banner.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Director of Photography Hiring Services",
        "description": "Global DOP and cinematography services for feature films, TV, commercials, music videos, and documentaries.",
        "provider": {
            "@type": "Organization",
            "name": "NEEDaFIXER",
            "url": "https://needafixer.com/"
        },
        "serviceType": "DOP Hiring",
        "areaServed": "Worldwide"
    }
    </script>
</head>

<body class="bg-vietnam-darker text-white font-sans">'''
    
    with open('hire-dop/index.html', 'w', encoding='utf-8') as f:
        f.write(content)

def create_location_manager_page():
    """Create the Hire Location Manager page"""
    content = '''<!DOCTYPE html>
<html lang="en-US" itemscope itemtype="http://schema.org/WebPage">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- SEO Meta Tags -->
    <title>Hire a Location Manager | Global Experts | NEEDaFIXER</title>
    <meta name="description" content="NEEDaFIXER provides Location Managers globally for all types of productions.">
    <meta name="keywords" content="hire location manager, location scout, filming locations, location services, production locations">
    <meta name="author" content="NEEDaFIXER">
    
    <!-- Geographic Meta Tags -->
    <meta name="geo.region" content="GLOBAL">
    <meta name="geo.placename" content="Worldwide">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:locale" content="en_US">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Hire a Location Manager | Global Experts | NEEDaFIXER">
    <meta property="og:description" content="NEEDaFIXER provides Location Managers globally for all types of productions.">
    <meta property="og:url" content="/hire-location-manager/">
    <meta property="og:site_name" content="NEEDaFIXER">
    <meta property="og:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:image" content="/wp-content/uploads/2016/10/needafixer-vietnam-retina.png">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="/hire-location-manager/">
    
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
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-FD4LC3V4DB');
    </script>

    <!-- Custom Styles -->
    <style>
        .page-hero-bg {
            background-image: url('/wp-content/uploads/2015/10/VIETNAM-home-main-banner.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Location Manager Hiring Services",
        "description": "Global location management services including scouting, permitting, and on-site coordination for film and TV productions.",
        "provider": {
            "@type": "Organization",
            "name": "NEEDaFIXER",
            "url": "https://needafixer.com/"
        },
        "serviceType": "Location Manager Hiring",
        "areaServed": "Worldwide"
    }
    </script>
</head>

<body class="bg-vietnam-darker text-white font-sans">'''
    
    with open('hire-location-manager/index.html', 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Create all remaining pages"""
    print("Creating remaining pages...")
    create_fixer_page()
    create_dop_page()
    create_location_manager_page()
    print("✅ Page headers created successfully!")

if __name__ == "__main__":
    main()
