FROM python:3.12-bullseye

# Install common dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        build-essential \
        curl \
        git

# Create a non-root user with sudo access
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd --gid $GROUP_ID vscode
RUN useradd --uid $USER_ID --gid $GROUP_ID --create-home vscode

# Switch to the non-root user
USER vscode

# Set working directory
WORKDIR /workspace

# Copy requirements and install dependencies
COPY requirements.txt .
