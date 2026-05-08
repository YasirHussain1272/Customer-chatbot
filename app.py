import os
import json
from flask import Flask, request, jsonify, render_template
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a bilingual customer support assistant. You MUST reply in the SAME language the user writes in.

CRITICAL LANGUAGE RULES:
- If the user writes in Arabic → reply ONLY in Arabic
- If the user writes in English → reply ONLY in English  
- If mixed → use whichever language dominates
- NEVER translate or switch languages mid-reply

You support customers for a Saudi Arabian business.
Greet in Arabic: مرحبا، كيف أقدر أساعدك؟
Greet in English: Hello! How can I help you today?

FAQ topics:
- Order tracking and delivery (التتبع والتوصيل)
- Returns & refunds - 7 day policy (الإرجاع خلال 7 أيام)
- Store hours: Sat–Thu 9AM–10PM, Fri 2PM–10PM
- Payment: Mada, Visa, Mastercard, Apple Pay, STC Pay
- VAT: 15% on all purchases
- WhatsApp support: +966-XXX-XXXX

Keep answers short and clear. Be warm and respectful."""

conversation_history = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    session_id = data.get("session_id", "default")

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    if session_id not in conversation_history:
        conversation_history[session_id] = []

    conversation_history[session_id].append({
        "role": "user",
        "content": user_message
    })

    # Keep last 10 messages for context
    recent_history = conversation_history[session_id][-10:]

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *recent_history
            ],
            max_tokens=500,
            temperature=0.3
        )

        assistant_message = response.choices[0].message.content

        conversation_history[session_id].append({
            "role": "assistant",
            "content": assistant_message
        })

        return jsonify({
            "reply": assistant_message,
            "timestamp": datetime.now().strftime("%I:%M %p")
        })

    except Exception as e:
        print(f"ERROR: {e}")  # add this line
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
