FROM ruby:3.4.4

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Install sudo, procps (for `ps` and other utilities) and create user
RUN apt-get update && apt-get install -y sudo procps && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # Give vscode user sudo privileges
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

WORKDIR /usr/src/app

# Copy Gemfile and Gemfile.lock first to leverage Docker cache
COPY Gemfile Gemfile.lock ./

# Set bundler to install gems to vendor/bundle (project specific)
# This configuration is stored in .bundle/config in the WORKDIR
RUN bundle config set --local path 'vendor/bundle'

# Create the app directory structure and set ownership before switching user
# This ensures that the subsequent operations by the vscode user have correct permissions.
# WORKDIR (/usr/src/app) is created by WORKDIR instruction if not existent, owned by root.
# vendor/bundle will be created inside /usr/src/app
RUN mkdir -p vendor/bundle && \
    chown -R $USERNAME:$USERNAME /usr/src/app

# Switch to the non-root user
USER $USERNAME

# Now run bundle install as the vscode user.
# Gems will be installed in /usr/src/app/vendor/bundle
RUN bundle install

# Copy the rest of the application code.
# These files will be owned by the vscode user due to USER $USERNAME.
# Using --chown for explicit ownership, good practice.
COPY --chown=$USERNAME:$USERNAME . .

EXPOSE 3000

CMD ["rails", "server", "-b", "0.0.0.0"]
