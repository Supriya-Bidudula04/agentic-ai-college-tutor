from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend to make requests

# Health check route
@app.route("/healthz")
def health():
    return {"status": "healthy"}

# Root route
@app.route("/")
def home():
    return jsonify({
        "status": "Backend is running 🚀",
        "message": "Agentic AI College Tutor API"
    })

# Set your OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Tutor agent endpoint
@app.route("/tutor", methods=["POST"])
def tutor_agent():
    data = request.json
    topic = data.get("topic", "")
    prompt = f"You are a patient college programming tutor. Explain {topic} simply with examples."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful programming tutor."},
            {"role": "user", "content": prompt}
        ]
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
        messages=[
            {"role": "system", "content": "You are a coding practice generator."},
            {"role": "user", "content": prompt}
        ]
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
        messages=[
            {"role": "system", "content": "You are a roadmap generator."},
            {"role": "user", "content": prompt}
        ]
    )
    
    answer = response.choices[0].message.content
    return jsonify({"reply": answer})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
