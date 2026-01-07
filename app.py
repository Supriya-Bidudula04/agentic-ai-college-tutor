from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------------- AGENTS ---------------- #

def tutor_agent(message):
    return f"[Tutor Agent]\nI will explain this simply:\n{message} is an important programming concept."

def practice_agent(message):
    return f"""[Practice Agent]
1. What is {message}?
2. Write a simple example of {message}.
3. Why is {message} useful?
"""

def roadmap_agent(message):
    return f"""[Roadmap Agent]
Step 1: Understand basics of {message}
Step 2: Practice simple examples
Step 3: Build small projects using {message}
"""

# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return "Chatbot backend is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    
    agent = data.get("agent")
    message = data.get("message")

    if agent == "tutor":
        reply = tutor_agent(message)
    elif agent == "practice":
        reply = practice_agent(message)
    elif agent == "roadmap":
        reply = roadmap_agent(message)
    else:
        reply = "Invalid agent selected"

    return jsonify({"reply": reply})

# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
