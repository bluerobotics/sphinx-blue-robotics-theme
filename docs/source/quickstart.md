# Quickstart

This guide will walk you through the steps to start contributing to the documentation of BlueRobotics project. By following these steps, you will be able to preview and edit the docs in no time.

## Requirements

Before getting started, make sure you have the following tools installed:

- Git
- Python 3.12 or higher
- Make
- [Poetry](https://python-poetry.org/)

## Step by step

To get started with editing and previewing the documentation for a BlueRobotics project, follow these steps:


1. Clone the BlueRobotics repository that contains the `docs` folder you want to contribute to:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the `docs` folder where the documentation files are located:

   ```bash
   cd docs
   ```

3. Run the following command to build and preview the documentation locally:

   ```bash
   make preview
   ```

   This will start a local server, and you can view the documentation at `http://localhost:5500`.

## Next steps

You can edit documentation in either Markdown (`.md`) or reStructuredText (`.rst`) format. Choose the format you're comfortable with and edit the respective files in the `docs` folder.

   - For **Markdown** files, refer to the [MyST Parser guide](https://myst-parser.readthedocs.io/en/latest/).
   - For **reStructuredText** (RST) files, check out the [Sphinx reStructuredText basics](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) for syntax and examples.


For day-to-day examples on how to work with components, refer to [Examples](examples/index.md).

Once you're happy with your changes, submit a pull request and describe the changes you made.