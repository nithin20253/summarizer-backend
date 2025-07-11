from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_file(file_path: str) -> str:
    if file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        return '\n'.join([page.extract_text() for page in reader.pages])
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    raise ValueError("Unsupported file format")
