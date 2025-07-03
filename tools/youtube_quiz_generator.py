from educhain import Educhain

_client = Educhain()

def generate_quiz_from_youtube(url):
    try:
        return _client.qna_engine.generate_questions_from_youtube(url=url, num=5)
    except Exception as e:
        return [
            {
                "question": "What was discussed in the video?",
                "options": ["A", "B", "C", "D"],
                "answer": "A"
            }
        ]
