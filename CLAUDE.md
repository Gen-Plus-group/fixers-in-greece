# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## IMPORTANT: Always Push Changes

**ALWAYS run `git push` after making commits. The user expects all changes to be pushed automatically after committing.**

## Project Overview

This is a **static HTML website** for "Fixers in Greece" - a film production services company. The site uses **Tailwind CSS** for styling and consists of multiple HTML pages with a complex directory structure that includes legacy WordPress-generated content.

**IMPORTANT: The production website domain is www.fixersingreece.gr (not .com)**

## Build Commands

### CSS Development
```bash
# Watch mode for development (auto-rebuild on changes)
npm run dev
# or
npm run build-css

# Production build (minified CSS)
npm run build
# or 
npm run build-css-prod
```

### Key Files
- **Source CSS**: `src/input.css` - Tailwind CSS with custom components and utilities
- **Output CSS**: `dist/output.css` - Generated CSS file used by HTML pages
- **Tailwind Config**: `tailwind.config.js` - Custom theme with Greece-specific colors and components

## Architecture

### CSS Architecture
The project uses a **component-based CSS architecture** with Tailwind:

- **Base Layer**: Typography, focus styles, accessibility features
- **Components Layer**: Reusable UI components (buttons, cards, forms, navigation)
- **Utilities Layer**: Custom utilities for backgrounds, animations, shadows

