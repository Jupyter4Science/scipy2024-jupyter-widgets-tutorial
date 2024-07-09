# Use the Jupyter SciPy notebook as the base image
FROM jupyter/scipy-notebook

# Define a build argument to pass the repository URL
ARG repourl

# Install additional packages and clone the specified repository
# - voila: A tool to convert Jupyter notebooks into standalone web applications
# - jupyterthemes: A set of custom themes for Jupyter notebooks
# - git clone: Clone the repository from the provided URL into the 'target' directory
RUN conda install -c conda-forge voila jupyterthemes \
    && git clone --depth 1 $repourl target

# Set the working directory to the cloned repository
WORKDIR /home/jovyan/target

# Define the default command to run when the container starts
# - voila: Serve the Jupyter notebook as a web application
# - notebook.ipynb: The notebook to be served
# - --no-browser: Do not open a web browser on the host machine
# - --Voila.ip: Bind the Voila server to all available IP addresses (0.0.0.0)
CMD ["voila", "notebook.ipynb", "--no-browser", "--Voila.ip", "0.0.0.0"]
