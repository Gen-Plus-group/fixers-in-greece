# Cache Busting Strategy Guide

## Overview

This guide explains how to implement cache busting for the Fixers in Greece website to ensure users always receive the latest versions of updated files while maintaining optimal caching performance.

## Why Cache Busting?

With our aggressive caching policy (1 year for static assets), we need a strategy to force browsers to download new versions when files are updated. The `immutable` directive tells browsers that files will never change during their cache lifetime, so we must change the filename or URL when content updates.

## Recommended Strategies

### 1. Query String Versioning (Simplest)

Add version numbers or timestamps to asset URLs:

```html
<!-- CSS -->
<link rel="stylesheet" href="/css/layout.css?v=1.2.3">
<link rel="stylesheet" href="/dist/output.css?v=20250626">

<!-- JavaScript -->
<script src="/js/component-loader.js?v=1.0.5"></script>
<script src="/js/inline-components.js?v=2.1.0"></script>

<!-- Images (for frequently updated images) -->
<img src="/assets/images/logo.png?v=2">
```

### 2. Filename Versioning (Most Reliable)

Include version in the actual filename:

```html
<!-- CSS -->
<link rel="stylesheet" href="/css/layout-v1.2.3.css">
<link rel="stylesheet" href="/dist/output-20250626.css">

<!-- JavaScript -->
<script src="/js/component-loader-v1.0.5.js"></script>
```

### 3. Content Hash Versioning (Automated)

Use build tools to generate hashes based on file content:

```html
<!-- CSS -->
<link rel="stylesheet" href="/dist/output.a3b4c5d6.css">

<!-- JavaScript -->
<script src="/js/app.e7f8g9h0.js"></script>
```

## Implementation Guide

### For Manual Updates

1. **Update HTML files** when changing CSS/JS:
   ```html
   <!-- Old -->
   <link rel="stylesheet" href="/dist/output.css">
   
   <!-- New -->
   <link rel="stylesheet" href="/dist/output.css?v=20250626">
   ```

2. **Create a versioning system**:
   ```javascript
   // In your HTML or a config file
   const ASSET_VERSION = '1.0.0'; // Update this when assets change
   
   // Use in HTML
   <link rel="stylesheet" href="/dist/output.css?v=${ASSET_VERSION}">
   ```

### For Build Process Integration

1. **Update package.json** scripts:
   ```json
   {
     "scripts": {
       "build": "node build-optimized.js --production --minify && npm run version-assets",
       "version-assets": "node version-assets.js"
     }
   }
   ```

2. **Create version-assets.js**:
   ```javascript
   const fs = require('fs');
   const crypto = require('crypto');
   const glob = require('glob');
   
   // Generate hash for file
   function getFileHash(filepath) {
     const content = fs.readFileSync(filepath);
     return crypto.createHash('md5').update(content).digest('hex').substring(0, 8);
   }
   
   // Update HTML files with versioned assets
   function updateHTMLFiles() {
     const htmlFiles = glob.sync('**/*.html', { ignore: 'node_modules/**' });
     
     htmlFiles.forEach(htmlFile => {
       let content = fs.readFileSync(htmlFile, 'utf8');
       
       // Update CSS references
       content = content.replace(
         /href="(\/[^"]+\.css)(\?v=[^"]*)?"/g,
         (match, path) => {
           const hash = getFileHash(`.${path}`);
           return `href="${path}?v=${hash}"`;
         }
       );
       
       // Update JS references
       content = content.replace(
         /src="(\/[^"]+\.js)(\?v=[^"]*)?"/g,
         (match, path) => {
           const hash = getFileHash(`.${path}`);
           return `src="${path}?v=${hash}"`;
         }
       );
       
       fs.writeFileSync(htmlFile, content);
     });
   }
   
   updateHTMLFiles();
   ```

### For Different Hosting Platforms

#### Azure Static Web Apps
Already configured with proper cache headers in `staticwebapp.config.json`. Use query string versioning for simplicity.

#### Apache (.htaccess)
Already configured. The `immutable` directive means you MUST change the URL when content changes.

#### Nginx
Already configured in `nginx-cache.conf`. Use the same versioning strategy.

#### Netlify
Already configured in `netlify.toml` and `_headers`. Netlify also supports automatic asset optimization.

## Quick Implementation Checklist

1. ✅ Choose a versioning strategy (query string is easiest to start)
2. ✅ Update all HTML files to include versions on CSS/JS references
3. ✅ Create a system to update versions when files change
4. ✅ Test that new versions are loaded after updates
5. ✅ Document your versioning process for team members

## Example Implementation

Here's what your HTML should look like with versioning:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Versioned CSS -->
    <link rel="stylesheet" href="/dist/output.css?v=20250626">
    <link rel="stylesheet" href="/css/theme.css?v=1.0.0">
    <link rel="stylesheet" href="/css/layout.css?v=1.2.0">
    
    <!-- Fonts don't need versioning as they rarely change -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
</head>
<body>
    <!-- Content -->
    
    <!-- Versioned JavaScript -->
    <script src="/js/component-loader.js?v=1.0.0"></script>
    <script src="/js/inline-components.js?v=1.0.0"></script>
</body>
</html>
```

## Maintenance Tips

1. **Update versions when files change** - This is critical for the cache busting to work
2. **Use semantic versioning** - Makes it easier to track changes
3. **Consider automation** - Build tools can handle this automatically
4. **Test after deployment** - Ensure new versions are being loaded
5. **Monitor performance** - Check that caching is working as expected

## Emergency Cache Clear

If you need to force all users to get new versions immediately:

1. Change all version numbers/hashes
2. Consider temporarily reducing cache times in your server config
3. Use cache-control headers with `no-cache` temporarily
4. Restore normal caching once users have updated versions