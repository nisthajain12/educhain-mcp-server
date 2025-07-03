from educhain import Educhain

_client = Educhain()

def generate_lesson_plan(topic):
    try:
        return _client.content_engine.generate_lesson_plan(topic=topic)
    except Exception as e:
        return {
            "topic": topic,
            "objectives": ["Understand basics", "Apply concepts"],
            "activities": ["Lecture", "Practice"],
            "assessment": "Quiz"
        }
