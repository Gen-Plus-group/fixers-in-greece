# Test Environment Setup for Fixers in Greece

## Quick Start

### Windows Users:
Simply double-click `start-test-server.bat` to launch the test server.

### Mac/Linux Users:
Run: `./start-test-server.sh`

### Manual Start:
```bash
python test-server.py
```

## What This Does

1. **Starts a local web server** on http://localhost:8000
2. **Opens your browser automatically** to view the site
3. **Disables caching** so you see changes immediately
4. **Shows request logs** in the terminal

## Testing the Navigation Fix

1. Start the test server using one of the methods above
2. The homepage will open automatically in your browser
3. Check that the navigation menu is visible:
   - Should show light gray text (#b4b4b4) by default
   - Should change to orange (#f9a531) on hover
   - Background should be dark (#1c1c1c)

## Making Changes While Testing

1. Keep the server running
2. Make any changes to HTML/CSS/JS files
3. Simply refresh your browser (F5 or Ctrl+R) to see changes
4. No need to restart the server

## Stop the Server

Press `Ctrl+C` in the terminal window to stop the server.

## Troubleshooting

### Port Already in Use
If you get an error about port 8000 being in use:
1. Stop any other local servers
2. Or edit `test-server.py` and change `PORT = 8000` to another number like `8080`

### Python Not Found
Make sure Python 3 is installed:
- Windows: Download from https://www.python.org/
- Mac: Usually pre-installed, or use `brew install python3`
- Linux: `sudo apt-get install python3` (Ubuntu/Debian)

## Alternative: Using Node.js

If you prefer Node.js, you can use:
```bash
npx http-server -p 8000 -c-1
```

## Browser Developer Tools

While testing, use browser developer tools:
- **Chrome/Edge**: Press F12 or Ctrl+Shift+I
- **Firefox**: Press F12 or Ctrl+Shift+I
- Check the Console tab for any JavaScript errors
- Use the Network tab to ensure all files load correctly
- Use the Elements/Inspector tab to examine the navigation HTML

## Current Changes Being Tested

1. Navigation visibility fix in `index.html`
2. Added CSS rules to ensure navigation links are visible
3. Updated to use minified JavaScript for better performance