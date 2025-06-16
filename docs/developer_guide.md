# دليل المطور

هذا الدليل يقدم معلومات تفصيلية للمطورين الذين يرغبون في المساهمة في مشروع المساعد الذكي الشخصي للتداول.

## بنية المشروع التفصيلية

### مجلد `src/models`
يحتوي على نماذج قاعدة البيانات:
- `user.py`: نموذج بيانات المستخدم الأساسية
- `user_profile.py`: نموذج الملف الشخصي للمستخدم مع تفضيلات التداول

### مجلد `src/routes`
يحتوي على مسارات API والصفحات:
- `user.py`: مسارات إدارة المستخدمين
- `user_profile.py`: مسارات إدارة الملف الشخصي
- `market_data.py`: مسارات الوصول إلى بيانات السوق
- `sentiment.py`: مسارات تحليل المشاعر

### مجلد `src/services`
يحتوي على خدمات معالجة البيانات:
- `market_data_service.py`: خدمة جلب وتحليل بيانات السوق
- `recommendation_engine.py`: محرك التوصيات الذكي
- `sentiment_analysis_service.py`: خدمة تحليل مشاعر الأخبار المالية

### مجلد `src/static`
يحتوي على ملفات واجهة المستخدم:
- `index.html`: الصفحة الرئيسية
- `user_profile.html`: صفحة إدارة الملف الشخصي

## تكامل Binance التفصيلي

لإضافة تكامل Binance إلى المشروع، يمكن إنشاء الملفات التالية:

1. `src/services/binance_service.py`:
```python
from binance.client import Client
import os

class BinanceService:
    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key or os.environ.get('BINANCE_API_KEY')
        self.api_secret = api_secret or os.environ.get('BINANCE_API_SECRET')
        self.client = Client(self.api_key, self.api_secret)
    
    def get_account_info(self):
        return self.client.get_account()
    
    def get_ticker_price(self, symbol):
        return self.client.get_symbol_ticker(symbol=symbol)
    
    def place_order(self, symbol, side, order_type, quantity):
        return self.client.create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity
        )
```

2. `src/routes/binance_api.py`:
```python
from flask import Blueprint, request, jsonify
from src.services.binance_service import BinanceService

binance_bp = Blueprint('binance', __name__)
binance_service = BinanceService()

@binance_bp.route('/account', methods=['GET'])
def get_account_info():
    try:
        account_info = binance_service.get_account_info()
        return jsonify(account_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

## أفضل الممارسات للتطوير

1. **اختبار الكود**: كتابة اختبارات وحدة لكل وظيفة جديدة
2. **التوثيق**: توثيق جميع الدوال والفئات بتعليقات واضحة
3. **الأمان**: عدم تخزين مفاتيح API في الكود، استخدام متغيرات البيئة
4. **التنسيق**: اتباع معيار PEP 8 لتنسيق كود Python

## خطوات تطوير ميزة جديدة

1. تحديث نماذج قاعدة البيانات إذا لزم الأمر
2. إضافة خدمة جديدة في مجلد `services`
3. إنشاء مسارات API في مجلد `routes`
4. تحديث واجهة المستخدم في مجلد `static`
5. تحديث ملف `main.py` لتسجيل المسارات الجديدة
6. اختبار الميزة الجديدة
7. تحديث الوثائق
