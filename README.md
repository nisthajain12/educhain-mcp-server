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

yaml
Copy
Edit

---

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

## 🚀 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/nisthajain12/educhain-mcp-server.git
cd educhain-mcp-server

2. Create a Virtual Environment
On Windows:
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
On macOS/Linux:
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ Make sure educhain is installed via PyPI or from source.

4. Run the MCP Server
bash
Copy
Edit
python mcp_server.py
The server will start on http://127.0.0.1:5000

5. Simulate Claude Desktop UI (Optional)
bash
Copy
Edit
python claude_desktop_sim.py
Use this to test the MCP tools via a desktop-like interface.


## 💡 Notes

If you're running in offline mode or without OpenAI API access, dummy responses are returned for each tool.

Proper error handling is built-in for unsupported or failed requests.

## ✨ Example Commands

From Claude Desktop (GUI), you can:

Enter a topic like Photosynthesis and press "Generate MCQs"

View structured output and saved result in /outputs/


## 📬 Contact
For questions or collaboration, feel free to reach out:
📧 nisthajain2812@gmail.com

---

## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![EduChain](https://img.shields.io/badge/Powered_by-EduChain-purple?style=flat&logo=github)
![MCP-Compatible](https://img.shields.io/badge/MCP-Compatible-green?style=flat)

---

## 📂 Output Samples

All generated content is saved to the `outputs/` directory in `.txt` format.

Each tool (e.g., MCQ Generator, Lesson Planner) automatically saves responses via the `helpers.py` utility.

### 📸 Screenshot of Output (Claude Desktop)

![Claude_desktop_sim](https://raw.githubusercontent.com/nisthajain12/educhain-mcp-server/refs/heads/main/Screenshot%20(79).png)

---

## 👥 Contributors

| Name         | Role                        | Contact                       |
|--------------|-----------------------------|-------------------------------|
| **Nistha Jain** | Developer & Integrator      | [nisthajain2812@gmail.com](mailto:nisthajain2812@gmail.com) |

Feel free to reach out for collaboration or questions!

---
## 📚 Citation
This project makes use of the following external tools and references:

EduChain
AI-based educational content generation engine.
🔗 GitHub Repository
📦 PyPI Package
📖 Official documentation and usage examples provided by the EduChain team.

Claude Desktop MCP Reference
MCP (Multi-Modal Control Protocol) UI simulation is inspired by Claude-style desktop interactions.
This implementation uses a local Tkinter GUI to simulate Claude-like functionality.

If you're using this project in your own research or application, you may cite it as:

bibtex
Copy
Edit
@misc{nisthajain2025educhainmcp,
  author       = {Nistha Jain},
  title        = {EduChain MCP Server: AI-powered educational content interface},
  year         = {2025},
  howpublished = {\url{https://github.com/nisthajain12/educhain-mcp-server}},
  note         = {Combines EduChain with a local MCP-compliant server and Claude-style desktop UI.}
}

## ⚖️ License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2025 Nistha Jain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

(Full license text at https://opensource.org/licenses/MIT)
⭐️ Show Your Support
If you found this useful, give it a ⭐️ on GitHub!


