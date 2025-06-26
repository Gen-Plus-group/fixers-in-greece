#!/usr/bin/env python3
"""
Image Optimization Script for Fixers in Greece
Converts large GIFs to optimized formats and resizes images
"""

import os
import sys
from PIL import Image, ImageSequence
import subprocess

def optimize_gif_to_webp(gif_path, quality=80):
    """Convert animated GIF to WebP format"""
    try:
        with Image.open(gif_path) as img:
            # Get base name without extension
            base_name = os.path.splitext(gif_path)[0]
            webp_path = f"{base_name}.webp"
            
            # Save as animated WebP with optimization
            img.save(webp_path, 
                    format='WebP',
                    save_all=True,
                    append_images=list(ImageSequence.Iterator(img))[1:],
                    optimize=True,
                    quality=quality,
                    method=6)  # Best compression
            
            return webp_path
    except Exception as e:
        print(f"Error converting {gif_path}: {e}")
        return None

def create_poster_frame(gif_path, quality=85):
    """Create a static poster frame from the first frame of GIF"""
    try:
        with Image.open(gif_path) as img:
            base_name = os.path.splitext(gif_path)[0]
            poster_path = f"{base_name}-poster.webp"
            
            # Get first frame and convert to WebP
            first_frame = img.copy()
            if first_frame.mode != 'RGB':
                first_frame = first_frame.convert('RGB')
            
            first_frame.save(poster_path, 
                           format='WebP',
                           optimize=True,
                           quality=quality)
            
            return poster_path
    except Exception as e:
        print(f"Error creating poster for {gif_path}: {e}")
        return None

def resize_and_optimize_image(image_path, max_width=800, max_height=600, quality=85):
    """Resize and optimize regular images"""
    try:
        with Image.open(image_path) as img:
            # Calculate new size maintaining aspect ratio
            width, height = img.size
            aspect_ratio = width / height
            
            if width > max_width or height > max_height:
                if aspect_ratio > 1:  # Landscape
                    new_width = min(width, max_width)
                    new_height = int(new_width / aspect_ratio)
                else:  # Portrait
                    new_height = min(height, max_height)
                    new_width = int(new_height * aspect_ratio)
                
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Save optimized version
            base_name = os.path.splitext(image_path)[0]
            ext = os.path.splitext(image_path)[1].lower()
            
            if ext in ['.jpg', '.jpeg']:
                optimized_path = f"{base_name}-optimized.webp"
                img.save(optimized_path, format='WebP', optimize=True, quality=quality)
            elif ext == '.webp':
                optimized_path = f"{base_name}-optimized.webp"
                img.save(optimized_path, format='WebP', optimize=True, quality=quality)
            else:
                return None
            
            return optimized_path
    except Exception as e:
        print(f"Error optimizing {image_path}: {e}")
        return None

def get_file_size(file_path):
    """Get file size in KB"""
    try:
        return os.path.getsize(file_path) / 1024
    except:
        return 0

def main():
    # Directory paths
    categories_dir = "/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/assets/images/portfolio/categories"
    home_images_dir = "/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/assets/images"
    
    print("🖼️  Starting image optimization for Fixers in Greece...")
    
    total_savings = 0
    
    # Optimize GIF files
    print("\n📁 Processing GIF files...")
    for filename in os.listdir(categories_dir):
        if filename.endswith('.gif'):
            gif_path = os.path.join(categories_dir, filename)
            original_size = get_file_size(gif_path)
            
            print(f"\n🔄 Processing {filename} ({original_size:.1f} KB)")
            
            # Convert to WebP
            webp_path = optimize_gif_to_webp(gif_path, quality=75)
            if webp_path:
                webp_size = get_file_size(webp_path)
                savings = original_size - webp_size
                total_savings += savings
                print(f"   ✅ WebP: {webp_size:.1f} KB (saved {savings:.1f} KB)")
            
            # Create poster frame
            poster_path = create_poster_frame(gif_path, quality=85)
            if poster_path:
                poster_size = get_file_size(poster_path)
                print(f"   📸 Poster: {poster_size:.1f} KB")
    
    # Optimize other images
    print("\n📁 Processing other images...")
    for filename in os.listdir(home_images_dir):
        if filename.endswith(('.webp', '.jpg', '.jpeg', '.png')):
            image_path = os.path.join(home_images_dir, filename)
            original_size = get_file_size(image_path)
            
            if original_size > 50:  # Only optimize files larger than 50KB
                print(f"\n🔄 Processing {filename} ({original_size:.1f} KB)")
                
                optimized_path = resize_and_optimize_image(image_path)
                if optimized_path:
                    optimized_size = get_file_size(optimized_path)
                    savings = original_size - optimized_size
                    total_savings += savings
                    print(f"   ✅ Optimized: {optimized_size:.1f} KB (saved {savings:.1f} KB)")
    
    print(f"\n🎉 Optimization complete!")
    print(f"💾 Total savings: {total_savings:.1f} KB ({total_savings/1024:.1f} MB)")
    
    print(f"\n💡 Next steps:")
    print("1. Update HTML to use optimized WebP files")
    print("2. Add proper width/height attributes")
    print("3. Consider lazy loading for better performance")

if __name__ == "__main__":
    try:
        from PIL import Image, ImageSequence
    except ImportError:
        print("❌ Pillow library is required. Install with: pip install Pillow")
        sys.exit(1)
    
    main()