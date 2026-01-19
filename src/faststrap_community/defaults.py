"""Community component defaults system.

This module provides a separate defaults system for community components,
independent from Faststrap core defaults.
"""

from typing import Any

# Default values for all community components
_DEFAULT_COMMUNITY_DEFAULTS: dict[str, dict[str, Any]] = {
    "FlipCard": {"height": "300px", "width": "100%", "duration": "0.6s"},
    "TiltCard": {"max_tilt": "15deg", "duration": "0.3s"},
    "RevealCard": {"overlay_opacity": "0.9"},
    "DotsLoader": {"variant": "primary"},
    "RingLoader": {"variant": "primary", "size": "3rem"},
    "TypewriterLoader": {"variant": "primary"},
    "PolygonLoader": {"variant": "primary", "sides": 6},
    "ScrollReveal": {"direction": "up", "delay": "0s", "duration": "0.6s"},
    "ParallaxSection": {"speed": "0.5"},
    "SlideMenuNavbar": {"position": "left", "width": "280px"},
    "MegaMenuNavbar": {"columns": 3},
}

# Active defaults (can be modified by user)
_COMMUNITY_DEFAULTS: dict[str, dict[str, Any]] = _DEFAULT_COMMUNITY_DEFAULTS.copy()


def set_community_defaults(component: str, **defaults: Any) -> None:
    """Set global defaults for a community component.

    Args:
        component: Component name (e.g., "FlipCard")
        **defaults: Default values to set

    Example:
        >>> from faststrap_community import set_community_defaults
        >>>
        >>> # Set global defaults for FlipCard
        >>> set_community_defaults("FlipCard", height="400px", duration="0.8s")
        >>>
        >>> # Now all FlipCards will use these defaults
        >>> FlipCard(front="Front", back="Back")  # Uses 400px height
    """
    if component not in _COMMUNITY_DEFAULTS:
        _COMMUNITY_DEFAULTS[component] = {}
    _COMMUNITY_DEFAULTS[component].update(defaults)


def get_community_defaults(component: str) -> dict[str, Any]:
    """Get defaults for a community component.

    Args:
        component: Component name

    Returns:
        Dictionary of default values for the component
    """
    return _COMMUNITY_DEFAULTS.get(component, {}).copy()


def reset_community_defaults() -> None:
    """Reset all community defaults to initial values.

    Example:
        >>> set_community_defaults("FlipCard", height="500px")
        >>> reset_community_defaults()
        >>> # FlipCard now uses original default (300px)
    """
    global _COMMUNITY_DEFAULTS
    _COMMUNITY_DEFAULTS = _DEFAULT_COMMUNITY_DEFAULTS.copy()


def list_community_components() -> list[str]:
    """List all community components with defaults.

    Returns:
        List of component names
    """
    return list(_COMMUNITY_DEFAULTS.keys())
