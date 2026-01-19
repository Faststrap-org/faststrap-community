"""StatCard component - Dashboard metric card."""

from fasthtml.common import H2, H6, Div, Span
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def StatCard(
    title: str,
    value: str,
    trend: str = None,
    trend_positive: bool = True,
    icon: str = None,
    variant: str = None,
    **kwargs,
) -> Div:
    """Dashboard statistic card with value, trend, and optional icon.

    Args:
        title: Metric title (e.g., "Total Sales")
        value: Metric value (e.g., "$12,345")
        trend: Trend indicator (e.g., "+12.5%", "-3.2%")
        trend_positive: Whether trend is positive (green) or negative (red)
        icon: Icon HTML or emoji
        variant: Bootstrap variant for accent color
        **kwargs: Additional HTML attributes

    Example:
        >>> StatCard(
        ...     title="Total Revenue",
        ...     value="$45,231",
        ...     trend="+12.5%",
        ...     trend_positive=True,
        ...     icon="💰",
        ...     variant="success"
        ... )
    """
    defaults = get_community_defaults("StatCard")
    v = variant or defaults.get("variant", "primary")

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-stat-card", "card", user_cls)

    # Icon element
    icon_el = None
    if icon:
        icon_el = Div(Span(icon, cls="fs-4"), cls=f"text-{v} mb-2")

    # Trend element
    trend_el = None
    if trend:
        trend_color = "success" if trend_positive else "danger"
        trend_icon = "↑" if trend_positive else "↓"
        trend_el = Span(
            trend_icon + " " + trend, cls=f"badge bg-{trend_color}-subtle text-{trend_color} ms-2"
        )

    return Div(
        Div(
            icon_el,
            H6(title, cls="text-muted mb-2"),
            Div(H2(value, cls="mb-0 d-inline"), trend_el, cls="d-flex align-items-center"),
            cls="card-body",
        ),
        cls=container_cls,
        **kwargs,
    )


register_component("StatCard", StatCard)
