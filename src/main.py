from flask import Flask, render_template, send_from_directory
import os

def create_app():
    app = Flask(__name__, static_folder='static')
   <!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>BinaMIX - المساعد الذكي للتداول</title>
</head>
<body>
    <h1>مرحبًا بك في BinaMIX!</h1>
    <p>نظام تداول ذكي يستخدم الذكاء الاصطناعي لتحليل الأسواق وتقديم التوصيات المالية.</p>
    <ul>
        <li>تحليل بيانات السوق بشكل مباشر</li>
        <li>توصيات تداول مخصصة</li>
        <li>تحليل مشاعر الأخبار المالية</li>
        <li>تكامل مع منصة Binance</li>
    </ul>
</body>
</html>
    from .auth import auth
app.register_blueprint(auth, url_prefix='/auth')
    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')
    
    @app.route('/profile')
    def profile():
        return send_from_directory(app.static_folder, 'user_profile.html')
    
    @app.route('/market-data')
    def market_data():
        return render_template('market_data.html', title="Données du marché")
    
    @app.route('/recommendations')
    def recommendations():
        return render_template('recommendations.html', title="Recommandations")
    
    @app.route('/sentiment')
    def sentiment():
        return render_template('sentiment.html', title="Analyse des sentiments")
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
