# -*- coding: utf-8 -*-
import os
import sys
from datetime import date

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(".."))

# Project information
project = "Blue Robotics Sphinx Theme"
copyright = f"{date.today().year}, Blue Robotics. All rights reserved."
author = "Blue Robotics Project Contributors"

# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx_blue_robotics_theme",
    "sphinx_immaterial.graphviz",
    "myst_parser",
    "sphinx_design",
]
master_doc = "index"
source_suffix = [".rst", ".md"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Syntax highlighting style
pygments_style = "sphinx"

# Substitutions
rst_prolog = """
.. |rst| replace:: restructuredText
"""

# Myst Parser options
myst_enable_extensions = ["colon_fence"]

# HTML output configuration
html_theme = "sphinx_blue_robotics_theme"
html_theme_path = ["../.."]
html_logo = "_static/logo.png"
html_theme_options = {
}
# end html_theme_options

html_last_updated_fmt = "%d %b %Y"
htmlhelp_basename = "BlueRoboticsDocumentationdoc"
html_baseurl = "https://sphinx-theme.bluerobotics.com"
html_context = {"html_baseurl": html_baseurl}
