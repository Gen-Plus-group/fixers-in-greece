const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const PORT = 8000;
const HOST = 'localhost';

// MIME types for different file extensions
const mimeTypes = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'text/javascript',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
    '.webp': 'image/webp',
    '.mp4': 'video/mp4',
    '.webm': 'video/webm',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
    '.ttf': 'font/ttf',
    '.otf': 'font/otf'
};

const server = http.createServer((req, res) => {
    // Decode URL
    let filePath = decodeURIComponent(req.url);
    
    // Default to index.html for directory requests
    if (filePath.endsWith('/')) {
        filePath += 'index.html';
    }
    
    // Remove query strings
    filePath = filePath.split('?')[0];
    
    // Security: prevent directory traversal
    filePath = path.join(__dirname, filePath);
    
    // Get file extension
    const extname = path.extname(filePath).toLowerCase();
    const contentType = mimeTypes[extname] || 'application/octet-stream';
    
    // Read and serve the file
    fs.readFile(filePath, (err, content) => {
        if (err) {
            if (err.code === 'ENOENT') {
                // File not found
                res.writeHead(404, { 'Content-Type': 'text/html' });
                res.end('<h1>404 - File Not Found</h1>', 'utf-8');
            } else {
                // Server error
                res.writeHead(500);
                res.end(`Server Error: ${err.code}`, 'utf-8');
            }
        } else {
            // Success
            res.writeHead(200, { 
                'Content-Type': contentType,
                'Cache-Control': 'no-store, no-cache, must-revalidate',
                'Expires': '0'
            });
            res.end(content, 'utf-8');
        }
    });
    
    // Log the request
    console.log(`[${new Date().toLocaleString()}] ${req.method} ${req.url}`);
});

server.listen(PORT, HOST, () => {
    console.log('\n🚀 Starting Fixers in Greece Test Server...');
    console.log(`📁 Serving files from: ${__dirname}`);
    console.log(`🌐 Server URL: http://${HOST}:${PORT}`);
    console.log('\n✨ Opening browser automatically...');
    console.log('📝 Press Ctrl+C to stop the server\n');
    
    // Open browser
    const url = `http://${HOST}:${PORT}`;
    const start = process.platform === 'darwin' ? 'open' : process.platform === 'win32' ? 'start' : 'xdg-open';
    exec(`${start} ${url}`);
});

// Handle server shutdown
process.on('SIGINT', () => {
    console.log('\n\n🛑 Server stopped by user');
    process.exit(0);
});