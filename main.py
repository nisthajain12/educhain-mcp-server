# main.py
from dotenv import load_dotenv
load_dotenv()

from educhain import Educhain

_client = Educhain()
qna_engine = _client.qna_engine

print(dir(qna_engine))


from tools.pdf_generator import generate_pdf
from tools.summarizer import summarize_text
from tools.flashcard_generator import generate_flashcards
from tools.youtube_quiz_generator import generate_quiz_from_youtube
from tools.mcq_generator import generate_mcqs
from tools.lesson_plan_generator import generate_lesson_plan
from utils.helpers import save_to_file

def main():
    print("\n🎓 Welcome to the EduChain MCP Server 🎓")
    print("Available tools:")
    print("1. PDF Generator")
    print("2. Summarizer")
    print("3. Flashcard Generator")
    print("4. YouTube Quiz Generator")
    print("5. MCQ Generator")
    print("6. Lesson Plan Generator")
    print("0. Exit\n")

    while True:
        choice = input("Select a tool (0-6): ")

        if choice == "1":
             title = input("Enter the title for the PDF: ")
             content = input("Enter the content for the PDF: ")
             generate_pdf(title, content)
             save_to_file("pdf_output.txt", content)


        elif choice == "2":
            topic = input("Enter the topic to summarize: ")
            content = summarize_text(topic)
            save_to_file("summary.txt", content)

        elif choice == "3":
            topic = input("Enter the topic for flashcards: ")
            content = generate_flashcards(topic)
            save_to_file("flashcards.txt", content)

        elif choice == "4":
            url = input("Enter the YouTube video URL: ")
            content = generate_quiz_from_youtube(url)
            save_to_file("youtube_quiz.txt", content)

        elif choice == "5":
            topic = input("Enter the topic for MCQs: ")
            content = generate_mcqs(topic)
            save_to_file("mcqs.txt", content)

        elif choice == "6":
            topic = input("Enter the topic for a lesson plan: ")
            content = generate_lesson_plan(topic)
            save_to_file("lesson_plan.txt", content)

        elif choice == "0":
            print("👋 Exiting MCP Server. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
