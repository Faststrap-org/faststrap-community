"""GlowCard component - Card with animated glow effect."""

from typing import Any

from fasthtml.common import Div
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def GlowCard(*children: Any, glow_color: str = None, intensity: str = None, **kwargs) -> Div:
    """Card with animated glow effect on hover.

    Args:
        *children: Card content
        glow_color: CSS color for glow (default: var(--bs-primary))
        intensity: Glow intensity: 'low', 'medium', 'high' (default: medium)
        **kwargs: Additional HTML attributes

    Example:
        >>> GlowCard(
        ...     H3("Premium Feature"),
        ...     P("Hover to see the glow!"),
        ...     glow_color="#ff6b6b",
        ...     intensity="high"
        ... )
    """
    defaults = get_community_defaults("GlowCard")
    color = glow_color or defaults.get("glow_color", "var(--bs-primary)")
    level = intensity or defaults.get("intensity", "medium")

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")

    container_cls = merge_classes("fs-comm-glow-card", "card", f"glow-{level}", user_cls)

    style = f"--glow-color: {color}; {user_style}".strip()

    return Div(*children, cls=container_cls, style=style, **kwargs)


register_component("GlowCard", GlowCard)
