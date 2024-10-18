FROM python:3.9-slim

# Set the working directory in the container to /home
WORKDIR /home

# Copy the script and data files to /home
COPY scripts.py /home/scripts.py
COPY home/data/ /home/data/

# Run the Python script when the container starts
CMD ["python", "/home/scripts.py"]