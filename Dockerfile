# Use an appropriate base image for your application
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install system-level dependencies
RUN apt-get update && apt-get install -y portaudio19-dev 

# Create a virtual environment named myenv
RUN python3 -m venv /myenv

# Set environment variables for the virtual environment
ENV VIRTUAL_ENV /myenv
ENV PATH /myenv/bin:$PATH

# Install dependencies from requirements.txt
COPY requirements.txt /app/
RUN /myenv/bin/pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set the entrypoint to run your Streamlit application
ENTRYPOINT [ "/myenv/bin/streamlit", "run", "/app/home.py", "--server.port", "8080" ]
