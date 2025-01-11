# Text 

Text formatting allows you to style and structure your text to enhance readability and emphasis.

## Examples

### Paragraph

```md
Lorem ipsum dolor sit amet, **consectetur adipiscing elit**. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. *Ut enim ad minim veniam*, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. <u>Excepteur sint occaecat cupidatat non proident</u>, sunt in culpa qui officia deserunt mollit anim id est laborum. ~~Sed ut perspiciatis unde omnis iste natus error sit voluptatem~~.
```

Renders:

Lorem ipsum dolor sit amet, **consectetur adipiscing elit**. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. *Ut enim ad minim veniam*, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. <u>Excepteur sint occaecat cupidatat non proident</u>, sunt in culpa qui officia deserunt mollit anim id est laborum. ~~Sed ut perspiciatis unde omnis iste natus error sit voluptatem~~.

### Headings

```md
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

### Lists

#### Unordered List

```md
- Apples
- Bananas
  - Subitem 1
  - Subitem 2
```

Renders:

- Apples
- Bananas
  - Subitem 1
  - Subitem 2

#### Ordered List

```md
1. Step 1
2. Step 2
   1. Substep 1
   2. Substep 2
```

Renders:

1. Step 1
2. Step 2
   1. Substep 1
   2. Substep 2


### Footnotes

Footnotes are useful for adding additional context without interrupting the text flow.

```md
This is a reference to a footnote.[^1]

[^1]: This is the footnote definition.
```

Renders:

This is a reference to a footnote.[1]

[1]: This is the footnote definition.


### Subscript & Superscript

```md
H{sub}`2`O and E=mc{sup}`2`
```

Renders:

H₂O and E=mc²

### Quotes

```md
> "We're on a mission to enable the future of marine robotics."
>
> — Blue Robotics
```

Renders:

> "We're on a mission to enable the future of marine robotics."
>
> — Blue Robotics

### Definition lists

```md
Term 1
: Definition

Term 2
: Longer definition

  With multiple paragraphs

  - And bullet points
```

Renders:

Term 1
: Definition

Term 2
: Longer definition

  With multiple paragraphs

  - And bullet points

### Field lists

Field lists are useful for technical documentation, such as documenting parameters and return values in code.

```md
:param name: The name of the user.
:param age: The age of the user.
:return: A formatted string with the user's details.
```

Renders:

- **param name**: The name of the user.  
- **param age**: The age of the user.  
- **return**: A formatted string with the user's details.

## See also

- [MyST Parser: Typography](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)
- [Sphinx: reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
