#!/usr/bin/env node

/**
 * Final Cleanup Script - Complete workspace organization
 * Moves remaining files to proper locations
 */

const fs = require('fs');
const path = require('path');

// Files that still need to be moved to dev-archive
const remainingPythonScripts = [
    'add-google-analytics.py',
    'apply-tailwind-to-all-pages.py',
    'bulk-update-navigation.py',
    'complete-fixer-page.py',
    'complete-main-preproduction-page.py',
    'complete-preproduction-pages.py',
    'complete-remaining-pages.py',
    'create-content-rich-pages.py',
    'create-modern-pages.py',
    'create-preproduction-pages.py',
    'create-remaining-pages.py',
    'enhance-pages-with-tailwind.py',
    'extract-and-rebuild-content.py',
    'fix-all-navigation-and-content.py',
    'fix-megamenu-positioning.py',
    'fix-megamenu-width.py',
    'fix-navigation-and-create-pages.py',
    'fix-navigation-and-footer.py',
    'improve-megamenu-visuals.py',
    'optimize-new-pages.py',
    'standardize-all-navigation.py',
    'standardize-navigation.py',
    'update-all-footers.py',
    'update-all-navigation-final.py',
    'update-mobile-navigation.py',
    'update-navigation-with-megamenu.py',
    'update-navigation-with-new-pages.py',
    'update-navigation.py',
    'update-to-dynamic-components.py',
    'verify-navigation.py'
];

// Additional backup files in root
const remainingBackupFiles = [
    'about-us-optimized.html',
    'about-us-tailwind.html',
    'equipment-rental-vietnam-tailwind.html',
    'film-production-services-tailwind.html',
    'index-modern.html',
    'index-original-backup.html',
    'index-tailwind.html'
];

// Test files to remove
const remainingTestFiles = [
    'create-test-video.html',
    'form-enhancement-test.html',
    'ga-verification.html',
    'test-contact-form.html',
    'test-video.html',
    'thank-you-test.html',
    'video-diagnostic.html'
];

// Content files to move to docs
const remainingContentFiles = [
    'clients-content.html',
    'contact-content.html',
    'filming-in-vietnam-content.html'
];

// Design files to move
const remainingDesignFiles = [
    'homepage-design.pdf',
    'homepage-design.png'
];

function moveFile(source, destination) {
    try {
        if (fs.existsSync(source)) {
            // Create destination directory if it doesn't exist
            const destDir = path.dirname(destination);
            if (!fs.existsSync(destDir)) {
                fs.mkdirSync(destDir, { recursive: true });
            }
            
            fs.renameSync(source, destination);
            console.log(`📦 Moved: ${source} → ${destination}`);
            return true;
        }
    } catch (error) {
        console.log(`❌ Error moving ${source}: ${error.message}`);
        return false;
    }
    return false;
}

function deleteFile(filePath) {
    try {
        if (fs.existsSync(filePath)) {
            fs.unlinkSync(filePath);
            console.log(`🗑️  Deleted: ${filePath}`);
            return true;
        }
    } catch (error) {
        console.log(`❌ Error deleting ${filePath}: ${error.message}`);
        return false;
    }
    return false;
}

function main() {
    console.log('🧹 Final Workspace Cleanup...');
    console.log('=' + '='.repeat(50));
    
    let totalMoved = 0;
    let totalDeleted = 0;
    
    // Move remaining Python scripts to dev-archive
    console.log('\n🔧 Moving remaining Python scripts to dev-archive...');
    remainingPythonScripts.forEach(file => {
        if (moveFile(file, path.join('dev-archive', file))) {
            totalMoved++;
        }
    });
    
    // Move remaining backup files
    console.log('\n💾 Moving remaining backup files...');
    remainingBackupFiles.forEach(file => {
        if (moveFile(file, path.join('backup', file))) {
            totalMoved++;
        }
    });
    
    // Delete remaining test files
    console.log('\n🧪 Removing remaining test files...');
    remainingTestFiles.forEach(file => {
        if (deleteFile(file)) {
            totalDeleted++;
        }
    });
    
    // Move remaining content files to docs
    console.log('\n📄 Moving remaining content files to docs...');
    remainingContentFiles.forEach(file => {
        if (moveFile(file, path.join('docs', file))) {
            totalMoved++;
        }
    });
    
    // Move remaining design files
    console.log('\n🎨 Moving remaining design files...');
    remainingDesignFiles.forEach(file => {
        if (moveFile(file, path.join('design', file))) {
            totalMoved++;
        }
    });
    
    // Clean up the cleanup scripts themselves
    console.log('\n🧹 Moving cleanup scripts to dev-archive...');
    if (moveFile('cleanup-workspace.js', 'dev-archive/cleanup-workspace.js')) {
        totalMoved++;
    }
    
    console.log('\n' + '='.repeat(50));
    console.log('🎉 Final cleanup completed!');
    console.log(`📊 Files moved: ${totalMoved}`);
    console.log(`📊 Files deleted: ${totalDeleted}`);
    console.log('\n✅ Workspace is now fully organized and optimized!');
    console.log('\n📁 Clean root directory structure:');
    console.log('   • Essential website files only');
    console.log('   • Organized backup/ directory');
    console.log('   • Archived dev-archive/ directory');
    console.log('   • Documentation in docs/');
    console.log('   • Design files in design/');
    console.log('   • Dynamic components system ready');
    
    // Self-cleanup - move this script to dev-archive too
    setTimeout(() => {
        if (fs.existsSync('final-cleanup.js')) {
            moveFile('final-cleanup.js', 'dev-archive/final-cleanup.js');
            console.log('\n🧹 Moved final-cleanup.js to dev-archive');
        }
    }, 1000);
}

if (require.main === module) {
    main();
}
