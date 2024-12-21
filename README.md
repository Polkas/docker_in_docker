# docker_in_docker

An environment to play with docker.

This project is part of a blog post and provides a playground to learn.

## Examples

### Python Shiny App

- Path: `examples/py-shiny-app`
- Description: A simple Python Shiny app with a slider input and a plot output.
- Command to run: `docker build -t py-shiny-app examples/py-shiny-app && docker run -p 3838:3838 py-shiny-app`

### R Shiny App

- Path: `examples/r-shiny-app`
- Description: A simple R Shiny app with a slider input and a plot output.
- Command to run: `docker build -t r-shiny-app examples/r-shiny-app && docker run -p 3838:3838 r-shiny-app`

### JupyterLab

- Path: `examples/jupyterlab`
- Description: An environment to run JupyterLab.
- Command to run: `docker build -t jupyterlab examples/jupyterlab && docker run -p 8888:8888 jupyterlab`

### RStudio

- Path: `examples/rstudio`
- Description: An environment to run RStudio.
- Command to run: `docker build -t rstudio examples/rstudio && docker run -p 8787:8787 rstudio`
- Login: `rstudio`
- Password: `rstudio`

#### User-PW-List.txt

The `user-pw-list.txt` file is used to manage user accounts for RStudio. It contains a list of users and their passwords in the following format:

```
username:password
```

Example:

```
rstudio:rstudio
user1:password1
user2:password2
```

To add more users, simply follow the format and add new lines to the file.

### VSCode

- Path: `examples/vscode`
- Description: An environment to run VSCode.
- Command to run: `docker build -t vscode examples/vscode && docker run -p 8080:8080 vscode`

### Docker Compose for Shiny Apps

- Path: `docker-compose.yml`
- Description: A compose file to run all apps, including Shiny apps, JupyterLab, RStudio, and VSCode, at the same time.
- Command to run: `docker-compose up`

## Continuous Integration with GitHub Actions

This project includes a GitHub Actions CI workflow to automate the build and run process for all examples. The workflow is located in the `.github/workflows/ci.yml` file. It sets up Docker, builds and runs each example, and verifies that they work correctly. The workflow includes steps to build and run the `py-shiny-app`, `r-shiny-app`, `jupyterlab`, `rstudio`, and `vscode` examples, as well as the `docker-compose.yml` file to run all apps simultaneously.

## Installing Docker Compose

To install Docker Compose, follow these steps:

1. Download the current stable release of Docker Compose:
   ```sh
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```

2. Apply executable permissions to the binary:
   ```sh
   sudo chmod +x /usr/local/bin/docker-compose
   ```

3. Test the installation:
   ```sh
   docker-compose --version
   ```
