"""FlipCard component for Faststrap Community."""

from typing import Any

from fasthtml.common import Div
from faststrap.core.base import merge_classes
from faststrap.core.theme import resolve_defaults

from ..registry import register_component


def FlipCard(
    front: Any, back: Any, height: str = None, width: str = None, duration: str = None, **kwargs
) -> Div:
    """A 3D flip card component.

    Args:
        front: Content for the front face
        back: Content for the back face
        height: Height of the card (default: 300px)
        width: Width of the card (default: 100%)
        duration: Duration of the flip animation (default: 0.6s)
        **kwargs: Additional attributes like cls, style, click handlers
    """
    # Resolve global defaults (if set via set_component_defaults("FlipCard", ...))
    cfg = resolve_defaults("FlipCard", height=height, width=width, duration=duration)

    # Extract resolved values or use hardcoded fallbacks
    h = cfg.get("height") or "300px"
    w = cfg.get("width") or "100%"
    d = cfg.get("duration") or "0.6s"

    # Extract user-provided style and class
    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")

    # Build container classes
    container_cls = merge_classes("fs-comm-flip-card", user_cls)

    # Build container styles - Merge user style with component required styles
    base_styles = f"height: {h}; width: {w};"
    if d != "0.6s":
        base_styles += f" --fs-comm-flip-duration: {d};"

    final_style = f"{base_styles} {user_style}".strip()

    # Structure:
    # Div (container)
    #   Div (inner)
    #     Div (front face)
    #     Div (back face)

    inner = Div(
        Div(front, cls="fs-comm-flip-card-front card"),  # Add 'card' for basic bs styling
        Div(back, cls="fs-comm-flip-card-back card"),
        cls="fs-comm-flip-card-inner",
    )

    return Div(inner, cls=container_cls, style=final_style, **kwargs)


# Register with community registry
register_component("FlipCard", FlipCard)
