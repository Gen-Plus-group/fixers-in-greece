#!/bin/bash

# GIF to Video Optimization Script for Fixers in Greece
# This script converts large GIF files to optimized MP4 and WebM videos

ASSETS_DIR="/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/assets/images/portfolio/categories"
OUTPUT_DIR="$ASSETS_DIR"

echo "🎬 Converting GIF animations to optimized video formats..."

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Function to convert GIF to MP4 and WebM
convert_gif() {
    local gif_file="$1"
    local base_name=$(basename "$gif_file" .gif)
    
    echo "🔄 Processing $gif_file..."
    
    # Convert to MP4 (H.264)
    ffmpeg -i "$gif_file" \
        -vcodec libx264 \
        -pix_fmt yuv420p \
        -crf 25 \
        -movflags +faststart \
        -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" \
        "$OUTPUT_DIR/${base_name}.mp4" \
        -y -loglevel error
    
    # Convert to WebM (VP9)
    ffmpeg -i "$gif_file" \
        -vcodec libvpx-vp9 \
        -crf 30 \
        -b:v 0 \
        -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" \
        "$OUTPUT_DIR/${base_name}.webm" \
        -y -loglevel error
    
    # Generate a poster frame (first frame as WebP)
    ffmpeg -i "$gif_file" \
        -vframes 1 \
        -f webp \
        -q:v 80 \
        "$OUTPUT_DIR/${base_name}-poster.webp" \
        -y -loglevel error
        
    echo "✅ Converted $base_name: MP4, WebM, and poster created"
}

# Check if ffmpeg is available
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ FFmpeg is required but not installed. Please install FFmpeg first."
    echo "   brew install ffmpeg (on macOS)"
    exit 1
fi

# Convert each GIF file
cd "$ASSETS_DIR"

for gif_file in *.gif; do
    if [ -f "$gif_file" ]; then
        convert_gif "$gif_file"
    fi
done

echo ""
echo "📊 File size comparison:"
echo "Before optimization:"
ls -lh *.gif 2>/dev/null | awk '{print $9 ": " $5}'

echo ""
echo "After optimization:"
ls -lh *.mp4 *.webm 2>/dev/null | awk '{print $9 ": " $5}'

echo ""
echo "🎉 GIF to video conversion complete!"
echo "💡 Remember to update HTML to use <video> elements instead of <img> tags"