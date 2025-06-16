from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from src.models.user_profile import UserProfile, db

user_profile_bp = Blueprint('user_profile', __name__)

@user_profile_bp.route('/profile', methods=['GET'])
def profile():
    """Display user profile form or existing profile."""
    # Check if user is in session (simplified for prototype)
    username = session.get('username', 'demo_user')
    
    # Try to get existing profile
    profile = UserProfile.query.filter_by(username=username).first()
    
    # Define options for dropdowns
    goal_types = [
        {'value': 'income', 'label': 'Income Generation', 'description': 'Focus on regular income from investments'},
        {'value': 'growth', 'label': 'Capital Growth', 'description': 'Focus on long-term appreciation of capital'},
        {'value': 'balanced', 'label': 'Balanced', 'description': 'Balance between income and growth'}
    ]
    
    time_horizons = [
        {'value': 'short', 'label': 'Short Term (< 1 year)', 'description': 'For goals within the next year'},
        {'value': 'medium', 'label': 'Medium Term (1-5 years)', 'description': 'For mid-term financial goals'},
        {'value': 'long', 'label': 'Long Term (> 5 years)', 'description': 'For long-term wealth building'}
    ]
    
    risk_tolerances = [
        {'value': 'conservative', 'label': 'Conservative', 'description': 'Prioritize capital preservation'},
        {'value': 'moderate', 'label': 'Moderate', 'description': 'Balance between risk and return'},
        {'value': 'aggressive', 'label': 'Aggressive', 'description': 'Willing to accept higher volatility for potentially higher returns'}
    ]
    
    markets = [
        {'value': 'us_stocks', 'label': 'US Stocks'},
        {'value': 'global_stocks', 'label': 'Global Stocks'},
        {'value': 'crypto', 'label': 'Cryptocurrencies'},
        {'value': 'forex', 'label': 'Forex'},
        {'value': 'commodities', 'label': 'Commodities'}
    ]
    
    sectors = [
        {'value': 'technology', 'label': 'Technology'},
        {'value': 'healthcare', 'label': 'Healthcare'},
        {'value': 'finance', 'label': 'Finance'},
        {'value': 'consumer', 'label': 'Consumer'},
        {'value': 'energy', 'label': 'Energy'},
        {'value': 'utilities', 'label': 'Utilities'},
        {'value': 'real_estate', 'label': 'Real Estate'},
        {'value': 'industrial', 'label': 'Industrial'}
    ]
    
    return render_template(
        'user_profile.html',
        profile=profile,
        goal_types=goal_types,
        time_horizons=time_horizons,
        risk_tolerances=risk_tolerances,
        markets=markets,
        sectors=sectors
    )

@user_profile_bp.route('/profile', methods=['POST'])
def update_profile():
    """Create or update user profile."""
    # Check if user is in session (simplified for prototype)
    username = session.get('username', 'demo_user')
    
    # Get form data
    goal_type = request.form.get('goal_type')
    time_horizon = request.form.get('time_horizon')
    risk_tolerance = request.form.get('risk_tolerance')
    max_drawdown = request.form.get('max_drawdown')
    
    # Get multi-select values
    preferred_markets = ','.join(request.form.getlist('preferred_markets'))
    preferred_sectors = ','.join(request.form.getlist('preferred_sectors'))
    preferred_assets = request.form.get('preferred_assets', '')
    
    # Get investment details
    investment_amount = request.form.get('investment_amount')
    monthly_contribution = request.form.get('monthly_contribution')
    
    # Try to get existing profile
    profile = UserProfile.query.filter_by(username=username).first()
    
    if profile:
        # Update existing profile
        profile.goal_type = goal_type
        profile.time_horizon = time_horizon
        profile.risk_tolerance = risk_tolerance
        profile.max_drawdown = max_drawdown if max_drawdown else None
        profile.preferred_markets = preferred_markets
        profile.preferred_sectors = preferred_sectors
        profile.preferred_assets = preferred_assets
        profile.investment_amount = float(investment_amount) if investment_amount else None
        profile.monthly_contribution = float(monthly_contribution) if monthly_contribution else None
    else:
        # Create new profile
        profile = UserProfile(
            username=username,
            goal_type=goal_type,
            time_horizon=time_horizon,
            risk_tolerance=risk_tolerance,
            max_drawdown=max_drawdown if max_drawdown else None,
            preferred_markets=preferred_markets,
            preferred_sectors=preferred_sectors,
            preferred_assets=preferred_assets,
            investment_amount=float(investment_amount) if investment_amount else None,
            monthly_contribution=float(monthly_contribution) if monthly_contribution else None
        )
        db.session.add(profile)
    
    # Commit changes
    db.session.commit()
    
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('user_profile.profile'))

@user_profile_bp.route('/api/profile', methods=['GET'])
def get_profile_api():
    """API endpoint to get user profile as JSON."""
    # Check if user is in session (simplified for prototype)
    username = session.get('username', 'demo_user')
    
    # Try to get existing profile
    profile = UserProfile.query.filter_by(username=username).first()
    
    if not profile:
        return jsonify({'error': 'Profile not found'}), 404
    
    return jsonify(profile.to_dict())
