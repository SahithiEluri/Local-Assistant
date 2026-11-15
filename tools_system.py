import os
import subprocess
from pathlib import Path

def search_files(directory: str, keyword: str) -> str:
    """
    Searches for files matching a keyword in a specified directory,
    skipping hidden folders like .venv to keep results clean.
    """
    path = Path(directory)
    if not path.exists():
        return f"Directory '{directory}' not found."

    matches = []
    for file in path.rglob("*"):
        # Skip hidden directories and virtual environment folders
        if any(part.startswith(".") or part == "venv" for part in file.parts):
            continue
            
        if keyword.lower() in file.name.lower():
            matches.append(str(file))

    if not matches:
        return f"No files matching '{keyword}' found in {directory}."
    
    return "\n".join(matches[:15])


def get_latest_resume(directory: str = r"C:\Users\sahit\Downloads") -> str:
    """
    Scans a directory for resume files (.pdf, .docx, .doc) and returns
    the file path of the most recently modified document.
    """
    path = Path(directory)
    if not path.exists():
        return f"Directory '{directory}' not found."

    resume_files = []
    valid_extensions = {".pdf", ".docx", ".doc"}

    for file in path.iterdir():
        if file.is_file() and file.suffix.lower() in valid_extensions:
            if "resume" in file.name.lower():
                resume_files.append((file, file.stat().st_mtime))

    if not resume_files:
        return f"No resume documents found in {directory}."

    # Sort files by modified timestamp in descending order (newest first)
    resume_files.sort(key=lambda x: x[1], reverse=True)
    latest_file = resume_files[0][0]
    
    return f"Latest resume: {latest_file.name} | Path: {latest_file}"


def open_file_or_folder(path: str) -> str:
    """Opens a file or folder on Windows using the default associated application."""
    target_path = Path(path)
    if not target_path.exists():
        return f"Error: Path '{path}' does not exist."
    
    try:
        os.startfile(str(target_path))
        return f"Successfully opened '{path}'."
    except Exception as e:
        return f"Failed to open '{path}': {str(e)}"