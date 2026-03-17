from flask import Flask, request, jsonify
from flask_cors import CORS

from backend.chatbot.conversation_engine import ConversationEngine


app = Flask(__name__)
CORS(app)

engine = ConversationEngine()


@app.route("/screening", methods=["POST"])
def screening():

    data = request.json
    answers = data.get("answers")

    scores = engine.calculate_screening_scores(answers)

    condition = engine.determine_condition(scores)

    questions = engine.get_feature_questions(condition)

    return jsonify({
        "condition": condition,
        "questions": questions
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    condition = data.get("condition")
    features = data.get("features")

    prediction = engine.run_prediction(condition, features)

    level = engine.map_prediction_to_level(prediction)

    response = engine.generate_cbt_response(condition, level)

    return jsonify({
        "prediction": prediction,
        "level": level,
        "cbt_response": response
    })


if __name__ == "__main__":
    app.run(debug=True)