# Installation

This guide explains how to install Sphinx and the custom theme in a BlueRobotics project. Follow the steps below to quickly get started with generating and previewing your documentation.

## Requirements

Before getting started, make sure you have the following tools installed:

- Python 3.12 or higher
- Make
- [Poetry](https://python-poetry.org/)

## Step by step

To install Sphinx and this theme in a BlueRobotics project, follow these steps:

1. Copy the `docs` folder [from this repository](https://github.com/bluerobotics/sphinx-blue-robotics-theme) into your own project.

2. Edit your `conf.py` global variables with your project details:

   ```python
   SITE_URL = "https://docs.bluerobotics.com/sphinx-theme/"
   REPO_URL = "https://github.com/bluerobotics/sphinx-blue-robotics-theme"
   REPO_NAME = "sphinx-blue-robotics-theme"
   PROJECT_NAME ="Blue Robotics Sphinx Theme"
   ```

3. Edit your documentation as needed.


4. To view the documentation locally, run the following command:

   ```bash
   make preview
   ```

   This will build the documentation and start a local preview server at `http://localhost:5500`.