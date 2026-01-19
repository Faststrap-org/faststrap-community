# Contributing to Faststrap Community

Thank you for your interest in contributing to Faststrap Community! This guide will help you get started.

## 🎯 Project Philosophy

Faststrap Community extends Faststrap Core with premium components while maintaining:

- **Pure Python** - Components are Python functions, not templates
- **Modern CSS** - Leverage CSS animations and effects
- **Zero-JS Core** - Most components use pure CSS (JavaScript only when necessary)
- **Seamless Integration** - Inherits Faststrap themes automatically
- **PWA Ready** - All components work offline where possible

## 🚀 Quick Start

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/faststrap-community
cd faststrap-community
```

### 2. Setup Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### 3. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=faststrap_community

# Run specific test file
pytest tests/test_cards.py -v
```

### 4. Code Quality

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Fix linting issues
ruff check src/ tests/ --fix
```

## 📝 Component Development

### Component Template

Use this template when creating new components:

```python
"""ComponentName - Brief description."""

from typing import Any
from fasthtml.common import Div
from faststrap.core.base import merge_classes
from ..defaults import get_community_defaults
from ..registry import register_component


def ComponentName(
    param1: str,
    param2: str = None,
    **kwargs
) -> Div:
    """Brief description.
    
    Args:
        param1: Description
        param2: Description (default: value)
        **kwargs: Additional HTML attributes
        
    Example:
        >>> ComponentName(param1="value")
    """
    # 1. Get defaults
    defaults = get_community_defaults("ComponentName")
    p2 = param2 or defaults.get("param2", "default")
    
    # 2. Extract user classes/styles
    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")
    
    # 3. Build component
    container_cls = merge_classes("fs-comm-component-name", user_cls)
    
    # 4. Return element
    return Div(
        # content
        cls=container_cls,
        style=user_style,
        **kwargs
    )


register_component("ComponentName", ComponentName)
```

### CSS Template

```css
/* ComponentName Styles */
.fs-comm-component-name {
    /* Base styles */
    display: block;
    transition: all 0.3s ease;
}

.fs-comm-component-name:hover {
    /* Hover effects */
}

/* Mobile optimization */
@media (max-width: 768px) {
    .fs-comm-component-name {
        /* Mobile-specific styles */
    }
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
    .fs-comm-component-name {
        animation: none !important;
        transition: none !important;
    }
}
```

### Testing Template

```python
"""Tests for ComponentName."""

from fasthtml.common import to_xml
from faststrap_community import ComponentName


class TestComponentName:
    def test_basic_rendering(self):
        """Test basic component rendering."""
        component = ComponentName(param1="value")
        html = to_xml(component)
        assert "fs-comm-component-name" in html
        assert "value" in html
    
    def test_with_custom_props(self):
        """Test component with custom properties."""
        component = ComponentName(param1="value", param2="custom")
        html = to_xml(component)
        assert "custom" in html
```

## 📂 Project Structure

```
faststrap-community/
├── src/faststrap_community/
│   ├── __init__.py           # Main exports
│   ├── defaults.py           # Defaults system
│   ├── pwa.py               # PWA integration
│   ├── registry.py          # Component registry
│   ├── cards/               # Card components
│   ├── loaders/             # Loader components
│   ├── forms/               # Form components
│   ├── buttons/             # Button components
│   ├── navbars/             # Navigation components
│   ├── effects/             # Effect components
│   └── static/
│       └── css/             # Component CSS
├── tests/                   # Test files
├── docs/                    # Documentation
├── examples/                # Usage examples
└── pyproject.toml          # Project configuration
```

## 🎨 Component Categories

### Cards
Premium card components with animations and effects.
- **Examples:** FlipCard, GlowCard, ProfileCard, PricingCard

### Loaders
Loading animations and progress indicators.
- **Examples:** PulseLoader, SkeletonLoader, ProgressRing

### Forms
Enhanced form inputs and controls.
- **Examples:** AnimatedInput, SearchBar, TagInput

### Buttons
Premium button styles and variants.
- **Examples:** GradientButton, IconButton, FloatingActionButton

### Navigation
Advanced navigation components.
- **Examples:** MorphingToggler, SlideMenuNavbar, MegaMenuNavbar

### Effects
Visual effects and animations.
- **Examples:** ParallaxSection, ScrollReveal

## ✅ Contribution Checklist

Before submitting a pull request:

- [ ] Code follows the component template
- [ ] Tests added and passing
- [ ] Code formatted with `black`
- [ ] Linting passes with `ruff`
- [ ] Component registered in `__init__.py`
- [ ] CSS added to appropriate file
- [ ] Documentation added to `docs/components/`
- [ ] Example added to showcase
- [ ] Defaults added to `defaults.py`
- [ ] PWA compatibility considered

## 📖 Documentation

### Component Documentation

Each component should have:

1. **Docstring** - Clear description and examples
2. **Props Table** - All parameters documented
3. **Usage Examples** - At least 2-3 examples
4. **Markdown Doc** - Entry in `docs/components/`

### Documentation Template

```markdown
## ComponentName

Brief description.

### Usage

\`\`\`python
from faststrap_community import ComponentName

ComponentName(param1="value")
\`\`\`

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `param1` | str | Required | Description |
| `param2` | str | `"default"` | Description |

### Example

\`\`\`python
ComponentName(
    param1="value",
    param2="custom"
)
\`\`\`
```

## 🐛 Bug Reports

When reporting bugs, include:

1. **Description** - Clear description of the issue
2. **Steps to Reproduce** - Minimal code example
3. **Expected Behavior** - What should happen
4. **Actual Behavior** - What actually happens
5. **Environment** - Python version, OS, browser

## 💡 Feature Requests

When requesting features:

1. **Use Case** - Why is this needed?
2. **Proposed Solution** - How should it work?
3. **Alternatives** - Other approaches considered
4. **Examples** - Similar features elsewhere

## 🔄 Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-component`)
3. **Commit** your changes (`git commit -m 'Add amazing component'`)
4. **Push** to the branch (`git push origin feature/amazing-component`)
5. **Open** a Pull Request

### PR Guidelines

- **Title:** Clear, descriptive title
- **Description:** What, why, and how
- **Tests:** All tests passing
- **Docs:** Documentation updated
- **Screenshots:** For UI components

## 🎯 Component Ideas

Looking for ideas? Check out:

- [GitHub Issues](https://github.com/Faststrap-org/faststrap-community/issues?label=component-idea)
- [Discussions](https://github.com/Faststrap-org/faststrap-community/discussions)

Popular requests:
- Additional form components (RangeSlider, ColorPicker)
- More button variants
- Template components
- Theme presets
- Data visualization components

## 📞 Getting Help

- **Documentation:** [docs/](docs/)
- **Discord:** Join the Faststrap community
- **GitHub Discussions:** Ask questions
- **GitHub Issues:** Report bugs

## 🏆 Recognition

Contributors are recognized in:
- `CONTRIBUTORS.md` file
- GitHub contributors page
- Release notes
- Project README

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Faststrap Community! 🎉**
