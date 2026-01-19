"""VerticalMegaMenu component for Faststrap Community."""

from typing import Any

from fasthtml.common import A, Div, Li, NotStr, Small, Ul
from faststrap import Icon
from faststrap.core.base import merge_classes

from ..registry import register_component


def _render_menu_item(item: dict[str, Any]) -> Li:
    """Recursive helper to render menu items."""
    label = item.get("label", "")
    icon_name = item.get("icon", "")
    subtitle = item.get("subtitle", "")
    href = item.get("href", "#")
    children = item.get("children", [])
    active = item.get("active", False)

    # Icon
    icon = Icon(icon_name) if icon_name else ""

    # Text Content
    text_content = [
        Div(
            NotStr(f"<strong>{label}</strong>"),
            Small(subtitle) if subtitle else "",
            cls="menu-text",
        )
    ]

    # Link
    link_cls = "active" if active else ""
    link = A(icon, *text_content, href=href, cls=link_cls)

    # Children (Submenu)
    submenu = ""
    if children:
        submenu = Ul(*[_render_menu_item(child) for child in children])

    return Li(link, submenu)


def VerticalMegaMenu(items: list[dict[str, Any]], width: str = "250px", **kwargs) -> Ul:
    """
    A vertical mega menu with multi-level dropdowns.
    Modernized CSS-only implementation.

    Args:
        items: List of dictionary items. Structure:
               {
                   "label": "Home",
                   "icon": "home",
                   "subtitle": "sweet home",
                   "href": "#",
                   "children": [...]
               }
        width: Width of the menu (default: 250px)
        **kwargs: Additional attributes
    """
    cls = merge_classes("fs-comm-vertical-mega", kwargs.pop("cls", ""))
    style = f"width: {width}; {kwargs.pop('style', '')}"

    menu_items = [_render_menu_item(item) for item in items]

    return Ul(*menu_items, cls=cls, style=style, **kwargs)


register_component("VerticalMegaMenu", VerticalMegaMenu)
