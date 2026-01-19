# Faststrap Community 🚀

**Premium, modern components for [Faststrap](https://github.com/Faststrap-org/Faststrap) and FastHTML.**

[![PyPI version](https://badge.fury.io/py/faststrap-community.svg)](https://badge.fury.io/py/faststrap-community)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Faststrap Community extends Faststrap Core with **28 premium components** including cards, loaders, forms, buttons, navigation, and effects. Built with the same philosophy: **Pure Python, Modern CSS, Zero JavaScript (where possible)**.

## ✨ Features

- 🎨 **28 Premium Components** - Cards, loaders, forms, buttons, navigation, effects
- 🎯 **Theme Inheritance** - Automatically inherits Faststrap themes
- 📱 **PWA Ready** - Full Progressive Web App support
- 🚀 **Zero-JS Core** - Most components use pure CSS animations
- ♿ **Accessible** - WCAG 2.1 AA compliant with reduced motion support
- 📦 **Modular** - Install only what you need

## 📦 Installation

### Basic Installation

All 28 components are included in the base installation:

```bash
pip install faststrap-community
```

### Optional Extras

While all components are included by default, you can use extras for documentation clarity:

```bash
# Install with specific category markers (all components still included)
pip install faststrap-community[cards]     # Card components
pip install faststrap-community[loaders]   # Loader components
pip install faststrap-community[forms]     # Form components
pip install faststrap-community[buttons]   # Button components
pip install faststrap-community[navbars]   # Navigation components
pip install faststrap-community[effects]   # Effect components
pip install faststrap-community[pwa]       # PWA utilities

# Install with development tools
pip install faststrap-community[dev]       # Includes pytest, black, ruff

# Install everything (same as base, but explicit)
pip install faststrap-community[all]
```

> **Note:** Unlike some packages, faststrap-community includes ALL components in the base install. The extras above are provided for documentation purposes only and don't change what's installed.

**Requirements:**
- Python 3.10+
- Faststrap >= 0.5.0
- python-fasthtml >= 0.10.0

## 🚀 Quick Start

```python
from fasthtml.common import *
from faststrap import add_bootstrap
from faststrap_community import setup_community, GlowCard, PulseLoader

app, rt = fast_app()

# 1. Add Faststrap (REQUIRED - must be first!)
add_bootstrap(app, theme="blue-ocean")

# 2. Setup Community (must be after add_bootstrap)
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

> **IMPORTANT:** Always call `add_bootstrap()` BEFORE `setup_community()`. Community components depend on Bootstrap variables.

## 📚 Components

### Cards (8 components)
Premium card components with animations and effects.

| Component | Description |
|-----------|-------------|
| **FlipCard** | 3D flip animation on hover |
| **TiltCard** | Tilt effect on hover |
| **RevealCard** | Overlay reveal animation |
| **GlowCard** | Animated glow effect |
| **ProfileCard** | User profile with avatar and actions |
| **PricingCard** | Pricing tier with features list |
| **StatCard** | Dashboard metric with trend |
| **TimelineCard** | Timeline event card |

### Loaders (8 components)
Beautiful loading animations.

| Component | Description |
|-----------|-------------|
| **DotsLoader** | Bouncing dots animation |
| **RingLoader** | Spinning ring animation |
| **PulseLoader** | Pulsing circle animation |
| **SkeletonLoader** | Shimmer loading placeholder |
| **ProgressRing** | SVG circular progress (0-100%) |
| **WaveLoader** | Wave bar animation |
| **TypewriterLoader** | Typing effect animation |
| **PolygonLoader** | Geometric animation |

### Forms (3 components)
Enhanced form inputs.

| Component | Description |
|-----------|-------------|
| **AnimatedInput** | Input with floating label animation |
| **SearchBar** | Search input with icon button |
| **TagInput** | Tag management with add/remove |

### Buttons (3 components)
Premium button styles.

| Component | Description |
|-----------|-------------|
| **GradientButton** | Button with gradient background |
| **IconButton** | Button with icon (emoji or HTML) |
| **FloatingActionButton** | Floating action button (FAB) |

### Navigation (4 components)
Advanced navigation components.

| Component | Description |
|-----------|-------------|
| **MorphingToggler** | Animated hamburger menu icon |
| **SlideMenuNavbar** | Slide-out navigation menu |
| **MegaMenuNavbar** | Mega menu with columns |
| **VerticalMegaMenu** | Vertical mega menu |

### Effects (2 components)
Visual effects and animations.

| Component | Description |
|-----------|-------------|
| **ParallaxSection** | Parallax scrolling effect |
| **ScrollReveal** | Scroll-triggered animations |

## 🎯 Examples

### Dashboard with Stats

```python
from faststrap_community import StatCard, PulseLoader

Row(
    Col(StatCard("Users", "12,543", "+8.2%", icon="👥"), md=3),
    Col(StatCard("Revenue", "$45,231", "+12.5%", icon="💰"), md=3),
    Col(StatCard("Tasks", "89", "-3%", icon="✅"), md=3),
    Col(PulseLoader(variant="primary"), md=3)
)
```

### Pricing Page

```python
from faststrap_community import PricingCard

Row(
    Col(
        PricingCard(
            title="Free",
            price="$0",
            features=["5 projects", "Community support"]
        ),
        md=4
    ),
    Col(
        PricingCard(
            title="Pro",
            price="$29",
            period="month",
            features=["Unlimited projects", "Priority support"],
            highlighted=True
        ),
        md=4
    ),
    Col(
        PricingCard(
            title="Enterprise",
            price="Custom",
            features=["Everything in Pro", "SLA"],
            cta_text="Contact Sales"
        ),
        md=4
    )
)
```

### Profile Cards

```python
from faststrap_community import ProfileCard
from faststrap import Button

ProfileCard(
    name="Jane Doe",
    title="Senior Developer",
    avatar="https://i.pravatar.cc/150",
    bio="Python enthusiast and open source contributor",
    Button("Follow", variant="primary", size="sm"),
    Button("Message", variant="outline-primary", size="sm")
)
```

## 🔧 Configuration

### Component Defaults

Set global defaults for components:

```python
from faststrap_community import set_community_defaults

# Set defaults for FlipCard
set_community_defaults("FlipCard", height="400px", duration="0.8s")

# Set defaults for loaders
set_community_defaults("PulseLoader", variant="success", size="lg")

# Now all components use these defaults
card = FlipCard(front="A", back="B")  # Uses 400px height
loader = PulseLoader()  # Uses success variant, lg size
```

### PWA Support

Enable Progressive Web App features:

```python
from faststrap.pwa import add_pwa
from faststrap_community import setup_community

add_bootstrap(app)
add_pwa(app, name="My App")
setup_community(app, pwa_mode=True)  # Caches community assets
```

## 📖 Documentation

- **[Getting Started](docs/getting-started.md)** - Installation and setup
- **[Components](docs/components/)** - Detailed component docs
- **[PWA Integration](docs/pwa-integration.md)** - Progressive Web App guide
- **[API Reference](docs/api-reference.md)** - Complete API documentation
- **[Examples](docs/examples/)** - Real-world examples

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
git clone https://github.com/Faststrap-org/faststrap-community
cd faststrap-community
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/ tests/
ruff check src/ tests/
```

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

Built with ❤️ by the Faststrap community.

- **Faststrap Core:** [github.com/Faststrap-org/Faststrap](https://github.com/Faststrap-org/Faststrap)
- **FastHTML:** [github.com/AnswerDotAI/fasthtml](https://github.com/AnswerDotAI/fasthtml)
- **Bootstrap:** [getbootstrap.com](https://getbootstrap.com)

## 🔗 Links

- **Documentation:** [docs/](docs/)
- **GitHub:** [github.com/Faststrap-org/faststrap-community](https://github.com/Faststrap-org/faststrap-community)
- **PyPI:** [pypi.org/project/faststrap-community](https://pypi.org/project/faststrap-community)
- **Discord:** Join the Faststrap community

---

**Made with Faststrap Community? [Share your project!](https://github.com/Faststrap-org/faststrap-community/discussions)**
