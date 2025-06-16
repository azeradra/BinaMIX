import requests
import os
from datetime import datetime
import json

class MarketDataService:
    """Service for fetching market data from free APIs."""
    
    def __init__(self):
        # Alpha Vantage API key (free tier)
        self.alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY', 'demo')
        
        # Finnhub API key (free tier)
        self.finnhub_api_key = os.getenv('FINNHUB_API_KEY', 'sandbox')
        
        # Base URLs
        self.alpha_vantage_base_url = 'https://www.alphavantage.co/query'
        self.finnhub_base_url = 'https://finnhub.io/api/v1'
        
        # Cache to minimize API calls (simple in-memory cache)
        self.cache = {}
        self.cache_expiry = 300  # 5 minutes in seconds
    
    def get_stock_quote(self, symbol):
        """Get current stock quote from Alpha Vantage."""
        cache_key = f'stock_quote_{symbol}'
        
        # Check cache first
        cached_data = self._get_from_cache(cache_key)
        if cached_data:
            return cached_data
        
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': self.alpha_vantage_api_key
        }
        
        try:
            response = requests.get(self.alpha_vantage_base_url, params=params)
            data = response.json()
            
            if 'Global Quote' in data and data['Global Quote']:
                result = {
                    'symbol': data['Global Quote']['01. symbol'],
                    'price': float(data['Global Quote']['05. price']),
                    'change': float(data['Global Quote']['09. change']),
                    'change_percent': data['Global Quote']['10. change percent'],
                    'volume': int(data['Global Quote']['06. volume']),
                    'latest_trading_day': data['Global Quote']['07. latest trading day'],
                    'timestamp': datetime.now().isoformat()
                }
                
                # Save to cache
                self._save_to_cache(cache_key, result)
                
                return result
            else:
                return {'error': 'No data found or API limit reached', 'raw_response': data}
        
        except Exception as e:
            return {'error': str(e)}
    
    def get_stock_intraday(self, symbol, interval='5min', limit=100):
        """Get intraday stock data from Alpha Vantage."""
        cache_key = f'stock_intraday_{symbol}_{interval}_{limit}'
        
        # Check cache first
        cached_data = self._get_from_cache(cache_key)
        if cached_data:
            return cached_data
        
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': interval,
            'outputsize': 'compact',
            'apikey': self.alpha_vantage_api_key
        }
        
        try:
            response = requests.get(self.alpha_vantage_base_url, params=params)
            data = response.json()
            
            time_series_key = f'Time Series ({interval})'
            
            if time_series_key in data:
                # Convert to list format for easier consumption by frontend
                time_series = data[time_series_key]
                result = []
                
                for timestamp, values in time_series.items():
                    point = {
                        'timestamp': timestamp,
                        'open': float(values['1. open']),
                        'high': float(values['2. high']),
                        'low': float(values['3. low']),
                        'close': float(values['4. close']),
                        'volume': int(values['5. volume'])
                    }
                    result.append(point)
                
                # Sort by timestamp (newest first) and limit
                result.sort(key=lambda x: x['timestamp'], reverse=True)
                result = result[:limit]
                
                output = {
                    'symbol': symbol,
                    'interval': interval,
                    'data': result,
                    'timestamp': datetime.now().isoformat()
                }
                
                # Save to cache
                self._save_to_cache(cache_key, output)
                
                return output
            else:
                return {'error': 'No data found or API limit reached', 'raw_response': data}
        
        except Exception as e:
            return {'error': str(e)}
    
    def get_crypto_price(self, symbol='BTC', currency='USD'):
        """Get current cryptocurrency price from Alpha Vantage."""
        cache_key = f'crypto_price_{symbol}_{currency}'
        
        # Check cache first
        cached_data = self._get_from_cache(cache_key)
        if cached_data:
            return cached_data
        
        params = {
            'function': 'CURRENCY_EXCHANGE_RATE',
            'from_currency': symbol,
            'to_currency': currency,
            'apikey': self.alpha_vantage_api_key
        }
        
        try:
            response = requests.get(self.alpha_vantage_base_url, params=params)
            data = response.json()
            
            if 'Realtime Currency Exchange Rate' in data:
                exchange_data = data['Realtime Currency Exchange Rate']
                result = {
                    'from_currency': exchange_data['1. From_Currency Code'],
                    'to_currency': exchange_data['3. To_Currency Code'],
                    'exchange_rate': float(exchange_data['5. Exchange Rate']),
                    'last_refreshed': exchange_data['6. Last Refreshed'],
                    'timezone': exchange_data['7. Time Zone'],
                    'timestamp': datetime.now().isoformat()
                }
                
                # Save to cache
                self._save_to_cache(cache_key, result)
                
                return result
            else:
                return {'error': 'No data found or API limit reached', 'raw_response': data}
        
        except Exception as e:
            return {'error': str(e)}
    
    def search_symbol(self, query):
        """Search for symbols using Alpha Vantage."""
        cache_key = f'symbol_search_{query}'
        
        # Check cache first
        cached_data = self._get_from_cache(cache_key)
        if cached_data:
            return cached_data
        
        params = {
            'function': 'SYMBOL_SEARCH',
            'keywords': query,
            'apikey': self.alpha_vantage_api_key
        }
        
        try:
            response = requests.get(self.alpha_vantage_base_url, params=params)
            data = response.json()
            
            if 'bestMatches' in data:
                result = {
                    'query': query,
                    'results': data['bestMatches'],
                    'timestamp': datetime.now().isoformat()
                }
                
                # Save to cache
                self._save_to_cache(cache_key, result)
                
                return result
            else:
                return {'error': 'No data found or API limit reached', 'raw_response': data}
        
        except Exception as e:
            return {'error': str(e)}
    
    def get_company_profile(self, symbol):
        """Get company profile from Finnhub (if API key is available)."""
        if self.finnhub_api_key == 'sandbox':
            return {'error': 'Finnhub API key not configured'}
        
        cache_key = f'company_profile_{symbol}'
        
        # Check cache first
        cached_data = self._get_from_cache(cache_key)
        if cached_data:
            return cached_data
        
        headers = {
            'X-Finnhub-Token': self.finnhub_api_key
        }
        
        url = f'{self.finnhub_base_url}/stock/profile2'
        params = {
            'symbol': symbol
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            
            if data and 'name' in data:
                # Add timestamp
                data['timestamp'] = datetime.now().isoformat()
                
                # Save to cache
                self._save_to_cache(cache_key, data)
                
                return data
            else:
                return {'error': 'No data found or API limit reached', 'raw_response': data}
        
        except Exception as e:
            return {'error': str(e)}
    
    def _save_to_cache(self, key, data):
        """Save data to cache with timestamp."""
        self.cache[key] = {
            'data': data,
            'timestamp': datetime.now().timestamp()
        }
    
    def _get_from_cache(self, key):
        """Get data from cache if not expired."""
        if key in self.cache:
            cache_entry = self.cache[key]
            current_time = datetime.now().timestamp()
            
            # Check if cache is still valid
            if current_time - cache_entry['timestamp'] < self.cache_expiry:
                return cache_entry['data']
        
        return None

# Create a singleton instance
market_data_service = MarketDataService()
