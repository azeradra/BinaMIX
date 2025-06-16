import requests
import re
from datetime import datetime
from textblob import TextBlob
import os

class SentimentAnalysisService:
    """Simple sentiment analysis service for financial news."""
    
    def __init__(self):
        # News API key (free tier)
        self.news_api_key = os.getenv('NEWS_API_KEY', 'demo')
        
        # Base URL for News API
        self.news_api_base_url = 'https://newsapi.org/v2'
        
        # Positive and negative financial terms for basic keyword analysis
        self.positive_terms = [
            'growth', 'profit', 'surge', 'rise', 'gain', 'positive', 'up', 'bullish',
            'outperform', 'beat', 'exceed', 'strong', 'opportunity', 'recovery',
            'upgrade', 'innovation', 'partnership', 'launch', 'success'
        ]
        
        self.negative_terms = [
            'loss', 'decline', 'drop', 'fall', 'negative', 'down', 'bearish',
            'underperform', 'miss', 'weak', 'risk', 'concern', 'warning',
            'downgrade', 'layoff', 'cut', 'debt', 'bankruptcy', 'investigation'
        ]
        
        # Cache to minimize API calls
        self.cache = {}
        self.cache_expiry = 1800  # 30 minutes in seconds
    
    def get_news(self, query, limit=10):
        """Get news articles for a given query."""
        cache_key = f'news_{query}_{limit}'
        
        # Check cache first
        cached_data = self._get_from_cache(cache_key)
        if cached_data:
            return cached_data
        
        # If we don't have a News API key, use a mock response
        if self.news_api_key == 'demo':
            return self._get_mock_news(query, limit)
        
        params = {
            'q': query,
            'apiKey': self.news_api_key,
            'language': 'en',
            'sortBy': 'publishedAt',
            'pageSize': limit
        }
        
        try:
            response = requests.get(f'{self.news_api_base_url}/everything', params=params)
            data = response.json()
            
            if 'articles' in data:
                result = {
                    'query': query,
                    'articles': data['articles'],
                    'timestamp': datetime.now().isoformat()
                }
                
                # Save to cache
                self._save_to_cache(cache_key, result)
                
                return result
            else:
                return {'error': 'No articles found or API limit reached', 'raw_response': data}
        
        except Exception as e:
            return {'error': str(e)}
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of a text using TextBlob and keyword analysis."""
        if not text:
            return {
                'score': 0,
                'label': 'neutral',
                'confidence': 0
            }
        
        # Use TextBlob for sentiment analysis
        blob = TextBlob(text)
        textblob_polarity = blob.sentiment.polarity
        textblob_subjectivity = blob.sentiment.subjectivity
        
        # Count positive and negative keywords
        text_lower = text.lower()
        positive_count = sum(1 for term in self.positive_terms if term in text_lower)
        negative_count = sum(1 for term in self.negative_terms if term in text_lower)
        
        # Calculate keyword-based sentiment
        total_keywords = positive_count + negative_count
        keyword_polarity = 0
        if total_keywords > 0:
            keyword_polarity = (positive_count - negative_count) / total_keywords
        
        # Combine TextBlob and keyword analysis (weighted average)
        combined_score = (textblob_polarity * 0.7) + (keyword_polarity * 0.3)
        
        # Determine sentiment label
        if combined_score > 0.2:
            label = 'positive'
        elif combined_score < -0.2:
            label = 'negative'
        else:
            label = 'neutral'
        
        # Calculate confidence based on subjectivity and keyword presence
        confidence = (textblob_subjectivity * 0.5) + (min(total_keywords / 10, 1) * 0.5)
        
        return {
            'score': round(combined_score, 2),
            'label': label,
            'confidence': round(confidence, 2),
            'details': {
                'textblob_polarity': round(textblob_polarity, 2),
                'textblob_subjectivity': round(textblob_subjectivity, 2),
                'positive_keywords': positive_count,
                'negative_keywords': negative_count
            }
        }
    
    def analyze_news_for_asset(self, symbol, limit=5):
        """Get and analyze news for a specific asset."""
        # Get news for the asset
        news_data = self.get_news(symbol, limit)
        
        if 'error' in news_data:
            return news_data
        
        # Analyze sentiment for each article
        articles_with_sentiment = []
        overall_sentiment_score = 0
        
        for article in news_data.get('articles', [])[:limit]:
            # Combine title and description for analysis
            text = f"{article.get('title', '')} {article.get('description', '')}"
            sentiment = self.analyze_sentiment(text)
            
            # Add sentiment to article
            article_with_sentiment = {
                'title': article.get('title', ''),
                'description': article.get('description', ''),
                'url': article.get('url', ''),
                'publishedAt': article.get('publishedAt', ''),
                'source': article.get('source', {}).get('name', ''),
                'sentiment': sentiment
            }
            
            articles_with_sentiment.append(article_with_sentiment)
            overall_sentiment_score += sentiment['score']
        
        # Calculate overall sentiment
        num_articles = len(articles_with_sentiment)
        if num_articles > 0:
            overall_sentiment_score /= num_articles
            
            if overall_sentiment_score > 0.2:
                overall_sentiment_label = 'positive'
            elif overall_sentiment_score < -0.2:
                overall_sentiment_label = 'negative'
            else:
                overall_sentiment_label = 'neutral'
        else:
            overall_sentiment_score = 0
            overall_sentiment_label = 'neutral'
        
        return {
            'symbol': symbol,
            'articles': articles_with_sentiment,
            'overall_sentiment': {
                'score': round(overall_sentiment_score, 2),
                'label': overall_sentiment_label
            },
            'timestamp': datetime.now().isoformat()
        }
    
    def _get_mock_news(self, query, limit=10):
        """Generate mock news data for demo purposes."""
        # Sample news templates
        positive_templates = [
            "{} Reports Strong Quarterly Earnings, Exceeding Expectations",
            "Analysts Upgrade {} with Positive Outlook for Coming Year",
            "{} Announces New Product Launch, Stock Surges",
            "Investors Bullish on {} Following Strategic Partnership Announcement",
            "{} Expands into New Markets, Growth Prospects Improve"
        ]
        
        negative_templates = [
            "{} Misses Earnings Expectations, Stock Falls",
            "Analysts Downgrade {} Citing Market Concerns",
            "{} Faces Regulatory Scrutiny, Investors Cautious",
            "Market Volatility Impacts {} Performance, Outlook Uncertain",
            "{} Announces Restructuring, Job Cuts Planned"
        ]
        
        neutral_templates = [
            "{} Holds Annual Shareholder Meeting, Discusses Future Plans",
            "{} CEO Interviewed on Market Trends and Company Strategy",
            "{} Releases Quarterly Report, In Line with Expectations",
            "Industry Report Includes {} in Market Analysis",
            "{} Participates in Industry Conference, Shares Insights"
        ]
        
        # Generate mock articles
        articles = []
        templates = positive_templates + negative_templates + neutral_templates
        
        for i in range(min(limit, len(templates))):
            template = templates[i]
            title = template.format(query)
            
            # Generate a description based on the title
            if "Strong" in title or "Upgrade" in title or "Surge" in title or "Bullish" in title or "Growth" in title:
                sentiment_type = "positive"
                description = f"Recent developments at {query} show promising signs for investors. Analysts point to strong fundamentals and positive market conditions."
            elif "Misses" in title or "Downgrade" in title or "Falls" in title or "Scrutiny" in title or "Cuts" in title:
                sentiment_type = "negative"
                description = f"Challenges continue for {query} as market conditions and internal factors create headwinds. Investors are advised to monitor developments closely."
            else:
                sentiment_type = "neutral"
                description = f"{query} continues to operate in a competitive market environment. Analysts maintain mixed opinions on future performance."
            
            # Create mock article
            article = {
                'title': title,
                'description': description,
                'url': f'https://example.com/news/{query.lower().replace(" ", "-")}-{i}',
                'publishedAt': datetime.now().isoformat(),
                'source': {
                    'name': ['Financial Times', 'Bloomberg', 'Reuters', 'CNBC', 'Wall Street Journal'][i % 5]
                }
            }
            
            articles.append(article)
        
        return {
            'query': query,
            'articles': articles,
            'timestamp': datetime.now().isoformat()
        }
    
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
sentiment_analysis_service = SentimentAnalysisService()
