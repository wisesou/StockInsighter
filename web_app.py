from flask import Flask, request, jsonify, render_template
import os
import json
from datetime import datetime
from cli.main import run_analysis_with_selections
import threading

app = Flask(__name__)
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

# Ensure results directory exists
os.makedirs(RESULTS_DIR, exist_ok=True)

@app.route('/')
def index():
    """Render the main page with a form to submit analysis requests"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Handle stock analysis requests"""
    data = request.json
    ticker = data.get('ticker', '').upper()
    
    if not ticker:
        return jsonify({'error': 'No ticker symbol provided'}), 400
    
    # Prepare selections based on request data
    selections = {
        'ticker': ticker,
        'date': data.get('date', datetime.now().strftime('%Y-%m-%d')),
        'analysts': data.get('analysts', 'market,fundamentals,social,news'),
        'research_depth': int(data.get('research_depth', 1)),
        'llm_provider': data.get('llm_provider', 'openai'),
        'backend_url': data.get('backend_url', 'https://api.openai.com/v1'),
        'shallow_thinker': data.get('shallow_thinker', 'gpt-4o-mini'),
        'deep_thinker': data.get('deep_thinker', 'gpt-4o')
    }
    
    # Start analysis in background thread
    thread = threading.Thread(target=run_background_analysis, args=(selections,))
    thread.daemon = True
    thread.start()
    
    return jsonify({
        'status': 'Analysis started',
        'ticker': ticker,
        'check_status_url': f'/status/{ticker}'
    })

def run_background_analysis(selections):
    """Run analysis in background thread"""
    try:
        run_analysis_with_selections(selections)
    except Exception as e:
        print(f"Error running analysis: {str(e)}")

@app.route('/status/<ticker>')
def status(ticker):
    """Check the status of an analysis"""
    ticker = ticker.upper()
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Check if results directory exists
    ticker_dir = os.path.join(RESULTS_DIR, ticker, today)
    if not os.path.exists(ticker_dir):
        return jsonify({
            'ticker': ticker,
            'status': 'not_found',
            'message': f'No analysis found for {ticker} on {today}'
        })
    
    # Check for final trade decision file
    final_decision_path = os.path.join(ticker_dir, 'reports', 'final_trade_decision.md')
    if os.path.exists(final_decision_path):
        with open(final_decision_path, 'r') as file:
            content = file.read()
        return jsonify({
            'ticker': ticker,
            'status': 'complete',
            'result_url': f'/results/{ticker}',
            'summary': content[:500] + '...' if len(content) > 500 else content
        })
    
    # If we have a message_tool.log but no final decision, analysis is in progress
    log_file = os.path.join(ticker_dir, 'message_tool.log')
    if os.path.exists(log_file):
        return jsonify({
            'ticker': ticker,
            'status': 'in_progress',
            'message': 'Analysis is currently running'
        })
    
    return jsonify({
        'ticker': ticker,
        'status': 'unknown',
        'message': 'Status unknown'
    })

@app.route('/results/<ticker>')
def results(ticker):
    """Get all results for a ticker"""
    ticker = ticker.upper()
    today = datetime.now().strftime('%Y-%m-%d')
    
    ticker_dir = os.path.join(RESULTS_DIR, ticker, today, 'reports')
    if not os.path.exists(ticker_dir):
        return jsonify({
            'error': f'No results found for {ticker} on {today}'
        }), 404
    
    results = {}
    for report_file in os.listdir(ticker_dir):
        if report_file.endswith('.md'):
            report_path = os.path.join(ticker_dir, report_file)
            with open(report_path, 'r') as file:
                results[report_file] = file.read()
    
    return jsonify({
        'ticker': ticker,
        'date': today,
        'reports': results
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
