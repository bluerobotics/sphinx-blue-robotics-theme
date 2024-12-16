# API docs

You can automatically create API references and other documentation directly from your source code to keep your documentation up-to-date with the latest code changes.

The MyST parser supports generating documentation for various programming languages, including Python, C++, and Lua. This approach allows you to integrate code documentation with your project’s general documentation, reducing manual effort and ensuring consistency.

## Python docs generation

For Python, Sphinx can use the `sphinx-autodoc2` extension to generate documentation directly from Python docstrings. This extension extracts relevant information from classes, functions, and methods.

Given the following Python code:

```python
class MyClass:
    """
    This is a simple class to demonstrate autodoc.
    """

    def my_method(self):
        """
        This is a method that does something.
        """
        pass
```

And the following configuration in `conf.py`:

```python
extensions = [
    "(...)",
    "sphinx_blue_robotics_theme.extensions.python",
]

# Python configuration
autodoc2_packages = [
    {
        "path": "../../src/python",  # Replace with the path to your Python source directory
        "auto_mode": True,
    },
]

autodoc2_output_dir = "python_api"
```

You can reference this class and its methods using the `automodule` directive:

````markdown
```{autodoc2-object} python.mymodule.MyClass
render_plugin = "myst"
```
````

This will automatically generate documentation for the `MyClass` class and its methods. For example, the above configuration renders:

```{autodoc2-object} python.mymodule.MyClass
render_plugin = "myst"
```

Additionally, setting the configuration option `autodoc2_packages[auto_mode]` to `True` will generate reference documentation for all Python files under the `python_api` directory.

For more details, refer to the [sphinx-autodoc2 documentation](https://sphinx-autodoc2.readthedocs.io/en/latest/).

## C++ docs generation

For C++, you can use tools like Doxygen, which generates XML output from your C++ code. This XML can then be processed by Sphinx with the `breathe` and `exhale` extensions to create formatted documentation.

With the following C++ code:

```cpp
class MyClass {
public:
    /**
     * This is a simple method.
     */
    void myMethod();
};
```

And the following configuration in `conf.py`:

```python
# -*- coding: utf-8 -*-
import os
import sys
from datetime import date


# Add the parent directory to the system path
root_path = os.path.abspath(os.path.join("..", ".."))

sys.path.insert(0, root_path)

# Project information
project = "Blue Robotics Sphinx Theme"
copyright = f"{date.today().year}, Blue Robotics. All rights reserved."
author = "Blue Robotics Project Contributors"

# General configuration
extensions = [
    "(...)",
    "breathe",
    "exhale",

]

# Breathe configuration (CPP documentation)
breathe_projects = {"myproject": root_path + "/src/cpp/xml"}
breathe_default_project = "myproject"

# Exhale configuration (CPP documentation)
exhale_args = {
    "containmentFolder":     "./api",
    "rootFileName":          "library_root.rst",
    "doxygenStripFromPath":  "..",
    "rootFileTitle":         "CPP API reference",
    "createTreeView":        True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin":    "INPUT = ../include"
}
```

You can reference and generate documentation for this C++ code as follows:

````md
```{doxygenfile} my_class.h
```
````

And `breathe` will render the documentation for the `MyClass` class, including method definitions and comments from your C++ code. For example, the previous example renders:

```{doxygenfile} my_class.h
:no-link:
```

Additionally, `exhale` will generate reference documentation for all Python files under the `cpp_api` directory.

For more details, refer to [breathe](https://breathe.readthedocs.io/en/latest/quickstart.html) documentation.

## Lua docs generation

For Lua, you can use the `sphinx-lua` extension, which allows you to generate documentation from Lua code.

With the following Lua code:

```lua
--- Define a car.
--- @class MyOrg.Car
local cls = class()

--- @param foo number
function cls:test(foo)
end
```

And the following configuration in `conf.py`:


```
# General configuration
extensions = [
    (...),
    "sphinx_blue_robotics_theme.extensions.lua",
]

# sphinx-lua (Lua documentation)
lua_source_path = [root_path + "/src/lua"]
lua_source_encoding = 'utf8'
lua_source_comment_prefix = '---'
lua_source_use_emmy_lua_syntax = True
lua_source_private_prefix = '_'
lua_output_folder = "lua_api"
lua_output_title = "Lua API reference"
```

You can generate documentation for the `MyOrg.Car` class using the `lua:automodule` directive in your Markdown files:

````md
```{lua:automodule} car
```
````

This will render the documentation for the `MyOrg.Car` class ` method. For example, the previous example renders:


```{lua:automodule} car
```

Additionally, the theme will generate reference documentation for all Lua modules under the `lua_api` directory.


For more details, see [sphinx-lua](https://github.com/boolangery/sphinx-lua).

## Sample references

```{toctree}
:maxdepth: 2

/python_api/index.rst
/cpp_api/library_root.rst
/lua_api/index.rst
```  
