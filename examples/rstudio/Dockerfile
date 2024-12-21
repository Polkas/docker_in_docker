# Use the official RStudio base image
FROM rocker/rstudio:latest

# Set working directory to /workspace
WORKDIR /workspace

# Expose port 8787
EXPOSE 8787

# Add environment variables for RStudio login and password
COPY user-pw-list.txt /etc/rstudio/user-pw-list.txt
COPY add_users.py /etc/rstudio/add_users.py
RUN python /etc/rstudio/add_users.py

# Command to start RStudio
CMD ["rserver", "--server-daemonize", "0"]
