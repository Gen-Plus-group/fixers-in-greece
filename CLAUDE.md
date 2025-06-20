# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **static HTML website** for "Fixers in Greece" - a film production services company. The site uses **Tailwind CSS** for styling and consists of multiple HTML pages with a complex directory structure that includes legacy WordPress-generated content.

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
- **Greece Brand Colors**: `greece-blue` (#0080ff), `greece-white` (#ffffff), `greece-dark` (#1c1c1c)
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
  - Primary: `greece-blue` (#0080ff) replacing vietnam-orange
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