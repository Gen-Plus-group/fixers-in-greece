#!/usr/bin/env node

/**
 * Workspace Cleanup and Optimization Script
 * Organizes files, removes temporary files, and creates a clean project structure
 */

const fs = require('fs');
const path = require('path');

// Define file categories for organization
const fileCategories = {
    // Development scripts that are no longer needed
    obsoleteScripts: [
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
        'verify-navigation.py',
        'convert-all-to-dynamic-components.js'
    ],

    // Backup and temporary files
    backupFiles: [
        'about-us-optimized.html',
        'about-us-tailwind.html',
        'equipment-rental-vietnam-tailwind.html',
        'film-production-services-tailwind.html',
        'index-modern.html',
        'index-original-backup.html',
        'index-tailwind.html'
    ],

    // Test and temporary files
    testFiles: [
        'create-test-video.html',
        'form-enhancement-test.html',
        'ga-verification.html',
        'test-contact-form.html',
        'test-video.html',
        'thank-you-test.html',
        'video-diagnostic.html'
    ],

    // Content files that should be moved to docs
    contentFiles: [
        'clients-content.html',
        'contact-content.html',
        'filming-in-vietnam-content.html'
    ],

    // Design files
    designFiles: [
        'homepage-design.pdf',
        'homepage-design.png'
    ]
};

// Directories to create for organization
const organizationDirs = {
    'dev-archive': 'Archive of development scripts and tools',
    'docs': 'Documentation and content files',
    'design': 'Design files and assets',
    'backup': 'Backup files and original versions'
};

function createDirectory(dirPath, description) {
    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath, { recursive: true });
        console.log(`📁 Created directory: ${dirPath} - ${description}`);
        return true;
    }
    return false;
}

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

function cleanupBackupFiles() {
    console.log('\n🧹 Cleaning up backup files in subdirectories...');
    
    const backupPatterns = [
        'index-backup.html',
        'index-original-backup.html'
    ];
    
    let cleanedCount = 0;
    
    // Find all subdirectories
    const items = fs.readdirSync('.', { withFileTypes: true });
    const directories = items.filter(item => item.isDirectory() && !item.name.startsWith('.') && item.name !== 'node_modules');
    
    directories.forEach(dir => {
        backupPatterns.forEach(pattern => {
            const backupPath = path.join(dir.name, pattern);
            if (fs.existsSync(backupPath)) {
                const newPath = path.join('backup', dir.name, pattern);
                if (moveFile(backupPath, newPath)) {
                    cleanedCount++;
                }
            }
        });
    });
    
    console.log(`📊 Moved ${cleanedCount} backup files to backup directory`);
}

function organizeFiles() {
    console.log('\n📋 Organizing workspace files...');
    
    let totalMoved = 0;
    
    // Move obsolete scripts to dev-archive
    console.log('\n🔧 Archiving development scripts...');
    fileCategories.obsoleteScripts.forEach(file => {
        if (moveFile(file, path.join('dev-archive', file))) {
            totalMoved++;
        }
    });
    
    // Move backup files
    console.log('\n💾 Organizing backup files...');
    fileCategories.backupFiles.forEach(file => {
        if (moveFile(file, path.join('backup', file))) {
            totalMoved++;
        }
    });
    
    // Delete test files (they're not needed anymore)
    console.log('\n🧪 Removing test files...');
    fileCategories.testFiles.forEach(file => {
        deleteFile(file);
    });
    
    // Move content files to docs
    console.log('\n📄 Organizing content files...');
    fileCategories.contentFiles.forEach(file => {
        if (moveFile(file, path.join('docs', file))) {
            totalMoved++;
        }
    });
    
    // Move design files
    console.log('\n🎨 Organizing design files...');
    fileCategories.designFiles.forEach(file => {
        if (moveFile(file, path.join('design', file))) {
            totalMoved++;
        }
    });
    
    return totalMoved;
}

function createReadmeFiles() {
    console.log('\n📝 Creating README files for organization...');
    
    const readmeContents = {
        'dev-archive/README.md': `# Development Archive

This directory contains development scripts and tools that were used during the website migration and optimization process.

## Scripts Included:
- Navigation standardization scripts
- Content creation and migration tools
- Tailwind CSS integration scripts
- Component conversion utilities

These files are kept for reference but are no longer needed for day-to-day operations.
`,
        'backup/README.md': `# Backup Files

This directory contains backup versions of files created during development.

## Contents:
- Original HTML file versions
- Backup copies of modified pages
- Alternative implementations

These files are preserved for safety but should not be used in production.
`,
        'docs/README.md': `# Documentation and Content

This directory contains documentation files and content templates.

## Contents:
- Content HTML files used for reference
- Documentation markdown files
- Setup guides and implementation notes
`,
        'design/README.md': `# Design Assets

This directory contains design files and visual assets.

## Contents:
- Homepage design files
- Visual mockups and references
- Design documentation
`
    };
    
    Object.entries(readmeContents).forEach(([filePath, content]) => {
        try {
            fs.writeFileSync(filePath, content);
            console.log(`📄 Created: ${filePath}`);
        } catch (error) {
            console.log(`❌ Error creating ${filePath}: ${error.message}`);
        }
    });
}

function main() {
    console.log('🚀 Starting Workspace Cleanup and Optimization...');
    console.log('=' + '='.repeat(70));
    console.log('📋 This will:');
    console.log('   • Create organized directory structure');
    console.log('   • Archive development scripts');
    console.log('   • Move backup files to backup directory');
    console.log('   • Remove temporary and test files');
    console.log('   • Organize content and design files');
    console.log('   • Create documentation for each directory');
    console.log('=' + '='.repeat(70));

    // Create organization directories
    console.log('\n📁 Creating organization directories...');
    Object.entries(organizationDirs).forEach(([dir, description]) => {
        createDirectory(dir, description);
    });

    // Organize files
    const totalMoved = organizeFiles();
    
    // Clean up backup files in subdirectories
    cleanupBackupFiles();
    
    // Create README files
    createReadmeFiles();

    console.log('\n' + '='.repeat(70));
    console.log('🎉 Workspace cleanup completed successfully!');
    console.log(`📊 Total files organized: ${totalMoved}`);
    console.log('\n🎯 Workspace is now organized with:');
    console.log('   ✅ Clean root directory with only essential files');
    console.log('   ✅ Archived development scripts in dev-archive/');
    console.log('   ✅ Backup files organized in backup/');
    console.log('   ✅ Documentation in docs/');
    console.log('   ✅ Design files in design/');
    console.log('   ✅ README files for each directory');
    console.log('\n📁 Current structure optimized for maintainability!');
}

if (require.main === module) {
    main();
}

module.exports = { organizeFiles, createDirectory, moveFile };
