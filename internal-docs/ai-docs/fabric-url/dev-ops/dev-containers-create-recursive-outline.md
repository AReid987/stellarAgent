# Developing inside a Container using Visual Studio Code Remote Development

## Introduction

This article provides a comprehensive guide on using the **Visual Studio Code Dev Containers** extension to set up a container as a full-featured development environment. The extension allows you to open any folder inside (or mounted into) a container and take advantage of Visual Studio Code's full feature set. A `devcontainer.json` file in your project defines the development container with a well-defined tool and runtime stack.

## Main Components

- **Overview of Dev Containers Extension**
  - **Purpose**: To use a container as a full-featured development environment.
  - **Key Features**:
    - Open any folder inside a container.
    - Use a `devcontainer.json` file to define the development container.
    - Seamlessly switch development environments by connecting to different containers.

- **System Requirements**
  - **Local / Remote Host**:
    - **Docker Installation**:
      - **Windows / macOS**:
        - Install [Docker Desktop for Windows/Mac](https://www.docker.com/products/docker-desktop).
        - For WSL 2 on Windows, ensure the [WSL 2 back-end](https://aka.ms/vscode-remote/containers/docker-wsl2) is enabled.
        - Update **Resources \> File Sharing** with any locations your source code is kept.
      - **Linux**:
        - Follow the [official install instructions for Docker CE/EE](https://docs.docker.com/install/#supported-platforms).
        - Add your user to the `docker` group.
    - **Remote Hosts**:
      - Ensure at least 2 GB RAM and a 2-core CPU.
  - **Containers**:
    - Supported Linux distributions and architectures.

- **Installation**
  - **Steps**:
    1. **Install Docker**:
       - **Windows / macOS**: Install Docker Desktop.
       - **Linux**: Follow official Docker CE/EE installation instructions.
    2. **Install Visual Studio Code**:
       - Install [Visual Studio Code](https://code.visualstudio.com/) or [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/).
    3. **Install Dev Containers Extension**:
       - Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

- **Working with Git**
  - **Tips**:
    - Ensure consistent line endings when working with repositories both locally and inside a container.
    - Share Git credentials with your container if using SSH keys.

- **Picking Your Quick Start**
  - **Options**:
    1. **Quick Start 1**: Try a development container.
    2. **Quick Start 2**: Open an existing folder in a container.
    3. **Quick Start 3**: Open a Git repository or PR in an isolated container volume.

- **Quick Start: Try a Development Container**
  - **Steps**:
    1. Follow the [Containers tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial).
    2. Use the **open in dev container** command if VS Code and Docker are already installed.

- **Quick Start: Open an Existing Folder in a Container**
  - **Steps**:
    1. Run the **Dev Containers: Open Folder in Container...** command.
    2. Select a base **Dev Container Template** or use an existing Dockerfile or Docker Compose file.
    3. VS Code will add the dev container configuration files to your project.
    4. The VS Code window will reload and start building the dev container.
    5. After the build completes, VS Code will automatically connect to the container.

- **Open a WSL 2 Folder in a Container on Windows**
  - **Steps**:
    1. Ensure Docker Desktop's WSL 2 back-end is enabled.
    2. Use the **Dev Containers: Reopen in Container** command from a folder already opened using the WSL extension.
    3. Select **Dev Containers: Open Folder in Container...** from the Command Palette and choose a WSL folder.

- **Open a Folder on a Remote SSH Host in a Container**
  - **Steps**:
    1. Follow the installation and SSH host setup steps for the Remote - SSH extension.
    2. Install Docker on your SSH host.
    3. Connect to a host and open a folder there.
    4. Use the **Dev Containers: Reopen in Container** command from the Command Palette.

- **Open a Folder on a Remote Tunnel Host in a Container**
  - **Steps**:
    1. Follow the Getting Started instructions for the Remote - Tunnels extension.
    2. Install Docker on your tunnel host.
    3. Connect to a tunnel host and open a folder there.
    4. Use the **Dev Containers: Reopen in Container** command from the Command Palette.

- **Open an Existing Workspace in a Container**
  - **Steps**:
    1. Use the **Dev Containers: Open Workspace in Container...** command.
    2. Add the `.devcontainer` folder to the workspace if it is not already visible.

- **Quick Start: Open a Git Repository or GitHub PR in an Isolated Container Volume**
  - **Steps**:
    1. Run **Dev Containers: Clone Repository in Container Volume...** from the Command Palette.
    2. Enter the repository name, Git URI, GitHub branch URL, or GitHub PR URL.
    3. Select a starting point from a filterable list or an existing Dockerfile or Docker Compose file.
    4. The VS Code window will reload, clone the source code, and start building the dev container.
    5. After the build completes, VS Code will automatically connect to the container.

- **Trusting Your Workspace**
  - **Scenarios**:
    - **Reopen Folder in Container**: Trust the local folder before the window reloads.
    - **Attach to Existing Container**: Confirm that attaching means you trust the container.
    - **Clone Repository in a Volume**: Confirm that cloning a repository means you trust the repository.
    - **Inspect Volume**: Starts in Restricted Mode, and you can trust the folder inside the container.
    - **Docker Daemon Running Remotely**: Implies trusting the machine the Docker daemon runs on.

- **Create a devcontainer.json File**
  - **Purpose**: To configure the development container.
  - **Steps**:
    1. Use the **Dev Containers: Add Dev Container Configuration Files...** command.
    2. Select a pre-defined container configuration or reuse an existing Dockerfile or Docker Compose file.
  - **Example**:
    ```json
    {
      "image": "mcr.microsoft.com/devcontainers/typescript-node",
      "forwardPorts": [3000],
      "customizations": {
        "vscode": {
          "extensions": ["streetsidesoftware.code-spell-checker"]
        }
      }
    }
    ```

- **Dev Container Features**
  - **Purpose**: To add tooling, runtime, or library features to your development container.
  - **Steps**:
    1. Use the **Dev Containers: Add Dev Container Configuration Files** command.
    2. Select features to customize the dev container configurations.
  - **Example**:
    ```json
    "features": {
        "ghcr.io/devcontainers/features/github-cli:1": {
            "version": "latest"
        }
    }
    ```

- **Pre-building Dev Container Images**
  - **Purpose**: To pre-build images with the tools you need for faster container startup.
  - **Steps**:
    1. Use the [Dev Container CLI](https://code.visualstudio.com/docs/devcontainers/devcontainer-cli) to pre-build your images.
    2. Push the pre-built image to a container registry.
    3. Reference the image directly in your `devcontainer.json`.
  - **Example**:
    ```json
    {
      "image": "mcr.microsoft.com/devcontainers/go:1"
    }
    ```

- **Inspecting Volumes**
  - **Purpose**: To inspect or make changes in a Docker named volume.
  - **Steps**:
    1. Use the **Dev Containers: Explore a Volume in a Dev Container...** command from the Command Palette.
    2. Inspect the volume in the Remote Explorer.

- **Managing Extensions**
  - **Purpose**: To manage extensions installed in the container.
  - **Steps**:
    1. Install extensions from the Extensions view.
    2. Use the **Install Local Extensions in Dev Container** command to install locally installed extensions in the container.
  - **Opt Out of Extensions**:
    ```json
    {
      "image": "mcr.microsoft.com/devcontainers/typescript-node:1-20-bookworm",
      "customizations": {
        "vscode": {
          "extensions": ["-dbaeumer.vscode-eslint"]
        }
      }
    }
    ```

- **Forwarding or Publishing a Port**
  - **Purpose**: To access a server, service, or other resource inside your container.
  - **Steps**:
    1. Use the `forwardPorts` property in `devcontainer.json` to always forward ports.
    2. Use the **Forward a Port** command from the Command Palette to temporarily forward a port.
    3. Use the `appPort` property or Docker Compose ports mapping to publish ports.

- **Opening a Terminal**
  - **Purpose**: To open a terminal in the container.
  - **Steps**:
    1. Open a terminal window in VS Code.
    2. Use the `code` command line to perform operations such as opening a new file or folder in the container.

- **Debugging in a Container**
  - **Purpose**: To use VS Code's debugger in the container.
  - **Steps**:
    1. Select a launch configuration in `launch.json` and start debugging (F5).

- **Container Specific Settings**
  - **Purpose**: To set container-specific settings.
  - **Steps**:
    1. Use the **Preferences: Open Remote Settings** command from the Command Palette.
    2. Add defaults for container-specific settings in `devcontainer.json`.
  - **Example**:
    ```json
    "customizations": {
        "vscode": {
            "settings": {
                "java.home": "/docker-java-home"
            }
        }
    }
    ```

- **Managing Containers**
  - **Purpose**: To manage containers using the Remote Explorer.
  - **Steps**:
    1. Use the Remote Explorer to stop, start, or remove containers.
    2. Use the **Dev Containers: Rebuild Container** command to rebuild the container.

- **Personalizing with Dotfile Repositories**
  - **Purpose**: To personalize your development container with dotfiles.
  - **Steps**:
    1. Add your dotfiles GitHub repository to VS Code's User Settings.
    2. The dotfiles repository will be used whenever a container is created.

- **Known Limitations**
  - **Dev Containers Limitations**:
    - Windows container images are not supported.
    - Multi-root workspaces will be opened in the same container.
    - The unofficial Ubuntu Docker snap package for Linux is not supported.
    - Docker Toolbox on Windows is not supported.
    - SSH key passphrase issues when cloning a Git repository.
    - Local proxy settings are not reused inside the container.
    - OpenSSH version incompatibility on Windows.
  - **Docker Limitations**:
    - See the Docker troubleshooting guide for Windows or Mac.
  - **Docker Extension Limitations**:
    - Using the **Attach Visual Studio Code** context menu action in the Docker or Kubernetes views will ask to pick from the available containers a second time.
  - **Extension Limitations**:
    - Most extensions will work inside Dev Containers without modification.
    - Some extensions may not work due to `glibc` dependencies in native code inside the extension.

- **Advanced Container Configuration**
  - **Topics**:
    - Adding environment variables.
    - Adding another local file mount.
    - Changing or removing the default source code mount.
    - Improving container disk performance.
    - Adding a non-root user to your dev container.
    - Setting the project name for Docker Compose.
    - Using Docker or Kubernetes from inside a container.
    - Connecting to multiple containers at once.
    - Developing inside a container on a remote Docker Machine or SSH host.
    - Reducing Dockerfile build warnings.
    - Sharing Git credentials with your container.

- **devcontainer.json Reference**
  - **Purpose**: To review the file schema for customizing development containers.
  - **Link**: [devcontainer.json reference](https://containers.dev/implementors/json_reference)

- **Questions or Feedback**
  - **Resources**:
    - See [Tips and Tricks](https://code.visualstudio.com/docs/devcontainers/tips-and-tricks) or the [FAQ](https://code.visualstudio.com/docs/devcontainers/faq).
    - Search on [Stack Overflow](https://stackoverflow.com/questions/tagged/vscode-remote).
    - Add a [feature request](https://aka.ms/vscode-remote/feature-requests) or [report a problem](https://aka.ms/vscode-remote/issues/new).
    - Create a [Dev Container Template](https://containers.dev/templates) or [Feature](https://containers.dev/features) for others to use.
    - Review and provide feedback on the [Development Containers Specification](https://containers.dev/).
    - Contribute to [our documentation](https://github.com/microsoft/vscode-docs) or [VS Code itself](https://github.com/microsoft/vscode).
    - See our [CONTRIBUTING](https://aka.ms/vscode-remote/contributing) guide for details.

- **Next Steps**
  - **Resources**:
    - [Attach to a Running Container](https://code.visualstudio.com/docs/devcontainers/attach-container)
    - [Create a Development Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
    - [Advanced Containers](https://code.visualstudio.com/remote/advancedcontainers/overview)
    - [devcontainer.json reference](https://containers.dev/implementors/json_reference)