### Key Tailwind Customizations
- **Greece Brand Colors**: `greece-blue` (#f9a531), `greece-white` (#ffffff), `greece-dark` (#1c1c1c)
- **Custom Components**: `.btn-primary`, `.card-hover`, `.nav-link`, `.form-input`, `.portfolio-item`
- **Custom Utilities**: `.text-gradient-greece`, `.bg-gradient-greece`, `.glass-effect`, `.hover-lift`

### Directory Structure
- **Main Pages**: Root-level HTML files and directories (`index.html`, `about-us/`, `contact/`, etc.)
- **Service Pages**: Specialized directories for different services (`film-production-services/`, `equipment-rental-greece/`, etc.)
- **Portfolio**: `portfolio-item/` contains individual project showcases
- **Clients**: `clients/` contains client logo pages
- **Legacy Content**: `wp-content/` contains WordPress assets and uploads

### Page Organization
- Each main section has its own directory with `index.html`
- Backup files are preserved with `-original-backup.html` suffix
- Tailwind-optimized versions exist alongside original files
- RSS feeds and XML sitemaps are auto-generated

## Navigation System

The site uses a **standardized navigation system** across all pages:
- Desktop navigation with dropdown menus
- Mobile hamburger menu
- Consistent styling with Greece brand colors
- Navigation standardization scripts available in Python files

## Development Workflow

### Content Updates
1. Edit HTML files directly in their respective directories
2. Use existing backup files as reference for original content
3. Maintain consistent navigation structure across all pages

### Styling Changes
1. Modify `src/input.css` for component or utility changes
2. Update `tailwind.config.js` for theme customizations
3. Run `npm run dev` to watch for changes
4. Run `npm run build` for production deployment

### SEO and Analytics
- Comprehensive SEO setup documented in `SEO-IMPLEMENTATION-GUIDE.md`
- Google Analytics integration via gtag
- Schema markup for local business
- XML sitemaps for all content types

## Contact Form Setup

The site includes a **PHP-based contact form** (`contact-form-handler.php`) with:
- Email validation and security
- Auto-reply functionality
- Greece branding in email templates
- Sends to `greece@needafixer.com`

## Important Notes

- This is a **static website** - no database or CMS backend
- All content is in HTML files with embedded CSS classes
- Maintain backup files when making changes
- Navigation should remain consistent across all pages
- Preserve Greece brand colors and styling throughout
- Test contact form functionality when making changes to contact pages

## Recent Work (2025-06-18)

### Service Pages Created
- **Production Services**: 40 pages across 6 categories (Camera & Cinematography, Lighting & Grip, Sound & Audio, Production Equipment, Production Team, Specialized Filming)
- **Post-Production Services**: 28 pages across 5 categories (Editing & Assembly, Color & Visual Finishing, Motion & VFX, Audio Post, Delivery & Output)
- **Film Crew Services**: 29 pages across 3 categories (Creative Roles, Technical Roles, Support Roles)

### Navigation Updates
- Fixed navigation links for all production services
- Added mega menus for Post-Production and Film Crew sections
- Reduced font size (text-sm) and spacing (space-x-4) for better mobile display
- Added Film Crew mobile menu that was missing

### Sitemap Restructure
- Rebuilt entire sitemap structure with 7 specialized sitemaps
- Total of 186 pages indexed across all categories
- Organized by priority (1.0 for main pages down to 0.1 for system pages)
- Main sitemap index references all sub-sitemaps

### Key Patterns Established
1. **Service Page Template**: Standard structure with hero, description, services grid, related services, and CTA
2. **Mega Menu Pattern**: Hover-based dropdowns with inline styles for reliability
3. **Mobile Menu Pattern**: Collapsible categories with nested subcategories
4. **Directory Structure**: `/category/subcategory/service-name/` pattern

### Testing Commands
- Build CSS: `npm run dev` (watch mode) or `npm run build` (production)
- Lint/Typecheck: Need to ask user for specific commands if issues arise

## Recent Work (2025-06-19)

### Complete Localization from Vietnam to Greece
- **Renamed all directories and files** containing 'vietnam' to 'greece'
- **Updated 765 files** with Greece-specific content and branding
- **Replaced brand colors**: 
  - Primary: `greece-blue` (#f9a531) replacing vietnam-orange
  - Secondary: `greece-white` (#ffffff) replacing vietnam-red
- **Updated city references**:
  - Hanoi → Athens
  - Ho Chi Minh City/Saigon → Thessaloniki
- **Fixed build script**: Corrected comment syntax errors in `build-optimized.js`
- **Rebuilt CSS**: Successfully compiled with new Greece brand colors
- **Updated all internal links**: All paths now reference Greece locations
- **Modified configuration files**: `tailwind.config.js`, `package.json`, and sitemap.xml
- **Git repository**: Committed and pushed all changes to https://github.com/Gen-Plus-group/fixers-in-greece

### Files and Directories Renamed
- `filming-in-vietnam/` → `filming-in-greece/`
- `commercial-video-production-vietnam/` → `commercial-video-production-greece/`
- `documentary-filming-vietnam/` → `documentary-filming-greece/`
- `equipment-rental-vietnam/` → `equipment-rental-greece/`
- And all other Vietnam-specific directories and files

### Next Steps
- Update contact form handler with Greece-specific information
- Review and update meta tags for Greece SEO
- Update Google Analytics for Greece market
- Create Greece-specific content for key pages
- Update logo and visual assets for Greece branding

## Recent Work (2025-06-23)

### Portfolio Updates - Commercials & Branded Content
- **Created 20 portfolio pages** for commercial projects from NAF Greece
- **Downloaded and stored GIF thumbnails** in `/assets/images/portfolio/` directory
- **Updated category page** to display all 20 projects without pagination
- **Added video embeds** for 18 projects (17 Vimeo, 1 YouTube)
- **Fixed layout issues**: Centered titles, updated project count, removed Load More button
- **Created 7 additional portfolio pages** for missing projects:
  - Elounda Gulf Happiness
  - Kenshō Awakening  
  - Abaton Sanctuary
  - Santanna Mykonos
  - Canaves Time Stops
  - Angsana Corfu
  - Galileo Wige

### Music Videos Category
- **Updated Music Videos category page** with 3 real projects from NAF Greece:
  - Keen'V: Dis toi que c'est la vie
  - The Temper Trap: Fall Together
  - Alesha Dixon: The Way We Are
- **Created portfolio pages** for all 3 music video projects
- **Added video embeds**: All 3 projects now have Vimeo videos embedded
- **Updated thumbnails** with correct images from Squarespace CDN
- **Removed filter menu** (All Projects, International, Greek Artists) for cleaner UI

### Homepage Updates
- **Fixed portfolio-hero CSS class** with margin-top: 2rem
- **Updated company introduction**: 
  - Changed to exclusive focus on Greece (removed Southeast Asia)
  - Fixed language from "Greeceese" to "Greek"
- **Replaced portfolio section** with 4-category grid from portfolio page:
  - Music Videos (3 Projects)
  - Drama & Entertainment (12 Projects)
  - Documentaries (25 Projects)
  - Commercials & Branded Content (20 Projects)

### Content Production Page Redesign
- **Reorganized layout** to match Post-Production Services page style
- **Created 4 main categories** from 17 individual services:
  - Broadcast & Television (6 services)
  - Commercial & Corporate (4 services)
  - Documentary & Factual (3 services)
  - Digital & Creative Content (5 services)
- **Changed to compact grid layout** (3-4 columns) from large cards
- **Removed "Learn More" links** for cleaner presentation

### Form Updates
- **Updated contact form** with new Formspree ID: xkgbqrdp
- **Maintained form structure** and validation

### Key Technical Updates
- **Always push after commits** - Added to configuration as per user preference
- **Consistent portfolio page template** with hero, video embed, services, and related projects
- **Responsive aspect-video containers** for all video embeds
- **Schema.org markup** for all portfolio pages
- **Navigation between portfolio items** maintained throughout

## Recent Work (2025-06-24)

### Documentary Portfolio Updates
- **Replaced 6 demo documentary projects** with real projects from nafgreece.plus
- **Created 6 portfolio pages** for documentary projects:
  - Cunk on Earth (BBC comedy documentary)
  - Greek Island Odyssey with Bettany Hughes (Channel 5)
  - Ancient Treasures with Bettany Hughes (Channel 5)
  - Medusa with Natalie Haynes (BBC)
  - Last Woman on Earth (Channel 4)
  - Greg Wallace: Big Weekends Away (Channel 5)
- **Added Vimeo video embeds** to all documentary pages with actual video IDs
- **Updated project count** from 25 to 6 to reflect actual content
- **Maintained consistent structure** with production details, services provided, and key locations

### Performance Optimization
- **Use parallel processing** whenever possible for optimal speed:
  - Run multiple tool calls simultaneously (e.g., multiple file reads/writes)
  - Execute independent bash commands in parallel
  - Create multiple files/directories concurrently
  - Batch operations instead of sequential execution
- **Example**: When creating 6 portfolio pages, use a Python script to generate all files at once rather than creating them one by one

## Recent Work (2025-06-25)

### Contact Form Fixes
- **Fixed JavaScript syntax errors** in contact form page that were preventing form submission
- **Corrected comment delimiters** throughout the JavaScript code (missing `//` and `/* */`)
- **Removed broken mobile menu code** fragments that were causing JavaScript errors
- **Updated form configuration**:
  - Confirmed Formspree form ID: `xkgbqrdp`
  - Added full URL for redirect: `https://www.fixersingreece.gr/contact/?success=true`
  - Fixed phone input initialization with Greece as default country
  - Enhanced form validation with better error handling
- **Improved form submission flow**:
  - Added preventDefault to handle validation before submission
  - Proper loading state on submit button
  - Clear error messages for users
  - Fallback mailto link remains functional
- **Tested form components**:
  - International phone input with Greece default
  - Date pickers for shoot dates
  - Multi-select services dropdown
  - Character counter for message field
  - All validation working correctly

## Recent Work (2025-07-09)

### Homepage Header Fix
- **Fixed navigation visibility issue** on homepage where menu wasn't showing
- **Resolved dynamic header loading** system that was broken due to minified JS issues
- **Added top bar** with phone (+30 210 6821895) and email (greece@needafixer.com) matching internal pages
- **Fixed mega menu hover behavior** - menus now show correctly on hover without offset issues
- **Aligned mobile menu items** to the left for consistency
- **Ensured header layout matches internal pages** with proper container width and spacing
- **Maintained dynamic header loading** for consistency across all pages
- **Fixed CSS specificity issues** by adding targeted overrides in index.html:
  ```css
  /* Keep header container visible */
  #header-container {
    display: block !important;
    visibility: visible !important;
  }

  /* Make sure the header elements are visible but not the mobile overlay */
  #header-container > div:not(#mobile-menu-overlay),
  #header-container > header {
    display: block !important;
    visibility: visible !important;
  }

  /* Mobile menu styles */
  #mobile-navigation-content > a,
  #mobile-navigation-content > div > button {
    text-align: left !important;
    justify-content: flex-start !important;
    width: 100% !important;
  }
  ```
- **Created test environment** with Node.js server for local testing
- **Committed and pushed all changes** to Git repository

## Recent Work (2025-07-10)

### Tax Incentives Page Updates
- **Updated cap on cash rebate** from "No cap" to "Cap rebate amount at €8 million per production"
- **Changed payment timing** from "within 6 months" to "after 6 months of production completion"
- **Updated application process note** - Removed outdated October 2024 reference
- **Updated FAQ answer** about rebate cap with official language: "The total of the rebate amount is disbursed as a one-time payment to the beneficiary production and does not exceed eight million (8.000.000) euros per audiovisual work"

### Client Logos Section Enhancement
- **Added actual SVG logo files** to `/assets/images/client-logos/` directory
- **Replaced inline SVG placeholders** with real logo files from major clients
- **Maintained two-row carousel structure** with opposite scrolling directions
- **Updated styling**:
  - Changed background from dark to white for better contrast
  - Added grayscale filter (70% opacity) with color on hover
  - Increased spacing between logos to prevent overlapping
  - Added gradient mask for smooth edge transitions
- **Distributed 23 unique logos** across both rows:
  - First row: Netflix, BBC, Disney, CNN, Warner Bros, National Geographic, Universal, Al Jazeera, Paramount, Discovery, HBO, YouTube
  - Second row: Amazon Studios, Sony, Apple TV, Fox, DreamWorks, Spotify, Pixar, Meta, Marvel Studios, TikTok, Hulu
- **Moved clients section** to appear immediately after hero video for better impact

### Key Files Modified
- `/filming-in-greece/tax-incentives/index.html` - Updated with latest tax incentive regulations
- `/index.html` - Enhanced client logos section and repositioned for better visibility
- Added 35 SVG files in `/assets/images/client-logos/`