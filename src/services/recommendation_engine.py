import numpy as np
from datetime import datetime
from src.models.user_profile import UserProfile

class RecommendationEngine:
    """Basic recommendation engine for the trading assistant."""
    
    def __init__(self):
        # Define risk scores for different risk tolerance levels
        self.risk_scores = {
            'conservative': 1,
            'moderate': 2,
            'aggressive': 3
        }
        
        # Define time horizon scores
        self.time_horizon_scores = {
            'short': 1,
            'medium': 2,
            'long': 3
        }
        
        # Define goal type weights
        self.goal_weights = {
            'income': {'dividend': 0.7, 'growth': 0.2, 'volatility': 0.1},
            'growth': {'dividend': 0.1, 'growth': 0.7, 'volatility': 0.2},
            'balanced': {'dividend': 0.4, 'growth': 0.4, 'volatility': 0.2}
        }
        
        # Sample asset characteristics (in a real system, this would come from a database or API)
        # Format: {symbol: {'type': asset_type, 'dividend': score, 'growth': score, 'volatility': score}}
        self.asset_characteristics = {
            # Stocks
            'AAPL': {'type': 'stock', 'dividend': 1, 'growth': 3, 'volatility': 2},
            'MSFT': {'type': 'stock', 'dividend': 2, 'growth': 3, 'volatility': 2},
            'GOOGL': {'type': 'stock', 'dividend': 0, 'growth': 3, 'volatility': 2},
            'AMZN': {'type': 'stock', 'dividend': 0, 'growth': 3, 'volatility': 3},
            'META': {'type': 'stock', 'dividend': 0, 'growth': 2, 'volatility': 3},
            'TSLA': {'type': 'stock', 'dividend': 0, 'growth': 3, 'volatility': 3},
            'JNJ': {'type': 'stock', 'dividend': 3, 'growth': 1, 'volatility': 1},
            'PG': {'type': 'stock', 'dividend': 3, 'growth': 1, 'volatility': 1},
            'KO': {'type': 'stock', 'dividend': 3, 'growth': 1, 'volatility': 1},
            'VZ': {'type': 'stock', 'dividend': 3, 'growth': 1, 'volatility': 1},
            'DIS': {'type': 'stock', 'dividend': 1, 'growth': 2, 'volatility': 2},
            'NFLX': {'type': 'stock', 'dividend': 0, 'growth': 3, 'volatility': 3},
            'V': {'type': 'stock', 'dividend': 1, 'growth': 2, 'volatility': 2},
            'JPM': {'type': 'stock', 'dividend': 2, 'growth': 2, 'volatility': 2},
            'BAC': {'type': 'stock', 'dividend': 2, 'growth': 2, 'volatility': 2},
            
            # Cryptocurrencies
            'BTC': {'type': 'crypto', 'dividend': 0, 'growth': 3, 'volatility': 3},
            'ETH': {'type': 'crypto', 'dividend': 0, 'growth': 3, 'volatility': 3},
            'SOL': {'type': 'crypto', 'dividend': 0, 'growth': 3, 'volatility': 3},
            'ADA': {'type': 'crypto', 'dividend': 0, 'growth': 2, 'volatility': 3},
            'XRP': {'type': 'crypto', 'dividend': 0, 'growth': 2, 'volatility': 3},
            
            # ETFs
            'SPY': {'type': 'etf', 'dividend': 2, 'growth': 2, 'volatility': 2},
            'QQQ': {'type': 'etf', 'dividend': 1, 'growth': 3, 'volatility': 2},
            'VTI': {'type': 'etf', 'dividend': 2, 'growth': 2, 'volatility': 2},
            'SCHD': {'type': 'etf', 'dividend': 3, 'growth': 1, 'volatility': 1},
            'VYM': {'type': 'etf', 'dividend': 3, 'growth': 1, 'volatility': 1}
        }
        
        # Sector mapping
        self.sector_assets = {
            'technology': ['AAPL', 'MSFT', 'GOOGL', 'META', 'TSLA', 'QQQ'],
            'healthcare': ['JNJ', 'PFE', 'UNH'],
            'finance': ['JPM', 'BAC', 'V'],
            'consumer': ['AMZN', 'PG', 'KO', 'DIS', 'NFLX'],
            'energy': ['XOM', 'CVX'],
            'utilities': ['NEE', 'DUK'],
            'real_estate': ['AMT', 'PLD'],
            'industrial': ['HON', 'UPS']
        }
        
        # Market mapping
        self.market_assets = {
            'us_stocks': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'JNJ', 'PG', 'KO', 'VZ', 'DIS', 'NFLX', 'V', 'JPM', 'BAC', 'SPY', 'QQQ', 'VTI', 'SCHD', 'VYM'],
            'global_stocks': ['SPY', 'VTI'],
            'crypto': ['BTC', 'ETH', 'SOL', 'ADA', 'XRP'],
            'forex': [],
            'commodities': []
        }
    
    def generate_recommendations(self, user_profile):
        """Generate investment recommendations based on user profile."""
        if not user_profile:
            return {
                'error': 'User profile not found',
                'timestamp': datetime.now().isoformat()
            }
        
        # Extract user preferences
        risk_tolerance = user_profile.risk_tolerance
        time_horizon = user_profile.time_horizon
        goal_type = user_profile.goal_type
        preferred_markets = user_profile.preferred_markets.split(',') if user_profile.preferred_markets else []
        preferred_sectors = user_profile.preferred_sectors.split(',') if user_profile.preferred_sectors else []
        
        # Get risk score
        risk_score = self.risk_scores.get(risk_tolerance, 2)
        
        # Get time horizon score
        time_score = self.time_horizon_scores.get(time_horizon, 2)
        
        # Get goal weights
        weights = self.goal_weights.get(goal_type, self.goal_weights['balanced'])
        
        # Filter assets based on user preferences
        candidate_assets = set()
        
        # Add assets from preferred markets
        for market in preferred_markets:
            if market in self.market_assets:
                candidate_assets.update(self.market_assets[market])
        
        # Add assets from preferred sectors
        for sector in preferred_sectors:
            if sector in self.sector_assets:
                candidate_assets.update(self.sector_assets[sector])
        
        # If no preferences specified, include all assets
        if not candidate_assets:
            for assets in self.market_assets.values():
                candidate_assets.update(assets)
        
        # Score each asset
        asset_scores = {}
        for symbol in candidate_assets:
            if symbol in self.asset_characteristics:
                asset = self.asset_characteristics[symbol]
                
                # Calculate weighted score
                score = (
                    weights['dividend'] * asset['dividend'] +
                    weights['growth'] * asset['growth'] -
                    weights['volatility'] * abs(asset['volatility'] - risk_score)
                )
                
                # Adjust for time horizon
                if time_score == 1:  # Short term
                    score -= asset['volatility'] * 0.5  # Penalize volatility for short term
                elif time_score == 3:  # Long term
                    score += asset['growth'] * 0.5  # Reward growth for long term
                
                asset_scores[symbol] = score
        
        # Sort assets by score
        sorted_assets = sorted(asset_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Create portfolio allocation
        portfolio = []
        total_score = sum(score for _, score in sorted_assets[:10]) if sorted_assets else 1
        
        for symbol, score in sorted_assets[:10]:  # Top 10 assets
            allocation = round((score / total_score) * 100, 2)
            asset_type = self.asset_characteristics[symbol]['type']
            
            portfolio.append({
                'symbol': symbol,
                'allocation': allocation,
                'type': asset_type,
                'score': round(score, 2)
            })
        
        # Generate explanation
        explanation = self._generate_explanation(user_profile, portfolio)
        
        return {
            'portfolio': portfolio,
            'explanation': explanation,
            'timestamp': datetime.now().isoformat()
        }
    
    def _generate_explanation(self, user_profile, portfolio):
        """Generate human-readable explanation for recommendations."""
        risk_level = user_profile.risk_tolerance
        time_horizon = user_profile.time_horizon
        goal_type = user_profile.goal_type
        
        # Count asset types
        asset_types = {}
        for item in portfolio:
            asset_type = item['type']
            if asset_type in asset_types:
                asset_types[asset_type] += 1
            else:
                asset_types[asset_type] = 1
        
        # Generate explanation
        explanation = f"Based on your {risk_level} risk tolerance, {time_horizon} time horizon, and focus on {goal_type}, "
        
        if goal_type == 'income':
            explanation += "we've prioritized assets with strong dividend potential. "
        elif goal_type == 'growth':
            explanation += "we've prioritized assets with strong growth potential. "
        else:
            explanation += "we've balanced income and growth potential. "
        
        explanation += f"Your recommended portfolio includes "
        
        asset_descriptions = []
        for asset_type, count in asset_types.items():
            asset_descriptions.append(f"{count} {asset_type}{'s' if count > 1 else ''}")
        
        explanation += ", ".join(asset_descriptions) + ". "
        
        if risk_level == 'conservative':
            explanation += "The allocation favors stability and lower volatility."
        elif risk_level == 'aggressive':
            explanation += "The allocation embraces higher volatility for potential higher returns."
        else:
            explanation += "The allocation balances risk and potential returns."
        
        return explanation

# Create a singleton instance
recommendation_engine = RecommendationEngine()
