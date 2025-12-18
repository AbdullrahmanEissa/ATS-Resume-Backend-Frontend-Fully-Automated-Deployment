from pathlib import Path
from typing import Optional
import PyPDF2
import docx

class CVParser:
    @staticmethod
    def parse_pdf(file_path: Path) -> str:
        text = ""
        try:
            with open(file_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            raise ValueError(f"Error parsing PDF: {str(e)}")
        return text.strip()

    @staticmethod
    def parse_docx(file_path: Path) -> str:
        try:
            doc = docx.Document(file_path)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        except Exception as e:
            raise ValueError(f"Error parsing DOCX: {str(e)}")
        return text.strip()

    @classmethod
    def parse_cv(cls, file_path: Path) -> str:
        suffix = file_path.suffix.lower()
        
        if suffix == ".pdf":
            return cls.parse_pdf(file_path)
        elif suffix == ".docx":
            return cls.parse_docx(file_path)
        else:
            raise ValueError(f"Unsupported file format: {suffix}")