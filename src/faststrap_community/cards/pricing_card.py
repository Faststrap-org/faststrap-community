"""PricingCard component - Pricing tier card."""

from fasthtml.common import H2, H3, Div, Li, Span, Ul
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def PricingCard(
    title: str,
    price: str,
    period: str = "month",
    features: list[str] = None,
    cta_text: str = "Get Started",
    cta_href: str = "#",
    cta_variant: str = None,
    highlighted: bool = False,
    **kwargs,
) -> Div:
    """Pricing tier card with features list and call-to-action.

    Args:
        title: Plan name (e.g., "Pro", "Enterprise")
        price: Price amount (e.g., "$29", "Free")
        period: Billing period (default: "month")
        features: List of feature strings
        cta_text: Call-to-action button text
        cta_href: CTA button link
        cta_variant: Button variant (default: primary if highlighted, outline-primary otherwise)
        highlighted: Whether this is the recommended/featured plan
        **kwargs: Additional HTML attributes

    Example:
        >>> PricingCard(
        ...     title="Pro",
        ...     price="$29",
        ...     period="month",
        ...     features=[
        ...         "Unlimited projects",
        ...         "Priority support",
        ...         "Advanced analytics",
        ...         "Custom domain"
        ...     ],
        ...     highlighted=True
        ... )
    """
    from faststrap import Button

    get_community_defaults("PricingCard")

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes(
        "fs-comm-pricing-card", "card", "h-100", "border-primary" if highlighted else "", user_cls
    )

    # Determine button variant
    if cta_variant is None:
        cta_variant = "primary" if highlighted else "outline-primary"

    # Build feature list
    feature_items = [
        Li(Span("✓ ", cls="text-success me-2"), feat, cls="mb-2") for feat in (features or [])
    ]

    # Highlighted badge
    badge = None
    if highlighted:
        badge = Div(Span("RECOMMENDED", cls="badge bg-primary"), cls="text-center mb-2")

    return Div(
        Div(
            badge,
            H3(title, cls="card-title text-center mb-3"),
            Div(
                H2(price, cls="display-4 mb-0"),
                Span(f"/ {period}", cls="text-muted"),
                cls="text-center mb-4",
            ),
            Ul(*feature_items, cls="list-unstyled mb-4") if features else None,
            Button(cta_text, href=cta_href, variant=cta_variant, full_width=True),
            cls="card-body d-flex flex-column",
        ),
        cls=container_cls,
        **kwargs,
    )


register_component("PricingCard", PricingCard)
