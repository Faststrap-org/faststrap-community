"""TiltCard component for Faststrap Community."""

from typing import Any

from fasthtml.common import Div
from faststrap.core.base import merge_classes
from faststrap.core.theme import resolve_defaults

from ..registry import register_component


def TiltCard(*content: Any, **kwargs) -> Div:
    """A card with a 3D lift/tilt effect on hover.

    Args:
        *content: Content to place inside the card
        **kwargs: Additional attributes like cls, style
    """
    resolve_defaults("TiltCard", **kwargs)

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-tilt-card card", user_cls)

    return Div(*content, cls=container_cls, **kwargs)


register_component("TiltCard", TiltCard)
