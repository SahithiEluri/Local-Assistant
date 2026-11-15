# 🤖 Local AI Laptop & Job Assistant

A modular, CLI-based AI assistant built with Python and the **Google Gemini API (`gemini-3.6-flash`)**. It uses automatic function calling (agentic tool use) to search local directories, open files, extract text from PDFs, and organize job application resumes.

## ✨ Features
* **Natural Language File Search:** Scans directories for matching keywords while automatically filtering out `.venv` and hidden folders.
* **Latest Resume Detection:** Identifies the most recently modified resume (`.pdf` or `.docx`) using OS file timestamps.
* **PDF Analysis & Organization:** Extracts text from PDF resumes and sorts documents by category.
* **Resilient API Execution:** Built-in retry logic with exponential backoff to handle transient API spikes (`503 UNAVAILABLE`).

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **AI SDK:** `google-genai` (`gemini-3.6-flash`)
* **Libraries:** `pypdf`, `python-dotenv`, `pathlib`

## 🚀 Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SahithiEluri/Local-Assistant.git
   cd Local-Assistant
   
## Example Usage
Here is what running and querying the assistant looks like in the terminal:

```text
> python assistant.py
Assistant initialized. What would you like to do?
> find my latest resume in downloads and check folder counts

[Tool Call: get_latest_resume(directory="C:\Users\sahit\Downloads")]
[Tool Call: count_folders(directory="C:\Users\sahit\Desktop")]

Assistant: I found your latest resume: C:\Users\sahit\Downloads\Sahithi_Eluri_Resume.pdf. Additionally, there are 12 folders in your Desktop directory.
