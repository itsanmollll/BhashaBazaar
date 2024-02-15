FROM python:3.9
# Create a virtual environment named myenv
RUN virtualenv /myenv -p python3

# Set environment variables for the virtual environment
ENV VIRTUAL_ENV /myenv
ENV PATH /myenv/bin:$PATH

# Install dependencies from requirements.txt

ADD requirements.txt /app/
RUN apt-get update && apt-get install -y portaudio19-dev 
RUN /myenv/bin/pip install -r /app/requirements.txt

# Copy the rest of the application code
ADD . /app

# Set the entrypoint to run your Streamlit application
ENTRYPOINT [ "/myenv/bin/streamlit", "run", "/app/home.py", "--server.port", "8080" ]
