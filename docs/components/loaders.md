# Loader Components

Beautiful loading animations for various use cases.

---

## PulseLoader

Pulsing circle animation.

### Usage

```python
from faststrap_community import PulseLoader

PulseLoader(variant="primary", size="lg")
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | str | `"primary"` | Bootstrap variant |
| `size` | str | `"md"` | Size: `sm`, `md`, `lg` |

---

## SkeletonLoader

Shimmer loading placeholder for content.

### Usage

```python
from faststrap_community import SkeletonLoader

SkeletonLoader(lines=4, avatar=True, width="100%")
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `lines` | int | `3` | Number of text lines |
| `avatar` | bool | False | Show avatar placeholder |
| `width` | str | `"100%"` | Skeleton width |

### Example

```python
# Loading state for profile
SkeletonLoader(lines=3, avatar=True)

# Loading state for article
SkeletonLoader(lines=5, width="80%")
```

---

## ProgressRing

SVG-based circular progress indicator.

### Usage

```python
from faststrap_community import ProgressRing

ProgressRing(value=75, max_value=100, variant="success", show_text=True)
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | int | Required | Current progress value |
| `max_value` | int | `100` | Maximum value |
| `size` | str | `"4rem"` | Ring size |
| `variant` | str | `"primary"` | Bootstrap variant |
| `show_text` | bool | True | Show percentage text |

### Example

```python
# Upload progress
ProgressRing(value=upload_percent, variant="success", size="6rem")

# Task completion
ProgressRing(value=completed_tasks, max_value=total_tasks, variant="info")
```

---

## WaveLoader

Wave bar animation.

### Usage

```python
from faststrap_community import WaveLoader

WaveLoader(variant="info")
```

---

## DotsLoader

Bouncing dots animation.

### Usage

```python
from faststrap_community import DotsLoader

DotsLoader(variant="primary")
```

---

## RingLoader

Spinning ring animation.

### Usage

```python
from faststrap_community import RingLoader

RingLoader(variant="primary", size="3rem")
```

---

**Next:** [Form Components](forms.md)
