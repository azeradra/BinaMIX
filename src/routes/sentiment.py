from flask import Blueprint, render_template, request, jsonify, session
from src.services.sentiment_analysis_service import sentiment_analysis_service

sentiment_bp = Blueprint('sentiment', __name__)

@sentiment_bp.route('/sentiment', methods=['GET'])
def sentiment_dashboard():
    """Render the sentiment analysis dashboard."""
    return render_template('sentiment.html')

@sentiment_bp.route('/api/sentiment/analyze-text', methods=['POST'])
def analyze_text():
    """API endpoint to analyze sentiment of text."""
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'})
    
    # Analyze sentiment
    sentiment = sentiment_analysis_service.analyze_sentiment(text)
    
    return jsonify(sentiment)

@sentiment_bp.route('/api/sentiment/asset-news', methods=['GET'])
def get_asset_news_sentiment():
    """API endpoint to get and analyze news for an asset."""
    symbol = request.args.get('symbol', '')
    limit = int(request.args.get('limit', 5))
    
    if not symbol:
        return jsonify({'error': 'No symbol provided'})
    
    # Get and analyze news
    result = sentiment_analysis_service.analyze_news_for_asset(symbol, limit)
    
    return jsonify(result)

@sentiment_bp.route('/api/sentiment/user-assets', methods=['GET'])
def get_user_assets_sentiment():
    """API endpoint to get sentiment for user's preferred assets."""
    # Check if user is in session (simplified for prototype)
    username = session.get('username', 'demo_user')
    
    # This would normally come from the database
    # For demo, we'll use some hardcoded assets
    assets = [
        {'symbol': 'AAPL', 'type': 'stock'},
        {'symbol': 'MSFT', 'type': 'stock'},
        {'symbol': 'GOOGL', 'type': 'stock'},
        {'symbol': 'BTC', 'type': 'crypto'},
        {'symbol': 'ETH', 'type': 'crypto'}
    ]
    
    # Get sentiment for each asset
    results = []
    
    for asset in assets:
        # Get only 3 news items per asset to avoid overloading
        sentiment_data = sentiment_analysis_service.analyze_news_for_asset(asset['symbol'], 3)
        
        if 'error' not in sentiment_data:
            # Simplify the response
            simplified = {
                'symbol': asset['symbol'],
                'type': asset['type'],
                'sentiment_score': sentiment_data['overall_sentiment']['score'],
                'sentiment_label': sentiment_data['overall_sentiment']['label'],
                'latest_news': sentiment_data['articles'][0] if sentiment_data['articles'] else None
            }
            results.append(simplified)
    
    return jsonify({'assets': results})
