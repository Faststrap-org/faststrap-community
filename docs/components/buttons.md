# Button Components

Premium button styles and variants.

---

## GradientButton

Button with gradient background.

### Usage

```python
from faststrap_community import GradientButton

GradientButton("Get Started", gradient="purple", size="lg")
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `text` | str | Required | Button text |
| `gradient` | str | `"purple"` | Gradient preset or custom CSS |
| `size` | str | None | Button size: `sm`, `lg` |

### Gradient Presets

- `purple` - Purple to violet
- `blue` - Blue to cyan
- `green` - Green to teal
- `orange` - Pink to yellow
- `pink` - Pink to red

### Example

```python
# Hero CTA
GradientButton("Start Free Trial", gradient="blue", size="lg", href="/signup")

# Custom gradient
GradientButton(
    "Custom",
    gradient="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
)
```

---

## IconButton

Button with icon (emoji or HTML).

### Usage

```python
from faststrap_community import IconButton

IconButton("🚀", "Launch", variant="primary")
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `icon` | str | Required | Icon emoji or HTML |
| `text` | str | None | Button text (optional) |
| `variant` | str | `"primary"` | Bootstrap variant |
| `size` | str | None | Button size: `sm`, `lg` |
| `icon_position` | str | `"left"` | Icon position: `left`, `right` |

### Example

```python
# Icon + text
IconButton("📥", "Download", variant="success")

# Icon only
IconButton("⚙️", variant="secondary")

# Icon on right
IconButton("➡️", "Next", icon_position="right", variant="primary")
```

---

## FloatingActionButton

Floating action button (FAB) for primary actions.

### Usage

```python
from faststrap_community import FloatingActionButton

FloatingActionButton("➕", variant="primary", position="bottom-right")
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `icon` | str | Required | Icon emoji or HTML |
| `variant` | str | `"primary"` | Bootstrap variant |
| `position` | str | `"bottom-right"` | Position on screen |

### Positions

- `bottom-right` - Bottom right corner
- `bottom-left` - Bottom left corner
- `top-right` - Top right corner
- `top-left` - Top left corner

### Example

```python
# Add button (mobile-friendly)
FloatingActionButton(
    "➕",
    variant="success",
    position="bottom-right",
    onclick="openCreateDialog()"
)

# Chat button
FloatingActionButton(
    "💬",
    variant="info",
    position="bottom-left"
)
```

---

**Next:** [Navigation Components](navigation.md)
