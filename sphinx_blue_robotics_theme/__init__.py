from os import path

import sphinx_immaterial
from sphinx_blue_robotics_theme._version import version

def update_context(app, pagename, templatename, context, doctree):
    file_meta = context.get("meta", None) or {}
    context["blue_robotics_theme_version"] = version


def setup(app):
    """Setup theme"""
    app.add_html_theme("sphinx_blue_robotics_theme", path.abspath(path.dirname(__file__)))
    app.add_css_file("css/main.css", priority=600)
    app.connect("html-page-context", update_context)

    """Setup thid-party extensions"""
    sphinx_immaterial.setup(app)

    return {"version": version, "parallel_read_safe": True}
