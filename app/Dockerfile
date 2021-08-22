FROM python:3
# Set application working directory
WORKDIR /app
# Install requirements
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Install application
COPY app.py /app

# Run application
ENTRYPOINT ["python3"]
CMD ["app.py"]