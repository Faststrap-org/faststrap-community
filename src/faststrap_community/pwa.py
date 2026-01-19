"""PWA integration for community components."""

from typing import Any


def get_community_cache_urls(static_url: str = "/community-static") -> list[str]:
    """Get list of community assets to cache for PWA.

    Args:
        static_url: URL prefix for community static files

    Returns:
        List of URLs to cache

    Example:
        >>> urls = get_community_cache_urls()
        >>> print(urls)
        ['/community-static/css/community-base.css', ...]
    """
    base = static_url.rstrip("/")
    return [
        f"{base}/css/community-base.css",
        f"{base}/css/cards.css",
        f"{base}/css/loaders.css",
        f"{base}/css/navbars.css",
        f"{base}/css/effects.css",
        f"{base}/css/forms.css",
        f"{base}/css/buttons.css",
    ]


def setup_community_pwa(app: Any, static_url: str = "/community-static") -> Any:
    """Setup community with PWA optimization.

    This function extends the Faststrap PWA cache to include community assets.
    Must be called AFTER add_pwa() and setup_community().

    Args:
        app: FastHTML application instance
        static_url: URL prefix for community static files

    Raises:
        RuntimeError: If PWA is not enabled

    Example:
        >>> from faststrap import add_bootstrap
        >>> from faststrap.pwa import add_pwa
        >>> from faststrap_community import setup_community, setup_community_pwa
        >>>
        >>> app, rt = fast_app()
        >>> add_bootstrap(app)
        >>> add_pwa(app, name="My App")
        >>> setup_community(app, pwa_mode=True)
        >>> setup_community_pwa(app)  # Optional: explicit PWA setup
    """
    # Check if PWA is enabled
    if not hasattr(app, "_faststrap_pwa_enabled"):
        raise RuntimeError(
            "setup_community_pwa() requires PWA to be enabled.\n"
            "Call add_pwa(app) before this function."
        )

    # Add community assets to cache
    cache_urls = get_community_cache_urls(static_url)

    if hasattr(app, "_faststrap_pwa_cache_urls"):
        # Avoid duplicates
        existing = set(app._faststrap_pwa_cache_urls)
        for url in cache_urls:
            if url not in existing:
                app._faststrap_pwa_cache_urls.append(url)

    return app
