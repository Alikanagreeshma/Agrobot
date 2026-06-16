from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


OPENROUTER_API_KEY = "OPENROUTER_API_KEY"

@app.route("/")
def home():
    return "AgroBot AI Backend Running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json() or {}
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({
                "reply": "Please enter a question."
            })

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3.1-8b-instruct",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are AgroBot, an agriculture assistant for Indian farmers. "
                            "If the user writes in Telugu, reply completely in Telugu. "
                            "If the user writes in Hindi, reply completely in Hindi. "
                            "If the user writes in English, reply completely in English. "
                            "Help with crops, soil, irrigation, fertilizers, pests, "
                            "plant diseases, weather impact and sustainable farming."
                        )
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            }
        )

        data = response.json()

        if "choices" not in data:
            return jsonify({
                "reply": f"OpenRouter Error: {data}"
            })

        reply = data["choices"][0]["message"]["content"]

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "reply": f"Backend Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)