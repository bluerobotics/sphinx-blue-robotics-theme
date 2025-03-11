from os import path
import json

import sphinx_immaterial
from sphinx_blue_robotics_theme._version import version

def _build_right_drawer(app):
    """Load right drawer configuration from JSON file"""
    try:
        drawer_path = path.join(path.dirname(__file__), 'drawer.json')
        with open(drawer_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        app.warning(f"Could not load drawer configuration: {e}")
        return []

def update_context(app, pagename, templatename, context, doctree):
    file_meta = context.get("meta", None) or {}
    context["blue_robotics_theme_version"] = version
    context["right_drawer"] = _build_right_drawer(app)
    context["favicon_url"] = app.config.html_static_path[0] + "/favicon.ico"
    file_meta = context.get("meta", None) or {}
    context["hide_date"] = "hide-date" in file_meta


def setup(app):
    """Setup theme"""
    app.add_html_theme("sphinx_blue_robotics_theme", path.abspath(path.dirname(__file__)))
    app.add_css_file("css/main.css", priority=600)
    app.add_js_file("js/jquery.min.js", priority=100)
    app.add_js_file("js/main.js", priority=600)

    app.connect("html-page-context", update_context)

    """Setup thid-party extensions"""
    sphinx_immaterial.setup(app)

    return {"version": version, "parallel_read_safe": True}
