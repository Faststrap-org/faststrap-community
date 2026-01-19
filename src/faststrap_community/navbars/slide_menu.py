"""SlideMenuNavbar component for Faststrap Community."""

from fasthtml.common import H4, A, Button, Div, Li, Ul
from faststrap.core.theme import resolve_defaults

from ..registry import register_component


def SlideMenuNavbar(items: list, brand: str = None, menu_id: str = None, **kwargs) -> Div:
    """An off-canvas slide-out navigation menu.

    Args:
        items: List of (label, href) tuples or elements
        brand: Optional brand text/element
        menu_id: Unique ID for the menu (default: slide-menu)
        **kwargs: Additional attributes
    """
    cfg = resolve_defaults("SlideMenuNavbar", menu_id=menu_id)
    mid = cfg.get("menu_id") or "slide-menu"

    # Overlay to close menu on click outside
    overlay = Div(cls="fs-comm-slide-overlay", id=f"{mid}-overlay")

    # Menu content
    menu_items = []
    if brand:
        menu_items.append(Div(H4(brand), cls="mb-4 text-center"))

    list_items = []
    for item in items:
        if isinstance(item, tuple):
            label, href = item
            list_items.append(Li(A(label, href=href, cls="nav-link"), cls="nav-item"))
        else:
            list_items.append(Li(item, cls="nav-item"))

    menu_items.append(Ul(*list_items, cls="navbar-nav flex-column"))

    menu = Div(*menu_items, cls="fs-comm-slide-menu", id=mid)

    # Minimal JS to toggle classes (preserving zero-JS where possible via HTMX if desired,
    # but for off-canvas, a tiny helper is standard in community plan).
    # However, let's try to make it work with HTMX or simple onclick.

    return Div(overlay, menu, **kwargs)


def SlideToggler(target_id: str, **kwargs) -> Button:
    """Button to toggle the slide menu."""
    # Simple JS toggle for demo purposes
    js_toggle = f"document.getElementById('{target_id}').classList.toggle('show'); document.getElementById('{target_id}-overlay').classList.toggle('show');"

    return Button("Open Menu", cls="btn btn-outline-primary", onclick=js_toggle, **kwargs)


register_component("SlideMenuNavbar", SlideMenuNavbar)
register_component("SlideToggler", SlideToggler)
