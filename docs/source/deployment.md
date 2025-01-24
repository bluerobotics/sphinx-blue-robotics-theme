# Deployment

This document outlines the process for deploying documentation using GitHub Actions.

## Workflow overview

The workflow that builds the documentation is located in `.github/workflows/docs-publish.yml`.

The documentation is built and deployed using the following steps:

1. **Preparation**: The workflow starts by checking the repository's default branch and extracting version information from the `versions.json` file.
2. **Building documentation**: The documentation is built for each version defined in the `versions.json` file. You can edit the default branch name from `master` to match your repository settings.
3. **Deploying documentation**: The built documentation is deployed to the `gh-pages` branch, where each version is stored in its respective folder. You can configure this step of the workflow to deploy to different hosting platforms.


Additional notes:
- If you push to the default branch docs folder, the workflow will automatically build and deploy the default branch version of the documentation.
- If you trigger the workflow manually, you can either build a specific version or build all versions defined in the `versions.json` file.


## Versions file

The `versions.json` file is at the core of this multiversion setup. This file defines the versions available for the project, and it is used to control which versions of the documentation are built and deployed. Here’s an example of how it might look:

```json
{
  "versions": [
    {
      "name": "v1.0",
      "branch": "v1.0",
      "is_default": true
    },
    {
      "name": "v2.0",
      "branch": "v2.0",
      "is_default": false
    }
  ]
}
```

In this example:

- `name`: The version name. This will be used to define the URL structure for the documentation.
- `branch`: Corresponds to the branch in your repository that the version will be built from.
- `is_default`: This field indicates the default version to which users will be redirected when they visit the documentation site without specifying a version. Ensure that only one version is marked as the default.


## Guides

### Publish a new version

To publish a new version of the documentation, follow these steps:

1. In your default branch, add a new entry for the version in the `docs/versions`.json file. Specify the version name, branch, and whether it is the default version. Example:

    ```json
    {
      "name": "v3.0",
      "branch": "v3.0",
      "is_default": false
    }
    ```

2. [Trigger the workflow manually](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow) via GitHub Actions. You can trigger the workflow from the GitHub Actions UI, and you have the option to:

    - **Build all versions**: If you leave the branch field empty, the workflow will build documentation for all versions listed in `versions.json`.
    - **Build a specific version**: If you specify a branch, only the corresponding version will be built.

3. Once the workflow completes successfully, the new version will be deployed. If the workflow fails, review the logs to identify and resolve any issues.


### Republish an existing version

To update an existing version, [trigger the workflow manually](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow) setting the branch name you want to rebuild.

This is useful when content in the versioned branch has changed and you want to reflect those updates in the documentation.


### Publish all versions

Publishing all versions is useful for the initial deployment or when making significant changes, as it ensures that every version is built from scratch.

To build all versions of the documentation, follow these streps:


1. Ensure that all versions are listed in `docs/versions.json` with the correct configuration.

2. Trigger the [workflow manually](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow) without specifying a branch.

3. Once the workflow completes successfully, the docs will be deployed. If the workflow fails, review the logs to identify and resolve any issues.




