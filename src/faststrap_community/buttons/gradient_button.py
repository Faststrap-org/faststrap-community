"""GradientButton component - Button with gradient background."""

from fasthtml.common import Button as HtmlButton
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def GradientButton(text: str, gradient: str = None, size: str = None, **kwargs) -> HtmlButton:
    """Button with gradient background.

    Args:
        text: Button text
        gradient: Gradient preset: 'purple', 'blue', 'green', 'orange', 'pink' or custom CSS
        size: Button size: 'sm', 'lg'
        **kwargs: Additional HTML attributes

    Example:
        >>> GradientButton("Get Started", gradient="purple", size="lg")
    """
    defaults = get_community_defaults("GradientButton")
    grad = gradient or defaults.get("gradient", "purple")

    # Gradient presets
    gradients = {
        "purple": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "blue": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
        "green": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
        "orange": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
        "pink": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
    }

    gradient_style = gradients.get(grad, grad)

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")

    size_cls = f"btn-{size}" if size else ""
    container_cls = merge_classes("fs-comm-gradient-button", "btn", size_cls, user_cls)

    style = f"background: {gradient_style}; border: none; color: white; {user_style}".strip()

    return HtmlButton(text, cls=container_cls, style=style, **kwargs)


register_component("GradientButton", GradientButton)
