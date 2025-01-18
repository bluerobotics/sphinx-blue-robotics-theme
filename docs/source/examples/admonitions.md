# Admonitions

Admonitions allow you to highlight important information, tips, warnings, and other notable content in your documentation.

## Syntax

Admonitions in MyST Markdown are created using the `:::` syntax followed by the admonition type. The general format is:

```md
:::{admonition-type}
Your content here
:::
```

## Examples

### Important

```md
:::{important}
This is an important piece of information that readers should pay close attention to.
:::
```

Renders:

:::{important}
This is an important piece of information that readers should pay close attention to.
:::

### Note

```md
:::{note}
This is a note providing additional context or helpful information.
:::
```

Renders:

:::{note}
This is a note providing additional context or helpful information.
:::


### Tip

```md
:::{tip}
Here's a helpful suggestion or best practice.
:::
```

Renders:

:::{tip}
Here's a helpful suggestion or best practice.
:::

### Warning

```md
:::{warning}
This is a warning about potential issues or risks that readers should be aware of.
:::
```

Renders:

:::{warning}
This is a warning about potential issues or risks that readers should be aware of.
:::

### Caution

```md
:::{caution}
This admonition highlights potential pitfalls.
:::
```

Renders:

:::{caution}
This admonition highlights potential pitfalls.
:::

### Error

```md
:::{error}
This indicates a critical error or something that must be avoided.
:::
```

Renders:

:::{error}
This indicates a critical error or something that must be avoided.
:::

## See also

- [Sphinx Immaterial: Admonitions](https://jbms.github.io/sphinx-immaterial/admonitions.html)
- [MyST Parser: Admonitions](https://myst-parser.readthedocs.io/en/latest/syntax/admonitions.html)
- [Sphinx: reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
