#!/usr/bin/env python3
"""
Script to complete the DOP and Location Manager pages
"""

def create_dop_page():
    """Create complete DOP page"""
    
    # Read the Line Producer page as a template
    with open('hire-line-producer/index.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Replace all content for DOP
    dop_content = template_content.replace(
        'Hire a Line Producer | Vetted Film & TV Talent | NEEDaFIXER',
        'Hire a DOP | Global Cinematography Experts | NEEDaFIXER'
    ).replace(
        'NEEDaFIXER provides vetted, experienced Line Producers for film, TV, and commercials globally.',
        'NEEDaFIXER provides expert DOPs globally for cinematic features, TV, commercials, and more.'
    ).replace(
        'Line Producer Hiring Services',
        'Director of Photography Hiring Services'
    ).replace(
        'Global line producer hiring services for feature films, TV series, commercials, and documentaries. Vetted professionals available worldwide.',
        'Global DOP and cinematography services for feature films, TV, commercials, music videos, and documentaries.'
    ).replace(
        '/hire-line-producer/',
        '/hire-dop/'
    ).replace(
        'hire-line-producer',
        'hire-dop'
    ).replace(
        'Hire Line Producer',
        'Hire DOP'
    ).replace(
        'Line Producer',
        'DOP'
    ).replace(
        'line producer',
        'DOP'
    ).replace(
        'Hire the Best DOP for Your Next Production',
        'Secure Your Expert Director of Photography'
    ).replace(
        'We connect you with top-tier DOPs for feature films, commercials, TV series, and special projects. Vetted professionals who deliver budget discipline and operational excellence.',
        'We provide DOPs for all genres, formats, and global locations.'
    ).replace(
        'Professional DOP Services Worldwide',
        'Expert Cinematography Services Worldwide'
    ).replace(
        'Why Clients Choose NEEDaFIXER for Their DOP Needs',
        'Why Choose NEEDaFIXER'
    ).replace(
        'Our DOP Talent Pool',
        'Our DOP Talent Pool'
    ).replace(
        'How to Hire a DOP Through NEEDaFIXER',
        'How to Access a DOP'
    ).replace(
        'DOP FAQs',
        'DOP FAQs'
    )
    
    # Write the complete content to the DOP page
    with open('hire-dop/index.html', 'w', encoding='utf-8') as f:
        f.write(dop_content)
    
    print("✅ DOP page completed successfully")

def create_location_manager_page():
    """Create complete Location Manager page"""
    
    # Read the Line Producer page as a template
    with open('hire-line-producer/index.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Replace all content for Location Manager
    location_content = template_content.replace(
        'Hire a Line Producer | Vetted Film & TV Talent | NEEDaFIXER',
        'Hire a Location Manager | Global Experts | NEEDaFIXER'
    ).replace(
        'NEEDaFIXER provides vetted, experienced Line Producers for film, TV, and commercials globally.',
        'NEEDaFIXER provides Location Managers globally for all types of productions.'
    ).replace(
        'Line Producer Hiring Services',
        'Location Manager Hiring Services'
    ).replace(
        'Global line producer hiring services for feature films, TV series, commercials, and documentaries. Vetted professionals available worldwide.',
        'Global location management services including scouting, permitting, and on-site coordination for film and TV productions.'
    ).replace(
        '/hire-line-producer/',
        '/hire-location-manager/'
    ).replace(
        'hire-line-producer',
        'hire-location-manager'
    ).replace(
        'Hire Line Producer',
        'Hire Location Manager'
    ).replace(
        'Line Producer',
        'Location Manager'
    ).replace(
        'line producer',
        'location manager'
    ).replace(
        'Hire the Best Location Manager for Your Next Production',
        'Hire a Location Manager'
    ).replace(
        'We connect you with top-tier Location Managers for feature films, commercials, TV series, and special projects. Vetted professionals who deliver budget discipline and operational excellence.',
        'Unlock perfect filming locations worldwide with expert support.'
    ).replace(
        'Professional Location Manager Services Worldwide',
        'Expert Location Management Services Worldwide'
    ).replace(
        'Why Clients Choose NEEDaFIXER for Their Location Manager Needs',
        'Why Partner with NEEDaFIXER'
    ).replace(
        'Our Location Manager Talent Pool',
        'Our Global Network'
    ).replace(
        'How to Hire a Location Manager Through NEEDaFIXER',
        'How to Access a Location Manager'
    ).replace(
        'Location Manager FAQs',
        'Location Manager FAQs'
    )
    
    # Write the complete content to the Location Manager page
    with open('hire-location-manager/index.html', 'w', encoding='utf-8') as f:
        f.write(location_content)
    
    print("✅ Location Manager page completed successfully")

def main():
    """Create both pages"""
    print("🚀 Creating complete DOP and Location Manager pages...")
    create_dop_page()
    create_location_manager_page()
    print("🎉 All pages completed successfully!")

if __name__ == "__main__":
    main()
