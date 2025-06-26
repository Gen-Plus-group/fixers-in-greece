#!/usr/bin/env python3
"""
Single GIF Optimization Script for Fixers in Greece
Optimizes one GIF at a time with progress feedback
"""

import os
import sys
from PIL import Image, ImageSequence

def get_file_size(file_path):
    """Get file size in MB"""
    try:
        return os.path.getsize(file_path) / (1024 * 1024)
    except:
        return 0

def optimize_gif_to_webp(gif_path, quality=75):
    """Convert animated GIF to WebP format with progress"""
    try:
        print(f"Opening {os.path.basename(gif_path)}...")
        with Image.open(gif_path) as img:
            base_name = os.path.splitext(gif_path)[0]
            webp_path = f"{base_name}.webp"
            
            print(f"Converting to WebP (quality={quality})...")
            
            # Get all frames
            frames = []
            for frame in ImageSequence.Iterator(img):
                frames.append(frame.copy())
            
            print(f"Processing {len(frames)} frames...")
            
            # Save as animated WebP
            frames[0].save(webp_path, 
                          format='WebP',
                          save_all=True,
                          append_images=frames[1:],
                          optimize=True,
                          quality=quality,
                          method=6)
            
            return webp_path
    except Exception as e:
        print(f"Error converting {gif_path}: {e}")
        return None

def create_poster_frame(gif_path, quality=85):
    """Create a static poster frame"""
    try:
        with Image.open(gif_path) as img:
            base_name = os.path.splitext(gif_path)[0]
            poster_path = f"{base_name}-poster.webp"
            
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

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 optimize-single-gif.py <gif-file>")
        sys.exit(1)
    
    gif_file = sys.argv[1]
    
    if not os.path.exists(gif_file):
        print(f"File not found: {gif_file}")
        sys.exit(1)
    
    if not gif_file.lower().endswith('.gif'):
        print("File must be a GIF")
        sys.exit(1)
    
    original_size = get_file_size(gif_file)
    print(f"🔄 Processing {os.path.basename(gif_file)} ({original_size:.1f} MB)")
    
    # Convert to WebP
    webp_path = optimize_gif_to_webp(gif_file, quality=75)
    if webp_path:
        webp_size = get_file_size(webp_path)
        savings = original_size - webp_size
        print(f"✅ WebP: {webp_size:.1f} MB (saved {savings:.1f} MB)")
    
    # Create poster frame
    poster_path = create_poster_frame(gif_file, quality=85)
    if poster_path:
        poster_size = get_file_size(poster_path)
        print(f"📸 Poster: {poster_size:.1f} MB")
    
    print("🎉 Optimization complete!")

if __name__ == "__main__":
    main()