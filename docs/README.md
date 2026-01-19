# Faststrap Community Documentation

Welcome to the **Faststrap Community** documentation! This library provides premium, modern components that seamlessly integrate with Faststrap Core.

## 📚 Documentation Structure

- **[Getting Started](getting-started.md)** - Installation and quick start
- **[Components](components/)** - Detailed component documentation
- **[Examples](examples/)** - Real-world usage examples
- **[PWA Integration](pwa-integration.md)** - Progressive Web App support
- **[API Reference](api-reference.md)** - Complete API documentation
- **[Contributing](../CONTRIBUTING.md)** - How to contribute

## 🎨 Component Categories

### Cards (8 components)
Premium card components with animations and effects.
- [FlipCard](components/cards.md#flipcard) - 3D flip animation
- [TiltCard](components/cards.md#tiltcard) - Tilt on hover
- [RevealCard](components/cards.md#revealcard) - Overlay reveal
- [GlowCard](components/cards.md#glowcard) - Animated glow effect
- [ProfileCard](components/cards.md#profilecard) - User profiles
- [PricingCard](components/cards.md#pricingcard) - Pricing tiers
- [StatCard](components/cards.md#statcard) - Dashboard metrics
- [TimelineCard](components/cards.md#timelinecard) - Timeline events

### Loaders (8 components)
Beautiful loading animations.
- [DotsLoader](components/loaders.md#dotsloader) - Bouncing dots
- [RingLoader](components/loaders.md#ringloader) - Spinning ring
- [PulseLoader](components/loaders.md#pulseloader) - Pulsing circle
- [SkeletonLoader](components/loaders.md#skeletonloader) - Shimmer placeholder
- [ProgressRing](components/loaders.md#progressring) - Circular progress
- [WaveLoader](components/loaders.md#waveloader) - Wave animation
- [TypewriterLoader](components/loaders.md#typewriterloader) - Typing effect
- [PolygonLoader](components/loaders.md#polygonloader) - Geometric animation

### Forms (3 components)
Enhanced form inputs.
- [AnimatedInput](components/forms.md#animatedinput) - Floating label
- [SearchBar](components/forms.md#searchbar) - Search with icon
- [TagInput](components/forms.md#taginput) - Tag management

### Buttons (3 components)
Premium button styles.
- [GradientButton](components/buttons.md#gradientbutton) - Gradient backgrounds
- [IconButton](components/buttons.md#iconbutton) - Icon + text
- [FloatingActionButton](components/buttons.md#floatingactionbutton) - FAB

### Navigation (4 components)
Advanced navigation components.
- [MorphingToggler](components/navigation.md#morphingtoggler) - Animated hamburger
- [SlideMenuNavbar](components/navigation.md#slidemenunavbar) - Slide-out menu
- [MegaMenuNavbar](components/navigation.md#megamenunavbar) - Mega menu
- [VerticalMegaMenu](components/navigation.md#verticalmegamenu) - Vertical mega menu

### Effects (2 components)
Visual effects and animations.
- [ParallaxSection](components/effects.md#parallaxsection) - Parallax scrolling
- [ScrollReveal](components/effects.md#scrollreveal) - Scroll animations

## 🚀 Quick Example

```python
from fasthtml.common import *
from faststrap import add_bootstrap
from faststrap_community import setup_community, GlowCard, PulseLoader

app, rt = fast_app()
add_bootstrap(app, theme="blue-ocean")
setup_community(app, pwa_mode=True)

@rt("/")
def get():
    return Container(
        H1("Welcome to Faststrap Community"),
        
        # Glowing card
        GlowCard(
            H3("Premium Feature"),
            P("Hover to see the glow effect!"),
            glow_color="#667eea",
            intensity="high"
        ),
        
        # Loading indicator
        PulseLoader(variant="success", size="lg")
    )

serve()
```

## 🎯 Key Features

- ✅ **28 Premium Components** - Cards, loaders, forms, buttons, navigation
- ✅ **Zero-JS Core** - Most components use pure CSS animations
- ✅ **PWA Ready** - Full Progressive Web App support
- ✅ **Theme Integration** - Inherits Faststrap themes automatically
- ✅ **Mobile Optimized** - Touch-friendly and responsive
- ✅ **Accessible** - WCAG 2.1 AA compliant with reduced motion support

## 📖 Learn More

- [Installation Guide](getting-started.md#installation)
- [Component Defaults](api-reference.md#defaults-system)
- [PWA Integration](pwa-integration.md)
- [Examples Gallery](examples/)

## 🤝 Community

- **GitHub:** [faststrap-community](https://github.com/Faststrap-org/faststrap-community)
- **Discord:** Join the Faststrap community
- **Contributing:** See [CONTRIBUTING.md](../CONTRIBUTING.md)

---

**Built with ❤️ by the Faststrap Community**
