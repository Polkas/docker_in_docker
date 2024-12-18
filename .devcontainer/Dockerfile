FROM rocker/r-ver:4.3.2

WORKDIR /workspace

COPY . /workspace

RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    && rm -rf /var/lib/apt/lists/*

# RUN Rscript -e "install.packages('renv'); renv::restore()"
