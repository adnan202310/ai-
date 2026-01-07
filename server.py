from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/check", methods=["POST"])
def check_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    return jsonify({
        "ai_generated_probability": 65.4,
        "result": "Possibly AI Generated"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
