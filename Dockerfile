FROM python:3.9-slim

WORKDIR /app

# Install poetry
RUN pip install poetry==1.7.0

# Copy poetry configuration files
COPY pyproject.toml poetry.lock* /app/

# Configure poetry to not use a virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev

# Copy application code
COPY . /app/

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 