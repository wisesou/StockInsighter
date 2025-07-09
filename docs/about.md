StockInsighter: A Multi-Agent Framework for Financial Trading Analysis
Application Overview
StockInsighter is a sophisticated multi-agent framework designed to mirror the dynamics of real-world trading firms. It uses multiple specialized AI agents powered by large language models (LLMs) to collaboratively analyze financial markets and make trading decisions.

Core Structure
The application is organized into several specialized teams, each with specific roles:

Analyst Team:
Market Analyst: Evaluates technical indicators and price movements
Social Analyst: Analyzes social media sentiment about stocks
News Analyst: Monitors relevant news that might impact stock prices
Fundamentals Analyst: Examines company financials and performance metrics
Research Team:
Bull Researcher: Argues the positive investment case
Bear Researcher: Argues the negative investment case
Research Manager: Evaluates both perspectives and makes a recommendation
Trading Team:
Trader: Determines timing and magnitude of trades based on analysis
Risk Management Team:
Risky Analyst: Advocates for aggressive positions
Neutral Analyst: Takes a balanced perspective
Safe Analyst: Emphasizes caution and risk mitigation
Portfolio Manager:
Makes the final investment decision based on all inputs
How Input Is Handled
The application reads two primary inputs:

Ticker Symbol (e.g., "NVDA"): The stock to analyze
Analysis Date: The date for which to conduct the analysis
These inputs can be provided either:

Through the simple 
main.py
 script where they're hardcoded
Via the interactive CLI interface (python -m cli.main) that prompts for inputs
Additionally, users can configure:

Which analysts to include in the analysis
Research depth (number of debate rounds)
LLM models to use (for deep thinking vs. quick thinking)
Whether to use online tools for real-time data or rely on cached data
Behind the Scenes
Under the hood, StockInsighter:

Creates a graph of specialized agents using LangGraph
Retrieves financial data through various tools (from APIs or cached data)
Orchestrates debates between agents with different perspectives
Generates detailed reports from each analytical angle
Produces a final investment recommendation
The framework uses a state-based propagation system where each agent adds their analysis to a growing state object that gets passed through the agent network.

Summary
StockInsighter demonstrates the power of specialized AI agents working together to tackle complex financial analysis. By decomposing trading decisions into specialized roles, it provides a comprehensive framework for market analysis that incorporates multiple perspectives, data sources, and risk assessments before reaching a final investment decision.
