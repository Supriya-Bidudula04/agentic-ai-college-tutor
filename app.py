from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Chatbot backend is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    return jsonify({
        "reply": f"You asked: {user_msg}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
