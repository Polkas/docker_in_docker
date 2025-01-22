# docker_in_docker

An environment to play with docker and docker compose.
Simply run the repository in the GitHub codespaces.

This project is part of a blog post and provides a playground to learn.

## Direct Play

You can play with docker itself, like running in terminal:

```bash
docker --help
docker ps
docker ps --help
docker pull polkas/rdevdash-app:latest
docker images
docker run -p 3838:3838 polkas/rdevdash-app:latest
docker stop $(docker ps -a -q)

docker build examples/py-shiny-app/ -t py-shiny-app && docker images
docker run -p 3839:3839 py-shiny-app
```

or you can reuse already existing images for Data Science.  
Example of images from Jupyter.  
[Here is the list of jupyter images with descriptions](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)

```bash

# https://quay.io/repository/jupyter/datascience-notebook
# You can use specific tag (version)
# docker run -p 8888:8888 quay.io/jupyter/datascience-notebook:2024-12-31
docker run -p 8888:8888 quay.io/jupyter/datascience-notebook

# https://quay.io/repository/jupyter/scipy-notebook
# You can use specific tag (version)
# docker run -p 8888:8888 quay.io/jupyter/scipy-notebook:2024-12-31
docker run -p 8888:8888 quay.io/jupyter/scipy-notebook

```

## Examples

More challenging is to try to understand and work with Dockerfiles in examples.

### Python Shiny App

- Path: `examples/py-shiny-app`
- Description: A simple Python Shiny app with a slider input and a plot output.
- Command to run: `docker compose up --build py-shiny-app `

Look for 3839 in the PORTS vscode tab

Press Control C in the terminal to close

### R Shiny App

- Path: `examples/r-shiny-app`
- Description: A simple R Shiny app with a slider input and a plot output.
- Command to run: `docker compose up --build r-shiny-app`

Look for 3838 in the PORTS vscode tab

Press Control C in the terminal to close

### Note 

The current setup runs Shiny and Py Shiny apps on the server side. 
The repository does not include any implementation for running Shiny apps using WebAssembly or Shiny Live on the client side.

### Jupyter scipy-notebook

- Path: `examples/jupyter`
- Description: An environment to run Jupyter.
- Command to run: `docker compose up --build jupyter`

Look for 8888 in the PORTS vscode tab, look for a token printed in the bottom of the terminal.

Press Control C in the terminal to close

### RStudio

- Path: `examples/rstudio`
- Description: An environment to run RStudio.
- Command to run: `docker compose up --build rstudio`

Look for 8787 in the PORTS vscode tab, Login: `rstudio` and Password: `rstudio`

Press Control C in the terminal to close

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

### Docker Compose

- Path: `docker-compose.yml`
- Description: A compose file to run all apps, including Shiny apps, JupyterLab, RStudio, at the same time.
- Command to run: `docker compose up` ; It can take more than 15+ minutes

## Continuous Integration with GitHub Actions

This project includes a GitHub Actions CI workflow to automate the build and run process for all examples. The workflow is located in the `.github/workflows/ci.yml` file. It sets up Docker, builds and runs each example, and verifies that they work correctly. The workflow run the all apps simultaneously by  `docker-compose.yml`.
