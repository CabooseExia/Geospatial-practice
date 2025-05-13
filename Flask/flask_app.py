from flask import Flask, render_template, request
from pathlib import Path

app = Flask(__name__)

app_dir = Path(__file__).parent
assets_dir = app_dir / "static" /"maps"
country_list = sorted(
    [f.stem for f in assets_dir.glob("*.html")]
)

@app.route("/", methods=["GET", "POST"])
def home():
    selected_country = request.form.get("country")
    return render_template("index.html", countries=country_list, selected=selected_country)


if __name__ == "__main__":
    app.run(debug=True)