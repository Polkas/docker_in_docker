# Use the official Jupyter base image
FROM jupyter/base-notebook:latest

# Set working directory to /workspace
WORKDIR /workspace

# Install JupyterLab
RUN pip install jupyterlab

# Expose port 8888
EXPOSE 8888

# Command to start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
