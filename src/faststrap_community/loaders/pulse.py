"""PulseLoader component - Pulsing circle loader."""

from fasthtml.common import Div
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def PulseLoader(variant: str = None, size: str = None, **kwargs) -> Div:
    """Pulsing circle loading animation.

    Args:
        variant: Bootstrap variant color (default: primary)
        size: Size: 'sm', 'md', 'lg' (default: md)
        **kwargs: Additional HTML attributes

    Example:
        >>> PulseLoader(variant="success", size="lg")
    """
    defaults = get_community_defaults("PulseLoader")
    v = variant or defaults.get("variant", "primary")
    s = size or defaults.get("size", "md")

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-pulse-loader", f"pulse-{s}", user_cls)

    # Single pulsing circle
    circle = Div(cls=f"pulse-circle bg-{v}", style=f"background-color: var(--bs-{v});")

    return Div(circle, cls=container_cls, **kwargs)


register_component("PulseLoader", PulseLoader)
