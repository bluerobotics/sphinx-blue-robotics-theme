# Links

Links allow you to create clickable references to external websites, files, or sections within your documentation.

## Syntax

Links in MyST Markdown are created using the `[text](URL)` syntax. The general format is:

```md
[Text](URL)
```

Optionally, you can add a title for the link by providing it after the URL:

```md
[Text](URL "Title text")
```

## Examples

### External Link

```md
[BlueRobotics](https://www.bluerobotics.com)
```

Renders:

[BlueRobotics](https://www.bluerobotics.com)

### Link with title

```md
[BlueRobotics](https://www.bluerobotics.com "Visit BlueRobotics's website")
```

Renders:

[BlueRobotics](https://www.bluerobotics.com "Visit BlueRobotics's website")

(internal-link-to-a-section)=
### Internal link to a section

To link to a section within the same document, use the section title with a lowercase URL and hyphens instead of spaces:

```md
[Go to internal link to a section](#internal-link-to-a-section)
```

:::{note}
The anchor must be defined previously. Example:

```md
(internal-link-to-a-section)=
```
### Internal link to a section
:::

Renders:

[Go to internal link to a section](#internal-link-to-a-section)

### Link to a file

You can also link to a file on your website or local directory:

```md
[Download the image](/_static/img/sample.png)
```

Renders:

[Download the image](/_static/sample.png)

### Link with anchor text

```md
[Click here for more information](https://bluerobotics.com "More info")
```

Renders:

[Click here for more information](https://bluerobotics.com "More info")

## Cross-reference to another file

You can also create links to sections in other files within your documentation. For example, to link to a section in another file, use the following format:

```md
[Go to Tabs page](tabs.md)
```

Renders:

[Go to Tabs page](tabs.md)

## See also

- [MyST Parser: Cross-references](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html)
- [Sphinx: reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
