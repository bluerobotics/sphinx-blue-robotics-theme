# Tabs

Tabs organize and allow navigation between groups of content that are related and at the same level of hierarchy. Each tab should contain content that is distinct from other tabs in a set.

We rely on the [Sphinx Design extension](https://github.com/executablebooks/sphinx-design) for implementing tabs.

## Installation

To have tabs support, you'll need to install the `extras` package by adding it to your `pyproject.toml` file:

```
[tool.poetry.extras]
sphinx-blue-robotics-theme = { version = "^0.0.1", extras = ["extras"] }
```

## Syntax

In MyST Markdown, tabs are created using the `:::{tab-set}` and `:::{tab-item}` directives. The basic format is:

```md
::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::
```

## Examples

### Basic tabs

```md
::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::
```

Renders:

::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::


## See also

- [Sphinx Design: Tabs](https://sphinx-design.readthedocs.io/en/latest/tabs.html)
