#!/usr/bin/env node

/**
 * Fix Mobile Menu JavaScript Conflicts
 * Remove duplicate mobile menu JavaScript that conflicts with dynamic component loading
 */

const fs = require('fs');
const path = require('path');

// All pages that were converted to dynamic components
const convertedPages = [
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

function fixMobileMenuConflicts(filePath) {
    try {
        if (!fs.existsSync(filePath)) {
            console.log(`⚠️  ${filePath} - File not found`);
            return false;
        }

        let content = fs.readFileSync(filePath, 'utf8');
        console.log(`📄 Processing ${filePath}...`);

        let originalContent = content;
        let changesMade = false;

        // Pattern 1: Remove mobile menu JavaScript blocks that reference mobile-menu-button
        const mobileMenuPattern1 = /<!-- Mobile Menu JavaScript -->[\s\S]*?document\.getElementById\('mobile-menu-button'\)[\s\S]*?<\/script>/g;
        if (mobileMenuPattern1.test(content)) {
            content = content.replace(mobileMenuPattern1, '    <!-- Mobile Menu JavaScript - Handled by component loader -->');
            console.log(`🔧 ${filePath} - Removed mobile menu JavaScript block`);
            changesMade = true;
        }

        // Pattern 2: Remove standalone mobile menu scripts
        const mobileMenuPattern2 = /document\.getElementById\('mobile-menu-button'\)\.addEventListener[\s\S]*?}\);/g;
        if (mobileMenuPattern2.test(content)) {
            content = content.replace(mobileMenuPattern2, '// Mobile menu handled by component loader');
            console.log(`🔧 ${filePath} - Removed mobile menu event listeners`);
            changesMade = true;
        }

        // Pattern 3: Remove mobile dropdown functions
        const mobileDropdownPattern = /function initializeMobileDropdowns\(\)[\s\S]*?function closeAllMobileSubmenus[\s\S]*?}\s*}/g;
        if (mobileDropdownPattern.test(content)) {
            content = content.replace(mobileDropdownPattern, '// Mobile dropdown functionality handled by component loader');
            console.log(`🔧 ${filePath} - Removed mobile dropdown functions`);
            changesMade = true;
        }

        // Pattern 4: Remove click outside handlers for mobile menu
        const clickOutsidePattern = /document\.addEventListener\('click', function\(event\)[\s\S]*?mobile-menu[\s\S]*?}\);/g;
        if (clickOutsidePattern.test(content)) {
            content = content.replace(clickOutsidePattern, '// Click outside handling managed by component loader');
            console.log(`🔧 ${filePath} - Removed click outside handlers`);
            changesMade = true;
        }

        // Pattern 5: Remove DOMContentLoaded mobile menu initialization
        const domLoadedPattern = /document\.addEventListener\('DOMContentLoaded', function\(\)[\s\S]*?initializeMobileDropdowns[\s\S]*?}\);/g;
        if (domLoadedPattern.test(content)) {
            content = content.replace(domLoadedPattern, '// Mobile menu initialization handled by component loader');
            console.log(`🔧 ${filePath} - Removed DOMContentLoaded mobile menu init`);
            changesMade = true;
        }

        // Clean up any empty script tags or excessive whitespace
        content = content.replace(/<script>\s*<\/script>/g, '');
        content = content.replace(/\n\s*\n\s*\n/g, '\n\n');

        if (changesMade) {
            // Create backup
            const backupPath = filePath.replace('.html', '-before-mobile-fix.html');
            fs.writeFileSync(backupPath, originalContent, 'utf8');
            console.log(`💾 Created backup: ${backupPath}`);

            // Write fixed content
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✅ ${filePath} - Mobile menu conflicts fixed`);
            return true;
        } else {
            console.log(`ℹ️  ${filePath} - No mobile menu conflicts found`);
            return true;
        }

    } catch (error) {
        console.log(`❌ ${filePath} - Error: ${error.message}`);
        return false;
    }
}

function main() {
    console.log('🔧 Fixing Mobile Menu JavaScript Conflicts');
    console.log('=' + '='.repeat(60));
    console.log('📋 This will:');
    console.log('   • Remove duplicate mobile menu JavaScript');
    console.log('   • Fix conflicts with dynamic component loading');
    console.log('   • Preserve other page functionality');
    console.log('   • Create backups before making changes');
    console.log('=' + '='.repeat(60));

    let successCount = 0;
    const totalCount = convertedPages.length;

    for (const filePath of convertedPages) {
        if (fixMobileMenuConflicts(filePath)) {
            successCount++;
        }
    }

    console.log(`\n📊 Results: ${successCount}/${totalCount} pages processed successfully`);

    if (successCount === totalCount) {
        console.log('\n🎉 All mobile menu conflicts fixed!');
        console.log('\n🔧 What was accomplished:');
        console.log('   ✅ Removed duplicate mobile menu JavaScript');
        console.log('   ✅ Fixed dynamic component loading conflicts');
        console.log('   ✅ Preserved other page functionality');
        console.log('   ✅ Created backups for all modified files');
        console.log('\n🎯 Result:');
        console.log('   • Dynamic components should now load properly on all pages');
        console.log('   • Mobile menu functionality handled by component loader');
        console.log('   • No more JavaScript conflicts');
    } else {
        console.log('\n⚠️  Some pages had issues. Please review before testing.');
    }
}

if (require.main === module) {
    main();
}

module.exports = { fixMobileMenuConflicts, convertedPages };
