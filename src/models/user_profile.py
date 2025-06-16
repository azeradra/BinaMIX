from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class UserProfile(db.Model):
    """Model for storing user profile information for the trading assistant."""
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    
    # Financial goals
    goal_type = db.Column(db.String(20), nullable=False)  # 'income', 'growth', 'balanced'
    time_horizon = db.Column(db.String(20), nullable=False)  # 'short', 'medium', 'long'
    
    # Risk profile
    risk_tolerance = db.Column(db.String(20), nullable=False)  # 'conservative', 'moderate', 'aggressive'
    max_drawdown = db.Column(db.Integer, nullable=True)  # Maximum acceptable drawdown percentage
    
    # Preferences
    preferred_markets = db.Column(db.String(255), nullable=True)  # Comma-separated list
    preferred_sectors = db.Column(db.String(255), nullable=True)  # Comma-separated list
    preferred_assets = db.Column(db.String(255), nullable=True)  # Comma-separated list
    
    # Additional settings
    investment_amount = db.Column(db.Float, nullable=True)
    monthly_contribution = db.Column(db.Float, nullable=True)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<UserProfile {self.username}>'
    
    def to_dict(self):
        """Convert user profile to dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'goal_type': self.goal_type,
            'time_horizon': self.time_horizon,
            'risk_tolerance': self.risk_tolerance,
            'max_drawdown': self.max_drawdown,
            'preferred_markets': self.preferred_markets.split(',') if self.preferred_markets else [],
            'preferred_sectors': self.preferred_sectors.split(',') if self.preferred_sectors else [],
            'preferred_assets': self.preferred_assets.split(',') if self.preferred_assets else [],
            'investment_amount': self.investment_amount,
            'monthly_contribution': self.monthly_contribution,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
