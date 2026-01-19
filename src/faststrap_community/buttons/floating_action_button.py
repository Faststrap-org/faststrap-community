"""FloatingActionButton component - Floating action button (FAB)."""

from fasthtml.common import Button as HtmlButton
from fasthtml.common import Span
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def FloatingActionButton(
    icon: str, variant: str = None, position: str = "bottom-right", **kwargs
) -> HtmlButton:
    """Floating action button (FAB) for primary actions.

    Args:
        icon: Icon HTML or emoji
        variant: Bootstrap variant (default: primary)
        position: Position: 'bottom-right', 'bottom-left', 'top-right', 'top-left'
        **kwargs: Additional HTML attributes

    Example:
        >>> FloatingActionButton("➕", variant="success", position="bottom-right")
    """
    defaults = get_community_defaults("FloatingActionButton")
    v = variant or defaults.get("variant", "primary")
    pos = position or defaults.get("position", "bottom-right")

    # Position styles
    positions = {
        "bottom-right": "bottom: 2rem; right: 2rem;",
        "bottom-left": "bottom: 2rem; left: 2rem;",
        "top-right": "top: 2rem; right: 2rem;",
        "top-left": "top: 2rem; left: 2rem;",
    }

    position_style = positions.get(pos, positions["bottom-right"])

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")

    container_cls = merge_classes("fs-comm-fab", f"btn btn-{v}", "rounded-circle", user_cls)

    style = (
        f"position: fixed; {position_style} "
        f"width: 56px; height: 56px; "
        f"box-shadow: 0 4px 8px rgba(0,0,0,0.3); "
        f"z-index: 1000; "
        f"{user_style}"
    ).strip()

    return HtmlButton(Span(icon, cls="fs-4"), cls=container_cls, style=style, **kwargs)


register_component("FloatingActionButton", FloatingActionButton)
