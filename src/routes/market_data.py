from flask import Blueprint, render_template, request, jsonify, session
from src.services.market_data_service import market_data_service

market_data_bp = Blueprint('market_data', __name__)

@market_data_bp.route('/market-data', methods=['GET'])
def market_data_dashboard():
    """Render the market data dashboard."""
    return render_template('market_data.html')

@market_data_bp.route('/api/market-data/stock-quote', methods=['GET'])
def get_stock_quote():
    """API endpoint to get stock quote."""
    symbol = request.args.get('symbol', 'AAPL')
    
    # Get data from service
    data = market_data_service.get_stock_quote(symbol)
    
    return jsonify(data)

@market_data_bp.route('/api/market-data/stock-intraday', methods=['GET'])
def get_stock_intraday():
    """API endpoint to get intraday stock data."""
    symbol = request.args.get('symbol', 'AAPL')
    interval = request.args.get('interval', '5min')
    limit = int(request.args.get('limit', 100))
    
    # Get data from service
    data = market_data_service.get_stock_intraday(symbol, interval, limit)
    
    return jsonify(data)

@market_data_bp.route('/api/market-data/crypto-price', methods=['GET'])
def get_crypto_price():
    """API endpoint to get cryptocurrency price."""
    symbol = request.args.get('symbol', 'BTC')
    currency = request.args.get('currency', 'USD')
    
    # Get data from service
    data = market_data_service.get_crypto_price(symbol, currency)
    
    return jsonify(data)

@market_data_bp.route('/api/market-data/search-symbol', methods=['GET'])
def search_symbol():
    """API endpoint to search for symbols."""
    query = request.args.get('query', '')
    
    if not query or len(query) < 2:
        return jsonify({'error': 'Query too short'})
    
    # Get data from service
    data = market_data_service.search_symbol(query)
    
    return jsonify(data)

@market_data_bp.route('/api/market-data/user-assets', methods=['GET'])
def get_user_assets():
    """API endpoint to get data for user's preferred assets."""
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
    
    # Get data for each asset
    results = []
    
    for asset in assets:
        if asset['type'] == 'stock':
            data = market_data_service.get_stock_quote(asset['symbol'])
        elif asset['type'] == 'crypto':
            data = market_data_service.get_crypto_price(asset['symbol'])
        else:
            continue
        
        if 'error' not in data:
            results.append(data)
    
    return jsonify({'assets': results})
