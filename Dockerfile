# Use Python 3.9 as base image (stable version that's widely available)
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    build-essential \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Create a non-root user to run the application
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

# Default command - run in interactive mode (can be overridden with command line arguments)
ENTRYPOINT ["python", "-m", "cli.main"]
CMD ["analyze"]

# Usage Instructions:
# Build the image:
# docker build -t stockinsighter .
#
# Run in interactive mode:
# docker run -it --rm \
#   -e FINNHUB_API_KEY=your_key \
#   -e OPENAI_API_KEY=your_key \
#   -e ANTHROPIC_API_KEY=your_key \
#   stockinsighter
#
# Run with command-line arguments:
# docker run -it --rm \
#   -e FINNHUB_API_KEY=your_key \
#   -e OPENAI_API_KEY=your_key \
#   stockinsighter run AAPL --analysts market,fundamentals --depth 2
#
# Save results to local directory:
# docker run -it --rm \
#   -e FINNHUB_API_KEY=your_key \
#   -e OPENAI_API_KEY=your_key \
#   -v $(pwd)/results:/app/results \
#   stockinsighter run TSLA --analysts market,news --depth 3
