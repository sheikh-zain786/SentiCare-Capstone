from flask import Flask, request, jsonify
import joblib
import pandas as pd
from conversational_manager import generate_response
from db import conversations_collection
import base64

app = Flask(__name__)

model = joblib.load("artifacts/stress_classifier.joblib")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    language = data.get("language", "en")

    # Example: Convert message to features (simplified)
    # You must replace this with real feature extraction
    features = {
        "sleep_hours": 5,
        "study_hours": 8,
        "anxiety_level": 7
    }

    df = pd.DataFrame([features])
    stress_level = model.predict(df)[0]

    bot_response = generate_response(stress_level, language)

    conversations_collection.insert_one({
        "user_message": user_message,
        "stress_level": stress_level,
        "bot_response": bot_response
    })

    return jsonify({
        "response": bot_response,
        "audio": None
    })


@app.route("/speak", methods=["POST"])
def speak():
    data = request.json
    text = data.get("text")

    # For now, return no audio (you can add TTS later)
    return jsonify({"audio": None})


@app.route("/transcribe", methods=["POST"])
def transcribe():
    # You need Whisper or speech-to-text here
    return jsonify({"text": "Transcription feature not implemented yet"})


if __name__ == "__main__":
    app.run(debug=True)
