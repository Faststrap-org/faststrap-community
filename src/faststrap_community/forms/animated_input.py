"""AnimatedInput component - Input with floating label animation."""

from fasthtml.common import Div, Input, Label
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def AnimatedInput(
    label: str,
    name: str,
    input_type: str = "text",
    placeholder: str = "",
    value: str = None,
    required: bool = False,
    **kwargs,
) -> Div:
    """Input field with floating label animation.

    Args:
        label: Label text
        name: Input name attribute
        input_type: HTML input type (default: text)
        placeholder: Placeholder text
        value: Initial value
        required: Whether field is required
        **kwargs: Additional HTML attributes

    Example:
        >>> AnimatedInput(
        ...     label="Email Address",
        ...     name="email",
        ...     input_type="email",
        ...     required=True
        ... )
    """
    get_community_defaults("AnimatedInput")

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-animated-input", "form-floating", user_cls)

    input_id = kwargs.pop("id", f"input-{name}")

    input_el = Input(
        type=input_type,
        name=name,
        id=input_id,
        placeholder=placeholder or label,
        value=value,
        required=required,
        cls="form-control",
        **kwargs,
    )

    label_el = Label(label, **{"for": input_id})

    return Div(input_el, label_el, cls=container_cls)


register_component("AnimatedInput", AnimatedInput)
