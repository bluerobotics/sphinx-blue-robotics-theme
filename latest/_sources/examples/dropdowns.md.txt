# Dropdowns

Dropdowns can be used to toggle content, usually non-essential, and show it only when a user clicks on the header panel. They are a great way to keep pages clean and organized.

We rely on the [Sphinx Design extension](https://github.com/executablebooks/sphinx-design) for implementing dropdowns.

## Syntax

In MyST Markdown, dropdowns are created using the `:::{dropdown}` directive. You can optionally provide a title and additional options. The basic format is:

```md
:::{dropdown} Dropdown title
Dropdown content
:::
```

## Examples

### Basic dropdown

```md
:::{dropdown} Dropdown title
Dropdown content
:::
```

Renders:

:::{dropdown} Dropdown title
Dropdown content
:::

## See also

- [Sphinx Design: Dropdowns](https://sphinx-design.readthedocs.io/en/latest/dropdowns.html)
