# EduChain MCP Server + Claude Desktop UI

This project integrates the **EduChain** content generation library with a custom **MCP-compliant Flask server**, 
along with a **desktop UI (Claude Desktop Simulator)** built using Tkinter.

It allows users to generate educational content such as:
- 📘 Multiple-choice questions (MCQs)
- 📋 Lesson plans
- 📄 Summaries
- 🃏 Flashcards
- 📎 Simulated PDFs
- 📺 Quizzes from YouTube videos

## 🧱 Folder Structure

educhain_mcp_server/
│
├── mcp_server.py # Main Flask server exposing EduChain tools via API
├── claude_desktop.py # Tkinter GUI client that simulates Claude Desktop
│
├── utils/
│ └── helpers.py # Utility to save output responses to the outputs/ folder
│
├── outputs/ # Auto-generated text files for each tool's output
│
├── requirements.txt # Required Python packages (Flask, EduChain, etc.)
└── README.md # This file

## 🚀 Features

| Tool               | Endpoint                  | Functionality                              |
|--------------------|---------------------------|---------------------------------------------|
| Generate MCQs      | `/generate-mcqs`          | Creates multiple-choice questions           |
| Lesson Plan        | `/generate-lesson-plan`   | Outputs a structured lesson plan            |
| Topic Summary      | `/summarize-topic`        | Summarizes a topic                          |
| Flashcards         | `/generate-flashcards`    | Flashcard Q&A pairs                         |
| Simulate PDF       | `/generate-pdf`           | Returns simulated PDF-like formatted text   |
| YouTube Quiz       | `/generate-youtube-quiz`  | Extracts quiz questions from a video URL    |

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/educhain-mcp-server.git
cd educhain-mcp-server
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Make sure you have educhain installed via PyPI or from source.

🖥️ Run the MCP Server
bash
Copy
Edit
python mcp_server.py
The Flask server will run at: http://127.0.0.1:5000

🪟 Launch Claude Desktop UI
bash
Copy
Edit
python claude_desktop.py
This opens a Tkinter-based GUI to interact with the tools like a Claude Desktop app.

📝 Output Storage
Each tool's result is automatically saved as a .txt file in the /outputs folder using the helper utility.

💡 Notes
If you're running in offline mode or without OpenAI API access, dummy responses are returned for each tool.

Proper error handling is built-in for unsupported or failed requests.

✨ Example Commands
From Claude Desktop (GUI), you can:

Enter a topic like Photosynthesis and press "Generate MCQs"

View structured output and saved result in /outputs/

📬 Contact
For questions or improvements, feel free to raise an issue or contact Nistha Jain.
