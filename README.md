# README

This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to cover:

* Ruby version

* System dependencies

* Configuration

* Database creation

* Database initialization

* How to run the test suite

* Services (job queues, cache servers, search engines, etc.)

* Deployment instructions

* ...


## Development Environment using Dev Containers

This project is configured to use [Visual Studio Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers). This allows you to have a consistent and fully configured development environment using Docker.

### Prerequisites

1.  **Docker Desktop**: Install Docker Desktop for your operating system ([Windows](https://docs.docker.com/desktop/install/windows-install/), [macOS](https://docs.docker.com/desktop/install/mac-install/), [Linux](https://docs.docker.com/desktop/install/linux-install/)).
2.  **Visual Studio Code**: Install [VS Code](https://code.visualstudio.com/).
3.  **VS Code Dev Containers extension**: Install the "Dev Containers" extension from the VS Code Marketplace (identifier: `ms-vscode-remote.remote-containers`).

### Getting Started

1.  **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    (Replace `<repository_url>` and `<repository_directory>` with the actual URL and local directory name.)

2.  **Open in Dev Container**:
    *   Open the cloned project folder in VS Code.
    *   VS Code should automatically detect the `.devcontainer/devcontainer.json` configuration and show a notification asking if you want to "Reopen in Container". Click it.
    *   If you don't see the notification, you can open the Command Palette (View > Command Palette or `Ctrl+Shift+P`/`Cmd+Shift+P`) and search for/select "**Dev Containers: Reopen in Container**".

3.  **First Time Setup**:
    *   The first time you open the project in the dev container, Docker will build the container images defined in `.devcontainer/docker-compose.yml`. This might take a few minutes.
    *   After the build, the `postCreateCommand` defined in `devcontainer.json` (`bundle install && rake db:prepare`) will run. This installs all gem dependencies and prepares the development and test databases. You can follow the progress in the VS Code terminal or by checking the logs for the "postCreateCommand" (View -> Output, then select "Dev Containers" from the dropdown).

4.  **Running the Rails Application**:
    *   Once the container is built and the `postCreateCommand` has finished, open a new terminal in VS Code (Terminal > New Terminal). This terminal is inside the `app` service of your dev container (you should see a prompt like `vscode@<some_hash>:/usr/src/app$`).
    *   The application directory (`/usr/src/app`) is your working directory.
    *   To start the Rails server, run:
        ```bash
        rails server -b 0.0.0.0
        ```
    *   The application will be accessible at `http://localhost:3000` on your host machine. The PostgreSQL database (service name `db`) will be accessible on `localhost:5432` from your host if you need to connect with an external tool (credentials are `postgres`/`password` for user/database `pingkong_dev`).

5.  **Running Tests**:
    *   To run the RSpec test suite, use the VS Code terminal within the dev container:
        ```bash
        bundle exec rspec
        ```
    *   Or, if you prefer using Rake:
        ```bash
        rake spec
        ```

### Working in the Dev Container

*   Your project files are directly mounted into the container from your local filesystem, so any changes you make in VS Code (or your local file system) are immediately reflected inside the container, and vice-versa.
*   You can use the VS Code debugger, terminal, and all your installed extensions within this isolated environment.
*   The Ruby version is 3.4.4, managed by the Docker image.
*   Databases (`pingkong_dev` for development, `pingkong_test` for testing) are provided by the `db` service (PostgreSQL 15) in Docker Compose. Data for the `db` service is persisted in a Docker volume named `pgdata` (defined in `.devcontainer/docker-compose.yml`), so your database contents will remain even if you stop and restart the containers.

### Troubleshooting

*   **VS Code doesn't prompt to reopen in container**: Ensure the "Dev Containers" extension is installed and enabled. You can always use the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and search for "Dev Containers: Reopen in Container".
*   **`postCreateCommand` fails**: Check the logs (View -> Output, then select "Dev Containers" from the dropdown in VS Code). Common issues could be network problems during `bundle install` or issues with `rake db:prepare` if database migrations have problems. You can try running the commands (`bundle install`, `rake db:prepare`) manually in the dev container terminal to debug.
*   **Port conflicts**: If port 3000 (for Rails) or 5432 (for PostgreSQL) is already in use on your host machine, you might need to stop the conflicting service. Alternatively, you can reconfigure the forwarded ports in `.devcontainer/docker-compose.yml`. For example, change `"3000:3000"` to `"3001:3000"` for the `app` service to access the Rails app on `http://localhost:3001` on your host.
*   **User Permissions**: Files created inside the container by the `vscode` user will typically have UID/GID `1000:1000`. Ensure this doesn't cause permission issues on your host system if your local user has a different UID/GID. Docker Desktop's volume mounting usually handles this well, but it can vary.
