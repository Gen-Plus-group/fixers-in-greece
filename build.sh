#!/bin/bash
# Build script for Digital Ocean App Platform

echo "Starting build process..."

# Check if node_modules exists, if not install dependencies
if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm install
fi

# Build CSS
echo "Building CSS..."
npm run build-css-prod

# Check if build was successful
if [ -f "dist/output.css" ]; then
    echo "Build successful! CSS file created at dist/output.css"
    exit 0
else
    echo "Build failed! CSS file not created"
    exit 1
fi