import os
from jinja2 import Template

# Template for module .rst file
MODULE_TEMPLATE = """
{{ title }}
{{ "=" * title|length }}

.. lua:automodule:: {{ module_name }}
"""

# Template for index.rst file
INDEX_TEMPLATE = """
{{ lua_output_title }}
{{ "=" * lua_output_title|length }}

.. toctree::
   :maxdepth: 2

   {% for module_file in module_files %}{{ module_file }}
   {% endfor %}

"""

def generate_lua_docs(app):
    lua_source_path = app.config.lua_source_path[0]
    lua_output_folder = app.config.lua_output_folder
    lua_output_title = app.config.lua_output_title

    src_path = os.path.abspath(lua_source_path)
    output_path = os.path.join(app.srcdir, lua_output_folder)

    lua_files = []
    for root, _, files in os.walk(src_path):
        for file in files:
            if file.endswith(".lua"):
                relative_path = os.path.relpath(os.path.join(root, file), src_path)
                lua_files.append(relative_path)

    os.makedirs(output_path, exist_ok=True)

    module_files = []
    title_counter = {}

    for lua_file in lua_files:
        module_name = lua_file.replace("/", ".").replace("\\", ".").replace(".lua", "")
        rst_file_name = f"{module_name}.rst"
        rst_file_path = os.path.join(output_path, rst_file_name)

        base_title = f"{module_name}"
        module_template = Template(MODULE_TEMPLATE)
        with open(rst_file_path, "w") as rst_file:
            rst_file.write(module_template.render(title=base_title, module_name=module_name))

        module_files.append(rst_file_name)

    index_file_path = os.path.join(output_path, "index.rst")
    index_template = Template(INDEX_TEMPLATE)
    with open(index_file_path, "w") as index_file:
        index_file.write(index_template.render(lua_output_title=lua_output_title, module_files=sorted(module_files)))

def setup(app):
    extensions = [
        "sphinxcontrib.luadomain",
        "sphinx_lua",
    ]

    for ext in extensions:
        try:
            app.setup_extension(ext)
        except Exception as e:
            raise RuntimeError(
                f"Required extension {ext} is missing. Please install it."
            )

    # Fix for https://github.com/boolangery/sphinx-lua/issues/13
    sphinx_lua_extension = app.extensions.get("sphinx_lua")
    if sphinx_lua_extension is not None:
        sphinx_lua_extension.parallel_read_safe = True
        sphinx_lua_extension.parallel_write_safe = True

    app.add_config_value("lua_output_folder", "lua_modules", "env")
    app.add_config_value("lua_output_title", "API reference", "env")
    app.connect("builder-inited", generate_lua_docs)

    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
