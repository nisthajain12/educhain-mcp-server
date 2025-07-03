import tkinter as tk
import requests
import json

def send_request(endpoint):
    topic = entry.get()
    extra = extra_input.get()

    payload = {
        "topic": topic
    }

    if endpoint == "generate-mcqs":
        payload.update({"num": 5, "question_type": "Multiple Choice"})

    if endpoint == "generate-pdf":
        payload.update({"title": topic, "content": extra})

    if endpoint == "generate-youtube-quiz":
        payload = {"url": extra or "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}

    output_box.delete("1.0", tk.END)

    try:
        response = requests.post(f"http://127.0.0.1:5000/{endpoint}", json=payload)
        result = response.json()
        output_box.insert(tk.END, json.dumps(result, indent=2))
    except Exception as e:
        output_box.insert(tk.END, f"❌ Error: {e}")

root = tk.Tk()
root.title("Claude Desktop - EduChain MCP Sim")

tk.Label(root, text="Topic / Title:").pack()
entry = tk.Entry(root, width=60)
entry.pack(pady=2)

tk.Label(root, text="Extra Input (e.g., PDF content or YouTube URL):").pack()
extra_input = tk.Entry(root, width=60)
extra_input.pack(pady=2)

# Buttons for all tools
buttons = [
    ("Generate MCQs", "generate-mcqs"),
    ("Generate Lesson Plan", "generate-lesson-plan"),
    ("Generate PDF", "generate-pdf"),
    ("Summarize Topic", "summarize-topic"),
    ("Generate Flashcards", "generate-flashcards"),
    ("Generate YouTube Quiz", "generate-youtube-quiz"),
]

for label, endpoint in buttons:
    tk.Button(root, text=label, width=30, command=lambda ep=endpoint: send_request(ep)).pack(pady=2)

output_box = tk.Text(root, wrap="word", height=25, width=90)
output_box.pack(pady=10)

root.mainloop()
