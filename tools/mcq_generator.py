from educhain import Educhain

_client = Educhain()

def generate_mcqs(topic):
    try:
        return _client.qna_engine.generate_questions(
            topic=topic,
            num=5,
            question_type="Multiple Choice"
        )
    except Exception as e:
        return [
            {
                "question": f"What is {topic}?",
                "options": ["A topic", "A place", "An animal", "A number"],
                "answer": "A topic"
            }
        ]

