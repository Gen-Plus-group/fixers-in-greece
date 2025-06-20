#!/bin/bash

# Script to fix geographic coordinates from Vietnam to Greece across all HTML files
# Vietnam coordinates: 14.0583;108.2772 -> Greece coordinates: 37.9838;23.7275

echo "Starting coordinate replacement for Greece..."
echo "=========================================="

# Count total files to process
TOTAL_FILES=$(find . -name "*.html" | wc -l)
echo "Found $TOTAL_FILES HTML files to process"
echo ""

# Initialize counters
UPDATED_FILES=0
TOTAL_REPLACEMENTS=0

# Function to process a single file
process_file() {
    local file="$1"
    local changes_made=0
    local temp_file="${file}.tmp"
    
    # Copy original file to temp for processing
    cp "$file" "$temp_file"
    
    # 1. Replace geo.region from VN to GR
    if sed -i 's/geo\.region.*content="VN"/geo.region" content="GR"/g' "$temp_file" 2>/dev/null; then
        if ! cmp -s "$file" "$temp_file"; then
            ((changes_made++))
        fi
    fi
    
    # 2. Replace geo.position coordinates (Vietnam to Greece)
    if sed -i 's/geo\.position.*content="14\.0583;108\.2772"/geo.position" content="37.9838;23.7275"/g' "$temp_file" 2>/dev/null; then
        if ! cmp -s "$file" "$temp_file"; then
            ((changes_made++))
        fi
    fi
    
    # 3. Replace ICBM coordinates
    if sed -i 's/ICBM.*content="14\.0583, 108\.2772"/ICBM" content="37.9838, 23.7275"/g' "$temp_file" 2>/dev/null; then
        if ! cmp -s "$file" "$temp_file"; then
            ((changes_made++))
        fi
    fi
    
    # 4. Replace addressCountry from VN to GR
    if sed -i 's/"addressCountry": "VN"/"addressCountry": "GR"/g' "$temp_file" 2>/dev/null; then
        if ! cmp -s "$file" "$temp_file"; then
            ((changes_made++))
        fi
    fi
    
    # 5. Replace latitude/longitude in structured data (Ho Chi Minh coordinates)
    if sed -i 's/"latitude": "10\.8231"/"latitude": "37.9838"/g' "$temp_file" 2>/dev/null; then
        if ! cmp -s "$file" "$temp_file"; then
            ((changes_made++))
        fi
    fi
    
    if sed -i 's/"longitude": "106\.6297"/"longitude": "23.7275"/g' "$temp_file" 2>/dev/null; then
        if ! cmp -s "$file" "$temp_file"; then
            ((changes_made++))
        fi
    fi
    
    # 6. Replace any other Vietnam coordinates that might be present
    if sed -i 's/14\.0583/37.9838/g' "$temp_file" 2>/dev/null; then
        if ! cmp -s "$file" "$temp_file"; then
            ((changes_made++))
        fi
    fi
    
    if sed -i 's/108\.2772/23.7275/g' "$temp_file" 2>/dev/null; then
        if ! cmp -s "$file" "$temp_file"; then
            ((changes_made++))
        fi
    fi
    
    # 7. Replace Ho Chi Minh coordinates
    if sed -i 's/10\.8231/37.9838/g' "$temp_file" 2>/dev/null; then
        if ! cmp -s "$file" "$temp_file"; then
            ((changes_made++))
        fi
    fi
    
    if sed -i 's/106\.6297/23.7275/g' "$temp_file" 2>/dev/null; then
        if ! cmp -s "$file" "$temp_file"; then
            ((changes_made++))
        fi
    fi
    
    # Check if any changes were made
    if ! cmp -s "$file" "$temp_file"; then
        mv "$temp_file" "$file"
        echo "✓ Updated: $file ($changes_made replacements)"
        ((UPDATED_FILES++))
        TOTAL_REPLACEMENTS=$((TOTAL_REPLACEMENTS + changes_made))
        return 1
    else
        rm "$temp_file"
        return 0
    fi
}

# Process all HTML files
echo "Processing files..."
echo "==================="

while IFS= read -r -d '' file; do
    if [[ -f "$file" ]]; then
        process_file "$file"
    fi
done < <(find . -name "*.html" -print0)

echo ""
echo "Summary:"
echo "========"
echo "Total HTML files found: $TOTAL_FILES"
echo "Files updated: $UPDATED_FILES"
echo "Total replacements made: $TOTAL_REPLACEMENTS"
echo ""

if [ $UPDATED_FILES -gt 0 ]; then
    echo "✓ Coordinate replacement completed successfully!"
    echo "Vietnam coordinates have been replaced with Greece coordinates:"
    echo "  • geo.region: VN → GR"
    echo "  • Coordinates: 14.0583;108.2772 → 37.9838;23.7275 (Athens)"
    echo "  • ICBM: 14.0583, 108.2772 → 37.9838, 23.7275"
    echo "  • addressCountry: VN → GR"
    echo "  • Structured data coordinates updated"
else
    echo "No files required updates."
fi