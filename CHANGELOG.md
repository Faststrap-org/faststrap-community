# Changelog

All notable changes to Faststrap Community will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-19

### Added

#### Cards (8 components)
- **FlipCard** - 3D flip card animation with customizable height, width, and duration
- **TiltCard** - Card with 3D tilt effect on hover
- **RevealCard** - Card with overlay reveal animation
- **GlowCard** - Card with animated glow effect (customizable color and intensity)
- **ProfileCard** - User profile card with avatar, name, title, bio, and action buttons
- **PricingCard** - Pricing tier card with features list, CTA button, and highlight option
- **StatCard** - Dashboard statistic card with value, trend indicator, and icon
- **TimelineCard** - Timeline event card with timestamp, icon, and description

#### Loaders (8 components)
- **DotsLoader** - Bouncing dots loading animation
- **RingLoader** - Spinning ring loading animation
- **PulseLoader** - Pulsing circle animation with size variants (sm/md/lg)
- **SkeletonLoader** - Shimmer loading placeholder with avatar and line options
- **ProgressRing** - SVG-based circular progress indicator (0-100%)
- **WaveLoader** - Wave bar animation
- **TypewriterLoader** - Typing effect animation
- **PolygonLoader** - Geometric loading animation

#### Forms (3 components)
- **AnimatedInput** - Input field with floating label animation (Bootstrap form-floating)
- **SearchBar** - Search input with icon button
- **TagInput** - Tag management input with add/remove functionality

#### Buttons (3 components)
- **GradientButton** - Button with gradient background (5 presets + custom)
- **IconButton** - Button with icon (emoji or HTML) and optional text
- **FloatingActionButton** - Floating action button (FAB) with position options

#### Navigation (4 components)
- **MorphingToggler** - Animated hamburger menu icon (morphs to X)
- **SlideMenuNavbar** - Slide-out navigation menu
- **MegaMenuNavbar** - Mega menu with multi-column layout
- **VerticalMegaMenu** - Vertical mega menu

#### Effects (2 components)
- **ParallaxSection** - Parallax scrolling effect
- **ScrollReveal** - Scroll-triggered reveal animations

#### Core Features
- **Community Defaults System** - Global configuration for all components
  - `set_community_defaults()` - Set global defaults
  - `get_community_defaults()` - Get component defaults
  - `reset_community_defaults()` - Reset to original values
  - `list_community_components()` - List all components

- **PWA Integration** - Full Progressive Web App support
  - `setup_community_pwa()` - PWA optimization
  - `get_community_cache_urls()` - Get cacheable assets
  - Automatic asset caching when `pwa_mode=True`
  - Mobile-responsive CSS optimizations
  - Touch-friendly sizing (44px minimum tap targets)
  - Battery-efficient animations on mobile
  - Reduced motion support for accessibility

- **Setup Functions**
  - `setup_community()` - Mount static files and inject CSS
  - Order enforcement (must be called after `add_bootstrap()`)
  - PWA mode support
  - Automatic theme inheritance

#### Documentation
- Comprehensive documentation in `docs/`
- Getting started guide
- Component documentation for all 28 components
- PWA integration guide
- API reference
- Examples and usage patterns

### Fixed
- **MorphingNavbar** - Removed broken implementation, kept working MorphingToggler
- **DotsLoader** - Fixed style assignment bug (was trying to assign `.style` attribute)
- **Dependencies** - Updated to support Faststrap v0.5.x and v0.6.x
- **setup_community()** - Added strict order enforcement with clear error messages

### Changed
- Improved error messages for common setup issues
- Enhanced mobile responsiveness across all components
- Optimized CSS animations for better performance
- Added comprehensive type hints throughout

### Security
- All components follow WCAG 2.1 AA accessibility guidelines
- XSS protection through proper HTML escaping
- Safe CSS variable usage

## [Unreleased]

### Planned for v0.2.0
- Additional form components (RangeSlider, ColorPicker)
- More button variants
- Template components
- Theme presets
- Enhanced PWA features

---

**Note:** This is the initial release of Faststrap Community. Future releases will maintain backward compatibility following semantic versioning.
