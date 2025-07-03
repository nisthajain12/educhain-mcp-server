from educhain import Educhain

_client = Educhain()

def summarize_text(topic):
    try:
        return _client.content_engine.generate_study_guide(topic=topic)
    except Exception as e:
        return f"📝 Dummy Summary:\n{topic} is a broad area. This is a sample summary generated for testing."
