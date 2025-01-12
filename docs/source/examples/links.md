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

### External link aliases

You can define external link aliases using the `extlinks` configuration option in the project's `conf.py` file. This allows you to create short, reusable links with custom aliases and captions.

To configure external link aliases, define them in your Sphinx configuration file (`conf.py`). Here's an example of setting up aliases for issues on GitHub:

```python
extlinks = {
    'issue': ('https://github.com/bluerobotics/sphinx-blue-robotics-theme/issues/%s', 'issue %s'
}
```

This creates an alias for links to GitHub issues. The format `%s` will be replaced by the issue number when the link is used.

Once the alias is configured, you can use the alias in your MyST Markdown files as follows:

```markdown
{issue}`123`
```

Renders:

{issue}`123`

(internal-link-to-a-section)=
### Internal link to a section

To link to a section within the same document, use the section title with a lowercase URL and hyphens instead of spaces:

```md
[Go to internal link to a section](#internal-link-to-a-section)
```

Renders:


:::{note}
The anchor must be defined previously. Example:

```md
(internal-link-to-a-section)=
### Internal link to a section
```
:::

### Internal link to a page

You can also create links to sections in other files within your documentation.
For example, to link to a section in another file, use the following format:

```md
[Go to Tabs page](tabs.md)
```

Renders:

[Go to Tabs page](tabs.md)

## See also

- [MyST Parser: Cross-references](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html)
- [Sphinx: reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
