#!/usr/bin/env python3
"""
Unify all sitemaps into a single comprehensive sitemap.xml
"""

import xml.etree.ElementTree as ET
from datetime import datetime
import os
from collections import OrderedDict

# List of all sitemap files to process
SITEMAP_FILES = [
    'attachment-sitemap.xml',
    'author-sitemap.xml', 
    'category-sitemap.xml',
    'page-sitemap.xml',
    'portfolio-sitemap.xml',
    'portfolio_category-sitemap.xml',
    'post-sitemap.xml',
    'services-sitemap.xml',
    'sitemap-entities.xml',
    'sitemap-film-crew-services.xml',
    'sitemap-main-pages.xml',
    'sitemap-portfolio-misc.xml',
    'sitemap-post-production-services.xml',
    'sitemap-pre-production-services.xml',
    'sitemap-production-services.xml',
    'sitemap-services.xml',
    'sitemap-specialized-services.xml',
    'ssp-form-sitemap.xml',
    'staff-sitemap.xml',
    'testimonials-sitemap.xml'
]

def get_url_priority(url):
    """Determine priority based on URL pattern"""
    loc = url.get('loc', '')
    
    # Homepage
    if loc.endswith('fixersinvietnam.com/'):
        return 1.0
    
    # Main category pages
    if any(x in loc for x in ['/pre-production-services/', '/production-services/', 
                               '/post-production-services/', '/film-crew/']):
        if loc.count('/') == 4:  # Main category page
            return 0.9
        else:  # Subcategory page
            return 0.8
    
    # Important pages
    if any(x in loc for x in ['/about-us/', '/contact/', '/portfolio/', '/filming-in-vietnam/']):
        return 0.9
    
    # Service pages
    if any(x in loc for x in ['/services/', '-services/', '-vietnam/', '/hire-']):
        return 0.7
    
    # Location pages
    if any(x in loc for x in ['/ho-chi-minh-city-', '/hanoi-', '-filming-location']):
        return 0.7
    
    # Portfolio items
    if '/portfolio-item/' in loc:
        return 0.5
    
    # Attachment and misc pages
    if any(x in loc for x in ['/attachment/', '/author/', '/category/', '/hello-world/', '/404/']):
        return 0.1
    
    # Default
    return 0.6

def extract_urls_from_sitemap(filepath):
    """Extract all URL entries from a sitemap file"""
    urls = []
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        # Handle different namespace formats
        namespaces = {
            'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9',
            'image': 'http://www.google.com/schemas/sitemap-image/1.1',
            'mobile': 'http://www.google.com/schemas/sitemap-mobile/1.0'
        }
        
        # Find all URL elements
        for url_elem in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            url_data = {}
            
            # Get loc
            loc_elem = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            if loc_elem is not None and loc_elem.text:
                url_data['loc'] = loc_elem.text.strip()
            
            # Get lastmod
            lastmod_elem = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
            if lastmod_elem is not None and lastmod_elem.text:
                url_data['lastmod'] = lastmod_elem.text.strip()
            
            # Get changefreq
            changefreq_elem = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq')
            if changefreq_elem is not None and changefreq_elem.text:
                url_data['changefreq'] = changefreq_elem.text.strip()
            
            # Get priority
            priority_elem = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}priority')
            if priority_elem is not None and priority_elem.text:
                url_data['priority'] = priority_elem.text.strip()
            
            if 'loc' in url_data:
                urls.append(url_data)
    
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    
    return urls

def main():
    """Collect all URLs and create unified sitemap"""
    all_urls = OrderedDict()  # Use OrderedDict to maintain order and avoid duplicates
    
    print("Collecting URLs from all sitemaps...")
    print("=" * 60)
    
    # Process each sitemap
    for sitemap_file in SITEMAP_FILES:
        if os.path.exists(sitemap_file):
            urls = extract_urls_from_sitemap(sitemap_file)
            print(f"✓ {sitemap_file}: Found {len(urls)} URLs")
            
            # Add URLs to collection (using loc as key to avoid duplicates)
            for url in urls:
                loc = url.get('loc', '')
                if loc:
                    # If URL already exists, update with newer lastmod if available
                    if loc in all_urls:
                        existing = all_urls[loc]
                        new_lastmod = url.get('lastmod', '')
                        old_lastmod = existing.get('lastmod', '')
                        if new_lastmod > old_lastmod:
                            all_urls[loc] = url
                    else:
                        all_urls[loc] = url
        else:
            print(f"✗ {sitemap_file}: Not found")
    
    print("=" * 60)
    print(f"Total unique URLs collected: {len(all_urls)}")
    
    # Create unified sitemap
    print("\nCreating unified sitemap...")
    
    # Create root element
    root = ET.Element('urlset')
    root.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    root.set('xsi:schemaLocation', 'http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd')
    
    # Sort URLs by priority and then by location
    sorted_urls = sorted(all_urls.values(), 
                        key=lambda x: (-get_url_priority(x), x.get('loc', '')))
    
    # Add URLs to sitemap
    for url_data in sorted_urls:
        url_elem = ET.SubElement(root, 'url')
        
        # Add loc
        loc_elem = ET.SubElement(url_elem, 'loc')
        loc_elem.text = url_data.get('loc', '')
        
        # Add lastmod
        if 'lastmod' in url_data:
            lastmod_elem = ET.SubElement(url_elem, 'lastmod')
            lastmod_elem.text = url_data['lastmod']
        
        # Add changefreq
        changefreq = url_data.get('changefreq', '')
        if not changefreq:
            # Determine changefreq based on priority
            priority = get_url_priority(url_data)
            if priority >= 0.9:
                changefreq = 'daily'
            elif priority >= 0.7:
                changefreq = 'weekly'
            elif priority >= 0.5:
                changefreq = 'monthly'
            else:
                changefreq = 'yearly'
        changefreq_elem = ET.SubElement(url_elem, 'changefreq')
        changefreq_elem.text = changefreq
        
        # Add priority
        priority_elem = ET.SubElement(url_elem, 'priority')
        priority_elem.text = str(get_url_priority(url_data))
    
    # Create tree and write to file
    tree = ET.ElementTree(root)
    
    # Backup existing sitemap.xml
    if os.path.exists('sitemap.xml'):
        os.rename('sitemap.xml', 'sitemap.xml.backup-unified')
    
    # Write new unified sitemap
    with open('sitemap-unified.xml', 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding='UTF-8', xml_declaration=False)
    
    print(f"✅ Created unified sitemap with {len(sorted_urls)} URLs")
    print("   Saved as: sitemap-unified.xml")
    print("   Original backed up as: sitemap.xml.backup-unified")
    
    # Generate summary report
    print("\n" + "=" * 60)
    print("URL Distribution by Priority:")
    priority_count = {}
    for url in sorted_urls:
        p = get_url_priority(url)
        priority_count[p] = priority_count.get(p, 0) + 1
    
    for priority in sorted(priority_count.keys(), reverse=True):
        print(f"  Priority {priority}: {priority_count[priority]} URLs")

if __name__ == "__main__":
    main()