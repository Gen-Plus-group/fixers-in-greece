#!/usr/bin/env node

/**
 * Add Cache Version Query Strings to HTML Files
 * This script adds version query parameters to CSS and JS files in all HTML files
 */

const fs = require('fs');
const path = require('path');
const glob = require('glob');

// Version number - update this when assets change
const ASSET_VERSION = '1.0.0';
const VERSION_DATE = new Date().toISOString().split('T')[0].replace(/-/g, '');

// Files to skip
const SKIP_PATTERNS = [
    'node_modules/**',
    'wordpress-backup*/**',
    'temp-clone/**',
    'backup/**',
    'dev-archive/**'
];

// Process HTML files
function processHTMLFiles() {
    console.log('Adding cache version strings to HTML files...');
    
    // Find all HTML files
    const htmlFiles = glob.sync('**/*.html', { 
        ignore: SKIP_PATTERNS 
    });
    
    let filesProcessed = 0;
    let linksUpdated = 0;
    
    htmlFiles.forEach(file => {
        try {
            let content = fs.readFileSync(file, 'utf8');
            let originalContent = content;
            
            // Skip if file already has versioning
            if (content.includes('?v=')) {
                console.log(`⏭️  Skipping ${file} (already has versions)`);
                return;
            }
            
            // Add version to CSS files
            content = content.replace(
                /<link([^>]*?)href=["']([^"']+\.css)["']([^>]*?)>/gi,
                (match, before, cssPath, after) => {
                    // Skip external URLs
                    if (cssPath.startsWith('http://') || cssPath.startsWith('https://') || cssPath.startsWith('//')) {
                        return match;
                    }
                    linksUpdated++;
                    return `<link${before}href="${cssPath}?v=${VERSION_DATE}"${after}>`;
                }
            );
            
            // Add version to JS files
            content = content.replace(
                /<script([^>]*?)src=["']([^"']+\.js)["']([^>]*?)>/gi,
                (match, before, jsPath, after) => {
                    // Skip external URLs
                    if (jsPath.startsWith('http://') || jsPath.startsWith('https://') || jsPath.startsWith('//')) {
                        return match;
                    }
                    linksUpdated++;
                    return `<script${before}src="${jsPath}?v=${VERSION_DATE}"${after}>`;
                }
            );
            
            // Only write if content changed
            if (content !== originalContent) {
                fs.writeFileSync(file, content, 'utf8');
                filesProcessed++;
                console.log(`✅ Updated ${file}`);
            }
            
        } catch (error) {
            console.error(`❌ Error processing ${file}:`, error.message);
        }
    });
    
    console.log(`\n✨ Cache versioning complete!`);
    console.log(`📁 Files processed: ${filesProcessed}`);
    console.log(`🔗 Links updated: ${linksUpdated}`);
    console.log(`📅 Version: ${VERSION_DATE}`);
}

// Run the script
if (require.main === module) {
    processHTMLFiles();
}

module.exports = { processHTMLFiles };