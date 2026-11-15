import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError

# Import local tool functions
from tools_system import search_files, get_latest_resume, open_file_or_folder
from tools_job import read_pdf, organize_resume_file

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please check your setup.")

# Define available tools for Gemini function calling
SYSTEM_TOOLS = [
    search_files,
    get_latest_resume,
    open_file_or_folder,
    read_pdf,
    organize_resume_file,
]

def main():
    client = genai.Client(api_key=api_key)

    print("🤖 Local AI Laptop & Job Assistant initialized!")
    print("Type 'exit' to quit.\n" + "-" * 50)

    # Initialize multi-turn chat session with local tools enabled
    chat = client.chats.create(
        model="gemini-3.6-flash",
        config=types.GenerateContentConfig(
            temperature=0.2,
            tools=SYSTEM_TOOLS,
        )
    )

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.strip().lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            if not user_input.strip():
                continue

            # Send message with automatic 503 retry handling
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    response = chat.send_message(user_input)
                    print(f"\nAssistant: {response.text}")
                    break
                except APIError as e:
                    if "503" in str(e) or "UNAVAILABLE" in str(e):
                        if attempt < max_retries - 1:
                            wait_time = (attempt + 1) * 3
                            print(f"\n[Google API busy (503). Retrying in {wait_time}s...]")
                            time.sleep(wait_time)
                        else:
                            print("\n[Error: Server is currently unreachable. Please try again in a few moments.]")
                    else:
                        raise e

        except KeyboardInterrupt:
            print("\nSession interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\nError processing command: {e}")

if __name__ == "__main__":
    main()