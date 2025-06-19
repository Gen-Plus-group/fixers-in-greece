#!/usr/bin/env python3
"""
Update sitemap.xml to add Content Production pages
"""

import xml.etree.ElementTree as ET
from datetime import datetime

# Register namespace
ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')

# Content Production pages to add
CONTENT_PRODUCTION_PAGES = [
    # Main page
    ('https://fixersinvietnam.com/content-production/', 0.9, 'daily'),
    # Sub-pages
    ('https://fixersinvietnam.com/content-production/tv-shows-broadcast-series/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/feature-films/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/drama-series/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/commercials-advertising/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/corporate-videos/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/documentaries-docuseries/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/social-media-content/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/narrative-films-web-series/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/music-videos/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/fashion-videos/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/travel-lifestyle-marketing/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/hotel-videos-reels/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/cookery-shows-food-content/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/talk-shows-panel-shows/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/competition-reality-shows/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/live-events-brand-activations/', 0.8, 'quarterly'),
    ('https://fixersinvietnam.com/content-production/educational-explainer-videos/', 0.8, 'quarterly'),
]

def update_sitemap():
    """Update the sitemap with new Content Production pages"""
    
    # Parse existing sitemap
    tree = ET.parse('sitemap.xml')
    root = tree.getroot()
    
    # Get namespace
    namespace = {'': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    # Get current date
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Find position to insert (after production-services main page)
    urls = root.findall('.//url', namespace)
    insert_index = None
    
    for i, url in enumerate(urls):
        loc = url.find('loc', namespace)
        if loc is not None and loc.text == 'https://fixersinvietnam.com/production-services/':
            insert_index = i + 1
            break
    
    if insert_index is None:
        # If production-services not found, insert after post-production
        for i, url in enumerate(urls):
            loc = url.find('loc', namespace)
            if loc is not None and loc.text == 'https://fixersinvietnam.com/post-production-services/':
                insert_index = i + 1
                break
    
    if insert_index is None:
        print("Warning: Could not find production or post-production services, appending to end")
        insert_index = len(urls)
    
    # Create new URL elements
    for i, (loc_text, priority, changefreq) in enumerate(CONTENT_PRODUCTION_PAGES):
        url_elem = ET.Element('url')
        
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = loc_text
        
        lastmod = ET.SubElement(url_elem, 'lastmod')
        lastmod.text = current_date
        
        changefreq_elem = ET.SubElement(url_elem, 'changefreq')
        changefreq_elem.text = changefreq
        
        priority_elem = ET.SubElement(url_elem, 'priority')
        priority_elem.text = str(priority)
        
        # Insert at the calculated position
        root.insert(insert_index + i, url_elem)
    
    # Count total URLs
    total_urls = len(root.findall('.//url', namespace))
    
    # Write updated sitemap
    tree.write('sitemap.xml', encoding='UTF-8', xml_declaration=True)
    
    print(f"✅ Added {len(CONTENT_PRODUCTION_PAGES)} Content Production pages to sitemap")
    print(f"📊 Total URLs in sitemap: {total_urls}")

if __name__ == "__main__":
    update_sitemap()