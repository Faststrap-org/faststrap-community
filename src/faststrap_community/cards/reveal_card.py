"""RevealCard component for Faststrap Community."""

from typing import Any

from fasthtml.common import H4, Div, Img, P
from faststrap.core.base import merge_classes
from faststrap.core.theme import resolve_defaults

from ..registry import register_component


def RevealCard(
    img_src: str,
    title: str,
    description: str = "",
    button: Any = None,
    height: str = None,
    **kwargs,
) -> Div:
    """A card that reveals content on hover.

    Args:
        img_src: Source URL for the background image
        title: Title to show in the overlay
        description: Description text for the overlay
        button: Optional action button/link
        height: Height of the card (default: 300px)
        **kwargs: Additional attributes like cls, style
    """
    cfg = resolve_defaults("RevealCard", height=height)
    h = cfg.get("height") or "300px"

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")

    container_cls = merge_classes("fs-comm-reveal-card card", user_cls)
    final_style = f"height: {h}; {user_style}".strip()

    overlay_content = [H4(title, cls="mb-2")]
    if description:
        overlay_content.append(P(description, cls="mb-3"))
    if button:
        overlay_content.append(button)

    overlay = Div(*overlay_content, cls="fs-comm-reveal-overlay")
    image = Img(src=img_src, cls="fs-comm-reveal-image", alt=title)

    return Div(image, overlay, cls=container_cls, style=final_style, **kwargs)


register_component("RevealCard", RevealCard)
