from flask import Flask, request, jsonify
from educhain import Educhain
from utils.helpers import save_to_file
import json

app = Flask(__name__)
client = Educhain()

@app.route("/")
def home():
    return jsonify({"message": "EduChain MCP Server is running"})


@app.route("/generate-mcqs", methods=["POST"])
def generate_mcqs():
    tool_name = "mcqs"
    try:
        data = request.get_json()
        topic = data.get("topic", "General Knowledge")
        num = data.get("num", 5)
        question_type = data.get("question_type", "Multiple Choice")

        response = client.qna_engine.generate_questions(
            topic=topic,
            num=num,
            question_type=question_type
        )
        result = {"status": "success", "questions": response.model_dump()}
    except Exception as e:
        result = {
            "status": "error",
            "message": str(e),
            "questions": [{
                "question": f"What is a key concept in {data.get('topic', 'science')}?",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": "Option A"
            }]
        }

    save_to_file(tool_name, json.dumps(result, indent=2))
    return jsonify(result)


@app.route("/generate-lesson-plan", methods=["POST"])
def generate_lesson_plan():
    tool_name = "lesson_plan"
    try:
        data = request.get_json()
        topic = data.get("topic", "Mathematics")

        response = client.content_engine.generate_lesson_plan(topic=topic)
        result = {"status": "success", "lesson_plan": response.model_dump()}
    except Exception as e:
        result = {
            "status": "error",
            "message": str(e),
            "lesson_plan": {
                "title": f"Lesson Plan on {data.get('topic', 'Math')}",
                "objectives": ["Understand key concepts", "Apply in real life"],
                "activities": ["Group discussion", "Worksheet practice"],
                "assessment": "Short quiz at the end"
            }
        }

    save_to_file(tool_name, json.dumps(result, indent=2))
    return jsonify(result)


@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    tool_name = "pdf"
    try:
        data = request.get_json()
        title = data.get("title", "Untitled")
        content = data.get("content", "No content provided")

        simulated_pdf = f"### {title} ###\n\n{content}"
        result = {"status": "success", "pdf_content": simulated_pdf}
    except Exception as e:
        result = {
            "status": "error",
            "message": str(e),
            "pdf_content": f"Dummy PDF content for {data.get('title', 'Unknown')}"
        }

    save_to_file(tool_name, json.dumps(result, indent=2))
    return jsonify(result)


@app.route("/summarize-topic", methods=["POST"])
def summarize_topic():
    tool_name = "summary"
    try:
        data = request.get_json()
        topic = data.get("topic", "Photosynthesis")

        response = client.content_engine.generate_study_guide(topic=topic)
        result = {"status": "success", "summary": response.model_dump()}
    except Exception as e:
        result = {
            "status": "error",
            "message": str(e),
            "summary": f"{data.get('topic', 'Topic')} is an important subject that helps students understand key concepts."
        }

    save_to_file(tool_name, json.dumps(result, indent=2))
    return jsonify(result)


@app.route("/generate-flashcards", methods=["POST"])
def generate_flashcards():
    tool_name = "flashcards"
    try:
        data = request.get_json()
        topic = data.get("topic", "Chemistry")

        response = client.content_engine.generate_flashcards(topic=topic)
        result = {"status": "success", "flashcards": response.model_dump()}
    except Exception as e:
        result = {
            "status": "error",
            "message": str(e),
            "flashcards": [
                {"question": f"What is {data.get('topic', 'AI')}?", "answer": f"{data.get('topic', 'AI')} is a study field."},
                {"question": f"Why is {data.get('topic', 'AI')} important?", "answer": f"It helps in solving real-world problems."}
            ]
        }

    save_to_file(tool_name, json.dumps(result, indent=2))
    return jsonify(result)


@app.route("/generate-youtube-quiz", methods=["POST"])
def generate_youtube_quiz():
    tool_name = "youtube_quiz"
    try:
        data = request.get_json()
        url = data.get("url")

        response = client.qna_engine.generate_questions_from_youtube(youtube_url=url)
        result = {"status": "success", "quiz": response.model_dump()}
    except Exception as e:
        result = {
            "status": "error",
            "message": str(e),
            "quiz": [{
                "question": "What is one point mentioned in the video?",
                "options": ["Point A", "Point B", "Point C", "Point D"],
                "answer": "Point A"
            }]
        }

    save_to_file(tool_name, json.dumps(result, indent=2))
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False)
