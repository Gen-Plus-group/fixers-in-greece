#!/usr/bin/env node

/**
 * Asset Minification Script for Fixers in Greece Website
 * Minifies CSS and JavaScript files for production use
 */

const fs = require('fs');
const path = require('path');

// Simple CSS minifier
function minifyCSS(css) {
    return css
        // Remove comments
        .replace(/\/\*[\s\S]*?\*\//g, '')
        // Remove unnecessary whitespace
        .replace(/\s+/g, ' ')
        // Remove spaces around certain characters
        .replace(/\s*([{}:;,>+~])\s*/g, '$1')
        // Remove trailing semicolons before closing braces
        .replace(/;}/g, '}')
        // Remove unnecessary quotes from urls
        .replace(/url\((['"]?)([^'")]+)\1\)/g, 'url($2)')
        // Remove leading/trailing whitespace
        .trim();
}

// Simple JS minifier (basic)
function minifyJS(js) {
    return js
        // Remove single-line comments (but keep URLs intact)
        .replace(/(?:^|\n|\r)\s*\/\/.*$/gm, '')
        // Remove multi-line comments
        .replace(/\/\*[\s\S]*?\*\//g, '')
        // Remove extra whitespace
        .replace(/\s+/g, ' ')
        // Remove spaces around operators and punctuation
        .replace(/\s*([{}()[\];,=+\-*\/])\s*/g, '$1')
        // Remove trailing semicolons where safe
        .replace(/;}/g, '}')
        // Remove leading/trailing whitespace
        .trim();
}

// File processing function
function processFile(inputPath, outputPath, minifyFunction) {
    try {
        console.log(`Processing: ${inputPath}`);
        const content = fs.readFileSync(inputPath, 'utf8');
        const minified = minifyFunction(content);
        const savings = ((content.length - minified.length) / content.length * 100).toFixed(1);
        
        // Create directory if it doesn't exist
        const dir = path.dirname(outputPath);
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }
        
        fs.writeFileSync(outputPath, minified, 'utf8');
        console.log(`✓ Minified: ${path.basename(inputPath)} (${savings}% smaller)`);
        console.log(`  Original: ${content.length} bytes → Minified: ${minified.length} bytes`);
        return true;
    } catch (error) {
        console.error(`✗ Error processing ${inputPath}:`, error.message);
        return false;
    }
}

// Main execution
console.log('🚀 Starting asset minification...\n');

// Define files to minify
const filesToProcess = [
    // CSS files
    { input: 'css/base.css', output: 'css/base.min.css', type: 'css' },
    { input: 'css/components.css', output: 'css/components.min.css', type: 'css' },
    { input: 'css/layout.css', output: 'css/layout.min.css', type: 'css' },
    { input: 'css/theme.css', output: 'css/theme.min.css', type: 'css' },
    { input: 'css/critical.css', output: 'css/critical.min.css', type: 'css' },
    { input: 'mobile-menu.css', output: 'mobile-menu.min.css', type: 'css' },
    { input: 'dark-theme.css', output: 'dark-theme.min.css', type: 'css' },
    { input: 'portfolio-spacing-fix.css', output: 'portfolio-spacing-fix.min.css', type: 'css' },
    { input: 'seo-optimizations.css', output: 'seo-optimizations.min.css', type: 'css' },
    
    // JavaScript files
    { input: 'js/component-loader.js', output: 'js/component-loader.min.js', type: 'js' },
    { input: 'js/inline-components.js', output: 'js/inline-components.min.js', type: 'js' },
];

let successful = 0;
let failed = 0;

filesToProcess.forEach(file => {
    const inputPath = path.resolve(file.input);
    const outputPath = path.resolve(file.output);
    
    // Check if input file exists
    if (!fs.existsSync(inputPath)) {
        console.log(`⚠ Skipping ${file.input} (file not found)`);
        return;
    }
    
    const minifyFunction = file.type === 'css' ? minifyCSS : minifyJS;
    const success = processFile(inputPath, outputPath, minifyFunction);
    
    if (success) {
        successful++;
    } else {
        failed++;
    }
});

console.log(`\n📊 Minification Summary:`);
console.log(`✓ Successfully minified: ${successful} files`);
if (failed > 0) {
    console.log(`✗ Failed to minify: ${failed} files`);
}

// Create a simple HTML update script suggestion
console.log(`\n📝 Next steps:`);
console.log(`1. Update HTML files to reference .min.css and .min.js files`);
console.log(`2. Add cache-busting parameters (e.g., ?v=20250626)`);
console.log(`3. Test all pages to ensure functionality is preserved`);

console.log(`\n✨ Asset minification complete!`);