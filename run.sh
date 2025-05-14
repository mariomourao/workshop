#!/bin/bash

# Install dependencies if needed
if [ ! -d ".venv" ]; then
  echo "Setting up Poetry virtual environment..."
  poetry install
fi

# Run the API
echo "Starting FastAPI application..."
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 