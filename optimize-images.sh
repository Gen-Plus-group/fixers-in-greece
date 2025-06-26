#!/bin/bash

# Image Optimization Script for Fixers in Greece
# This script optimizes images to achieve significant bandwidth savings

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
IMAGES_DIR="/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/assets/images"
BACKUP_DIR="/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/assets/images-backup"
REPORT_FILE="/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/optimization-report.txt"
MAX_WIDTH=1920
MAX_HEIGHT=1080
JPEG_QUALITY=85
WEBP_QUALITY=80

echo -e "${BLUE}=== Image Optimization Script ===${NC}"
echo "Starting optimization process..."

# Function to log messages
log() {
    echo -e "$1" | tee -a "$REPORT_FILE"
}

# Function to check if tools are installed
check_tools() {
    log "${YELLOW}Checking for required tools...${NC}"
    
    local tools_needed=()
    
    if ! command -v magick &> /dev/null && ! command -v convert &> /dev/null; then
        tools_needed+=("imagemagick")
    fi
    
    if ! command -v cwebp &> /dev/null; then
        tools_needed+=("webp")
    fi
    
    if ! command -v gifsicle &> /dev/null; then
        tools_needed+=("gifsicle")
    fi
    
    if [ ${#tools_needed[@]} -gt 0 ]; then
        log "${YELLOW}Installing missing tools: ${tools_needed[*]}${NC}"
        brew install "${tools_needed[@]}"
    else
        log "${GREEN}All required tools are installed.${NC}"
    fi
}

# Function to get file size in bytes
get_file_size() {
    stat -f%z "$1" 2>/dev/null || echo 0
}

# Function to format bytes to human readable
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

# Function to create backup
create_backup() {
    log "${YELLOW}Creating backup of original images...${NC}"
    if [ ! -d "$BACKUP_DIR" ]; then
        mkdir -p "$BACKUP_DIR"
        cp -R "$IMAGES_DIR"/* "$BACKUP_DIR/"
        log "${GREEN}Backup created at: $BACKUP_DIR${NC}"
    else
        log "${YELLOW}Backup already exists, skipping...${NC}"
    fi
}

# Function to optimize GIF files (convert to WebP)
optimize_gif() {
    local file="$1"
    local dir=$(dirname "$file")
    local basename=$(basename "$file" .gif)
    local webp_file="$dir/$basename.webp"
    
    local original_size=$(get_file_size "$file")
    
    # Convert GIF to WebP with animation support
    if command -v gif2webp &> /dev/null; then
        gif2webp -q $WEBP_QUALITY "$file" -o "$webp_file"
    else
        # Fallback: extract first frame and convert
        magick "$file[0]" -quality $WEBP_QUALITY "$webp_file"
    fi
    
    if [ -f "$webp_file" ]; then
        local new_size=$(get_file_size "$webp_file")
        local savings=$((original_size - new_size))
        log "  GIF→WebP: $(basename "$file") | $(format_bytes $original_size) → $(format_bytes $new_size) | Saved: $(format_bytes $savings)"
        return $savings
    fi
    return 0
}

# Function to optimize JPEG files
optimize_jpeg() {
    local file="$1"
    local temp_file="${file}.tmp"
    local original_size=$(get_file_size "$file")
    
    # Resize if too large and optimize quality
    magick "$file" -resize "${MAX_WIDTH}x${MAX_HEIGHT}>" -quality $JPEG_QUALITY "$temp_file"
    
    if [ -f "$temp_file" ]; then
        local new_size=$(get_file_size "$temp_file")
        if [ $new_size -lt $original_size ]; then
            mv "$temp_file" "$file"
            local savings=$((original_size - new_size))
            log "  JPEG opt: $(basename "$file") | $(format_bytes $original_size) → $(format_bytes $new_size) | Saved: $(format_bytes $savings)"
            return $savings
        else
            rm "$temp_file"
        fi
    fi
    return 0
}

# Function to optimize PNG files
optimize_png() {
    local file="$1"
    local dir=$(dirname "$file")
    local basename=$(basename "$file" .png)
    local webp_file="$dir/$basename.webp"
    local temp_file="${file}.tmp"
    
    local original_size=$(get_file_size "$file")
    
    # First optimize PNG
    magick "$file" -resize "${MAX_WIDTH}x${MAX_HEIGHT}>" -quality 95 "$temp_file"
    
    # Also create WebP version
    magick "$file" -resize "${MAX_WIDTH}x${MAX_HEIGHT}>" -quality $WEBP_QUALITY "$webp_file"
    
    local png_size=$(get_file_size "$temp_file")
    local webp_size=$(get_file_size "$webp_file")
    
    # Use the smaller file
    if [ $png_size -le $webp_size ]; then
        mv "$temp_file" "$file"
        rm -f "$webp_file"
        local savings=$((original_size - png_size))
        log "  PNG opt: $(basename "$file") | $(format_bytes $original_size) → $(format_bytes $png_size) | Saved: $(format_bytes $savings)"
        return $savings
    else
        rm "$temp_file"
        local savings=$((original_size - webp_size))
        log "  PNG→WebP: $(basename "$file") | $(format_bytes $original_size) → $(format_bytes $webp_size) | Saved: $(format_bytes $savings)"
        return $savings
    fi
}

# Function to optimize WebP files
optimize_webp() {
    local file="$1"
    local temp_file="${file}.tmp"
    local original_size=$(get_file_size "$file")
    
    # Re-optimize WebP
    cwebp -q $WEBP_QUALITY -resize $MAX_WIDTH $MAX_HEIGHT "$file" -o "$temp_file"
    
    if [ -f "$temp_file" ]; then
        local new_size=$(get_file_size "$temp_file")
        if [ $new_size -lt $original_size ]; then
            mv "$temp_file" "$file"
            local savings=$((original_size - new_size))
            log "  WebP opt: $(basename "$file") | $(format_bytes $original_size) → $(format_bytes $new_size) | Saved: $(format_bytes $savings)"
            return $savings
        else
            rm "$temp_file"
        fi
    fi
    return 0
}

# Main optimization function
optimize_images() {
    local total_savings=0
    local files_processed=0
    
    log "${BLUE}Starting image optimization...${NC}"
    log "Configuration:"
    log "  Max dimensions: ${MAX_WIDTH}x${MAX_HEIGHT}"
    log "  JPEG quality: ${JPEG_QUALITY}%"
    log "  WebP quality: ${WEBP_QUALITY}%"
    log ""
    
    # Process files by size (largest first)
    while IFS= read -r -d '' file; do
        local size=$(get_file_size "$file")
        if [ $size -gt 102400 ]; then # Only process files > 100KB
            local savings=0
            local ext="${file##*.}"
            
            case "$(echo "$ext" | tr '[:upper:]' '[:lower:]')" in
                gif)
                    savings=$(optimize_gif "$file")
                    ;;
                jpg|jpeg)
                    savings=$(optimize_jpeg "$file")
                    ;;
                png)
                    savings=$(optimize_png "$file")
                    ;;
                webp)
                    savings=$(optimize_webp "$file")
                    ;;
            esac
            
            total_savings=$((total_savings + savings))
            files_processed=$((files_processed + 1))
        fi
    done < <(find "$IMAGES_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" -o -name "*.webp" \) -size +100k -print0 | sort -z)
    
    log ""
    log "${GREEN}=== OPTIMIZATION COMPLETE ===${NC}"
    log "Files processed: $files_processed"
    log "Total savings: $(format_bytes $total_savings)"
    
    # Calculate percentage savings
    local original_total=$(find "$BACKUP_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" -o -name "*.webp" \) -exec du -cb {} + | tail -1 | cut -f1)
    local current_total=$(find "$IMAGES_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" -o -name "*.webp" \) -exec du -cb {} + | tail -1 | cut -f1)
    local percentage_saved=$(echo "scale=1; ($original_total - $current_total) * 100 / $original_total" | bc)
    
    log "Percentage reduction: ${percentage_saved}%"
}

# Function to generate final report
generate_report() {
    log ""
    log "${BLUE}=== FINAL REPORT ===${NC}"
    
    # List largest remaining files
    log ""
    log "Top 10 largest remaining files:"
    find "$IMAGES_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" -o -name "*.webp" \) -exec ls -lh {} \; | sort -k5 -hr | head -10 | while read -r line; do
        log "  $line"
    done
    
    log ""
    log "Optimization complete! Check $REPORT_FILE for detailed report."
    log "${GREEN}Consider updating your HTML to use the new WebP files where available.${NC}"
}

# Main execution
main() {
    # Initialize report file
    echo "Image Optimization Report - $(date)" > "$REPORT_FILE"
    echo "========================================" >> "$REPORT_FILE"
    
    check_tools
    create_backup
    optimize_images
    generate_report
    
    echo -e "${GREEN}Script completed successfully!${NC}"
}

# Run the script
main "$@"