#!/usr/bin/env node

/**
 * Convert all pages to use dynamic component loading system
 * Preserves original content while replacing header/footer with dynamic containers
 */

const fs = require('fs');
const path = require('path');

/ List of all HTML files to update (excluding homepage which already has dynamic components)
const htmlFiles = [
    'about-us/index.html',
    'contact/index.html',
    'film-production-services/index.html',
    'equipment-rental-Greece/index.html',
    'location-scouting-Greece/index.html',
    'film-permits-Greece/index.html',
    'filming-in-Greece/index.html',
    'portfolio/index.html',
    'clients/index.html',
    'Greece-filming-locations/index.html',
    'Greece-film-crew/index.html',
    'documentary-filming-Greece/index.html',
    'drone-filming-Greece/index.html',
    'commercial-video-production-Greece/index.html',
    'news-filming-Greece/index.html',
    'ho-chi-minh-city-filming/index.html',
    'Athens-film-production/index.html',
    'casting-services-Greece/index.html',
    'corporate-video-Greece/index.html',
    'equipment-transport-Greece/index.html',
    'event-filming-Greece/index.html',
    'live-streaming-Greece/index.html',
    'music-video-production-Greece/index.html',
    'post-production-Greece/index.html',
    'translation-services-Greece/index.html',
    'hire-film-director/index.html',
    'hire-film-producer/index.html',
    'hire-line-producer/index.html',
    'hire-fixer/index.html',
    'hire-dop/index.html',
    'hire-location-manager/index.html'
];

function convertPageToDynamicComponents(filePath) {
    try {
        if (!fs.existsSync(filePath)) {
            console.log(`⚠️  ${filePath} - File not found`);
            return false;
        }

        let content = fs.readFileSync(filePath, 'utf8');
        console.log(`📄 Processing ${filePath}...`);

        / Check if already converted
        if (content.includes('id="header-container"') && content.includes('component-loader.js')) {
            console.log(`✅ ${filePath} - Already has dynamic components`);
            return true;
        }

        / 1. Replace header section (from <!-- Top Bar --> or <header> to </header>)
        const headerPatterns = [
            /<!-- Top Bar -->.*?<\/header>/gs,
            /<header[^>]*>.*?<\/header>/gs
        ];

        let headerReplaced = false;
        for (const pattern of headerPatterns) {
            if (pattern.test(content)) {
                content = content.replace(pattern, `    <!-- Dynamic Header Container -->
    <div id="header-container">
        <!-- Header will be loaded here dynamically -->
    </div>`);
                headerReplaced = true;
                break;
            }
        }

        if (!headerReplaced) {
            console.log(`⚠️  ${filePath} - No header found to replace`);
        }

        / 2. Replace footer section (from <!-- Footer --> or <footer> to </footer>)
        const footerPatterns = [
            /<!-- Footer -->.*?<\/footer>/gs,
            /<footer[^>]*>.*?<\/footer>/gs
        ];

        let footerReplaced = false;
        for (const pattern of footerPatterns) {
            if (pattern.test(content)) {
                content = content.replace(pattern, `    <!-- Dynamic Footer Container -->
    <div id="footer-container">
        <!-- Footer will be loaded here dynamically -->
    </div>`);
                footerReplaced = true;
                break;
            }
        }

        if (!footerReplaced) {
            / Add footer container before closing body tag if no footer exists
            content = content.replace('</body>', `    <!-- Dynamic Footer Container -->
    <div id="footer-container">
        <!-- Footer will be loaded here dynamically -->
    </div>

</body>`);
            console.log(`📝 ${filePath} - Added footer container`);
        }

        / 3. Add component loader script before closing body tag if not present
        if (!content.includes('/js/component-loader.js')) {
            const scriptTag = `    <!-- Component Loader Script -->
    <script src="/js/component-loader.js"></script>

    <!-- Page-specific JavaScript -->
    <script>
        / Wait for components to load before initializing page-specific functionality
        document.addEventListener('componentsLoaded', function() {
            console.log('Components loaded, initializing page functionality...');
            
            / Any existing page-specific JavaScript can be moved here
        });
    </script>

`;
            / Insert before existing scripts or before closing body tag
            if (content.includes('<script>')) {
                const scriptPos = content.lastIndexOf('</body>');
                const beforeBody = content.substring(0, scriptPos);
                const afterBody = content.substring(scriptPos);
                content = beforeBody + scriptTag + afterBody;
            } else {
                content = content.replace('</body>', scriptTag + '</body>');
            }
        }

        / 4. Ensure proper CSS links are present
        if (!content.includes('/dist/output.css') && !content.includes('tailwindcss')) {
            / Add Tailwind CSS if not present
            const headClosePos = content.indexOf('</head>');
            if (headClosePos !== -1) {
                const cssLink = '    <!-- Tailwind CSS -->\n    <link href="/dist/output.css" rel="stylesheet">\n\n';
                content = content.substring(0, headClosePos) + cssLink + content.substring(headClosePos);
            }
        }

        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ ${filePath} - Successfully converted to dynamic components`);
        return true;

    } catch (error) {
        console.log(`❌ ${filePath} - Error: ${error.message}`);
        return false;
    }
}

function main() {
    console.log('🚀 Converting all pages to use dynamic component loading...');
    console.log('=' + '='.repeat(70));
    console.log('📋 This will:');
    console.log('   • Replace static headers with dynamic header containers');
    console.log('   • Replace static footers with dynamic footer containers');
    console.log('   • Add component loader script to each page');
    console.log('   • Preserve ALL original page content and functionality');
    console.log('   • Skip homepage (already has dynamic components)');
    console.log('=' + '='.repeat(70));

    let successCount = 0;
    const totalCount = htmlFiles.length;

    for (const filePath of htmlFiles) {
        if (convertPageToDynamicComponents(filePath)) {
            successCount++;
        }
    }

    console.log('\n' + '='.repeat(70));
    console.log(`📊 Conversion completed: ${successCount}/${totalCount} files updated`);

    if (successCount === totalCount) {
        console.log('🎉 All pages have been successfully converted to dynamic components!');
        console.log('\n🔧 What was accomplished:');
        console.log('   ✅ Consistent header/navigation across all pages');
        console.log('   ✅ Consistent footer across all pages');
        console.log('   ✅ Dynamic component loading system implemented');
        console.log('   ✅ Original page content and functionality preserved');
        console.log('   ✅ Component loader script added to all pages');
        console.log('\n🎯 Next steps:');
        console.log('   • Test the dynamic components on a few pages');
        console.log('   • Commit and push changes to repository');
        console.log('   • Verify navigation consistency across the website');
    } else {
        console.log(`⚠️  ${totalCount - successCount} files had issues and may need manual review`);
    }
}

if (require.main === module) {
    main();
}

module.exports = { convertPageToDynamicComponents, htmlFiles };
