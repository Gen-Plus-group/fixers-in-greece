#!/usr/bin/env node

/**
 * Safe Dynamic Component Conversion Script
 * Carefully converts pages to use dynamic components while preserving all functionality
 */

const fs = require('fs');
const path = require('path');

// All pages to convert (excluding homepage which already has dynamic components)
const allPages = [
    'about-us/index.html',
    'contact/index.html',
    'film-production-services/index.html',
    'equipment-rental-vietnam/index.html',
    'location-scouting-vietnam/index.html',
    'film-permits-vietnam/index.html',
    'filming-in-vietnam/index.html',
    'portfolio/index.html',
    'clients/index.html',
    'vietnam-filming-locations/index.html',
    'vietnam-film-crew/index.html',
    'documentary-filming-vietnam/index.html',
    'drone-filming-vietnam/index.html',
    'commercial-video-production-vietnam/index.html',
    'news-filming-vietnam/index.html',
    'ho-chi-minh-city-filming/index.html',
    'hanoi-film-production/index.html',
    'casting-services-vietnam/index.html',
    'corporate-video-vietnam/index.html',
    'equipment-transport-vietnam/index.html',
    'event-filming-vietnam/index.html',
    'live-streaming-vietnam/index.html',
    'music-video-production-vietnam/index.html',
    'post-production-vietnam/index.html',
    'translation-services-vietnam/index.html',
    'hire-film-director/index.html',
    'hire-film-producer/index.html',
    'hire-line-producer/index.html',
    'hire-fixer/index.html',
    'hire-dop/index.html',
    'hire-location-manager/index.html'
];

function createBackup(filePath) {
    const backupPath = filePath.replace('.html', '-backup-before-dynamic.html');
    try {
        fs.copyFileSync(filePath, backupPath);
        console.log(`💾 Created backup: ${backupPath}`);
        return true;
    } catch (error) {
        console.log(`❌ Failed to create backup for ${filePath}: ${error.message}`);
        return false;
    }
}

