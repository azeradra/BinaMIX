# المساعد الذكي الشخصي للتداول (BinaMIX)

![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/language-Python-blue)

نظام متكامل للتداول الذكي يجمع بين تحليل البيانات المالية وتقنيات الذكاء الاصطناعي لتقديم توصيات تداول مخصصة.

## صورة توضيحية
> يمكنك إضافة صورة لشاشة التطبيق هنا (screenshot.png).

## المزايا الرئيسية
- ملف المستخدم الشخصي: إدارة أهداف المستخدم ومستوى المخاطر.
- بيانات السوق الحية: عرض بيانات مباشرة للأسهم والعملات المشفرة.
- محرك توصيات ذكي: توصيات استثمارية مخصصة.
- تحليل مشاعر الأخبار المالية.
- تكامل مع Binance للتداول الآلي.

## التثبيت والتشغيل
1. أنشئ بيئة افتراضية:
    ```bash
    python -m venv venv
    source venv/bin/activate  # لينكس/ماك
    venv\Scripts\activate     # ويندوز
    ```
2. ثبت المتطلبات:
    ```bash
    pip install -r requirements.txt
    ```
3. حمل بيانات NLTK:
    ```bash
    python -c "import nltk; nltk.download('punkt')"
    ```
4. شغل التطبيق:
    ```bash
    python -m src.main
    ```
5. تصفح التطبيق:
    ```
    http://localhost:5000
    ```

## المساهمة
انظر [CONTRIBUTING.md](CONTRIBUTING.md).

## الأمان
انظر [SECURITY.md](SECURITY.md).

## الرخصة
[MIT](LICENSE)

# المساعد الذكي الشخصي للتداول

نظام متكامل للتداول الذكي يجمع بين تحليل البيانات المالية وتقنيات الذكاء الاصطناعي لتقديم توصيات تداول مخصصة.

## الميزات الرئيسية

- **ملف المستخدم الشخصي**: إنشاء وإدارة ملف تعريفي يتضمن أهداف المستخدم المالية ومستوى تحمل المخاطر
- **بيانات السوق الحية**: عرض بيانات مباشرة للأسهم والعملات المشفرة من خلال واجهات برمجة تطبيقات مجانية
- **محرك توصيات ذكي**: تقديم توصيات استثمارية مخصصة بناءً على الملف الشخصي وظروف السوق
- **تحليل مشاعر الأخبار**: تحليل الأخبار المالية لتقييم تأثيرها المحتمل على الاستثمارات
- **تكامل مع Binance**: إمكانية الربط مع منصة Binance للتداول الآلي

## متطلبات التشغيل

```
blinker==1.9.0
click==8.2.1
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.2
MarkupSafe==2.1.3
nltk==3.9.1
regex==2024.11.6
SQLAlchemy==2.0.23
textblob==0.19.0
Werkzeug==3.0.1
```

## هيكل المشروع

```
trading_assistant/
├── src/                      # مجلد الكود المصدري
│   ├── models/               # نماذج قاعدة البيانات
│   ├── routes/               # مسارات API والصفحات
│   ├── services/             # خدمات معالجة البيانات والتوصيات
│   ├── static/               # ملفات ثابتة (HTML, CSS, JS)
│   └── main.py               # نقطة الدخول الرئيسية للتطبيق
├── docs/                     # وثائق المشروع
├── requirements.txt          # متطلبات بيئة Python
└── wsgi.py                   # ملف تكوين WSGI للنشر
```

## التثبيت والتشغيل

1. إنشاء بيئة Python افتراضية:
   ```
   python -m venv venv
   source venv/bin/activate  # لينكس/ماك
   venv\Scripts\activate     # ويندوز
   ```

2. تثبيت المتطلبات:
   ```
   pip install -r requirements.txt
   ```

3. تثبيت موارد NLTK:
   ```
   python -c "import nltk; nltk.download('punkt')"
   ```

4. تشغيل التطبيق:
   ```
   python -m src.main
   ```

5. الوصول إلى التطبيق عبر المتصفح:
   ```
   http://localhost:5000
   ```

## تكامل Binance

لربط التطبيق مع منصة Binance، اتبع الخطوات التالية:

1. إنشاء حساب API في Binance
2. إضافة مفاتيح API إلى ملف الإعدادات
3. استخدام واجهة Binance في التطبيق للوصول إلى بيانات الحساب والتداول

## المساهمة في المشروع

نرحب بمساهماتكم! يرجى اتباع الخطوات التالية:

1. عمل Fork للمشروع
2. إنشاء فرع جديد (`git checkout -b feature/amazing-feature`)
3. تنفيذ التغييرات (`git commit -m 'إضافة ميزة رائعة'`)
4. رفع التغييرات (`git push origin feature/amazing-feature`)
5. فتح طلب دمج (Pull Request)

## الترخيص

هذا المشروع مرخص تحت رخصة MIT - انظر ملف [LICENSE](LICENSE) للتفاصيل.

## الاتصال

- مطور المشروع: [اسم المطور](mailto:example@example.com)
- رابط المشروع: [https://github.com/username/trading-assistant](https://github.com/username/trading-assistant)
