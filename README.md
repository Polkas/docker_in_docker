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

### VSCode

- Path: `examples/vscode`
- Description: An environment to run VSCode.
- Command to run: `docker build -t vscode examples/vscode && docker run -p 8080:8080 vscode`

### Docker Compose for Shiny Apps

- Path: `docker-compose.yml`
- Description: A compose file to run both shiny apps, one in R and one in Python, at the same time.
- Command to run: `docker-compose up`
