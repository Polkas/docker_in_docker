# Use the official RStudio base image
FROM rocker/rstudio:latest

# Set working directory to /workspace
WORKDIR /workspace

# Expose port 8787
EXPOSE 8787

# Install Python
RUN apt-get update && apt-get install -y python3

# Add environment variables for RStudio login and password
# The user-pw-list.txt file contains a list of users and their passwords
COPY user-pw-list.txt /etc/rstudio/user-pw-list.txt
COPY add_users.py /etc/rstudio/add_users.py
RUN python3 /etc/rstudio/add_users.py

COPY testdir /home/rstudio/testdir
VOLUME /home/rstudio/testdir

# Command to start RStudio
CMD ["rserver", "--server-daemonize", "0"]
