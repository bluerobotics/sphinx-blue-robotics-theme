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
author = "Blue Robotics contributors"

# General configuration
extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_blue_robotics_theme",
    "sphinx_blue_robotics_theme.extensions.extras",
    "sphinx_blue_robotics_theme.extensions.python",
    "sphinx_blue_robotics_theme.extensions.cpp",
    "sphinx_blue_robotics_theme.extensions.lua",
    "myst_parser", 

]
master_doc = "index"
source_suffix = {'.rst': 'restructuredtext', '.md': 'restructuredtext'}
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Syntax highlighting style
pygments_style = "sphinx"

# Substitutions
myst_substitutions = {
  "project_name": "Blue Robotics"
}

# Myst Parser options
myst_enable_extensions = ["substitution", "colon_fence"]

# HTML output configuration
html_theme = "sphinx_blue_robotics_theme"
html_theme_path = ["../.."]
html_logo = "_static/logo.png"
# "html_favicon = "_static/images/favicon.ico""
html_theme_options = {
    "site_url": "https://sphinx-theme.bluerobotics.com",
    "repo_url": "https://github.com/bluerobotics/sphinx-blue-robotics-theme",
    "repo_name": "sphinx-blue-robotics-theme",
    "edit_uri": "blob/master/docs/source",
        "features": [
        #"navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        #"search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "toc_title_is_page_title": True,
    "globaltoc_collapse": False,
}

html_last_updated_fmt = "%d %b %Y"
htmlhelp_basename = "BlueRoboticsDocumentationdoc"
html_baseurl = "https://sphinx-theme.bluerobotics.com"
html_context = {"html_baseurl": html_baseurl}

# Autodoc configuration (Python documentation)
autodoc2_packages = [
    {
        "path": "../../src/python",
    },
]

autodoc2_output_dir = "python_api"

# Breathe configuration (CPP documentation)
breathe_projects = {"myproject": root_path + "/src/cpp/xml"}
breathe_default_project = "myproject"

# Exhale configuration (CPP documentation)
exhale_args = {
    "containmentFolder":     "./cpp_api",
    "rootFileName":          "library_root.rst",
    "doxygenStripFromPath":  "..",
    "rootFileTitle":         "CPP API reference",
    "createTreeView":        True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin":    """
        INPUT       = ../../src/cpp
        GENERATE_XML = YES
        XML_OUTPUT  = ./xml
    """,}

# sphinx-lua (Lua documentation)
lua_source_path = [root_path + "/src/lua"]
lua_source_encoding = 'utf8'
lua_source_comment_prefix = '---'
lua_source_use_emmy_lua_syntax = True
lua_source_private_prefix = '_'
lua_output_folder = "lua_api"
lua_output_title = "Lua API reference"