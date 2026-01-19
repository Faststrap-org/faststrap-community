"""ParallaxSection component for Faststrap Community."""

from typing import Any

from fasthtml.common import Div
from faststrap.core.base import merge_classes
from faststrap.core.theme import resolve_defaults

from ..registry import register_component


def ParallaxSection(
    *content: Any, img_src: str, height: str = None, overlay_opacity: float = None, **kwargs
) -> Div:
    """A section with a parallax background effect.

    Args:
        *content: Content to display over the background
        img_src: Source URL for the background image
        height: Height of the section (default: 500px)
        overlay_opacity: Opacity of the background darken overlay (0.0 to 1.0)
        **kwargs: Additional attributes
    """
    cfg = resolve_defaults("ParallaxSection", height=height, overlay_opacity=overlay_opacity)
    h = cfg.get("height") or "500px"
    o = cfg.get("overlay_opacity") if cfg.get("overlay_opacity") is not None else 0.5

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")

    container_cls = merge_classes("fs-comm-parallax-section", user_cls)

    # Base style with background image
    base_style = f"background-image: url('{img_src}'); " f"height: {h};"

    final_style = f"{base_style} {user_style}".strip()

    # Internal darkened overlay
    overlay = Div(
        *content,
        style=f"background: rgba(0,0,0,{o}); width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;",
    )

    return Div(overlay, cls=container_cls, style=final_style, **kwargs)


register_component("ParallaxSection", ParallaxSection)
