"""TimelineCard component - Timeline event card."""

from fasthtml.common import H5, Div, P, Small, Span
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def TimelineCard(
    title: str,
    description: str = None,
    timestamp: str = None,
    icon: str = None,
    variant: str = None,
    **kwargs,
) -> Div:
    """Timeline event card for displaying chronological information.

    Args:
        title: Event title
        description: Event description
        timestamp: Event timestamp (e.g., "2 hours ago", "Jan 15, 2026")
        icon: Icon HTML or emoji
        variant: Bootstrap variant for accent color
        **kwargs: Additional HTML attributes

    Example:
        >>> TimelineCard(
        ...     title="Project Launched",
        ...     description="Successfully deployed v1.0 to production",
        ...     timestamp="2 hours ago",
        ...     icon="🚀",
        ...     variant="success"
        ... )
    """
    defaults = get_community_defaults("TimelineCard")
    v = variant or defaults.get("variant", "primary")

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-timeline-card", "card", user_cls)

    # Icon badge
    icon_badge = None
    if icon:
        icon_badge = Div(
            Span(icon, cls="fs-5"),
            cls=f"fs-comm-timeline-icon bg-{v} text-white rounded-circle d-flex align-items-center justify-content-center",
            style="width: 40px; height: 40px; position: absolute; left: -20px; top: 20px;",
        )

    # Timestamp
    time_el = Small(timestamp, cls="text-muted") if timestamp else None

    # Description
    desc_el = P(description, cls="card-text mb-0") if description else None

    return Div(
        icon_badge,
        Div(
            Div(H5(title, cls="card-title mb-1"), time_el, cls="mb-2"),
            desc_el,
            cls="card-body",
            style="margin-left: 20px;",
        ),
        cls=container_cls,
        style="position: relative; margin-left: 20px; border-left: 2px solid var(--bs-border-color);",
        **kwargs,
    )


register_component("TimelineCard", TimelineCard)
