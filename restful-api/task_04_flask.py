#!/usr/bin/python3
"""simple Flask API handling users and JSON responses."""

from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    """return API status
    """
    return "OK"

@app.route('/data')
def get_usernames():
   """return list of all users names
   """
   return jsonify(list(users.keys()))

@app.route('/users/<username>')
def get_user(username):
    """return data of a user
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """add a new user with POST request
    """
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
        users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run()
