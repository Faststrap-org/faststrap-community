# Form Components

Enhanced form inputs with modern styling.

---

## AnimatedInput

Input field with floating label animation (Bootstrap form-floating).

### Usage

```python
from faststrap_community import AnimatedInput

AnimatedInput(
    label="Email Address",
    name="email",
    input_type="email",
    required=True
)
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `label` | str | Required | Label text |
| `name` | str | Required | Input name attribute |
| `input_type` | str | `"text"` | HTML input type |
| `placeholder` | str | `""` | Placeholder text |
| `value` | str | None | Initial value |
| `required` | bool | False | Required field |

### Example

```python
Form(
    AnimatedInput(
        label="Full Name",
        name="name",
        required=True
    ),
    AnimatedInput(
        label="Email",
        name="email",
        input_type="email",
        required=True
    ),
    AnimatedInput(
        label="Password",
        name="password",
        input_type="password",
        required=True
    ),
    Button("Submit", type="submit", variant="primary"),
    action="/signup",
    method="POST"
)
```

---

## SearchBar

Search input with icon button.

### Usage

```python
from faststrap_community import SearchBar

SearchBar(
    placeholder="Search products...",
    name="q",
    action="/search",
    method="GET"
)
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `placeholder` | str | `"Search..."` | Placeholder text |
| `name` | str | `"q"` | Input name |
| `action` | str | `"/search"` | Form action URL |
| `method` | str | `"GET"` | HTTP method |

### Example

```python
# Product search
SearchBar(
    placeholder="Search 1000+ products...",
    action="/products/search"
)

# Documentation search
SearchBar(
    placeholder="Search docs...",
    action="/docs/search",
    name="query"
)
```

---

## TagInput

Input for adding and removing tags.

### Usage

```python
from faststrap_community import TagInput

TagInput(
    name="skills",
    tags=["Python", "FastHTML", "Bootstrap"],
    placeholder="Add a skill..."
)
```

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `name` | str | Required | Input name |
| `tags` | List[str] | None | Initial tags |
| `placeholder` | str | `"Add tag..."` | Placeholder text |

### Example

```python
# Skills input
TagInput(
    name="skills",
    tags=user.skills,
    placeholder="Add a skill..."
)

# Categories
TagInput(
    name="categories",
    tags=["Web", "Mobile"],
    placeholder="Add category..."
)
```

> **Note:** TagInput uses minimal JavaScript for tag management. Press Enter to add tags, click × to remove.

---

**Next:** [Button Components](buttons.md)
