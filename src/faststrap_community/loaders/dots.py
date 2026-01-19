"""DotsLoader component for Faststrap Community."""

from fasthtml.common import Div
from faststrap.core.base import merge_classes
from faststrap.core.theme import resolve_defaults

from ..registry import register_component


def DotsLoader(variant: str = None, **kwargs) -> Div:
    """A bouncing dots loading animation.

    Args:
        variant: Bootstrap variant color (default: primary)
        **kwargs: Additional attributes
    """
    cfg = resolve_defaults("DotsLoader", variant=variant)
    v = cfg.get("variant") or "primary"

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-dots-loader", user_cls)

    # Create 3 dots with proper style parameter
    if v != "primary":
        # Use inline style for non-primary variants
        dots = [Div(style=f"background-color: var(--bs-{v});") for _ in range(3)]
    else:
        # Default styling from CSS
        dots = [Div() for _ in range(3)]

    return Div(*dots, cls=container_cls, **kwargs)


register_component("DotsLoader", DotsLoader)
