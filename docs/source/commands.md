# Commands

This page documents the commands used for setting up and managing the Sphinx project.

## Setup commands

### `setupenv`

Installs Poetry, the dependency manager.

Run in terminal:

```bash
make setupenv
```

### `setup`

Installs the required dependencies for the project using Poetry.

Run in terminal:

```bash
make setup
```

### `update`

Updates the dependencies using Poetry.

Run in terminal:

```bash
make update
```

### `clean`

Cleans the build directory by removing all its contents.

Run in terminal:

```bash
make clean
```

## Docs generation commands

### `dirhtml`

Builds the documentation as a set of HTML files in a directory.

Run in terminal:

```bash
make dirhtml
```

### `singlehtml`

Builds the documentation as a single HTML page.

Run in terminal:

```bash
make singlehtml
```

### `preview`

Starts a local server to preview the generated documentation with auto-reload.

Run in terminal:

```bash
make preview
```

## Testing commands

### `test`

Builds the documentation to ensure everything is working as expected.

**Run in terminal:**

```bash
make test
```

### `linkcheck`

Checks all links in the documentation to ensure they are valid.

Run in terminal:

```bash
make linkcheck
```
