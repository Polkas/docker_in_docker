# Use the official R base image
FROM r-base:latest

# Install Shiny package
RUN R -e "install.packages('shiny', repos='http://cran.rstudio.com/')"

# Copy application code to /app directory
COPY . /app

# Set working directory
WORKDIR /app

# Expose port 3838
EXPOSE 3838

# Command to run the Shiny app with specified host and port
CMD ["R", "-e", "shiny::runApp('/app', host='0.0.0.0', port=3838)"]
