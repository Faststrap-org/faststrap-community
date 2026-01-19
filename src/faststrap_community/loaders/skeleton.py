"""SkeletonLoader component - Skeleton loading placeholder."""

from fasthtml.common import Div
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def SkeletonLoader(lines: int = None, avatar: bool = False, width: str = None, **kwargs) -> Div:
    """Skeleton loading placeholder with shimmer effect.

    Args:
        lines: Number of text lines to show (default: 3)
        avatar: Whether to show avatar placeholder
        width: Width of skeleton (default: 100%)
        **kwargs: Additional HTML attributes

    Example:
        >>> SkeletonLoader(lines=4, avatar=True)
    """
    defaults = get_community_defaults("SkeletonLoader")
    num_lines = lines or defaults.get("lines", 3)
    w = width or defaults.get("width", "100%")

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-skeleton-loader", user_cls)

    elements = []

    # Avatar
    if avatar:
        elements.append(Div(cls="skeleton-avatar rounded-circle mb-3"))

    # Text lines
    for i in range(num_lines):
        # Vary widths for realism
        line_width = "100%" if i < num_lines - 1 else "60%"
        elements.append(Div(cls="skeleton-line mb-2", style=f"width: {line_width};"))

    return Div(*elements, cls=container_cls, style=f"width: {w};", **kwargs)


register_component("SkeletonLoader", SkeletonLoader)
