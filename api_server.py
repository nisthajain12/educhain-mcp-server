# api_server.py
from flask import Flask, request, jsonify
from tools.mcq_generator import generate_mcqs
from tools.lesson_plan_generator import generate_lesson_plan

app = Flask(__name__)

@app.route("/generate_mcqs", methods=["POST"])
def mcqs():
    data = request.json
    topic = data.get("topic")
    if not topic:
        return jsonify({"error": "Topic required"}), 400
    result = generate_mcqs(topic)
    return jsonify({"result": result})

@app.route("/generate_lesson_plan", methods=["POST"])
def lesson_plan():
    data = request.json
    subject = data.get("subject")
    if not subject:
        return jsonify({"error": "Subject required"}), 400
    result = generate_lesson_plan(subject)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(port=5000)
