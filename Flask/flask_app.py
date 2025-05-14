from flask import Flask, render_template, request, redirect, url_for, session
from pathlib import Path
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'your_secret_key'
load_dotenv()

USERNAME = os.getenv("ADMIN_USERNAME")
PASSWORD = os.getenv("ADMIN_PASSWORD")

users = {USERNAME: PASSWORD}

app_dir = Path(__file__).parent
assets_dir = app_dir / "static" /"maps"
country_list = sorted(
    [f.stem for f in assets_dir.glob("*.html")]
)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    selected_country = request.form.get("country") or country_list[0]
    return render_template("index.html", user=session["username"], countries=country_list, selected=selected_country)

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)