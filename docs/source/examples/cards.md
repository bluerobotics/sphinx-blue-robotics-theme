# Cards

Cards are a visually appealing way to present content. They can be used to highlight features, group related information, or create structured layouts.

We rely on the [Sphinx Design extension](https://github.com/executablebooks/sphinx-design) for implementing cards.

## Installation

To have cards support, you'll need to install the `extras` package by adding it to your `pyproject.toml` file:

```
[tool.poetry.extras]
sphinx-blue-robotics-theme = { version = "^0.0.1", extras = ["extras"] }
```

## Syntax

In MyST Markdown, cards are created using the `:::{card}` directive and grouped with the `::::{grid}` directive. The basic format is:

```md
::::{grid} 2
:::{grid-item-card} Card Title
Card content goes here.
:::
::::
```

## Examples

### Basic cards

```md
::::{grid} 2
:::{grid-item-card} Card 1
This is the content of the first card.
:::
:::{grid-item-card} Card 2
This is the content of the second card.
:::
::::
```

Renders:

::::{grid} 2
:::{grid-item-card} Card 1
This is the content of the first card.
:::
:::{grid-item-card} Card 2
This is the content of the second card.
:::
::::

## See also

- [Sphinx Design: Cards](https://sphinx-design.readthedocs.io/en/latest/cards.html)
