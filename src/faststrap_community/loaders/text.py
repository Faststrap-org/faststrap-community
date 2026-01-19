"""Text-based loaders for Faststrap Community."""

from fasthtml.common import Div
from faststrap.core.base import merge_classes

from ..registry import register_component


def TypewriterLoader(text: str = "Loading...", **kwargs) -> Div:
    """
    A typewriter effect loader.

    Args:
        text: Text to display (default: "Loading...")
        **kwargs: Additional attributes
    """
    cls = merge_classes("fs-comm-typewriter-loader", kwargs.pop("cls", ""))
    return Div(cls=cls, data_text=text, **kwargs)


def ShadowLoader(text: str = "Loading...", **kwargs) -> Div:
    """
    A text shadow animation loader.

    Args:
        text: Text to display (default: "Loading...")
        **kwargs: Additional attributes
    """
    cls = merge_classes("fs-comm-shadow-loader", kwargs.pop("cls", ""))
    return Div(cls=cls, data_text=text, **kwargs)


register_component("TypewriterLoader", TypewriterLoader)
register_component("ShadowLoader", ShadowLoader)
