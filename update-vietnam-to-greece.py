#!/usr/bin/env python3
import os
import re

def update_file_content(file_path):
    """Update Vietnam references to Greece in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update URLs and paths
        content = re.sub(r'/filming-in-vietnam/', '/filming-in-greece/', content)
        content = re.sub(r'/commercial-video-production-vietnam/', '/commercial-video-production-greece/', content)
        content = re.sub(r'/documentary-filming-vietnam/', '/documentary-filming-greece/', content)
        content = re.sub(r'/event-filming-vietnam/', '/event-filming-greece/', content)
        content = re.sub(r'/live-streaming-vietnam/', '/live-streaming-greece/', content)
        content = re.sub(r'/music-video-production-vietnam/', '/music-video-production-greece/', content)
        content = re.sub(r'/news-filming-vietnam/', '/news-filming-greece/', content)
        content = re.sub(r'/equipment-rental-vietnam/', '/equipment-rental-greece/', content)
        content = re.sub(r'/film-permits-vietnam/', '/film-permits-greece/', content)
        content = re.sub(r'/location-scouting-vietnam/', '/location-scouting-greece/', content)
        
        # Update image references
        content = re.sub(r'needafixer-vietnam\.png', 'needafixer-greece.png', content)
        content = re.sub(r'needafixer-vietnam-retina\.png', 'needafixer-greece-retina.png', content)
        
        # Update CSS classes and IDs
        content = re.sub(r'vietnam-orange', 'greece-blue', content)
        content = re.sub(r'vietnam-red', 'greece-white', content)
        content = re.sub(r'vietnam-dark', 'greece-dark', content)
        content = re.sub(r'text-gradient-vietnam', 'text-gradient-greece', content)
        content = re.sub(r'bg-gradient-vietnam', 'bg-gradient-greece', content)
        content = re.sub(r'hover:bg-vietnam-', 'hover:bg-greece-', content)
        content = re.sub(r'text-vietnam-', 'text-greece-', content)
        content = re.sub(r'bg-vietnam-', 'bg-greece-', content)
        content = re.sub(r'border-vietnam-', 'border-greece-', content)
        
        # Update text content (case-insensitive)
        content = re.sub(r'Vietnam', 'Greece', content, flags=re.IGNORECASE)
        content = re.sub(r'Vietnamese', 'Greek', content, flags=re.IGNORECASE)
        content = re.sub(r'Hanoi', 'Athens', content, flags=re.IGNORECASE)
        content = re.sub(r'Ho Chi Minh City', 'Thessaloniki', content, flags=re.IGNORECASE)
        content = re.sub(r'Saigon', 'Thessaloniki', content, flags=re.IGNORECASE)
        
        # Update schema references
        content = re.sub(r'vietnam-local-business-schema\.json', 'greece-local-business-schema.json', content)
        
        # Update email addresses if they contain vietnam
        content = re.sub(r'vietnam@', 'greece@', content)
        
        # Fix any double slashes that might have been created
        content = re.sub(r'//', '/', content)
        content = re.sub(r'https:/', 'https://', content)
        content = re.sub(r'http:/', 'http://', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def process_directory(directory):
    """Process all HTML, CSS, JS, JSON, and MD files in directory."""
    updated_files = []
    
    for root, dirs, files in os.walk(directory):
        # Skip node_modules
        if 'node_modules' in root:
            continue
            
        for file in files:
            if file.endswith(('.html', '.css', '.js', '.json', '.md', '.php', '.xml')):
                file_path = os.path.join(root, file)
                if update_file_content(file_path):
                    updated_files.append(file_path)
    
    return updated_files

# Main execution
if __name__ == "__main__":
    base_dir = "/home/moister/vietnam/fiexers/fixers-in-greece"
    
    print("Updating Vietnam references to Greece...")
    updated = process_directory(base_dir)
    
    print(f"\nUpdated {len(updated)} files:")
    for file in sorted(updated)[:20]:  # Show first 20 files
        print(f"  - {file}")
    
    if len(updated) > 20:
        print(f"  ... and {len(updated) - 20} more files")
    
    print("\nDone!")