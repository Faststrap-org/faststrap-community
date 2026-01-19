# API Reference

Complete API documentation for Faststrap Community.

## Setup Functions

### setup_community()

Mount community static files and inject CSS headers.

```python
def setup_community(
    app: Any,
    static_url: str = "/community-static",
    pwa_mode: bool = False
) -> Any
```

**Parameters:**
- `app` (Any): FastHTML application instance
- `static_url` (str): URL prefix for community static files (default: `"/community-static"`)
- `pwa_mode` (bool): Enable PWA optimizations (default: `False`)

**Returns:** The app instance

**Raises:**
- `RuntimeError`: If app is invalid or Bootstrap not detected

**Example:**
```python
from faststrap import add_bootstrap
from faststrap_community import setup_community

app, rt = fast_app()
add_bootstrap(app)
setup_community(app, pwa_mode=True)
```

---

### setup_community_pwa()

Setup community with PWA optimization.

```python
def setup_community_pwa(
    app: Any,
    static_url: str = "/community-static"
) -> Any
```

**Parameters:**
- `app` (Any): FastHTML application instance (must have PWA enabled)
- `static_url` (str): URL prefix for community static files

**Returns:** The app instance

**Raises:**
- `RuntimeError`: If PWA is not enabled

**Example:**
```python
from faststrap.pwa import add_pwa
from faststrap_community import setup_community, setup_community_pwa

add_pwa(app, name="My App")
setup_community(app)
setup_community_pwa(app)
```

---

### get_community_cache_urls()

Get list of community assets to cache for PWA.

```python
def get_community_cache_urls(
    static_url: str = "/community-static"
) -> List[str]
```

**Parameters:**
- `static_url` (str): URL prefix for community static files

**Returns:** List of URLs to cache

**Example:**
```python
from faststrap_community import get_community_cache_urls

urls = get_community_cache_urls()
# ['/community-static/css/community-base.css', ...]
```

---

## Defaults System

### set_community_defaults()

Set global defaults for a community component.

```python
def set_community_defaults(
    component: str,
    **defaults: Any
) -> None
```

**Parameters:**
- `component` (str): Component name (e.g., `"FlipCard"`)
- `**defaults`: Default values to set

**Example:**
```python
from faststrap_community import set_community_defaults

# Set defaults for FlipCard
set_community_defaults("FlipCard", height="400px", duration="0.8s")

# Set defaults for loaders
set_community_defaults("PulseLoader", variant="success", size="lg")
```

---

### get_community_defaults()

Get defaults for a community component.

```python
def get_community_defaults(
    component: str
) -> Dict[str, Any]
```

**Parameters:**
- `component` (str): Component name

**Returns:** Dictionary of default values

**Example:**
```python
from faststrap_community import get_community_defaults

defaults = get_community_defaults("FlipCard")
# {'height': '300px', 'width': '100%', 'duration': '0.6s'}
```

---

### reset_community_defaults()

Reset all community defaults to initial values.

```python
def reset_community_defaults() -> None
```

**Example:**
```python
from faststrap_community import reset_community_defaults

set_community_defaults("FlipCard", height="500px")
reset_community_defaults()
# FlipCard now uses original default (300px)
```

---

### list_community_components()

List all community components with defaults.

```python
def list_community_components() -> List[str]
```

**Returns:** List of component names

**Example:**
```python
from faststrap_community import list_community_components

components = list_community_components()
# ['FlipCard', 'GlowCard', 'DotsLoader', ...]
```

---

## Component Categories

### Cards (8)
- `FlipCard` - 3D flip animation
- `TiltCard` - Tilt on hover
- `RevealCard` - Overlay reveal
- `GlowCard` - Animated glow effect
- `ProfileCard` - User profiles
- `PricingCard` - Pricing tiers
- `StatCard` - Dashboard metrics
- `TimelineCard` - Timeline events

### Loaders (8)
- `DotsLoader` - Bouncing dots
- `RingLoader` - Spinning ring
- `PulseLoader` - Pulsing circle
- `SkeletonLoader` - Shimmer placeholder
- `ProgressRing` - Circular progress
- `WaveLoader` - Wave animation
- `TypewriterLoader` - Typing effect
- `PolygonLoader` - Geometric animation

### Forms (3)
- `AnimatedInput` - Floating label
- `SearchBar` - Search with icon
- `TagInput` - Tag management

### Buttons (3)
- `GradientButton` - Gradient backgrounds
- `IconButton` - Icon + text
- `FloatingActionButton` - FAB

### Navigation (4)
- `MorphingToggler` - Animated hamburger
- `SlideMenuNavbar` - Slide-out menu
- `MegaMenuNavbar` - Mega menu
- `VerticalMegaMenu` - Vertical mega menu

### Effects (2)
- `ParallaxSection` - Parallax scrolling
- `ScrollReveal` - Scroll animations

---

## Type Definitions

### Common Types

```python
# Bootstrap variant
VariantType = Literal[
    "primary", "secondary", "success", "danger",
    "warning", "info", "light", "dark"
]

# Size
SizeType = Literal["sm", "md", "lg"]

# Position
PositionType = Literal[
    "top-left", "top-right",
    "bottom-left", "bottom-right"
]
```

---

## CSS Variables

Community components use Bootstrap CSS variables for theming:

```css
/* Colors */
--bs-primary
--bs-secondary
--bs-success
--bs-danger
--bs-warning
--bs-info

/* Shadows */
--fs-comm-shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1)
--fs-comm-shadow-md: 0 4px 8px rgba(0, 0, 0, 0.15)
--fs-comm-shadow-lg: 0 8px 16px rgba(0, 0, 0, 0.2)
```

---

## Static Files

Community static files are served from `/community-static/` by default:

```
/community-static/
├── css/
│   ├── community-base.css    # Base styles & PWA optimizations
│   ├── cards.css             # Card components
│   ├── loaders.css           # Loader animations
│   ├── navbars.css           # Navigation components
│   ├── effects.css           # Visual effects
│   ├── forms.css             # Form components
│   └── buttons.css           # Button components
```

---

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile: iOS Safari 14+, Chrome Android

---

## Accessibility

All components follow WCAG 2.1 AA guidelines:

- ✅ Keyboard navigation
- ✅ Screen reader support
- ✅ Reduced motion support
- ✅ Touch-friendly sizing (44px minimum)
- ✅ Color contrast compliance

---

**Next:** [Examples](examples/)
