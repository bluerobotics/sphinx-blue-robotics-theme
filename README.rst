==========================
sphinx-blue-robotics-theme
==========================

A customized toolchain for Blue Robotics documentation projects, built on the Sphinx framework.

.. warning::

   **This project is currently under development. Features and functionality may change without notice.**

Features
--------

This theme extends the `sphinx-immaterial <https://jbms.github.io/sphinx-immaterial/>`_ theme, enhanced with the following features:

- **Custom branding:** Incorporates the Blue Robotics logo and colors for consistent branding across documentation.
- **Multiversion support:** Includes a dropdown menu for switching between different versions of the documentation.
- **Built-in extensions:** Pre-configured extensions tailored for use in all Blue Robotics documentation projects.

Prerequisites
-------------

Before getting started, make sure you have the following tools installed:

- Git
- Python 3.12 or higher
- Make
- `Poetry <https://python-poetry.org/>`_

Quickstart
----------

.. code-block:: bash

   cd docs
   make preview

Release a new theme version
---------------------------

To release a new theme version:

1. Update the version in the `pyproject.toml` file.
2. Run `poetry build` to build the package.
3. Run `poetry publish` to publish the package to the Python Package Index.

License
-------

More info coming soon.
