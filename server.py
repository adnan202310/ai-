from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "AI Server Running",
        "message": "Backend is live"
    })

@app.route("/check", methods=["POST"])
def check_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]

    # ⚠️ Demo response (FREE setup)
    # Yahan baad me AI model add kar sakte ho
    return jsonify({
        "ai_generated_probability": 65.4,
        "result": "Possibly AI Generated"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
