# FastAPI Workshop - GitHub CI/CD Demo

This project demonstrates how to set up a CI/CD pipeline with GitHub Actions for a FastAPI application.

## Features

- FastAPI application with 3 endpoints
- Poetry for dependency management
- Pytest for testing
- GitHub Actions for CI/CD pipeline with test, build, and deploy stages

## Setup

1. Install Poetry if you don't have it already:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```
   poetry install
   ```

3. Run the application locally:
   ```
   poetry run uvicorn app.main:app --reload
   ```

4. Access the API documentation at http://localhost:8000/docs

## Tests

Run tests with:
```
poetry run pytest
```

## CI/CD Pipeline

The GitHub Actions workflow includes:

1. **Test**: Runs the test suite
2. **Build**: Builds a Docker image
3. **Deploy**: Deploys the application

All stages are executed on the GitHub runner machine. 