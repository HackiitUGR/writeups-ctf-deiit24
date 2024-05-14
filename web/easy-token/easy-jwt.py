from flask import Flask, request, jsonify, make_response
import sqlite3
import jwt

app = Flask(__name__)

@app.route('/')
def home():
    payload = {'role': 'guest'}
    token = jwt.encode(payload, 'fasdfa89sdf9asdhfiuahsdf89yasd89fya', algorithm='HS256')
    resp = make_response()
    resp.set_cookie('jwt', token)
    return resp 


@app.route('/admin')
def admin_dashboard():
    token = request.cookies.get('jwt')
    if not token:
        return jsonify({"message": "Token is missing"}), 401
    try:
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        if decoded_token['role'] == 'admin':
            return jsonify({"message": "Welcome admin!", "flag": "ETSIIT_CTF{R-U-SUR3-AB0UT-D4T?}"}), 200
        else:
            return jsonify({"message": "Unauthorized"}), 401
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")

