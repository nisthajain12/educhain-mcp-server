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

🚀 Setup Instructions
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

🧪 Available Tools
Endpoint	Functionality
/generate-mcqs	Generate multiple-choice questions
/generate-lesson-plan	Create a lesson plan
/generate-pdf	Simulate PDF creation
/summarize-topic	Generate a study summary
/generate-flashcards	Flashcards for a topic
/generate-youtube-quiz	MCQs from a YouTube video

📂 Folder Structure
graphql
Copy
Edit
educhain-mcp-server/
├── educhain/               # (if installed from source, otherwise external)
├── tools/                  # Tool-specific logic (API wrappers etc.)
├── utils/                  # Helper functions like file saving
├── claude_desktop_sim.py   # Claude-like interface using Tkinter
├── mcp_server.py           # Main Flask MCP Server
├── requirements.txt        # Python dependencies
├── README.md               # You’re reading it!
└── outputs/                # Saved text files from responses
📬 Contact
For questions or collaboration, feel free to reach out:
📧 nisthajain2812@gmail.com
