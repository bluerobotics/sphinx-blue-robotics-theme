# Substitutions

Substitutions in Sphinx allow you to define reusable text, links, or content that can be inserted throughout your documentation. Using `myst_substitutions`, you can define substitutions once and reference them multiple times, keeping your documentation consistent and easy to maintain.

## Define substitutions in `conf.py`

You can define substitutions globally in your Sphinx configuration file (`conf.py`) using the `myst_substitutions` variable. For example:

```python
myst_substitutions = {
  "project_name": "Blue Robotics"
}
```

### Use substitutions in your content

Once substitutions are defined, you can use them in `.rst` or `.md` files as follows:

```rst
{{ project_name }} documentation.
``` 

Which renders:

{{project_name}} documentation.

## See also

- [Myst Parser: Substitutions](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2)
