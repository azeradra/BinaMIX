# المساعد الذكي الشخصي للتداول (BinaMIX)

![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/language-Python-blue)

نظام متكامل للتداول الذكي يجمع بين تحليل البيانات المالية وتقنيات الذكاء الاصطناعي لتقديم توصيات تداول مخصصة.

---

## صورة توضيحية
> يمكنك إضافة صورة لشاشة التطبيق هنا (screenshot.png).

---

## المزايا الرئيسية
- **ملف المستخدم الشخصي:** إدارة أهداف المستخدم ومستوى المخاطر.
- **بيانات السوق الحية:** عرض بيانات مباشرة للأسهم والعملات المشفرة.
- **محرك توصيات ذكي:** توصيات استثمارية مخصصة.
- **تحليل مشاعر الأخبار المالية.**
- **تكامل مع Binance للتداول الآلي.**

---

## التثبيت والتشغيل

1. أنشئ بيئة افتراضية:
    ```bash
    python -m venv venv
    # لينكس/ماك
    source venv/bin/activate
    # ويندوز
    venv\Scripts\activate
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

---

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

---

## هيكل المشروع

```
BinaMIX/
├── src/                      # مجلد الكود المصدري
│   ├── models/               # نماذج قاعدة البيانات
│   ├── routes/               # مسارات API والصفحات
│   ├── services/             # خدمات معالجة البيانات والتوصيات
│   ├── static/               # ملفات ثابتة (HTML, CSS, JS)
│   └── main.py               # نقطة الدخول الرئيسية للتطبيق
├── docs/                     # وثائق المشروع
├── requirements.txt          # متطلبات بيئة Python
├── wsgi.py                   # ملف تكوين WSGI للنشر
└── README.md                 # ملف التوثيق الرئيسي
```

---

## تكامل Binance

لربط التطبيق مع منصة Binance، اتبع الخطوات التالية:
1. إنشاء حساب API في Binance
2. إضافة مفاتيح API إلى ملف الإعدادات
3. استخدام واجهة Binance في التطبيق للوصول إلى بيانات الحساب والتداول

---

## المساهمة

نرحب بمساهماتكم! يرجى اتباع الخطوات التالية:

1. عمل Fork للمشروع
2. إنشاء فرع جديد (`git checkout -b feature/amazing-feature`)
3. تنفيذ التغييرات (`git commit -m 'إضافة ميزة رائعة'`)
4. رفع التغييرات (`git push origin feature/amazing-feature`)
5. فتح Pull Request

لمزيد من التفاصيل، راجع [CONTRIBUTING.md](CONTRIBUTING.md).

---

## الأمان

انظر [SECURITY.md](SECURITY.md).

---

## الرخصة

هذا المشروع مرخص تحت رخصة MIT - انظر ملف [LICENSE](LICENSE) للتفاصيل.

---

## الاتصال

- مطور المشروع: **AZEDNE ABDERRAZAK**
- البريد الإلكتروني: [1983adra@gmail.com](mailto:1983adra@gmail.com)
- رابط المشروع: [https://github.com/username/BinaMIX](https://github.com/username/BinaMIX)