function safelyConvertPage(filePath) {
    try {
        if (!fs.existsSync(filePath)) {
            console.log(`⚠️  ${filePath} - File not found`);
            return false;
        }

        let content = fs.readFileSync(filePath, 'utf8');
        console.log(`📄 Processing ${filePath}...`);

        // Check if already converted
        if (content.includes('id="header-container"') && content.includes('component-loader.js')) {
            console.log(`✅ ${filePath} - Already has dynamic components`);
            return true;
        }

        // Create backup before making changes
        if (!createBackup(filePath)) {
            return false;
        }

        let originalContent = content;

        // 1. Replace header section more carefully
        // Look for the pattern from <!-- Top Bar --> to </header>
        const headerPattern = /<!-- Top Bar -->[\s\S]*?<\/header>/;
        if (headerPattern.test(content)) {
            const headerMatch = content.match(headerPattern);
            console.log(`🔍 ${filePath} - Found header pattern, length: ${headerMatch[0].length} chars`);
            content = content.replace(headerPattern, `    <!-- Dynamic Header Container -->
    <div id="header-container">
        <!-- Header will be loaded here dynamically -->
    </div>`);
            console.log(`🔧 ${filePath} - Header section replaced`);
        } else {
            console.log(`⚠️  ${filePath} - No standard header pattern found, trying alternative`);
            // Try alternative header pattern
            const altHeaderPattern = /<header[\s\S]*?<\/header>/;
            if (altHeaderPattern.test(content)) {
                const altHeaderMatch = content.match(altHeaderPattern);
                console.log(`🔍 ${filePath} - Found alt header pattern, length: ${altHeaderMatch[0].length} chars`);
                content = content.replace(altHeaderPattern, `    <!-- Dynamic Header Container -->
    <div id="header-container">
        <!-- Header will be loaded here dynamically -->
    </div>`);
                console.log(`🔧 ${filePath} - Alternative header pattern replaced`);
            } else {
                console.log(`❌ ${filePath} - No header pattern found at all`);
            }
        }

        // 2. Replace footer section carefully
        const footerPattern = /<!-- Footer -->[\s\S]*?<\/footer>/;
        if (footerPattern.test(content)) {
            const footerMatch = content.match(footerPattern);
            console.log(`🔍 ${filePath} - Found footer pattern, length: ${footerMatch[0].length} chars`);
            content = content.replace(footerPattern, `    <!-- Dynamic Footer Container -->
    <div id="footer-container">
        <!-- Footer will be loaded here dynamically -->
    </div>`);
            console.log(`🔧 ${filePath} - Footer section replaced`);
        } else {
            console.log(`⚠️  ${filePath} - No standard footer pattern found, trying alternative`);
            // Try alternative footer pattern
            const altFooterPattern = /<footer[\s\S]*?<\/footer>/;
            if (altFooterPattern.test(content)) {
                const altFooterMatch = content.match(altFooterPattern);
                console.log(`🔍 ${filePath} - Found alt footer pattern, length: ${altFooterMatch[0].length} chars`);
                content = content.replace(altFooterPattern, `    <!-- Dynamic Footer Container -->
    <div id="footer-container">
        <!-- Footer will be loaded here dynamically -->
    </div>`);
                console.log(`🔧 ${filePath} - Alternative footer pattern replaced`);
            } else {
                console.log(`⚠️  ${filePath} - No footer pattern found, adding container before </body>`);
                // Add footer container before closing body tag if no footer exists
                content = content.replace('</body>', `    <!-- Dynamic Footer Container -->
    <div id="footer-container">
        <!-- Footer will be loaded here dynamically -->
    </div>

</body>`);
                console.log(`📝 ${filePath} - Added footer container`);
            }
        }

        // 3. Preserve existing JavaScript and add component loader
        if (!content.includes('/js/component-loader.js')) {
            // Find the last script tag or before closing body
            const lastScriptMatch = content.lastIndexOf('</script>');
            const bodyCloseMatch = content.lastIndexOf('</body>');
            
            const componentScript = `
    <!-- Component Loader Script -->
    <script src="/js/component-loader.js"></script>

    <!-- Page-specific JavaScript Integration -->
    <script>
        // Wait for components to load before initializing page-specific functionality
        document.addEventListener('componentsLoaded', function() {
            console.log('Components loaded for ${filePath}, page functionality ready');
            
            // Trigger any existing page initialization that might depend on DOM structure
            if (typeof initializePageFunctionality === 'function') {
                initializePageFunctionality();
            }
        });
    </script>

`;

            if (lastScriptMatch > bodyCloseMatch) {
                // Insert after the last script tag
                const insertPos = content.indexOf('</script>', lastScriptMatch) + '</script>'.length;
                content = content.substring(0, insertPos) + componentScript + content.substring(insertPos);
            } else {
                // Insert before closing body tag
                content = content.replace('</body>', componentScript + '</body>');
            }
            
            console.log(`🔧 ${filePath} - Component loader script added`);
        }

        // 4. Ensure proper CSS links are present
        if (!content.includes('/dist/output.css') && !content.includes('tailwindcss')) {
            const headClosePos = content.indexOf('</head>');
            if (headClosePos !== -1) {
                const cssLink = '    <!-- Tailwind CSS -->\n    <link href="/dist/output.css" rel="stylesheet">\n\n';
                content = content.substring(0, headClosePos) + cssLink + content.substring(headClosePos);
                console.log(`🎨 ${filePath} - Tailwind CSS link added`);
            }
        }

        // 5. Validate the conversion
        if (!content.includes('header-container') || !content.includes('footer-container')) {
            console.log(`❌ ${filePath} - Conversion validation failed, restoring original`);
            content = originalContent;
            return false;
        }

        // Write the updated content
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ ${filePath} - Successfully converted to dynamic components`);
        return true;

    } catch (error) {
        console.log(`❌ ${filePath} - Error: ${error.message}`);
        return false;
    }
}

function convertBatch(pages, batchName) {
    console.log(`\n🚀 Converting ${batchName} (${pages.length} pages)...`);
    console.log('=' + '='.repeat(60));
    
    let successCount = 0;
    const results = [];
    
    for (const filePath of pages) {
        const success = safelyConvertPage(filePath);
        results.push({ file: filePath, success });
        if (success) successCount++;
    }
    
    console.log(`\n📊 ${batchName} Results: ${successCount}/${pages.length} pages converted successfully`);
    
    if (successCount < pages.length) {
        console.log('\n⚠️  Failed conversions:');
        results.filter(r => !r.success).forEach(r => console.log(`   • ${r.file}`));
    }
    
    return { successCount, totalCount: pages.length, results };
}

function main() {
    const mode = process.argv[2] || 'test';
    
    console.log('🛡️  Safe Dynamic Component Conversion');
    console.log('=' + '='.repeat(60));
    console.log('📋 This will:');
    console.log('   • Create backups before making changes');
    console.log('   • Replace static headers with dynamic containers');
    console.log('   • Replace static footers with dynamic containers');
    console.log('   • Add component loader script');
    console.log('   • Preserve ALL existing JavaScript functionality');
    console.log('   • Validate conversions before saving');
    console.log('=' + '='.repeat(60));

    if (mode === 'test') {
        // Test mode: convert only a few pages first
        const testPages = [
            'about-us/index.html',
            'contact/index.html',
            'film-production-services/index.html'
        ];
        
        console.log('\n🧪 RUNNING IN TEST MODE');
        console.log('Converting only 3 pages first for testing...');
        
        const result = convertBatch(testPages, 'Test Batch');
        
        if (result.successCount === result.totalCount) {
            console.log('\n🎉 Test conversion successful!');
            console.log('💡 Run with "all" parameter to convert all pages:');
            console.log('   node safe-dynamic-conversion.js all');
        } else {
            console.log('\n⚠️  Test conversion had issues. Please review before proceeding.');
        }
        
    } else if (mode === 'all') {
        // Full conversion mode
        console.log('\n🚀 RUNNING FULL CONVERSION');
        console.log('Converting all pages...');
        
        const result = convertBatch(allPages, 'Full Conversion');
        
        if (result.successCount === result.totalCount) {
            console.log('\n🎉 All pages converted successfully!');
            console.log('\n🔧 What was accomplished:');
            console.log('   ✅ Consistent header/navigation across all pages');
            console.log('   ✅ Consistent footer across all pages');
            console.log('   ✅ Dynamic component loading system implemented');
            console.log('   ✅ Original page functionality preserved');
            console.log('   ✅ Backups created for all modified files');
            console.log('\n🎯 Next steps:');
            console.log('   • Test a few pages in browser');
            console.log('   • Commit changes if everything works');
            console.log('   • Clean up backup files if satisfied');
        } else {
            console.log('\n⚠️  Some conversions failed. Please review before committing.');
        }
    } else {
        console.log('\n📖 Usage:');
        console.log('   node safe-dynamic-conversion.js test    # Convert 3 pages for testing');
        console.log('   node safe-dynamic-conversion.js all     # Convert all pages');
    }
}

if (require.main === module) {
    main();
}

module.exports = { safelyConvertPage, convertBatch, allPages };
