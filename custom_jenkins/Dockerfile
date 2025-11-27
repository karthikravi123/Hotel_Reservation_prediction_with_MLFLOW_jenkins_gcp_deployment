# Base image
FROM jenkins/jenkins:lts

# Switch to root to install packages
USER root

# Install prerequisites
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    git \
    curl \
    wget \
    vim \
    unzip \
    gnupg \
    lsb-release \
    ca-certificates \
    dirmngr \
    apt-transport-https \
    && rm -rf /var/lib/apt/lists/*

# Install Docker CLI
RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh

# Add Jenkins user to docker group
RUN usermod -aG docker jenkins


# Create Docker directories
RUN mkdir -p /var/run/docker /var/lib/docker && \
    chown -R jenkins:docker /var/run/docker /var/lib/docker



# Switch back to Jenkins user
USER jenkins


