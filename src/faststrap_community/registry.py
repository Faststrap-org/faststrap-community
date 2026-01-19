"""Registry for Faststrap Community components."""

from typing import Any

_COMMUNITY_COMPONENTS: dict[str, Any] = {}


def register_component(name: str, component: Any):
    """Register a component with the community registry."""
    _COMMUNITY_COMPONENTS[name] = component


def list_components() -> list[str]:
    """Return a list of registered community components."""
    return list(_COMMUNITY_COMPONENTS.keys())


def get_component(name: str) -> Any:
    """Retrieve a component from the registry."""
    return _COMMUNITY_COMPONENTS.get(name)
