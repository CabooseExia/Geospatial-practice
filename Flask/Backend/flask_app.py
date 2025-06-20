from flask import Flask, request, jsonify, session
from pathlib import Path
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)  # allow requests from frontend

load_dotenv()

USERNAME = os.getenv("ADMIN_USERNAME")
PASSWORD = os.getenv("ADMIN_PASSWORD")
app.secret_key = os.getenv("SECRET_KEY")

users = {USERNAME: PASSWORD}

app_dir = Path(__file__).parent
assets_dir = app_dir / "static" / "maps"
country_list = sorted([f.stem for f in assets_dir.glob("*.html")])

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        session["username"] = username
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Invalid credentials"}), 401

@app.route("/api/logout", methods=["POST"])
def api_logout():
    session.pop("username", None)
    return jsonify({"success": True})

@app.route("/api/user", methods=["GET"])
def api_user():
    if "username" not in session:
        return jsonify({"authenticated": False}), 401
    return jsonify({"authenticated": True, "username": session["username"]})

@app.route("/api/countries", methods=["GET"])
def api_countries():
    if "username" not in session:
        return jsonify({"error": "Not logged in"}), 401
    return jsonify({"countries": country_list})

if __name__ == "__main__":
    app.run(debug=True)
