"""MorphingToggler component for Faststrap Community."""

from fasthtml.common import Button, Div, Span
from faststrap.core.base import merge_classes

from ..registry import register_component


def MorphingToggler(target_id: str, **kwargs) -> Button:
    """A navbar toggler button with morphing hamburger icon.

    The icon morphs from hamburger (☰) to X (✕) when clicked.
    Use this with Faststrap's core Navbar component.

    Args:
        target_id: ID of the navbar collapse element to toggle
        **kwargs: Additional button attributes

    Example:
        >>> from faststrap import Navbar
        >>> from faststrap_community import MorphingToggler
        >>>
        >>> navbar_id = "mainNav"
        >>> Navbar(
        ...     brand="My App",
        ...     items=[...],
        ...     id=navbar_id,
        ...     toggler=MorphingToggler(target_id=navbar_id)
        ... )
    """
    user_cls = kwargs.pop("cls", "")

    icon = Div(
        Span(cls="fs-comm-morph-span-1"),
        Span(cls="fs-comm-morph-span-2"),
        Span(cls="fs-comm-morph-span-3"),
        cls="fs-comm-morph-toggler",
    )

    button_cls = merge_classes("navbar-toggler", user_cls)

    return Button(
        icon,
        cls=button_cls,
        type="button",
        data_bs_toggle="collapse",
        data_bs_target=f"#{target_id}",
        aria_controls=target_id,
        aria_expanded="false",
        aria_label="Toggle navigation",
        **kwargs,
    )


register_component("MorphingToggler", MorphingToggler)
