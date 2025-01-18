# Code blocks

Code blocks allow you to display code in your documentation with proper formatting and syntax highlighting.

## Syntax

Code blocks in MyST Markdown are created using the triple backtick syntax. The general format is:

````md
```{language}
Your code here
```
````

## Examples

### Python

````md
```{python}
def hello_world():
    print("Hello, world!")
```
````

Renders:

```python
def hello_world():
    print("Hello, world!")
```

### Bash

````md
```{bash}
echo "Hello, world!"
```
````

Renders:

```bash
echo "Hello, world!"
```

### JavaScript

````md
```{javascript}
console.log("Hello, world!");
```
````

Renders:

```javascript
console.log("Hello, world!");
```

## See also

- [Myst Parser: Source code and APIs](https://myst-parser.readthedocs.io/en/latest/syntax/code_and_apis.html)
- [Sphinx: reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
