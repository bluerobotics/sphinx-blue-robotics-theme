# Hero

The hero directive creates a banner section at the top of your page. It can include a title, description, and optional call-to-action buttons.

## Prerequisites

To use the hero directive, ensure the extension is enabled in your `conf.py`:

```python
extensions = [
    'sphinx_blue_robotics_theme.extensions.hero',
    # ... other extensions
]
```

## Syntax

In MyST Markdown, hero sections are created using the `{hero}` directive. The basic format is:

```md
:::{hero}
  :title: Your Title
  :description: Your description text
```

## Options

The hero directive supports the following options:

- `:title:` - Main heading text
- `:title-level:` - Level of the heading (default: `h1`)
- `:description:` - Subheading or descriptive text
- `:bg-image:` - Background image URL (optional)
- `:landing:` - If set, the hero will take the full page width

## Examples

### Basic hero

```md
:::{hero}
  :title: Welcome to Documentation
  :description: Find guides, samples, and references.
:::
```

Renders:

:::{hero}
  :title: Welcome to Documentation
  :description: Find guides, samples, and references.
:::


### Hero with background image

```md
:::{hero}
  :title: Welcome to Documentation
  :description: Find guides, samples, and references.
  :bg-image: img/bg.jpg
:::
```

Renders:

:::{hero}
  :title: Welcome to Documentation
  :description: Find guides, samples, and references.
  :bg-image: img/bg.jpg
:::
