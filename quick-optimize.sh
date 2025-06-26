#!/bin/bash

# Quick optimization script for the largest files
# Focus on maximum impact with minimal complexity

IMAGES_DIR="/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/assets/images"
REPORT_FILE="/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/quick-optimization-report.txt"

echo "=== Quick Image Optimization Report ===" > "$REPORT_FILE"
echo "Started: $(date)" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

total_savings=0
files_processed=0

log() {
    echo "$1" | tee -a "$REPORT_FILE"
}

get_file_size() {
    stat -f%z "$1" 2>/dev/null || echo 0
}

format_bytes() {
    local bytes=$1
    if [ $bytes -ge 1048576 ]; then
        echo "$(echo "scale=1; $bytes / 1048576" | bc)MB"
    elif [ $bytes -ge 1024 ]; then
        echo "$(echo "scale=1; $bytes / 1024" | bc)KB"
    else
        echo "${bytes}B"
    fi
}

# Process GIF files in portfolio directory
log "Processing GIF files in portfolio directory..."
cd "$IMAGES_DIR/portfolio"

for gif_file in *.gif; do
    if [ -f "$gif_file" ]; then
        original_size=$(get_file_size "$gif_file")
        if [ $original_size -gt 5242880 ]; then # Only files > 5MB
            log "Processing: $gif_file ($(format_bytes $original_size))"
            
            webp_file="${gif_file%.gif}.webp"
            
            # Skip if already processed
            if [ ! -f "$webp_file" ]; then
                gif2webp -q 75 -m 6 "$gif_file" -o "$webp_file" 2>/dev/null
                
                if [ -f "$webp_file" ]; then
                    webp_size=$(get_file_size "$webp_file")
                    
                    # Only keep WebP if it's smaller
                    if [ $webp_size -lt $original_size ]; then
                        savings=$((original_size - webp_size))
                        total_savings=$((total_savings + savings))
                        files_processed=$((files_processed + 1))
                        log "  ✓ GIF→WebP: $(format_bytes $original_size) → $(format_bytes $webp_size) | Saved: $(format_bytes $savings)"
                    else
                        rm "$webp_file"
                        log "  ✗ WebP larger than GIF, keeping original"
                    fi
                else
                    log "  ✗ Failed to convert $gif_file"
                fi
            else
                webp_size=$(get_file_size "$webp_file")
                if [ $webp_size -lt $original_size ]; then
                    savings=$((original_size - webp_size))
                    total_savings=$((total_savings + savings))
                    files_processed=$((files_processed + 1))
                    log "  ✓ Already processed: $(format_bytes $original_size) → $(format_bytes $webp_size) | Saved: $(format_bytes $savings)"
                fi
            fi
        fi
    fi
done

# Process category GIF files
cd "$IMAGES_DIR/portfolio/categories"
log ""
log "Processing category GIF files..."

for gif_file in *.gif; do
    if [ -f "$gif_file" ]; then
        original_size=$(get_file_size "$gif_file")
        if [ $original_size -gt 2097152 ]; then # Only files > 2MB
            log "Processing: $gif_file ($(format_bytes $original_size))"
            
            webp_file="${gif_file%.gif}.webp"
            
            if [ ! -f "$webp_file" ]; then
                gif2webp -q 75 -m 6 "$gif_file" -o "$webp_file" 2>/dev/null
                
                if [ -f "$webp_file" ]; then
                    webp_size=$(get_file_size "$webp_file")
                    
                    if [ $webp_size -lt $original_size ]; then
                        savings=$((original_size - webp_size))
                        total_savings=$((total_savings + savings))
                        files_processed=$((files_processed + 1))
                        log "  ✓ GIF→WebP: $(format_bytes $original_size) → $(format_bytes $webp_size) | Saved: $(format_bytes $savings)"
                    else
                        rm "$webp_file"
                        log "  ✗ WebP larger than GIF, keeping original"
                    fi
                fi
            fi
        fi
    fi
done

# Process large JPEG files
log ""
log "Processing large JPEG files..."
find "$IMAGES_DIR" -name "*.jpg" -size +500k | while read jpeg_file; do
    original_size=$(get_file_size "$jpeg_file")
    log "Processing: $(basename "$jpeg_file") ($(format_bytes $original_size))"
    
    temp_file="${jpeg_file}.tmp"
    magick "$jpeg_file" -resize "1920x1080>" -quality 85 "$temp_file" 2>/dev/null
    
    if [ -f "$temp_file" ]; then
        new_size=$(get_file_size "$temp_file")
        if [ $new_size -lt $original_size ]; then
            mv "$temp_file" "$jpeg_file"
            savings=$((original_size - new_size))
            total_savings=$((total_savings + savings))
            files_processed=$((files_processed + 1))
            log "  ✓ JPEG optimized: $(format_bytes $original_size) → $(format_bytes $new_size) | Saved: $(format_bytes $savings)"
        else
            rm "$temp_file"
            log "  ✗ No improvement for JPEG"
        fi
    fi
done

log ""
log "=== SUMMARY ==="
log "Files processed: $files_processed"
log "Total savings: $(format_bytes $total_savings)"
log "Completed: $(date)"

echo ""
echo "Optimization complete! Total savings: $(format_bytes $total_savings)"
echo "Check $REPORT_FILE for detailed report."