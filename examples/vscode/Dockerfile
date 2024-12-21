# Use the official VSCode base image
FROM codercom/code-server:latest

# Set working directory to /workspace
WORKDIR /workspace

# Expose port 8080
EXPOSE 8080

# Command to start VSCode
CMD ["code-server", "--bind-addr", "0.0.0.0:8080"]
