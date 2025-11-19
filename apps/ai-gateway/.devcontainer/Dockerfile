FROM python:3.13-slim-bullseye
ENV TURBO_TOKEN=$TURBO_TOKEN
ENV TURBO_TEAM=$TURBO_TEAM

# Install common dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        build-essential \
        curl \
        git \
        procps \
        nodejs \
        npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd --gid $GROUP_ID developer \
    && useradd --uid $USER_ID --gid $GROUP_ID -m developer \
    && apt-get update \
    && apt-get install -y sudo \
    && echo developer ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/developer \
    && chmod 0440 /etc/sudoers.d/developer

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Switch to the non-root user
USER developer

# Set working directory
WORKDIR /workspace

# Copy requirements
COPY --chown=developer:developer requirements.txt .

# Initialize uv
RUN uv venv
