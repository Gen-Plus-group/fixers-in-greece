# Portfolio Container and Spacing System Guide

## Overview

This guide documents the unified container and spacing system implemented to fix layout inconsistencies across all portfolio pages in the Fixers in Greece website.

## Problem Solved

The previous system had multiple issues:
- Mixed container usage (`container`, `max-w-full`, `portfolio-container`)
- Conflicting inline styles and margin inconsistencies
- Excessive use of `!important` declarations
- Inconsistent spacing between sections
- Hero section background and spacing issues
- Navigation container inconsistencies

## New Unified System

### Primary CSS File
- **File**: `/css/portfolio-layout-unified.css`
- **Purpose**: Single source of truth for all container and spacing styles
- **Loads**: After Tailwind CSS but before any page-specific styles

### Container Classes

#### `.portfolio-container`
- **Use**: Primary container for most portfolio content
- **Width**: `max-width: 1200px`
- **Padding**: `1rem` (mobile), `2rem` (tablet+)
- **Centering**: `margin: 0 auto`

```html
<section class="portfolio-section">
    <div class="portfolio-container">
        <!-- Content here -->
    </div>
</section>
```

#### `.portfolio-container-wide`
- **Use**: Wider sections (hero backgrounds, full-width content)
- **Width**: `max-width: 1400px`
- **Padding**: `1rem` (mobile), `2rem` (tablet+)

#### `.portfolio-container-narrow`
- **Use**: Text-focused content (articles, testimonials)
- **Width**: `max-width: 800px`
- **Padding**: `1rem` (mobile), `2rem` (tablet+)

#### `.portfolio-container-full`
- **Use**: Full-width backgrounds and media
- **Width**: `width: 100%`
- **Padding**: `0`

### Section Spacing Classes

#### `.portfolio-section`
- **Use**: Standard section spacing
- **Padding**: `4rem 0`

#### `.portfolio-section-lg`
- **Use**: Large sections (major content areas)
- **Padding**: `6rem 0`

#### `.portfolio-section-sm`
- **Use**: Minor content areas
- **Padding**: `2rem 0`

#### `.portfolio-hero`
- **Use**: Hero sections
- **Padding**: `8rem 0`
- **Includes**: Background positioning and overflow fixes

### Grid Systems

#### `.portfolio-details-grid`
- **Use**: Project details (Client, Type, Services, etc.)
- **Layout**: 1 column (mobile) → 2 columns (tablet) → 4 columns (desktop)
- **Gap**: Responsive spacing

#### `.portfolio-services-grid`
- **Use**: Services showcase grids
- **Layout**: 1 column (mobile) → 2 columns (tablet+)

#### `.portfolio-locations-grid`
- **Use**: Location cards
- **Layout**: 1 column (mobile) → 2 columns (tablet) → 3 columns (desktop)

### Content Wrappers

#### `.portfolio-overview`
- **Use**: Project overview text sections
- **Width**: `max-width: 56rem`
- **Centering**: `margin: 0 auto`

#### `.portfolio-cta`
- **Use**: Call-to-action sections
- **Width**: `max-width: 56rem`
- **Centering**: `margin: 0 auto`

#### `.portfolio-testimonial`
- **Use**: Testimonial sections
- **Width**: `max-width: 48rem`
- **Centering**: `margin: 0 auto`
- **Alignment**: `text-align: center`

## Implementation Examples

### Basic Page Structure
```html
<!-- Hero Section -->
<section class="portfolio-hero relative">
    <div class="portfolio-container relative z-10">
        <h1>Page Title</h1>
        <p>Subtitle content</p>
    </div>
</section>

<!-- Content Section -->
<section class="portfolio-section bg-gray-800">
    <div class="portfolio-container">
        <div class="portfolio-overview">
            <h2>Section Title</h2>
            <p>Content...</p>
        </div>
    </div>
</section>

<!-- Details Grid -->
<section class="portfolio-section bg-greece-dark">
    <div class="portfolio-container">
        <div class="portfolio-details-grid">
            <div class="portfolio-detail-item">
                <h3>Client</h3>
                <p class="text-greece-blue">BBC</p>
            </div>
            <!-- More details... -->
        </div>
    </div>
</section>
```

### Video Section
```html
<section class="portfolio-section portfolio-video-section">
    <div class="portfolio-container-wide">
        <div class="portfolio-container-narrow mx-auto">
            <div class="video-container">
                <iframe src="..."></iframe>
            </div>
        </div>
    </div>
</section>
```

## Responsive Behavior

### Breakpoints
- **Mobile**: `< 768px` - Single column layouts, smaller padding
- **Tablet**: `768px - 1024px` - Two column grids, medium padding
- **Desktop**: `> 1024px` - Full grid layouts, larger padding

### Container Padding
- **Mobile**: `1rem` left/right padding
- **Tablet+**: `2rem` left/right padding

### Grid Responsiveness
All grids automatically adapt:
- Mobile: Stack to single column
- Tablet: Reduce to 2 columns
- Desktop: Full multi-column layout

## Migration from Old System

### Deprecated Files
- ❌ `/portfolio-alignment-fix.css` - Replaced
- ❌ `/portfolio-spacing-fix.css` - Replaced
- ⚠️ CSS with `!important` declarations - Being phased out

### Common Replacements

#### Container Classes
```html
<!-- OLD -->
<div class="container mx-auto px-4 max-w-full">
<div class="max-w-4xl mx-auto">

<!-- NEW -->
<div class="portfolio-container">
<div class="portfolio-overview">
```

#### Section Spacing
```html
<!-- OLD -->
<section class="py-16">
<section class="py-20">

<!-- NEW -->
<section class="portfolio-section">
<section class="portfolio-section-lg">
```

#### Grid Systems
```html
<!-- OLD -->
<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">

<!-- NEW -->
<div class="portfolio-details-grid">
```

## Benefits

1. **Consistency**: Single source of truth for all layouts
2. **Maintainability**: One file to update instead of multiple scattered styles
3. **Performance**: Eliminates conflicting CSS and reduces specificity wars
4. **Responsive**: Built-in responsive behavior for all components
5. **Semantic**: Clear, descriptive class names
6. **Accessibility**: Proper focus states and layout containment

## File Integration

### In HTML Files
Add after Tailwind CSS:
```html
<!-- Portfolio Layout Unified CSS -->
<link rel="preload" href="/css/portfolio-layout-unified.css?v=20250626" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/css/portfolio-layout-unified.css?v=20250626"></noscript>
```

### CSS Load Order
1. Tailwind CSS (base)
2. Portfolio Layout Unified CSS (layout system)
3. Theme/component CSS (styling)
4. Page-specific CSS (if needed)

## Future Maintenance

### Adding New Components
When creating new portfolio components:
1. Use existing container classes first
2. Only create new classes if absolutely necessary
3. Follow the naming convention: `.portfolio-{component}-{modifier}`
4. Add responsive behavior from the start

### Performance Considerations
- All containers use `contain: layout style` for better performance
- No `!important` declarations to reduce specificity conflicts
- Efficient grid systems with `minmax()` for better browser optimization

This system provides a solid foundation for consistent, maintainable, and responsive portfolio layouts across the entire website.