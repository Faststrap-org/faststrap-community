"""WaveLoader component - Wave animation loader."""

from fasthtml.common import Div
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def WaveLoader(variant: str = None, **kwargs) -> Div:
    """Wave animation loading indicator.

    Args:
        variant: Bootstrap variant color (default: primary)
        **kwargs: Additional HTML attributes

    Example:
        >>> WaveLoader(variant="info")
    """
    defaults = get_community_defaults("WaveLoader")
    v = variant or defaults.get("variant", "primary")

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-wave-loader", user_cls)

    # Create 5 wave bars
    bars = [
        Div(cls="wave-bar", style=f"background-color: var(--bs-{v}); animation-delay: {i * 0.1}s;")
        for i in range(5)
    ]

    return Div(*bars, cls=container_cls, **kwargs)


register_component("WaveLoader", WaveLoader)
