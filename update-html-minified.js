#!/usr/bin/env node

/**
 * HTML Update Script for Minified Assets
 * Updates all HTML files to reference minified CSS and JS files
 */

const fs = require('fs');
const path = require('path');
const glob = require('glob');

// Get current date for cache busting
const cacheVersion = new Date().toISOString().slice(0, 10).replace(/-/g, '');

// Asset mappings for replacement
const assetMappings = [
    // CSS files
    { from: '/css/base.css', to: `/css/base.min.css?v=${cacheVersion}` },
    { from: '/css/components.css', to: `/css/components.min.css?v=${cacheVersion}` },
    { from: '/css/layout.css', to: `/css/layout.min.css?v=${cacheVersion}` },
    { from: '/css/theme.css', to: `/css/theme.min.css?v=${cacheVersion}` },
    { from: '/css/critical.css', to: `/css/critical.min.css?v=${cacheVersion}` },
    { from: '/mobile-menu.css', to: `/mobile-menu.min.css?v=${cacheVersion}` },
    { from: '/dark-theme.css', to: `/dark-theme.min.css?v=${cacheVersion}` },
    { from: '/portfolio-spacing-fix.css', to: `/portfolio-spacing-fix.min.css?v=${cacheVersion}` },
    { from: '/seo-optimizations.css', to: `/seo-optimizations.min.css?v=${cacheVersion}` },
    
    // JavaScript files
    { from: '/js/component-loader.js', to: `/js/component-loader.min.js?v=${cacheVersion}` },
    { from: '/js/inline-components.js', to: `/js/inline-components.min.js?v=${cacheVersion}` },
    
    // Handle versioned files
    { from: /\/css\/base\.css\?v=\d+/g, to: `/css/base.min.css?v=${cacheVersion}` },
    { from: /\/css\/components\.css\?v=\d+/g, to: `/css/components.min.css?v=${cacheVersion}` },
    { from: /\/css\/layout\.css\?v=\d+/g, to: `/css/layout.min.css?v=${cacheVersion}` },
    { from: /\/css\/theme\.css\?v=\d+/g, to: `/css/theme.min.css?v=${cacheVersion}` },
    { from: /\/js\/component-loader\.js\?v=\d+/g, to: `/js/component-loader.min.js?v=${cacheVersion}` },
    { from: /\/js\/inline-components\.js\?v=\d+/g, to: `/js/inline-components.min.js?v=${cacheVersion}` },
];

// Function to update HTML file
function updateHtmlFile(filePath) {
    try {
        console.log(`Processing: ${filePath}`);
        let content = fs.readFileSync(filePath, 'utf8');
        let changes = 0;
        
        // Apply all mappings
        assetMappings.forEach(mapping => {
            if (mapping.from instanceof RegExp) {
                // Handle regex patterns
                const matches = content.match(mapping.from);
                if (matches) {
                    content = content.replace(mapping.from, mapping.to);
                    changes += matches.length;
                }
            } else {
                // Handle string patterns
                const beforeCount = (content.match(new RegExp(escapeRegExp(mapping.from), 'g')) || []).length;
                content = content.replace(new RegExp(escapeRegExp(mapping.from), 'g'), mapping.to);
                changes += beforeCount;
            }
        });
        
        if (changes > 0) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✓ Updated ${path.basename(filePath)} (${changes} asset references updated)`);
            return changes;
        } else {
            console.log(`- No changes needed for ${path.basename(filePath)}`);
            return 0;
        }
    } catch (error) {
        console.error(`✗ Error updating ${filePath}:`, error.message);
        return 0;
    }
}

// Escape string for regex
function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// Function to find all HTML files
function findHtmlFiles() {
    const htmlFiles = [];
    
    // Add main HTML files
    const mainFiles = [
        'index.html',
        'template-page.html',
        '404.html',
        'form-success.html',
        'thank-you-page.html',
        'test.html',
        'test-components.html',
        'css-test.html',
        'test-contact-form.html'
    ];
    
    mainFiles.forEach(file => {
        if (fs.existsSync(file)) {
            htmlFiles.push(file);
        }
    });
    
    // Find HTML files in subdirectories (production pages)
    const patterns = [
        '**/index.html',
        '!node_modules/**',
        '!wordpress-backup-*/**',
        '!dev-archive/**',
        '!temp-clone/**'
    ];
    
    try {
        // Using a simple directory traversal since glob might not be available
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
        
    } catch (error) {
        console.log('Using fallback HTML file discovery method');
    }
    
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
console.log('🔄 Updating HTML files to use minified assets...\n');
console.log(`Cache version: ${cacheVersion}\n`);

const htmlFiles = findHtmlFiles();
console.log(`Found ${htmlFiles.length} HTML files to process\n`);

let totalChanges = 0;
let filesUpdated = 0;

htmlFiles.forEach(file => {
    const changes = updateHtmlFile(file);
    totalChanges += changes;
    if (changes > 0) {
        filesUpdated++;
    }
});

console.log(`\n📊 Update Summary:`);
console.log(`✓ Files processed: ${htmlFiles.length}`);
console.log(`✓ Files updated: ${filesUpdated}`);
console.log(`✓ Total asset references updated: ${totalChanges}`);
console.log(`✓ Cache version applied: ${cacheVersion}`);

console.log(`\n✨ HTML update complete!`);
console.log(`\n📝 All HTML files now reference minified assets with cache busting.`);