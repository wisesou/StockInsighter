# Run with default settings for AAPL
python -m cli.main run AAPL

# Run analysis for TSLA with specific analyst types
python -m cli.main run TSLA --analysts market,fundamentals

# Run deep analysis (more debate rounds)
python -m cli.main run GOOG --depth 3

# Complete Examples with All Parameters

# Full example with all parameters
python -m cli.main run AAPL \
  --date 2025-07-08 \
  --analysts market,social,news,fundamentals \
  --depth 2 \
  --provider openai \
  --backend-url https://api.openai.com/v1 \
  --shallow gpt-4o-mini \
  --deep gpt-4o


# Full example with all parameters (Docker)
docker run -it --rm \
  -e FINNHUB_API_KEY=your_key \
  -e OPENAI_API_KEY=your_key \
  stockinsighter \
  python -m cli.main run AAPL \
  --date 2025-07-08 \
  --analysts market,social,news,fundamentals \
  --depth 2 \
  --provider openai \
  --backend-url https://api.openai.com/v1 \
  --shallow gpt-4o-mini \
  --deep gpt-4o


# Run in Docker with API keys
docker run -it --rm \
  -e FINNHUB_API_KEY=your_key \
  -e OPENAI_API_KEY=your_key \
  stockinsighter run AAPL --analysts market,fundamentals --depth 2

# Save results to local directory
docker run -it --rm \
  -e FINNHUB_API_KEY=your_key \
  -e OPENAI_API_KEY=your_key \
  -v $(pwd)/results:/app/results \
  stockinsighter run TSLA --analysts market,news --depth 3
