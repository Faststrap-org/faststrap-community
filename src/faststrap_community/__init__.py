"""
Faststrap Community - Premium Components for FastHTML.
Seamlessly integrates with Faststrap Core themes and configurations.
"""

from pathlib import Path
from typing import Any

from fasthtml.common import Link
from starlette.staticfiles import StaticFiles

from .buttons.floating_action_button import FloatingActionButton
from .buttons.gradient_button import GradientButton
from .buttons.icon_button import IconButton

# Export components
from .cards.flip_card import FlipCard
from .cards.glow_card import GlowCard
from .cards.pricing_card import PricingCard
from .cards.profile_card import ProfileCard
from .cards.reveal_card import RevealCard
from .cards.stat_card import StatCard
from .cards.tilt_card import TiltCard
from .cards.timeline_card import TimelineCard

# Export defaults system
from .defaults import (
    get_community_defaults,
    list_community_components,
    reset_community_defaults,
    set_community_defaults,
)
from .effects.parallax import ParallaxSection
from .effects.scroll_reveal import ScrollReveal
from .forms.animated_input import AnimatedInput
from .forms.search_bar import SearchBar
from .forms.tag_input import TagInput
from .loaders.dots import DotsLoader
from .loaders.geometric import PolygonLoader
from .loaders.progress_ring import ProgressRing
from .loaders.pulse import PulseLoader
from .loaders.ring import RingLoader
from .loaders.skeleton import SkeletonLoader
from .loaders.text import ShadowLoader, TypewriterLoader
from .loaders.wave import WaveLoader
from .navbars.mega_menu import MegaMenuItem, MegaMenuNavbar
from .navbars.morphing import MorphingToggler
from .navbars.slide_menu import SlideMenuNavbar, SlideToggler
from .navbars.vertical_mega import VerticalMegaMenu

# Export PWA integration
from .pwa import get_community_cache_urls, setup_community_pwa


# Asset management
def get_community_assets(static_url: str = "/community-static") -> list[Link]:
    """Get Link elements for community CSS files."""
    base = static_url.rstrip("/")
    return [
        Link(rel="stylesheet", href=f"{base}/css/community-base.css"),
        Link(rel="stylesheet", href=f"{base}/css/cards.css"),
        Link(rel="stylesheet", href=f"{base}/css/loaders.css"),
        Link(rel="stylesheet", href=f"{base}/css/navbars.css"),
        Link(rel="stylesheet", href=f"{base}/css/effects.css"),
    ]


def setup_community(app: Any, static_url: str = "/community-static", pwa_mode: bool = False) -> Any:
    """
    Mount community static files and inject CSS headers.

    IMPORTANT: Must be called AFTER add_bootstrap(app).

    Args:
        app: FastHTML application instance
        static_url: URL prefix for community static files (default: /community-static)
        pwa_mode: Enable PWA optimizations (default: False)

    Raises:
        RuntimeError: If app is invalid or Bootstrap not detected
    """
    # 1. Validate app instance
    if not hasattr(app, "hdrs"):
        raise RuntimeError(
            "setup_community() requires a valid FastHTML app instance. "
            "Did you pass the correct app object?"
        )

    # 2. ENFORCE: Check for Bootstrap
    bootstrap_found = any(
        hasattr(h, "attrs") and "bootstrap" in h.attrs.get("href", "")
        for h in app.hdrs
        if hasattr(h, "attrs")
    )

    if not bootstrap_found:
        raise RuntimeError(
            "setup_community() must be called AFTER add_bootstrap().\n"
            "Bootstrap styles not detected in app headers.\n\n"
            "Correct order:\n"
            "  1. add_bootstrap(app)\n"
            "  2. setup_community(app)"
        )

    # 3. Mount static files
    from starlette.routing import Mount

    static_path = Path(__file__).parent / "static"

    if not static_path.exists():
        raise FileNotFoundError(f"Community static files not found at {static_path}")

    existing_paths = [r.path for r in app.routes if isinstance(r, Mount)]
    if static_url not in existing_paths:
        app.routes.insert(
            0, Mount(static_url, StaticFiles(directory=str(static_path)), name="community_static")
        )

    # 4. Inject CSS headers
    assets = get_community_assets(static_url)
    current_hrefs = {
        h.attrs.get("href") for h in app.hdrs if hasattr(h, "attrs") and "href" in h.attrs
    }

    for asset in assets:
        if asset.attrs.get("href") not in current_hrefs:
            app.hdrs.append(asset)

    # 5. PWA Mode
    if pwa_mode and hasattr(app, "_faststrap_pwa_cache_urls"):
        cache_urls = [
            f"{static_url}/css/community-base.css",
            f"{static_url}/css/cards.css",
            f"{static_url}/css/loaders.css",
            f"{static_url}/css/navbars.css",
            f"{static_url}/css/effects.css",
        ]
        app._faststrap_pwa_cache_urls.extend(cache_urls)

    return app
