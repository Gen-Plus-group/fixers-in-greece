#!/usr/bin/env node
/**
 * Optimized Build Script for Fixers in Greece
 * Enhanced CSS build process with optimization and monitoring
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Configuration
const config = {
    input: 'src/input.css',
    output: 'dist/output.css',
    minOutput: 'dist/output.min.css',
    statsFile: 'dist/build-stats.json',
    watch: process.argv.includes('--watch'),
    minify: process.argv.includes('--minify') || process.argv.includes('--production'),
    verbose: process.argv.includes('--verbose')
};

// Utility functions
function log(message, level = 'info') {
    const timestamp = new Date().toISOString();
    const colors = {
        info: '\x1b[36m',    // Cyan
        success: '\x1b[32m', // Green
        warning: '\x1b[33m', // Yellow
        error: '\x1b[31m',   // Red
        reset: '\x1b[0m'     // Reset
    };
    
    console.log(`${colors[level]}[${timestamp}] ${message}${colors.reset}`);
}

function getFileSize(filePath) {
    try {
        const stats = fs.statSync(filePath);
        return stats.size;
    } catch (error) {
        return 0;
    }
}

function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

// Build statistics
function generateBuildStats(startTime, inputSize, outputSize, minifiedSize = null) {
    const buildTime = Date.now() - startTime;
    const stats = {
        timestamp: new Date().toISOString(),
        buildTime: `${buildTime}ms`,
        inputSize: formatBytes(inputSize),
        outputSize: formatBytes(outputSize),
        compression: `${((1 - outputSize / inputSize) * 100).toFixed(2)}%`,
        files: {
            input: config.input,
            output: config.output
        }
    };
    
    if (minifiedSize) {
        stats.minifiedSize = formatBytes(minifiedSize);
        stats.minifiedOutput = config.minOutput;
        stats.minificationSavings = `${((1 - minifiedSize / outputSize) * 100).toFixed(2)}%`;
    }
    
    return stats;
}

// Main build function
function buildCSS() {
    const startTime = Date.now();
    log('Starting CSS build process...', 'info');
    
    try {
        // Check if input file exists
        if (!fs.existsSync(config.input)) {
            throw new Error(`Input file not found: ${config.input}`);
        }
        
        const inputSize = getFileSize(config.input);
        log(`Input file size: ${formatBytes(inputSize)}`, 'info');
        
        // Create dist directory if it doesn't exist
        const distDir = path.dirname(config.output);
        if (!fs.existsSync(distDir)) {
            fs.mkdirSync(distDir, { recursive: true });
            log(`Created directory: ${distDir}`, 'info');
        }
        
        // Build command
        let buildCommand = `npx tailwindcss -i ${config.input} -o ${config.output}`;
        
        if (config.minify) {
            buildCommand += ' --minify';
            log('Building with minification enabled...', 'info');
        }
        
        if (config.watch) {
            buildCommand += ' --watch';
            log('Watch mode enabled - monitoring for changes...', 'info');
        }
        
        // Execute build
        const buildOutput = execSync(buildCommand, { 
            encoding: 'utf8',
            stdio: config.verbose ? 'inherit' : 'pipe'
        });
        
        if (config.verbose && buildOutput) {
            log(`Build output: ${buildOutput}`, 'info');
        }
        
        // Get output file size
        const outputSize = getFileSize(config.output);
        
        if (outputSize === 0) {
            throw new Error('Build failed - output file is empty or missing');
        }
        
        // Create additional minified version if not already minified
        let minifiedSize = null;
        if (!config.minify && !config.watch) {
            try {
                const minifyCommand = `npx tailwindcss -i ${config.input} -o ${config.minOutput} --minify`;
                execSync(minifyCommand, { stdio: 'pipe' });
                minifiedSize = getFileSize(config.minOutput);
                log(`Created minified version: ${formatBytes(minifiedSize)}`, 'success');
            } catch (error) {
                log(`Warning: Could not create minified version: ${error.message}`, 'warning');
            }
        }
        
        // Generate and save build statistics
        const stats = generateBuildStats(startTime, inputSize, outputSize, minifiedSize);
        
        if (!config.watch) {
            fs.writeFileSync(config.statsFile, JSON.stringify(stats, null, 2));
            log(`Build statistics saved to: ${config.statsFile}`, 'info');
        }
        
        // Success message
        log(`✓ CSS build completed successfully!`, 'success');
        log(`Output: ${config.output} (${formatBytes(outputSize)})`, 'success');
        log(`Build time: ${stats.buildTime}`, 'success');
        log(`Size reduction: ${stats.compression}`, 'success');
        
        if (minifiedSize) {
            log(`Minified: ${config.minOutput} (${stats.minifiedSize})`, 'success');
            log(`Minification savings: ${stats.minificationSavings}`, 'success');
        }
        
        return true;
        
    } catch (error) {
        log(`✗ Build failed: ${error.message}`, 'error');
        process.exit(1);
    }
}

// Watch mode file monitoring
function setupFileWatcher() {
    const chokidar = require('chokidar');
    
    // Watch source files
    const watcher = chokidar.watch([
        config.input,
        'tailwind.config.js',
        '**/*.html'
    ], {
        ignored: /node_modules/,
        persistent: true
    });
    
    let buildTimeout;
    
    watcher.on('change', (path) => {
        log(`File changed: ${path}`, 'info');
        
        // Debounce builds (wait 100ms after last change)
        clearTimeout(buildTimeout);
        buildTimeout = setTimeout(() => {
            buildCSS();
        }, 100);
    });
    
    watcher.on('error', (error) => {
        log(`Watcher error: ${error}`, 'error');
    });
    
    log('File watcher initialized', 'success');
    return watcher;
}

// Performance monitoring
function monitorPerformance() {
    const performanceData = {
        timestamp: new Date().toISOString(),
        memory: process.memoryUsage(),
        platform: process.platform,
        nodeVersion: process.version,
        cpuUsage: process.cpuUsage()
    };
    
    if (config.verbose) {
        log(`Memory usage: ${formatBytes(performanceData.memory.heapUsed)}`, 'info');
    }
    
    return performanceData;
}

// Main execution
function main() {
    log('Fixers in Greece - Optimized CSS Build Tool', 'info');
    log(`Mode: ${config.minify ? 'Production' : 'Development'}`, 'info');
    
    // Monitor performance
    const perfStart = monitorPerformance();
    
    if (config.watch) {
        // Initial build
        buildCSS();
        
        // Setup watcher for continuous building
        const watcher = setupFileWatcher();
        
        // Graceful shutdown
        process.on('SIGINT', () => {
            log('Stopping build process...', 'info');
            watcher.close();
            process.exit(0);
        });
        
        // Keep process alive
        log('Press Ctrl+C to stop watching...', 'info');
        
    } else {
        // Single build
        const success = buildCSS();
        
        if (success) {
            const perfEnd = monitorPerformance();
            log(`Build process completed in ${Date.now() - Date.parse(perfStart.timestamp)}ms`, 'success');
        }
    }
}

// Run if called directly
if (require.main === module) {
    main();
}

module.exports = { buildCSS, log, formatBytes };