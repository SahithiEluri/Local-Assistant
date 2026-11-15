import shutil
from datetime import datetime
from pathlib import Path
from pypdf import PdfReader


def read_pdf(file_path: str) -> str:
    """Extracts raw text from a PDF document."""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text[:3000]
    except Exception as e:
        return f"Error reading PDF: {e}"


def organize_resume_file(file_path: str, category: str) -> str:
    """Moves a resume into a organized subfolder structured by year and category."""
    src = Path(file_path)
    if not src.exists():
        return f"File '{file_path}' not found."

    mod_year = str(datetime.fromtimestamp(src.stat().st_mtime).year)
    dest_dir = src.parent / mod_year / category
    dest_dir.mkdir(parents=True, exist_ok=True)

    target = dest_dir / src.name
    shutil.move(str(src), str(target))
    return f"Organized '{src.name}' -> '{dest_dir}'."