from pathlib import Path
from pypdf import PdfReader
from docx import Document


def extract_pdf_text(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def extract_docx_text(file_path):

    document = Document(file_path)

    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )

    return text


def extract_resume_text(file_path):

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError("Resume file not found")

    extension = path.suffix.lower()

    if extension == ".pdf":
        text = extract_pdf_text(path)

    elif extension == ".docx":
        text = extract_docx_text(path)

    else:
        raise ValueError("Only PDF and DOCX files are supported")

    if not text.strip():
        raise ValueError("No readable text found in resume")

    return text.strip()