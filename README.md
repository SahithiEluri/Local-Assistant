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
   git clone <your-repo-url>
   cd Local-Assistant