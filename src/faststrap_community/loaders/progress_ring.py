"""ProgressRing component - Circular progress indicator."""

from fasthtml.common import Circle, Div, Svg
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def ProgressRing(
    value: int,
    max_value: int = 100,
    size: str = None,
    variant: str = None,
    show_text: bool = True,
    **kwargs,
) -> Div:
    """Circular progress indicator using SVG.

    Args:
        value: Current progress value
        max_value: Maximum value (default: 100)
        size: Size in pixels or rem (default: 4rem)
        variant: Bootstrap variant color (default: primary)
        show_text: Whether to show percentage text
        **kwargs: Additional HTML attributes

    Example:
        >>> ProgressRing(value=75, variant="success")
    """
    defaults = get_community_defaults("ProgressRing")
    s = size or defaults.get("size", "4rem")
    v = variant or defaults.get("variant", "primary")

    # Calculate percentage
    percentage = min(100, max(0, (value / max_value) * 100))

    # SVG circle math
    radius = 45
    circumference = 2 * 3.14159 * radius
    stroke_offset = circumference - (percentage / 100) * circumference

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-progress-ring", user_cls)

    # SVG circle
    svg = Svg(
        # Background circle
        Circle(
            cx="50",
            cy="50",
            r=str(radius),
            fill="none",
            stroke="var(--bs-border-color)",
            stroke_width="8",
        ),
        # Progress circle
        Circle(
            cx="50",
            cy="50",
            r=str(radius),
            fill="none",
            stroke=f"var(--bs-{v})",
            stroke_width="8",
            stroke_dasharray=str(circumference),
            stroke_dashoffset=str(stroke_offset),
            stroke_linecap="round",
            transform="rotate(-90 50 50)",
            style="transition: stroke-dashoffset 0.3s ease;",
        ),
        viewBox="0 0 100 100",
        style=f"width: {s}; height: {s};",
    )

    # Text overlay
    text_el = None
    if show_text:
        text_el = Div(
            f"{int(percentage)}%",
            cls="position-absolute top-50 start-50 translate-middle fw-bold",
            style="font-size: 0.875rem;",
        )

    return Div(
        svg,
        text_el,
        cls=container_cls,
        style="position: relative; display: inline-block;",
        **kwargs,
    )


register_component("ProgressRing", ProgressRing)
