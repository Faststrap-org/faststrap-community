"""RingLoader component for Faststrap Community."""

from fasthtml.common import Div
from faststrap.core.base import merge_classes
from faststrap.core.theme import resolve_defaults

from ..registry import register_component


def RingLoader(variant: str = None, size: str = None, **kwargs) -> Div:
    """A spinning ring loading animation.

    Args:
        variant: Bootstrap variant color (default: primary)
        size: Size of the ring (default: 64px)
        **kwargs: Additional attributes
    """
    cfg = resolve_defaults("RingLoader", variant=variant, size=size)
    v = cfg.get("variant") or "primary"
    s = cfg.get("size") or "64px"

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")

    container_cls = merge_classes("fs-comm-ring-loader", user_cls)

    # Responsive size
    final_style = f"width: {s}; height: {s}; {user_style}".strip()

    # Create 4 ring segments
    segments = [Div() for _ in range(4)]

    # If variant is not primary, override border color
    if v != "primary":
        for seg in segments:
            seg.style = f"border-color: var(--bs-{v}) transparent transparent transparent;"

    return Div(*segments, cls=container_cls, style=final_style, **kwargs)


register_component("RingLoader", RingLoader)
