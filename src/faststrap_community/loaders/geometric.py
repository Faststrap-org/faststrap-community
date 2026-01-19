"""Geometric loaders for Faststrap Community."""

from fasthtml.common import Div
from faststrap.core.base import merge_classes

from ..registry import register_component


def PolygonLoader(**kwargs) -> Div:
    """
    A shape-shifting polygon loader.

    Args:
        **kwargs: Additional attributes
    """
    cls = merge_classes("fs-comm-polygon-loader", kwargs.pop("cls", ""))
    return Div(cls=cls, **kwargs)


register_component("PolygonLoader", PolygonLoader)
