#!/usr/bin/python3
"""Module Flask"""

from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """home method"""
    return "Welcome to the Flask API!"


@app.route("/data")
def my_data():
    """data method"""
    return jsonify(list(users.keys()))


@app.route("/status")
def my_status():
    """status method"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """username method"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username]), 200


@app.route("/add_user", methods=["POST"])
def adding_user():
    """adding user method"""
    datas = request.get_json()
    username = datas.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400
    users[username] = {
        "username": username,
        "name": datas.get('name'),
        "age": datas.get('age'),
        "city": datas.get('city')
    }
    return jsonify({'message': 'User added', 'user': users[username]}), 201


if __name__ == "__main__":
    app.run()
