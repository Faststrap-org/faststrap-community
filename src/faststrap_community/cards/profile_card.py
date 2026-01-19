"""ProfileCard component - User profile card."""

from typing import Any

from fasthtml.common import H5, Div, Img, P
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def ProfileCard(
    name: str, title: str = None, avatar: str = None, bio: str = None, *actions: Any, **kwargs
) -> Div:
    """User profile card with avatar, name, title, and action buttons.

    Args:
        name: User's name (required)
        title: User's title/role
        avatar: Avatar image URL (uses placeholder if not provided)
        bio: Short bio text
        *actions: Action buttons or links
        **kwargs: Additional HTML attributes

    Example:
        >>> from faststrap import Button
        >>> ProfileCard(
        ...     name="Jane Doe",
        ...     title="Senior Developer",
        ...     avatar="/img/jane.jpg",
        ...     bio="Python enthusiast and open source contributor",
        ...     Button("Follow", variant="primary", size="sm"),
        ...     Button("Message", variant="outline-primary", size="sm")
        ... )
    """
    get_community_defaults("ProfileCard")

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-profile-card", "card", "text-center", user_cls)

    # Avatar
    avatar_url = avatar or "https://via.placeholder.com/150"
    avatar_el = Img(
        src=avatar_url,
        alt=name,
        cls="rounded-circle mb-3",
        style="width: 100px; height: 100px; object-fit: cover;",
    )

    # Optional elements
    title_el = P(title, cls="text-muted mb-2") if title else None
    bio_el = P(bio, cls="card-text small") if bio else None
    actions_el = Div(*actions, cls="mt-3 d-flex gap-2 justify-content-center") if actions else None

    return Div(
        Div(
            avatar_el,
            H5(name, cls="card-title mb-1"),
            title_el,
            bio_el,
            actions_el,
            cls="card-body",
        ),
        cls=container_cls,
        **kwargs,
    )


register_component("ProfileCard", ProfileCard)
