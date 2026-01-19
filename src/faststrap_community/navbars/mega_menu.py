"""MegaMenuNavbar component for Faststrap Community."""

from typing import Any

from fasthtml.common import A, Div, Li, Nav
from faststrap.components.navigation.navbar import Navbar

from ..registry import register_component


def MegaMenuNavbar(
    brand: str = None, items: list = None, container_type: str = "container", **kwargs
) -> Nav:
    """A Navbar supporting wide multi-column dropdowns (Mega Menus).

    Args:
        brand: Brand content
        items: List of nav items or MegaMenuItems
        container_type: Bootstrap container class (default: container)
        **kwargs: Additional Navbar attributes
    """
    # This component primarily sets the stage for MegaMenuItems.
    # It passes through to the core Navbar but can add specific wrappers if needed.
    return Navbar(brand=brand, items=items, container_type=container_type, **kwargs)


def MegaMenuItem(label: str, content: Any, **kwargs) -> Li:
    """A dropdown menu item that expands into a mega menu.

    Args:
        label: Label for the dropdown toggle
        content: The content of the mega menu (usually Rows and Cols)
    """
    # Structure:
    # Li (nav-item fs-comm-mega-menu)
    #   A (nav-link dropdown-toggle)
    #   Div (dropdown-menu)
    #     Div (fs-comm-mega-menu-content)
    #       content

    toggle = A(
        label,
        cls="nav-link dropdown-toggle",
        href="#",
        role="button",
        data_bs_toggle="dropdown",
        aria_expanded="false",
    )

    menu = Div(Div(content, cls="fs-comm-mega-menu-content"), cls="dropdown-menu")

    return Li(toggle, menu, cls="nav-item dropdown fs-comm-mega-menu", **kwargs)


register_component("MegaMenuNavbar", MegaMenuNavbar)
register_component("MegaMenuItem", MegaMenuItem)
