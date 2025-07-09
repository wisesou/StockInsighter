LLM Models Supported in StockInsighter
Based on the code examination, StockInsighter supports multiple LLM providers and models:

Supported Providers
OpenAI
Default models: o4-mini (deep thinking) and gpt-4o-mini (quick thinking)
Other compatible models include GPT-4 variants like gpt-4o, gpt-4-turbo, and GPT-3.5 variants
Uses the ChatOpenAI integration
Anthropic
Compatible with Claude models like claude-3-opus, claude-3-sonnet, and claude-3-haiku
Uses the ChatAnthropic integration
Requires an Anthropic API key
Google
Compatible with Gemini models like gemini-2.0-flash, gemini-1.5-pro, and gemini-1.5-flash
Uses the ChatGoogleGenerativeAI integration
The default configuration in 
main.py
 actually uses Google models
OpenAI-Compatible APIs
Ollama: For running models locally
OpenRouter: For accessing various open and closed-source models
Configuration
The app configures LLMs through several key settings:

llm_provider: The provider to use (openai, anthropic, google, ollama, openrouter)
deep_think_llm: Model for complex reasoning tasks (debate, analysis)
quick_think_llm: Model for simpler, faster tasks
backend_url: API endpoint (for custom endpoints or proxies)
