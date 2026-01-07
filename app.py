from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend to make requests
@app.route("/")
def home():
    return "Chatbot backend is running!"

@app.route("/healthz")
def health():
    return {"status": "healthy"}

# Set your OpenAI API key from environment variable
openai.api_key = os.environ.get("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")

# Tutor agent endpoint
@app.route("/tutor", methods=["POST"])
def tutor_agent():
    data = request.json
    topic = data.get("topic", "")
    prompt = f"You are a patient college programming tutor. Explain {topic} simply with examples."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"You are a helpful programming tutor."},
                  {"role":"user","content":prompt}]
    )
    
    answer = response.choices[0].message.content
    return jsonify({"reply": answer})

# Practice agent endpoint
@app.route("/practice", methods=["POST"])
def practice_agent():
    data = request.json
    topic = data.get("topic", "")
    prompt = f"Create 3 practice questions on {topic} with increasing difficulty."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"You are a coding practice generator."},
                  {"role":"user","content":prompt}]
    )
    
    answer = response.choices[0].message.content
    return jsonify({"reply": answer})

# Roadmap agent endpoint
@app.route("/roadmap", methods=["POST"])
def roadmap_agent():
    data = request.json
    topic = data.get("topic", "")
    prompt = f"Create a simple learning roadmap for {topic} for college students."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"You are a roadmap generator."},
                  {"role":"user","content":prompt}]
    )
    
    answer = response.choices[0].message.content
    return jsonify({"reply": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
