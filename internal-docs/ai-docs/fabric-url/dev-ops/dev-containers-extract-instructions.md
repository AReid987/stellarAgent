### Objectives
- Learn to set up and use Visual Studio Code Dev Containers for development.
- Understand how to configure and manage development containers using `devcontainer.json`.
- Work with Git repositories and manage extensions within the container.
- Explore advanced container configurations and troubleshooting tips.

### Instructions
1. **Install Docker**:
   - **Windows / macOS**: Install [Docker Desktop for Windows/Mac](https://www.docker.com/products/docker-desktop).
   - **Linux**: Follow the [official install instructions for Docker CE/EE](https://docs.docker.com/install/#supported-platforms).
2. **Install Visual Studio Code**:
   - Install [Visual Studio Code](https://code.visualstudio.com/) or [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/).
3. **Install Dev Containers Extension**:
   - Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
4. **Ensure Consistent Line Endings**:
   - Ensure consistent line endings when working with repositories both locally and inside a container.
5. **Share Git Credentials**:
   - Share Git credentials with your container if using SSH keys.
6. **Quick Start: Try a Development Container**:
   - Follow the [Containers tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial).
   - Use the **open in dev container** command if VS Code and Docker are already installed.
7. **Quick Start: Open an Existing Folder in a Container**:
   - Run the **Dev Containers: Open Folder in Container...** command.
   - Select a base **Dev Container Template** or use an existing Dockerfile or Docker Compose file.
   - VS Code will add the dev container configuration files to your project.
   - The VS Code window will reload and start building the dev container.
   - After the build completes, VS Code will automatically connect to the container.
8. **Open a WSL 2 Folder in a Container on Windows**:
   - Ensure Docker Desktop's WSL 2 back-end is enabled.
   - Use the **Dev Containers: Reopen in Container** command from a folder already opened using the WSL extension.
   - Select **Dev Containers: Open Folder in Container...** from the Command Palette and choose a WSL folder.
9. **Open a Folder on a Remote SSH Host in a Container**:
   - Follow the installation and SSH host setup steps for the Remote - SSH extension.
   - Install Docker on your SSH host.
   - Connect to a host and open a folder there.
   - Use the **Dev Containers: Reopen in Container** command from the Command Palette.
10. **Open a Folder on a Remote Tunnel Host in a Container**:
    - Follow the Getting Started instructions for the Remote - Tunnels extension.
    - Install Docker on your tunnel host.
    - Connect to a tunnel host and open a folder there.
    - Use the **Dev Containers: Reopen in Container** command from the Command Palette.
11. **Open an Existing Workspace in a Container**:
    - Use the **Dev Containers: Open Workspace in Container...** command.
    - Add the `.devcontainer` folder to the workspace if it is not already visible.
12. **Quick Start: Open a Git Repository or GitHub PR in an Isolated Container Volume**:
    - Run **Dev Containers: Clone Repository in Container Volume...** from the Command Palette.
    - Enter the repository name, Git URI, GitHub branch URL, or GitHub PR URL.
    - Select a starting point from a filterable list or an existing Dockerfile or Docker Compose file.
    - The VS Code window will reload, clone the source code, and start building the dev container.
    - After the build completes, VS Code will automatically connect to the container.
13. **Trusting Your Workspace**:
    - **Reopen Folder in Container**: Trust the local folder before the window reloads.
    - **Attach to Existing Container**: Confirm that attaching means you trust the container.
    - **Clone Repository in a Volume**: Confirm that cloning a repository means you trust the repository.
    - **Inspect Volume**: Starts in Restricted Mode, and you can trust the folder inside the container.
    - **Docker Daemon Running Remotely**: Implies trusting the machine the Docker daemon runs on.
14. **Create a devcontainer.json File**:
    - Use the **Dev Containers: Add Dev Container Configuration Files...** command.
    - Select a pre-defined container configuration or reuse an existing Dockerfile or Docker Compose file.
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
15. **Add Dev Container Features**:
    - Use the **Dev Containers: Add Dev Container Configuration Files** command.
    - Select features to customize the dev container configurations.
    - **Example**:
      ```json
      "features": {
          "ghcr.io/devcontainers/features/github-cli:1": {
              "version": "latest"
          }
      }
      ```
16. **Pre-build Dev Container Images**:
    - Use the [Dev Container CLI](https://code.visualstudio.com/docs/devcontainers/devcontainer-cli) to pre-build your images.
    - Push the pre-built image to a container registry.
    - Reference the image directly in your `devcontainer.json`.
    - **Example**:
      ```json
      {
        "image": "mcr.microsoft.com/devcontainers/go:1"
      }
      ```
17. **Inspect Volumes**:
    - Use the **Dev Containers: Explore a Volume in a Dev Container...** command from the Command Palette.
    - Inspect the volume in the Remote Explorer.
18. **Manage Extensions**:
    - Install extensions from the Extensions view.
    - Use the **Install Local Extensions in Dev Container** command to install locally installed extensions in the container.
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
19. **Forward or Publish a Port**:
    - Use the `forwardPorts` property in `devcontainer.json` to always forward ports.
    - Use the **Forward a Port** command from the Command Palette to temporarily forward a port.
    - Use the `appPort` property or Docker Compose ports mapping to publish ports.
20. **Open a Terminal**:
    - Open a terminal window in VS Code.
    - Use the `code` command line to perform operations such as opening a new file or folder in the container.
21. **Debug in a Container**:
    - Select a launch configuration in `launch.json` and start debugging (F5).
22. **Set Container-Specific Settings**:
    - Use the **Preferences: Open Remote Settings** command from the Command Palette.
    - Add defaults for container-specific settings in `devcontainer.json`.
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
23. **Manage Containers**:
    - Use the Remote Explorer to stop, start, or remove containers.
    - Use the **Dev Containers: Rebuild Container** command to rebuild the container.
24. **Personalize with Dotfile Repositories**:
    - Add your dotfiles GitHub repository to VS Code's User Settings.
    - The dotfiles repository will be used whenever a container is created.
25. **Review Known Limitations**:
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
26. **Explore Advanced Container Configuration**:
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
27. **Review devcontainer.json Reference**:
    - **Purpose**: To review the file schema for customizing development containers.
    - **Link**: [devcontainer.json reference](https://containers.dev/implementors/json_reference)
28. **Questions or Feedback**:
    - See [Tips and Tricks](https://code.visualstudio.com/docs/devcontainers/tips-and-tricks) or the [FAQ](https://code.visualstudio.com/docs/devcontainers/faq).
    - Search on [Stack Overflow](https://stackoverflow.com/questions/tagged/vscode-remote).
    - Add a [feature request](https://aka.ms/vscode-remote/feature-requests) or [report a problem](https://aka.ms/vscode-remote/issues/new).
    - Create a [Dev Container Template](https://containers.dev/templates) or [Feature](https://containers.dev/features) for others to use.
    - Review and provide feedback on the [Development Containers Specification](https://containers.dev/).
    - Contribute to [our documentation](https://github.com/microsoft/vscode-docs) or [VS Code itself](https://github.com/microsoft/vscode).
    - See our [CONTRIBUTING](https://aka.ms/vscode-remote/contributing) guide for details.
29. **Next Steps**:
    - **Resources**:
      - [Attach to a Running Container](https://code.visualstudio.com/docs/devcontainers/attach-container)
      - [Create a Development Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
      - [Advanced Containers](https://code.visualstudio.com/remote/advancedcontainers/overview)
      - [devcontainer.json reference](https://containers.dev/implementors/json_reference)
