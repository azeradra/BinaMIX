from flask import Blueprint, request, jsonify, session

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    # هذه فقط نقطة بداية، يجب استخدام حماية قوية مثل JWT أو OAuth لاحقًا
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # TODO: تحقق من بيانات المستخدم من قاعدة البيانات
    if username == "admin" and password == "admin":
        session['user'] = username
        return jsonify({"message": "تم تسجيل الدخول بنجاح"}), 200
    return jsonify({"error": "بيانات غير صحيحة"}), 401

@auth.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({"message": "تم تسجيل الخروج"}), 200
