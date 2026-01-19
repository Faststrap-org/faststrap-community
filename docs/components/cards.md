# Card Components

Premium card components with animations and visual effects.

---

## FlipCard

3D flip card that rotates on hover to reveal back content.

### Usage

```python
from faststrap_community import FlipCard

FlipCard(
    front=H3("Front Content"),
    back=P("Back Content"),
    height="300px",
    width="100%",
    duration="0.6s"
)
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `front` | Any | Required | Front side content |
| `back` | Any | Required | Back side content |
| `height` | str | `"300px"` | Card height |
| `width` | str | `"100%"` | Card width |
| `duration` | str | `"0.6s"` | Flip animation duration |

### Example

```python
FlipCard(
    front=Div(
        H3("Hover Me!"),
        P("I'll flip around"),
        cls="p-4"
    ),
    back=Div(
        H3("Surprise!"),
        P("This is the back"),
        cls="p-4"
    ),
    height="350px"
)
```

---

## GlowCard

Card with animated glow effect on hover.

### Usage

```python
from faststrap_community import GlowCard

GlowCard(
    H3("Premium Feature"),
    P("Hover to see the glow!"),
    glow_color="#667eea",
    intensity="high"
)
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `*children` | Any | Required | Card content |
| `glow_color` | str | `"var(--bs-primary)"` | Glow color (CSS color) |
| `intensity` | str | `"medium"` | Glow intensity: `low`, `medium`, `high` |

### Example

```python
GlowCard(
    Div(
        H3("Pro Plan"),
        P("$29/month"),
        Button("Subscribe", variant="primary"),
        cls="card-body text-center"
    ),
    glow_color="#ff6b6b",
    intensity="high",
    cls="mb-3"
)
```

---

## ProfileCard

User profile card with avatar, name, title, and action buttons.

### Usage

```python
from faststrap_community import ProfileCard
from faststrap import Button

ProfileCard(
    name="Jane Doe",
    title="Senior Developer",
    avatar="/img/jane.jpg",
    bio="Python enthusiast and open source contributor",
    Button("Follow", variant="primary", size="sm"),
    Button("Message", variant="outline-primary", size="sm")
)
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `name` | str | Required | User's name |
| `title` | str | None | User's title/role |
| `avatar` | str | Placeholder | Avatar image URL |
| `bio` | str | None | Short bio text |
| `*actions` | Any | None | Action buttons |

### Example

```python
ProfileCard(
    name="John Smith",
    title="Product Manager",
    avatar="https://i.pravatar.cc/150?img=12",
    bio="Building amazing products with FastHTML",
    Button("Connect", variant="primary", size="sm"),
    Button("View Profile", variant="outline-secondary", size="sm")
)
```

---

## PricingCard

Pricing tier card with features list and call-to-action.

### Usage

```python
from faststrap_community import PricingCard

PricingCard(
    title="Pro",
    price="$29",
    period="month",
    features=[
        "Unlimited projects",
        "Priority support",
        "Advanced analytics",
        "Custom domain"
    ],
    cta_text="Get Started",
    cta_href="/signup",
    highlighted=True
)
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | str | Required | Plan name |
| `price` | str | Required | Price amount |
| `period` | str | `"month"` | Billing period |
| `features` | List[str] | None | List of features |
| `cta_text` | str | `"Get Started"` | Button text |
| `cta_href` | str | `"#"` | Button link |
| `highlighted` | bool | False | Recommended plan |

### Example

```python
Row(
    Col(
        PricingCard(
            title="Free",
            price="$0",
            features=["5 projects", "Community support"],
            cta_variant="outline-primary"
        ),
        md=4
    ),
    Col(
        PricingCard(
            title="Pro",
            price="$29",
            features=["Unlimited projects", "Priority support", "Analytics"],
            highlighted=True
        ),
        md=4
    ),
    Col(
        PricingCard(
            title="Enterprise",
            price="Custom",
            features=["Everything in Pro", "Dedicated support", "SLA"],
            cta_text="Contact Sales"
        ),
        md=4
    )
)
```

---

## StatCard

Dashboard statistic card with value, trend, and icon.

### Usage

```python
from faststrap_community import StatCard

StatCard(
    title="Total Revenue",
    value="$45,231",
    trend="+12.5%",
    trend_positive=True,
    icon="💰",
    variant="success"
)
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | str | Required | Metric title |
| `value` | str | Required | Metric value |
| `trend` | str | None | Trend indicator (e.g., "+12%") |
| `trend_positive` | bool | True | Trend direction (green/red) |
| `icon` | str | None | Icon emoji or HTML |
| `variant` | str | `"primary"` | Bootstrap variant |

### Example

```python
Row(
    Col(
        StatCard(
            title="Total Users",
            value="12,543",
            trend="+8.2%",
            icon="👥",
            variant="primary"
        ),
        md=3
    ),
    Col(
        StatCard(
            title="Revenue",
            value="$45,231",
            trend="+12.5%",
            icon="💰",
            variant="success"
        ),
        md=3
    ),
    Col(
        StatCard(
            title="Bounce Rate",
            value="32.1%",
            trend="-2.4%",
            trend_positive=True,  # Lower is better
            icon="📊",
            variant="warning"
        ),
        md=3
    )
)
```

---

## TimelineCard

Timeline event card for chronological information.

### Usage

```python
from faststrap_community import TimelineCard

TimelineCard(
    title="Project Launched",
    description="Successfully deployed v1.0 to production",
    timestamp="2 hours ago",
    icon="🚀",
    variant="success"
)
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | str | Required | Event title |
| `description` | str | None | Event description |
| `timestamp` | str | None | Event time |
| `icon` | str | None | Icon emoji or HTML |
| `variant` | str | `"primary"` | Bootstrap variant |

### Example

```python
Div(
    TimelineCard(
        title="Project Started",
        description="Initial planning and setup",
        timestamp="3 days ago",
        icon="📝",
        variant="primary"
    ),
    TimelineCard(
        title="Development Phase",
        description="Built core features",
        timestamp="2 days ago",
        icon="💻",
        variant="info"
    ),
    TimelineCard(
        title="Testing Complete",
        description="All tests passing",
        timestamp="1 day ago",
        icon="✅",
        variant="success"
    ),
    TimelineCard(
        title="Deployed",
        description="Live in production",
        timestamp="2 hours ago",
        icon="🚀",
        variant="success"
    )
)
```

---

## TiltCard

Card with 3D tilt effect on hover.

### Usage

```python
from faststrap_community import TiltCard

TiltCard(
    H3("Tilt Card"),
    P("Hover to see the tilt effect"),
    cls="p-4"
)
```

---

## RevealCard

Card with overlay reveal animation on hover.

### Usage

```python
from faststrap_community import RevealCard

RevealCard(
    image="/img/product.jpg",
    content=Div(
        H3("Product Name"),
        P("Product description"),
        Button("Learn More", variant="light")
    )
)
```

---

**Next:** [Loader Components](loaders.md)
