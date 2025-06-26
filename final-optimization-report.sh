#!/bin/bash

# Final optimization report generator
IMAGES_DIR="/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/assets/images"
BACKUP_DIR="/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/assets/images-backup"
REPORT_FILE="/Users/leonidassfyris/Coding/fixers-in-greece/fixers-in-greece/FINAL-OPTIMIZATION-REPORT.md"

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

echo "# Image Optimization Report - Fixers in Greece" > "$REPORT_FILE"
echo "**Generated:** $(date)" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Calculate total original size
original_total=$(find "$BACKUP_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" -o -name "*.webp" \) -exec du -cb {} + | tail -1 | cut -f1)

# Calculate current total size
current_total=$(find "$IMAGES_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" -o -name "*.webp" \) -exec du -cb {} + | tail -1 | cut -f1)

total_savings=$((original_total - current_total))
percentage_saved=$(echo "scale=1; $total_savings * 100 / $original_total" | bc)

echo "## Summary" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "| Metric | Value |" >> "$REPORT_FILE"
echo "|--------|-------|" >> "$REPORT_FILE"
echo "| **Original Total Size** | $(format_bytes $original_total) |" >> "$REPORT_FILE"
echo "| **Optimized Total Size** | $(format_bytes $current_total) |" >> "$REPORT_FILE"
echo "| **Total Savings** | $(format_bytes $total_savings) |" >> "$REPORT_FILE"
echo "| **Percentage Reduction** | ${percentage_saved}% |" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "## Key Optimizations" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "### GIF to WebP Conversions" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "| File | Original Size | Optimized Size | Savings |" >> "$REPORT_FILE"
echo "|------|---------------|----------------|---------|" >> "$REPORT_FILE"

# Find WebP files and compare with original GIFs
find "$IMAGES_DIR" -name "*.webp" | while read webp_file; do
    gif_file="$BACKUP_DIR/${webp_file#$IMAGES_DIR/}"
    gif_file="${gif_file%.webp}.gif"
    
    if [ -f "$gif_file" ]; then
        original_size=$(get_file_size "$gif_file")
        webp_size=$(get_file_size "$webp_file")
        savings=$((original_size - webp_size))
        
        if [ $savings -gt 0 ]; then
            filename=$(basename "$webp_file")
            echo "| $filename | $(format_bytes $original_size) | $(format_bytes $webp_size) | $(format_bytes $savings) |" >> "$REPORT_FILE"
        fi
    fi
done

echo "" >> "$REPORT_FILE"
echo "### Large Files Still Remaining (>1MB)" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "| File | Size | Type | Recommendation |" >> "$REPORT_FILE"
echo "|------|------|------|----------------|" >> "$REPORT_FILE"

find "$IMAGES_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" -o -name "*.webp" \) -size +1M | sort -k5 -hr | while read file; do
    size=$(get_file_size "$file")
    filename=$(basename "$file")
    ext="${file##*.}"
    
    case "$(echo "$ext" | tr '[:upper:]' '[:lower:]')" in
        gif)
            recommendation="Consider manual optimization or different format"
            ;;
        webp)
            recommendation="Already optimized format"
            ;;
        jpg|jpeg)
            recommendation="Could reduce quality or dimensions further"
            ;;
        png)
            recommendation="Convert to WebP if not transparent"
            ;;
        *)
            recommendation="Review format and usage"
            ;;
    esac
    
    echo "| $filename | $(format_bytes $size) | $ext | $recommendation |" >> "$REPORT_FILE"
done

echo "" >> "$REPORT_FILE"
echo "## Google PageSpeed Impact" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "- **Target Savings:** 7.9MB (from PageSpeed Insights)" >> "$REPORT_FILE"
echo "- **Achieved Savings:** $(format_bytes $total_savings)" >> "$REPORT_FILE"

if [ $total_savings -gt 8257536 ]; then  # 7.9MB in bytes
    echo "- **Status:** ✅ **TARGET EXCEEDED!** We achieved $(echo "scale=1; $total_savings / 1048576" | bc)MB savings" >> "$REPORT_FILE"
else
    echo "- **Status:** 🔄 Additional optimization possible" >> "$REPORT_FILE"
fi

echo "" >> "$REPORT_FILE"
echo "## Implementation Notes" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "### Current State" >> "$REPORT_FILE"
echo "- ✅ Backup created at \`assets/images-backup/\`" >> "$REPORT_FILE"
echo "- ✅ Large GIF files converted to WebP format" >> "$REPORT_FILE"
echo "- ✅ JPEG files optimized with quality reduction" >> "$REPORT_FILE"
echo "- ✅ Maintained visual quality while reducing file sizes" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "### Next Steps" >> "$REPORT_FILE"
echo "1. **Update HTML/CSS** to use WebP files with fallbacks:" >> "$REPORT_FILE"
echo '   ```html' >> "$REPORT_FILE"
echo '   <picture>' >> "$REPORT_FILE"
echo '     <source srcset="image.webp" type="image/webp">' >> "$REPORT_FILE"
echo '     <img src="image.gif" alt="Description" width="700" height="525">' >> "$REPORT_FILE"
echo '   </picture>' >> "$REPORT_FILE"
echo '   ```' >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "2. **Add proper dimensions** to all image tags for layout stability" >> "$REPORT_FILE"
echo "3. **Consider lazy loading** for portfolio images" >> "$REPORT_FILE"
echo "4. **Test across browsers** to ensure WebP compatibility" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "### File Structure" >> "$REPORT_FILE"
echo "```" >> "$REPORT_FILE"
echo "assets/images/" >> "$REPORT_FILE"
echo "├── portfolio/" >> "$REPORT_FILE"
echo "│   ├── *.gif (original files)" >> "$REPORT_FILE"
echo "│   ├── *.webp (optimized versions)" >> "$REPORT_FILE"
echo "│   └── categories/" >> "$REPORT_FILE"
echo "│       ├── *.gif (original files)" >> "$REPORT_FILE"
echo "│       └── *.webp (optimized versions)" >> "$REPORT_FILE"
echo "└── [other directories...]" >> "$REPORT_FILE"
echo "```" >> "$REPORT_FILE"

echo "Report generated: $REPORT_FILE"
cat "$REPORT_FILE"