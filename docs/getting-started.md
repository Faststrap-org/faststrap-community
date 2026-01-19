# Getting Started with Faststrap Community

## Installation

### Using pip

```bash
pip install faststrap-community
```

### From source

```bash
git clone https://github.com/Faststrap-org/faststrap-community
cd faststrap-community
pip install -e .
```

## Requirements

- Python 3.10+
- Faststrap >= 0.5.0
- python-fasthtml >= 0.10.0

## Quick Start

### 1. Basic Setup

```python
from fasthtml.common import *
from faststrap import add_bootstrap
from faststrap_community import setup_community

# Create app
app, rt = fast_app()

# Setup Faststrap (REQUIRED - must be first!)
add_bootstrap(app, theme="blue-ocean")

# Setup Community (must be after add_bootstrap)
setup_community(app)

@rt("/")
def get():
    return Container(H1("Hello, Faststrap Community!"))

serve()
```

> **IMPORTANT:** Always call `add_bootstrap()` BEFORE `setup_community()`. The community components depend on Bootstrap variables and themes.

### 2. Using Components

```python
from faststrap_community import (
    FlipCard, GlowCard, ProfileCard,
    PulseLoader, SkeletonLoader,
    GradientButton, IconButton
)

@rt("/")
def get():
    return Container(
        # Flip card
        FlipCard(
            front=H3("Front Side"),
            back=P("Back Side"),
            height="300px"
        ),
        
        # Glow card
        GlowCard(
            H3("Premium Feature"),
            P("Hover me!"),
            glow_color="#667eea"
        ),
        
        # Loading indicator
        PulseLoader(variant="primary", size="lg"),
        
        # Gradient button
        GradientButton("Get Started", gradient="purple", size="lg")
    )
```

### 3. PWA Support

```python
from faststrap.pwa import add_pwa
from faststrap_community import setup_community

app, rt = fast_app()
add_bootstrap(app)

# Enable PWA
add_pwa(app, name="My App", short_name="App")

# Setup community with PWA mode
setup_community(app, pwa_mode=True)
```

## Component Defaults

Set global defaults for components:

```python
from faststrap_community import set_community_defaults

# Set defaults for FlipCard
set_community_defaults("FlipCard", height="400px", duration="0.8s")

# Set defaults for loaders
set_community_defaults("PulseLoader", variant="success", size="lg")

# Now all FlipCards will use these defaults
card = FlipCard(front="A", back="B")  # Uses 400px height
```

## Project Structure

```
my-app/
├── main.py              # Your FastHTML app
├── requirements.txt     # Dependencies
└── static/             # Your static files
```

**requirements.txt:**
```
fasthtml>=0.10.0
faststrap>=0.5.0
faststrap-community>=0.1.0
```

## Next Steps

- **[Component Documentation](components/)** - Learn about all 28 components
- **[Examples](examples/)** - See real-world examples
- **[PWA Integration](pwa-integration.md)** - Build Progressive Web Apps
- **[API Reference](api-reference.md)** - Complete API documentation

## Common Issues

### "Bootstrap not detected" error

**Problem:** `RuntimeError: setup_community() must be called AFTER add_bootstrap()`

**Solution:** Ensure you call `add_bootstrap()` before `setup_community()`:

```python
# ✅ Correct order
add_bootstrap(app)
setup_community(app)

# ❌ Wrong order
setup_community(app)  # Will raise error!
add_bootstrap(app)
```

### Components not styled correctly

**Problem:** Components render but don't have proper styling.

**Solution:** Make sure community CSS is loaded:

```python
# Check that setup_community was called
setup_community(app)

# Verify static files are mounted
# Community CSS should be at /community-static/css/
```

### PWA cache not working

**Problem:** Community assets not cached offline.

**Solution:** Enable PWA mode:

```python
setup_community(app, pwa_mode=True)
```

## Support

- **Documentation:** [docs/](README.md)
- **GitHub Issues:** [Report a bug](https://github.com/Faststrap-org/faststrap-community/issues)
- **Discord:** Join the community

---

Ready to build? Check out the [Component Documentation](components/) next!
