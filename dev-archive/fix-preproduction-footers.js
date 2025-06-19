#!/usr/bin/env node

/**
 * Fix Pre-Production Services Sub-Pages
 * Add missing footers and component loaders to all pre-production sub-pages
 */

const fs = require('fs');
const path = require('path');

// All pre-production sub-pages that need footer fixes
const preProductionSubPages = [
    'pre-production-services/casting-services/index.html',
    'pre-production-services/catering-services/index.html',
    'pre-production-services/concept-development/index.html',
    'pre-production-services/contract-management/index.html',
    'pre-production-services/cost-estimation/index.html',
    'pre-production-services/covid-compliance/index.html',
    'pre-production-services/creative-direction/index.html',
    'pre-production-services/crew-hiring/index.html',
    'pre-production-services/equipment-planning/index.html',
    'pre-production-services/film-permit-acquisition/index.html',
    'pre-production-services/fixer-services-local/index.html',
    'pre-production-services/licensing-rights/index.html',
    'pre-production-services/line-producing-services/index.html',
    'pre-production-services/location-agreements/index.html',
    'pre-production-services/location-management/index.html',
    'pre-production-services/location-scouting-services/index.html',
    'pre-production-services/moodboard-creation/index.html',
    'pre-production-services/pitch-deck-design/index.html',
    'pre-production-services/production-budgeting/index.html',
    'pre-production-services/production-insurance/index.html',
    'pre-production-services/production-scheduling/index.html',
    'pre-production-services/script-consultation/index.html',
    'pre-production-services/site-surveys/index.html',
    'pre-production-services/storyboarding/index.html',
    'pre-production-services/talent-coordination/index.html',
    'pre-production-services/talent-releases/index.html',
    'pre-production-services/travel-logistics/index.html',
    'pre-production-services/union-talent-management/index.html',
    'pre-production-services/voiceover-casting/index.html',
    'pre-production-services/call-sheets/index.html'
];

function addFooterToPage(filePath) {
    try {
        if (!fs.existsSync(filePath)) {
            console.log(`⚠️  ${filePath} - File not found`);
            return false;
        }

        let content = fs.readFileSync(filePath, 'utf8');
        console.log(`📄 Processing ${filePath}...`);

        // Check if footer is already present
        if (content.includes('footer-container') && content.includes('component-loader.js')) {
            console.log(`ℹ️  ${filePath} - Already has footer and component loader`);
            return true;
        }

        // Create backup
        const backupPath = filePath.replace('.html', '-before-footer-fix.html');
        fs.writeFileSync(backupPath, content, 'utf8');
        console.log(`💾 Created backup: ${backupPath}`);

        // Check if file ends abruptly without proper closing
        const lines = content.split('\n');
        const lastMeaningfulLine = lines.reverse().find(line => line.trim() !== '');
        
        if (lastMeaningfulLine && lastMeaningfulLine.includes('</section>')) {
            // File ends with section, needs main closing, footer, and body/html closing
            const footerContent = `    </main>

    <!-- Dynamic Footer Container -->
    <div id="footer-container">
        <!-- Footer will be loaded here dynamically -->
    </div>

    <!-- Component Loader Script -->
    <script src="/js/component-loader.js"></script>

    <!-- Page-specific JavaScript Integration -->
    <script>
        // Wait for components to load before initializing page-specific functionality
        document.addEventListener('componentsLoaded', function() {
            console.log('Components loaded for ${filePath}, page functionality ready');
            
            // Mobile menu and other functionality handled by component loader
        });
    </script>

</body>
</html>`;

            content = content + footerContent;
            
            // Write the updated content
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✅ ${filePath} - Successfully added footer and component loader`);
            return true;
        } else {
            console.log(`⚠️  ${filePath} - Unexpected file structure, skipping`);
            return false;
        }

    } catch (error) {
        console.log(`❌ ${filePath} - Error: ${error.message}`);
        return false;
    }
}

function main() {
    console.log('🔧 Adding Footers to Pre-Production Sub-Pages');
    console.log('=' + '='.repeat(60));
    console.log('📋 This will:');
    console.log('   • Add missing footer containers to pre-production sub-pages');
    console.log('   • Add component loader scripts');
    console.log('   • Close main, body, and html tags properly');
    console.log('   • Create backups before making changes');
    console.log('=' + '='.repeat(60));

    let successCount = 0;
    const totalCount = preProductionSubPages.length;

    for (const filePath of preProductionSubPages) {
        if (addFooterToPage(filePath)) {
            successCount++;
        }
    }

    console.log(`\n📊 Results: ${successCount}/${totalCount} pages processed successfully`);

    if (successCount === totalCount) {
        console.log('\n🎉 All pre-production sub-pages fixed!');
        console.log('\n🔧 What was accomplished:');
        console.log('   ✅ Added missing footer containers');
        console.log('   ✅ Added component loader scripts');
        console.log('   ✅ Properly closed HTML structure');
        console.log('   ✅ Created backups for all modified files');
        console.log('\n🎯 Result:');
        console.log('   • All pre-production sub-pages now have dynamic footers');
        console.log('   • Consistent navigation across entire website');
        console.log('   • No more missing footers');
    } else {
        console.log('\n⚠️  Some pages had issues. Please review before testing.');
    }
}

if (require.main === module) {
    main();
}

module.exports = { addFooterToPage, preProductionSubPages };
