# Images

Images allow you to embed visual content in your documentation to support and enhance the information presented.

## Syntax

Images in MyST Markdown are embedded using the `![alt text](image URL)` syntax. The general format is:

```md
![Alt text](image_url)
```

Optionally, you can add a title to the image by providing it after the URL:

```md
![Alt text](image_url "Title text")
```

## Examples

### Simple Image

```md
![A sample image](https://bluerobotics.com/wp-content/uploads/2020/01/BlueRobotics-Logo-Blue-Black.png)
```

Renders:

![A sample image](https://bluerobotics.com/wp-content/uploads/2020/01/BlueRobotics-Logo-Blue-Black.png)

### Local image

```md
![A sample image](/_static/sample.png)
```

Renders:

![A sample image](/_static/sample.png)

### Image with title

```md
![A sample image](https://bluerobotics.com/wp-content/uploads/2020/01/BlueRobotics-Logo-Blue-Black.png "This is a sample image")
```

Renders:

![A sample image](https://bluerobotics.com/wp-content/uploads/2020/01/BlueRobotics-Logo-Blue-Black.png "This is a sample image")

## See also

- [MyST Parser: Images and figures](https://myst-parser.readthedocs.io/en/latest/syntax/images_and_figures.html)
- [Sphinx: reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
