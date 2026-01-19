"""SearchBar component - Animated search bar with icon."""

from fasthtml.common import Button, Div, Input, Span
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def SearchBar(
    placeholder: str = "Search...",
    name: str = "q",
    action: str = "/search",
    method: str = "GET",
    **kwargs,
) -> Div:
    """Animated search bar with icon.

    Args:
        placeholder: Placeholder text
        name: Input name attribute
        action: Form action URL
        method: HTTP method (GET or POST)
        **kwargs: Additional HTML attributes

    Example:
        >>> SearchBar(
        ...     placeholder="Search products...",
        ...     action="/products/search"
        ... )
    """
    from fasthtml.common import Form

    get_community_defaults("SearchBar")

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-search-bar", user_cls)

    search_input = Input(
        type="search", name=name, placeholder=placeholder, cls="form-control", **kwargs
    )

    search_button = Button(Span("🔍", cls="fs-5"), type="submit", cls="btn btn-primary")

    return Form(
        Div(search_input, search_button, cls="input-group"),
        action=action,
        method=method,
        cls=container_cls,
    )


register_component("SearchBar", SearchBar)
