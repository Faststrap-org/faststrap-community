# PWA Integration

Faststrap Community provides full Progressive Web App (PWA) support, allowing your components to work seamlessly offline and on mobile devices.

## Overview

PWA integration includes:
- ✅ **Offline Asset Caching** - All community CSS cached for offline use
- ✅ **Mobile Optimization** - Touch-friendly sizing and responsive design
- ✅ **Battery Efficiency** - Reduced animations on mobile
- ✅ **Accessibility** - Reduced motion support

## Setup

### Basic PWA Setup

```python
from fasthtml.common import *
from faststrap import add_bootstrap
from faststrap.pwa import add_pwa
from faststrap_community import setup_community

app, rt = fast_app()

# 1. Add Bootstrap
add_bootstrap(app, theme="blue-ocean")

# 2. Enable PWA
add_pwa(
    app,
    name="My App",
    short_name="App",
    description="My awesome PWA",
    theme_color="#667eea"
)

# 3. Setup Community with PWA mode
setup_community(app, pwa_mode=True)
```

### Manual PWA Integration

For more control, use `setup_community_pwa()`:

```python
from faststrap_community import setup_community, setup_community_pwa

# Basic setup
setup_community(app)

# Then add PWA integration
setup_community_pwa(app)
```

## Cached Assets

When `pwa_mode=True`, the following assets are automatically cached:

- `/community-static/css/community-base.css`
- `/community-static/css/cards.css`
- `/community-static/css/loaders.css`
- `/community-static/css/navbars.css`
- `/community-static/css/effects.css`
- `/community-static/css/forms.css`
- `/community-static/css/buttons.css`

## Mobile Optimizations

### Touch-Friendly Sizing

All interactive elements have minimum 44px tap targets on touch devices:

```css
/* Automatically applied on touch devices */
@media (hover: none) and (pointer: coarse) {
    .fs-comm-icon-button,
    .fs-comm-gradient-button {
        min-height: 44px;
        min-width: 44px;
    }
    
    .fs-comm-fab {
        width: 64px !important;
        height: 64px !important;
    }
}
```

### Responsive Components

Components automatically adapt to mobile:

```python
# FlipCard reduces height on mobile
FlipCard(
    front="Front",
    back="Back",
    height="300px"  # Becomes 250px on mobile automatically
)

# TiltCard disables tilt on mobile (saves battery)
TiltCard("Content")  # No tilt on touch devices
```

### Battery-Efficient Animations

Animations are reduced on mobile to save battery:

```css
@media (max-width: 768px) {
    /* Reduced glow intensity */
    .fs-comm-glow-card::before {
        filter: blur(5px) !important;
    }
}
```

## Accessibility

### Reduced Motion Support

Respects user's motion preferences:

```css
@media (prefers-reduced-motion: reduce) {
    /* All animations disabled */
    .fs-comm-flip-card,
    .fs-comm-pulse-loader,
    .fs-comm-wave-loader {
        animation: none !important;
        transition: none !important;
    }
}
```

### Testing Reduced Motion

```python
# Components work with or without animations
PulseLoader(variant="primary")  # Gracefully degrades
```

## Offline Behavior

### Components Work Offline

All CSS-based components work offline:

```python
# These work offline (CSS only)
✅ FlipCard
✅ GlowCard
✅ PulseLoader
✅ SkeletonLoader
✅ GradientButton

# These require JavaScript (may not work offline)
⚠️ TagInput (uses JS for tag management)
⚠️ ScrollReveal (uses IntersectionObserver)
```

### Handling Offline State

```python
from faststrap_community import SkeletonLoader

@rt("/data")
def get():
    try:
        data = fetch_data()  # May fail offline
        return render_data(data)
    except:
        # Show skeleton loader while offline
        return SkeletonLoader(lines=5, avatar=True)
```

## PWA Best Practices

### 1. Use Offline-First Components

Prefer CSS-only components for critical UI:

```python
# ✅ Good - works offline
GlowCard(
    H3("Offline Ready"),
    P("This card works without internet"),
    glow_color="#667eea"
)

# ⚠️ Requires JavaScript
TagInput(name="tags", tags=["Python"])
```

### 2. Progressive Enhancement

Build with fallbacks:

```python
def render_content(online=True):
    if online:
        return TagInput(name="skills", tags=user_skills)
    else:
        # Fallback to simple input
        return Input(name="skills", value=",".join(user_skills))
```

### 3. Optimize for Mobile

Use mobile-friendly components:

```python
# FloatingActionButton is perfect for mobile
FloatingActionButton(
    icon="➕",
    variant="primary",
    position="bottom-right"
)

# SearchBar is touch-optimized
SearchBar(
    placeholder="Search...",
    action="/search"
)
```

## Testing PWA

### Local Testing

```bash
# Run with HTTPS (required for PWA)
python main.py --ssl

# Or use ngrok
ngrok http 5000
```

### Chrome DevTools

1. Open DevTools → Application
2. Check "Service Workers" - should see community assets
3. Check "Cache Storage" - verify CSS files cached
4. Test offline mode

### Mobile Testing

```bash
# Get local IP
ipconfig  # Windows
ifconfig  # Mac/Linux

# Access from phone
http://192.168.1.x:5000
```

## API Reference

### setup_community()

```python
def setup_community(
    app: Any,
    static_url: str = "/community-static",
    pwa_mode: bool = False
) -> Any
```

**Parameters:**
- `app` - FastHTML app instance
- `static_url` - URL prefix for static files
- `pwa_mode` - Enable PWA optimizations

### setup_community_pwa()

```python
def setup_community_pwa(
    app: Any,
    static_url: str = "/community-static"
) -> Any
```

**Parameters:**
- `app` - FastHTML app instance (must have PWA enabled)
- `static_url` - URL prefix for static files

### get_community_cache_urls()

```python
def get_community_cache_urls(
    static_url: str = "/community-static"
) -> List[str]
```

Returns list of URLs to cache for offline use.

## Examples

### Complete PWA App

```python
from fasthtml.common import *
from faststrap import add_bootstrap
from faststrap.pwa import add_pwa
from faststrap_community import (
    setup_community,
    GlowCard,
    StatCard,
    FloatingActionButton,
    PulseLoader
)

app, rt = fast_app()

# Setup
add_bootstrap(app, theme="blue-ocean")
add_pwa(app, name="Dashboard", theme_color="#667eea")
setup_community(app, pwa_mode=True)

@rt("/")
def get():
    return Container(
        H1("Dashboard"),
        
        # Stats (work offline)
        Row(
            Col(StatCard("Users", "1,234", "+12%", icon="👥"), md=4),
            Col(StatCard("Revenue", "$45K", "+8%", icon="💰"), md=4),
            Col(StatCard("Tasks", "89", "-3%", icon="✅"), md=4),
        ),
        
        # Loading state
        PulseLoader(variant="primary"),
        
        # FAB for mobile
        FloatingActionButton("➕", variant="primary")
    )

serve()
```

---

**Next:** [API Reference](api-reference.md)
