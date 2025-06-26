#!/usr/bin/env node

/**
 * Fix Duplicate Cache Version Script
 * Fixes URLs that ended up with duplicate cache version parameters
 */

const fs = require('fs');
const path = require('path');

// Function to fix duplicate cache versions in a file
function fixDuplicateCacheVersions(filePath) {
    try {
        console.log(`Processing: ${filePath}`);
        let content = fs.readFileSync(filePath, 'utf8');
        
        // Fix pattern: ?v=YYYYMMDD?v=YYYYMMDD -> ?v=YYYYMMDD
        const fixes = [
            {
                pattern: /\?v=(\d{8})\?v=\d{8}/g,
                replacement: '?v=$1'
            }
        ];
        
        let changes = 0;
        fixes.forEach(fix => {
            const matches = content.match(fix.pattern);
            if (matches) {
                content = content.replace(fix.pattern, fix.replacement);
                changes += matches.length;
            }
        });
        
        if (changes > 0) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✓ Fixed ${path.basename(filePath)} (${changes} duplicate cache versions fixed)`);
            return changes;
        } else {
            console.log(`- No duplicates in ${path.basename(filePath)}`);
            return 0;
        }
    } catch (error) {
        console.error(`✗ Error fixing ${filePath}:`, error.message);
        return 0;
    }
}

// Function to find all HTML files
function findHtmlFiles() {
    const htmlFiles = [];
    
    // Add main HTML files
    const mainFiles = [
        'index.html',
        'template-page.html',
        '404.html',
        'css-test.html',
        'test-components.html'
    ];
    
    mainFiles.forEach(file => {
        if (fs.existsSync(file)) {
            htmlFiles.push(file);
        }
    });
    
    // Find HTML files in subdirectories
    const directories = [
        'pre-production-services',
        'production-services', 
        'post-production-services',
        'content-production',
        'film-crew',
        'portfolio-category',
        'about-us',
        'contact',
        'portfolio',
        'clients',
        'filming-in-greece'
    ];
    
    directories.forEach(dir => {
        if (fs.existsSync(dir)) {
            findHtmlFilesRecursive(dir, htmlFiles);
        }
    });
    
    return htmlFiles;
}

// Recursive function to find HTML files
function findHtmlFilesRecursive(dir, htmlFiles) {
    const items = fs.readdirSync(dir);
    
    items.forEach(item => {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);
        
        if (stat.isDirectory()) {
            findHtmlFilesRecursive(fullPath, htmlFiles);
        } else if (item === 'index.html') {
            htmlFiles.push(fullPath);
        }
    });
}

// Main execution
console.log('🔧 Fixing duplicate cache version parameters...\n');

const htmlFiles = findHtmlFiles();
console.log(`Found ${htmlFiles.length} HTML files to process\n`);

let totalChanges = 0;
let filesFixed = 0;

htmlFiles.forEach(file => {
    const changes = fixDuplicateCacheVersions(file);
    totalChanges += changes;
    if (changes > 0) {
        filesFixed++;
    }
});

console.log(`\n📊 Fix Summary:`);
console.log(`✓ Files processed: ${htmlFiles.length}`);
console.log(`✓ Files fixed: ${filesFixed}`);
console.log(`✓ Total duplicate cache versions fixed: ${totalChanges}`);

console.log(`\n✨ Cache version fix complete!`);