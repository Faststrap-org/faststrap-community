"""IconButton component - Button with icon."""

from fasthtml.common import Button as HtmlButton
from fasthtml.common import Span
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def IconButton(
    icon: str,
    text: str = None,
    variant: str = None,
    size: str = None,
    icon_position: str = "left",
    **kwargs,
) -> HtmlButton:
    """Button with icon.

    Args:
        icon: Icon HTML or emoji
        text: Button text (optional for icon-only button)
        variant: Bootstrap variant
        size: Button size: 'sm', 'lg'
        icon_position: Icon position: 'left' or 'right'
        **kwargs: Additional HTML attributes

    Example:
        >>> IconButton("🚀", "Launch", variant="primary")
        >>> IconButton("⚙️", variant="secondary")  # Icon only
    """
    defaults = get_community_defaults("IconButton")
    v = variant or defaults.get("variant", "primary")

    user_cls = kwargs.pop("cls", "")
    size_cls = f"btn-{size}" if size else ""
    container_cls = merge_classes("fs-comm-icon-button", f"btn btn-{v}", size_cls, user_cls)

    icon_el = Span(icon, cls="me-2" if text and icon_position == "left" else "ms-2" if text else "")

    if text:
        if icon_position == "left":
            content = [icon_el, text]
        else:
            content = [text, icon_el]
    else:
        content = [icon_el]

    return HtmlButton(*content, cls=container_cls, **kwargs)


register_component("IconButton", IconButton)
