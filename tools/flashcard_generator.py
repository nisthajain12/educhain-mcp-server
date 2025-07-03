from educhain import Educhain

_client = Educhain()

def generate_flashcards(topic):
    try:
        return _client.content_engine.generate_flashcards(topic=topic)
    except Exception as e:
        return [
            {"question": f"What is {topic}?", "answer": f"{topic} is a test concept."},
            {"question": f"Why study {topic}?", "answer": "Because it's important for learning!"}
        ]
