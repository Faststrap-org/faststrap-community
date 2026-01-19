"""TagInput component - Input for adding/removing tags."""

from fasthtml.common import Button, Div, Input, Script, Span
from faststrap.core.base import merge_classes

from ..defaults import get_community_defaults
from ..registry import register_component


def TagInput(name: str, tags: list[str] = None, placeholder: str = "Add tag...", **kwargs) -> Div:
    """Input for adding and removing tags.

    Args:
        name: Input name attribute
        tags: Initial list of tags
        placeholder: Placeholder text
        **kwargs: Additional HTML attributes

    Example:
        >>> TagInput(
        ...     name="skills",
        ...     tags=["Python", "FastHTML", "Bootstrap"],
        ...     placeholder="Add a skill..."
        ... )
    """
    get_community_defaults("TagInput")
    initial_tags = tags or []

    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes("fs-comm-tag-input", user_cls)

    # Tag badges
    tag_elements = [
        Span(
            tag,
            Button(
                "×", type="button", cls="btn-close btn-close-white ms-2", style="font-size: 0.7rem;"
            ),
            cls="badge bg-primary me-2 mb-2 d-inline-flex align-items-center",
            data_tag=tag,
        )
        for tag in initial_tags
    ]

    # Input field
    input_el = Input(type="text", name=name, placeholder=placeholder, cls="form-control", **kwargs)

    # Hidden input to store tags as JSON
    hidden_input = Input(type="hidden", name=f"{name}_tags", value=",".join(initial_tags))

    # Simple JavaScript for tag management (minimal)
    script = Script(
        """
        // Tag input functionality (minimal JS for interactivity)
        document.querySelectorAll('.fs-comm-tag-input').forEach(container => {
            const input = container.querySelector('input[type="text"]');
            const hidden = container.querySelector('input[type="hidden"]');
            const tagsDiv = container.querySelector('.tags-container');

            input.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    const tag = input.value.trim();
                    if (tag) {
                        addTag(tag);
                        input.value = '';
                    }
                }
            });

            function addTag(tag) {
                const badge = document.createElement('span');
                badge.className = 'badge bg-primary me-2 mb-2 d-inline-flex align-items-center';
                badge.innerHTML = tag + '<button type="button" class="btn-close btn-close-white ms-2" style="font-size: 0.7rem;"></button>';
                badge.querySelector('button').onclick = () => removeTag(badge, tag);
                tagsDiv.appendChild(badge);
                updateHidden();
            }

            function removeTag(badge, tag) {
                badge.remove();
                updateHidden();
            }

            function updateHidden() {
                const tags = Array.from(tagsDiv.querySelectorAll('.badge')).map(b => b.textContent.replace('×', '').trim());
                hidden.value = tags.join(',');
            }

            // Setup remove buttons for initial tags
            container.querySelectorAll('.btn-close').forEach(btn => {
                btn.onclick = (e) => {
                    e.target.closest('.badge').remove();
                    updateHidden();
                };
            });
        });
    """
    )

    return Div(
        Div(*tag_elements, cls="tags-container mb-2"),
        input_el,
        hidden_input,
        script,
        cls=container_cls,
    )


register_component("TagInput", TagInput)
