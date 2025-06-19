#!/usr/bin/env python3
"""
Script to complete the Fixer page with full content
"""

def create_complete_fixer_content():
    """Create complete content for the Fixer page"""
    
    # Read the Line Producer page as a template
    with open('hire-line-producer/index.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Replace all Line Producer specific content with Fixer content
    fixer_content = template_content.replace(
        'Hire a Line Producer | Vetted Film & TV Talent | NEEDaFIXER',
        'Hire a Fixer | Global In-House & Vetted Local Experts | NEEDaFIXER'
    ).replace(
        'NEEDaFIXER provides vetted, experienced Line Producers for film, TV, and commercials globally.',
        'NEEDaFIXER offers fixers globally with full production support in 100+ countries.'
    ).replace(
        'Line Producer Hiring Services',
        'Fixer Hiring Services'
    ).replace(
        'Global line producer hiring services for feature films, TV series, commercials, and documentaries. Vetted professionals available worldwide.',
        'Global fixer services providing local expertise, permits, crew, and production support in 100+ countries.'
    ).replace(
        'Line Producer Services',
        'Fixer Services'
    ).replace(
        'Feature Film Line Producers',
        'In-House Fixers'
    ).replace(
        'Budget discipline and artistic integrity',
        'Consistent quality'
    ).replace(
        'TV Series Line Producers',
        'Vetted Local Experts'
    ).replace(
        'Management of complex episodic schedules',
        'Street-smart and culturally aware'
    ).replace(
        'Commercial Line Producers',
        'Permits & Paperwork'
    ).replace(
        'Efficiency under tight timelines',
        'Handled efficiently'
    ).replace(
        '/hire-line-producer/',
        '/hire-fixer/'
    ).replace(
        'hire-line-producer',
        'hire-fixer'
    ).replace(
        'Hire Line Producer',
        'Hire Fixer'
    ).replace(
        'Line Producer',
        'Fixer'
    ).replace(
        'line producer',
        'fixer'
    ).replace(
        'Hire the Best Fixer for Your Next Production',
        'Hire a Fixer & Unlock Seamless Global Production'
    ).replace(
        'We connect you with top-tier Fixers for feature films, commercials, TV series, and special projects. Vetted professionals who deliver budget discipline and operational excellence.',
        'We provide fixers who deliver smooth, fast, and stress-free shoots in 100+ countries. Local expertise, global support, zero surprises.'
    )
    
    # Replace specific content sections
    fixer_content = fixer_content.replace(
        'Professional Fixer Services Worldwide',
        'Professional Fixer Services Worldwide'
    ).replace(
        'We connect you with top-tier Fixers for feature films, commercials, TV series, and special projects. Our vetted professionals bring proven expertise in budget management, scheduling, and operational excellence to ensure your production runs smoothly from pre-production through wrap.',
        'We provide fixers who deliver smooth, fast, and stress-free shoots in 100+ countries. Our global network combines in-house expertise with vetted local professionals who understand the intricacies of filming in their regions.'
    )
    
    # Write the complete content to the Fixer page
    with open('hire-fixer/index.html', 'w', encoding='utf-8') as f:
        f.write(fixer_content)
    
    print("✅ Fixer page completed successfully")

if __name__ == "__main__":
    create_complete_fixer_content()
