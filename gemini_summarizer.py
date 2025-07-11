import google.generativeai as genai
import os
from typing import Optional
from utils.text_extractor import extract_text_from_file  # ✅ Fixed import

class GeminiDocumentSummarizer:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def summarize(self, input_source: str, is_file: bool = True) -> str:
        """
        Summarize content from file path or raw text.
        :param input_source: File path or text content
        :param is_file: True if input is file path
        :return: Generated summary
        """
        try:
            text = extract_text_from_file(input_source) if is_file else input_source
            response = self.model.generate_content(
                f"Create a concise, professional summary of this document:\n\n{text}"
            )
            return response.text.strip()
        except Exception as e:
            raise RuntimeError(f"Summarization error: {str(e)}")

