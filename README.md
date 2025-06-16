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

1. **إنشاء بيئة افتراضية:**
    ```bash
    python -m venv venv
    # لينكس/ماك
    source venv/bin/activate
    # ويندوز
    venv\Scripts\activate
    ```
2. **تثبيت المتطلبات:**
    ```bash
    pip install -r requirements.txt
    ```
3. **تحميل بيانات NLTK:**
    ```bash
    python -c "import nltk; nltk.download('punkt')"
    ```
4. **تشغيل التطبيق:**
    ```bash
    python -m src.main
    ```
5. **تصفح التطبيق:**
    ```
    http://localhost:5000
    ```

---

## متطلبات التشغيل

```txt
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
requests==2.31.0
python-binance==1.0.19
```
> **ملاحظة:** تأكد من وجود مكتبة requests لدعم جلب البيانات من الإنترنت، وpython-binance لدعم التكامل مع Binance.

---

## هيكل المشروع

```text
BinaMIX/
├── src/                      # الكود المصدري
│   ├── models/               # نماذج قاعدة البيانات
│   ├── routes/               # مسارات API والصفحات
│   ├── services/             # الخدمات الذكية ومعالجة البيانات
│   ├── static/               # ملفات ثابتة (HTML, CSS, JS)
│   └── main.py               # نقطة الدخول الرئيسية للتطبيق
├── docs/                     # وثائق المشروع
├── requirements.txt          # متطلبات بيئة Python
├── wsgi.py                   # ملف تشغيل WSGI للنشر
└── README.md                 # ملف التوثيق الرئيسي
```

---

## تكامل Binance

لربط التطبيق مع منصة Binance:
1. إنشاء حساب API في منصة Binance.
2. إضافة مفاتيح API في ملف الإعدادات الآمن (يفضل استخدام متغيرات بيئية).
3. استخدام واجهة Binance في التطبيق للوصول إلى بيانات الحساب وتنفيذ التداولات.

---

## المساهمة

نرحب بجميع المساهمات!  
يرجى اتباع الخطوات التالية:

1. عمل Fork للمشروع
2. إنشاء فرع جديد (`git checkout -b feature/اسم-الميزة`)
3. تنفيذ التغييرات مع كتابة رسالة واضحة للكوميت (`git commit -m 'إضافة ميزة...'`)
4. رفع التغييرات (`git push origin feature/اسم-الميزة`)
5. فتح Pull Request

لمزيد من التفاصيل، راجع [CONTRIBUTING.md](CONTRIBUTING.md).

---

## الأمان

يرجى مراجعة [SECURITY.md](SECURITY.md) قبل إضافة أي كود أو بيانات حساسة.

---

## الرخصة

هذا المشروع مرخص تحت رخصة MIT.  
انظر ملف [LICENSE](LICENSE) للتفاصيل.

---

## الاتصال

- مطور المشروع: **AZEDNE ABDERRAZAK**
- البريد الإلكتروني: [1983adra@gmail.com](mailto:1983adra@gmail.com)
- رابط المشروع: [https://github.com/username/BinaMIX](https://github.com/username/BinaMIX)
