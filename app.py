from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# -------------------- Setup --------------------
app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can call backend

# Replace this with your OpenAI API key
openai.api_key = "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"

# -------------------- Helper Functions --------------------
def tutor_agent(topic):
    prompt = f"You are a patient college programming tutor. Explain {topic} simply with examples."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful programming tutor."},
                  {"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message['content']

def practice_agent(topic):
    prompt = f"Generate 3 practice questions on {topic} with increasing difficulty."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a coding practice generator."},
                  {"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message['content']

def roadmap_agent(topic):
    prompt = f"Create a simple roadmap for learning {topic} step by step."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a learning roadmap guide."},
                  {"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message['content']

# -------------------- Routes --------------------
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    agent = data.get("agent")
    topic = data.get("topic")

    if agent == "tutor":
        reply = tutor_agent(topic)
    elif agent == "practice":
        reply = practice_agent(topic)
    elif agent == "roadmap":
        reply = roadmap_agent(topic)
    else:
        return jsonify({"error": "Invalid agent selected"}), 400

    return jsonify({"reply": reply})

# -------------------- Main --------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
