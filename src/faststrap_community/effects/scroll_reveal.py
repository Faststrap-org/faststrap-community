"""ScrollReveal component for Faststrap Community."""

from typing import Any

from fasthtml.common import Div, Script
from faststrap.core.base import merge_classes
from faststrap.core.theme import resolve_defaults

from ..registry import register_component


def ScrollReveal(
    content: Any, direction: str = None, delay: str = None, duration: str = None, **kwargs
) -> Div:
    """A wrapper that reveals content when it enters the viewport.

    Args:
        content: Component or elements to reveal
        direction: Direction to move from ('up', 'down', 'left', 'right', 'zoom')
        delay: Delay before animation starts (default: 0s)
        duration: Duration of animation (default: 0.6s)
        **kwargs: Additional attributes
    """
    cfg = resolve_defaults("ScrollReveal", direction=direction, delay=delay, duration=duration)

    dir_val = cfg.get("direction") or "up"
    del_val = cfg.get("delay") or "0s"
    dur_val = cfg.get("duration") or "0.6s"

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")

    container_cls = merge_classes("fs-comm-reveal", dir_val, user_cls)

    final_style = (
        f"--fs-comm-reveal-delay: {del_val}; "
        f"--fs-comm-reveal-duration: {dur_val}; "
        f"{user_style}"
    ).strip()

    # We need a small script to initialize the IntersectionObserver
    # This script is idempotent and handles all .fs-comm-reveal elements.
    reveal_script = Script(
        """
        if (!window.fsCommRevealInit) {
            window.fsCommRevealInit = true;
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('revealed');
                    }
                });
            }, { threshold: 0.1 });

            const initReveals = () => {
                document.querySelectorAll('.fs-comm-reveal').forEach(el => observer.observe(el));
            };

            document.addEventListener('DOMContentLoaded', initReveals);
            if (window.htmx) document.body.addEventListener('htmx:afterSwap', initReveals);
        }
    """
    )

    return Div(content, reveal_script, cls=container_cls, style=final_style, **kwargs)


register_component("ScrollReveal", ScrollReveal)
