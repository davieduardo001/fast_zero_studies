# Build stage
FROM python:3.12-slim as builder

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only the files needed for dependency installation
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy installed dependencies from builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . /app
WORKDIR /app

# Install Poetry for development
RUN pip install --no-cache-dir poetry

# Install application dependencies
RUN poetry install --no-dev --no-interaction --no-root
