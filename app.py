# app.py
from flask import Flask, request, render_template, jsonify
from graph_agent import run_agent

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        api_key = request.form.get("api_key")
        repo_url = request.form.get("repo_url")
        language = request.form.get("language", "python")
        try:
            final_state = run_agent(api_key, repo_url, language)
            generated_code = final_state.get("generated_code")

            return jsonify({"generated_code": generated_code})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)