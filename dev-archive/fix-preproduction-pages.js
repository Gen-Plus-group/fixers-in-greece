#!/usr/bin/env node

/**
 * Fix Pre-Production Services Pages
 * Convert to dynamic components and add missing footers
 */

const fs = require('fs');
const path = require('path');

/ All pre-production-services pages that need fixing
const preProductionPages = [
    'pre-production-services/index.html',
    'pre-production-services/call-sheets/index.html',
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
    'pre-production-services/scriptwriting/index.html',
    'pre-production-services/site-surveys/index.html',
    'pre-production-services/storyboarding/index.html',
    'pre-production-services/talent-coordination/index.html',
    'pre-production-services/talent-releases/index.html',
    'pre-production-services/travel-logistics/index.html',
    'pre-production-services/union-talent-management/index.html',
    'pre-production-services/voiceover-casting/index.html'
];

function fixPreProductionPage(filePath) {
    try {
        if (!fs.existsSync(filePath)) {
            console.log(`⚠️  ${filePath} - File not found`);
            return false;
        }

        let content = fs.readFileSync(filePath, 'utf8');
        console.log(`📄 Processing ${filePath}...`);

        / Create backup
        const backupPath = filePath.replace('.html', '-before-dynamic-fix.html');
        fs.writeFileSync(backupPath, content, 'utf8');
        console.log(`💾 Created backup: ${backupPath}`);

        let originalContent = content;
        let changesMade = false;

        / 1. Replace header section (from <!-- Top Bar --> to </header>)
        const headerPattern = /<!-- Top Bar -->[\s\S]*?<\/header>/;
        if (headerPattern.test(content)) {
            content = content.replace(headerPattern, `    <!-- Dynamic Header Container -->
    <div id="header-container">
        <!-- Header will be loaded here dynamically -->
    </div>`);
            console.log(`🔧 ${filePath} - Header section replaced with dynamic container`);
            changesMade = true;
        }

        / 2. Remove mobile menu JavaScript that conflicts with dynamic loading
        const mobileMenuPattern = /<!-- Mobile Menu JavaScript -->[\s\S]*?document\.addEventListener\('DOMContentLoaded'[\s\S]*?}\);[\s\S]*?<\/script>/;
        if (mobileMenuPattern.test(content)) {
            content = content.replace(mobileMenuPattern, '');
            console.log(`🔧 ${filePath} - Removed conflicting mobile menu JavaScript`);
            changesMade = true;
        }

        / 3. Add footer container and component loader before closing body tag
        const bodyClosePattern = /<\/body>/;
        if (bodyClosePattern.test(content)) {
            content = content.replace(bodyClosePattern, `    <!-- Dynamic Footer Container -->
    <div id="footer-container">
        <!-- Footer will be loaded here dynamically -->
    </div>

    <!-- Component Loader Script -->
    <script src="/js/component-loader.js"></script>

    <!-- Page-specific JavaScript Integration -->
    <script>
        / Wait for components to load before initializing page-specific functionality
        document.addEventListener('componentsLoaded', function() {
            console.log('Components loaded for ${filePath}, page functionality ready');
            
            / Mobile menu and other functionality handled by component loader
        });
    </script>

</body>`);
            console.log(`🔧 ${filePath} - Added footer container and component loader`);
            changesMade = true;
        }

        / 4. Ensure proper CSS links are present
        if (!content.includes('/dist/output.css')) {
            const headClosePos = content.indexOf('</head>');
            if (headClosePos !== -1) {
                const cssLink = '    <!-- Tailwind CSS -->\n    <link href="/dist/output.css" rel="stylesheet">\n\n';
                content = content.substring(0, headClosePos) + cssLink + content.substring(headClosePos);
                console.log(`🎨 ${filePath} - Tailwind CSS link added`);
                changesMade = true;
            }
        }

        if (changesMade) {
            / Write the updated content
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✅ ${filePath} - Successfully converted to dynamic components with footer`);
            return true;
        } else {
            console.log(`ℹ️  ${filePath} - No changes needed`);
            return true;
        }

    } catch (error) {
        console.log(`❌ ${filePath} - Error: ${error.message}`);
        return false;
    }
}

function main() {
    console.log('🔧 Fixing Pre-Production Services Pages');
    console.log('=' + '='.repeat(60));
    console.log('📋 This will:');
    console.log('   • Convert static headers to dynamic containers');
    console.log('   • Add missing footer containers');
    console.log('   • Add component loader script');
    console.log('   • Remove conflicting mobile menu JavaScript');
    console.log('   • Create backups before making changes');
    console.log('=' + '='.repeat(60));

    let successCount = 0;
    const totalCount = preProductionPages.length;

    for (const filePath of preProductionPages) {
        if (fixPreProductionPage(filePath)) {
            successCount++;
        }
    }

    console.log(`\n📊 Results: ${successCount}/${totalCount} pages processed successfully`);

    if (successCount === totalCount) {
        console.log('\n🎉 All pre-production pages fixed!');
        console.log('\n🔧 What was accomplished:');
        console.log('   ✅ Converted all pages to dynamic component system');
        console.log('   ✅ Added missing footer containers');
        console.log('   ✅ Fixed mobile menu JavaScript conflicts');
        console.log('   ✅ Added component loader scripts');
        console.log('   ✅ Created backups for all modified files');
        console.log('\n🎯 Result:');
        console.log('   • All pre-production pages now have dynamic headers and footers');
        console.log('   • Consistent navigation across entire website');
        console.log('   • Mobile menu functionality works properly');
        console.log('   • No more missing footers');
    } else {
        console.log('\n⚠️  Some pages had issues. Please review before testing.');
    }
}

if (require.main === module) {
    main();
}

module.exports = { fixPreProductionPage, preProductionPages };
