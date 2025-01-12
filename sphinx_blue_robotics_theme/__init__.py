from os import path

import sphinx_immaterial
from sphinx_blue_robotics_theme._version import version

def update_context(app, pagename, templatename, context, doctree):
    file_meta = context.get("meta", None) or {}
    context["blue_robotics_theme_version"] = version

    # Define right_drawer
    context["right_drawer"] = [
    {
        "title": "Docs",
        "url": "https://docs.bluerobotics.com",
        "children": [],
        "active": False,
        "current": False,
    },
    {
        "title": "Projects",
        "url": "#",
        "children": [
            {
                "title": "BlueOS",
                "url": "#",
                "children": [
                    {"title": "BlueOS docs", "url": "https://blueos.cloud/docs/", "children": []},
                    {"title": "Cockpit docs", "url": "https://blueos.cloud/cockpit/docs/", "children": []},
                    {"title": "BlueOS Community (GitHub)", "url": "https://github.com/orgs/BlueOS-community/repositories", "children": []},
                    {"title": "About BlueOS", "url": "hhttps://blueos.cloud/", "children": []},
                ],
            },
            {
                "title": "Navigator",
                "url": "#",
                "children": [
                    {"title": "Navigator Libraries (Python)", "url": "#", "children": []},
                    {"title": "Navigator Libraries (C++)", "url": "#", "children": []},
                    {"title": "Navigator Libraries (Rust)", "url": "#", "children": []},
                    {"title": "See Navigator Product", "url": "https://bluerobotics.com/store/comm-control-power/control/navigator/", "children": []},
                ],
            },
            {
                "title": "Ping Sonars and Ping Protocol",
                "url": "#",
                "children": [
                    {"title": "Ping Viewer", "url": "#", "children": []},
                    {"title": "Ping Protocol", "url": "#", "children": []},
                    {"title": "ping-rs", "url": "#", "children": []},
                    {"title": "ping-cpp", "url": "#", "children": []},
                    {"title": "ping-arduino", "url": "#", "children": []},
                    {"title": "ping-python", "url": "#", "children": []},
                    {"title": "See Ping Sonar Products", "url": "https://bluerobotics.com/product-category/sonars/", "children": []},
                ],
            },
            {
                "title": "Sensors",
                "url": "#",
                "children": [
                    {"title": "ms5837-python", "url": "#", "children": []},
                    {"title": "BlueRobotics_MS5837_Library (Arduino)", "url": "#", "children": []},
                    {"title": "KellerLD-python", "url": "#", "children": []},
                    {"title": "BlueRobotics_KellerLD_Library (Arduino)", "url": "#", "children": []},
                    {"title": "tsys01-python", "url": "#", "children": []},
                    {"title": "BlueRobotics_TSYS01_Library (Arduino)", "url": "#", "children": []},
                    {"title": "See Sensor Products", "url": "https://bluerobotics.com/product-category/sensors-cameras/sensors/", "children": []},
                ],
            },
        ],
    },
    {
        "title": "Community",
        "url": "#",
        "children": [
            {
                "title": "Blue Robotics",
                "url": "#",
                "children": [
                    {"title": "About Blue Robotics", "url": "https://bluerobotics.com/about/", "children": []},
                    {"title": "Visit the Store", "url": "https://bluerobotics.com/store/", "children": []},
                    {"title": "Blue Robotics Guides", "url": "https://bluerobotics.com/learn/", "children": []},
                    {"title": "Blue Robotics Github", "url": "https://github.com/bluerobotics", "children": []},
                ],
            },
            {
                "title": "Support",
                "url": "#",
                "children": [
                    {"title": "Blue Robotics Forum", "url": "https://discuss.bluerobotics.com/", "children": []},
                    {"title": "Blue Robotics Support", "url": "https://bluerobotics.com/help/?want=report", "children": []},
                ],
            },
        ],
    },
]

def setup(app):
    """Setup theme"""
    app.add_html_theme("sphinx_blue_robotics_theme", path.abspath(path.dirname(__file__)))
    app.add_css_file("css/main.css", priority=600)
    app.connect("html-page-context", update_context)

    """Setup thid-party extensions"""
    sphinx_immaterial.setup(app)

    return {"version": version, "parallel_read_safe": True}
