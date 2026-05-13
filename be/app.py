from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/")
def index():
    return "Todo API is running"

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password_hash = data.get("password_hash")

    if not name or not email or not password_hash:
        return jsonify