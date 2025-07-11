from flask import Blueprint, request, jsonify
from flask_cors import CORS
import os

from gemini_summarizer import GeminiDocumentSummarizer
from utils.file_handler import save_uploaded_file, validate_file  # ✅ Fixed path

summarize_bp = Blueprint('summarize', __name__)
summarizer = GeminiDocumentSummarizer()

@summarize_bp.route('/file', methods=['POST'])
def handle_file_summarization():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
            
        file = request.files['file']
        if not validate_file(file.filename):
            return jsonify({"error": "Invalid file type"}), 400

        file_path = save_uploaded_file(file)
        summary = summarizer.summarize(file_path, is_file=True)
        os.remove(file_path)  # Cleanup temporary file
        
        return jsonify({"summary": summary})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@summarize_bp.route('/text', methods=['POST'])
def handle_text_summarization():
    try:
        data = request.get_json()
        if 'text' not in data or not data['text'].strip():
            return jsonify({"error": "No text provided"}), 400
            
        summary = summarizer.summarize(data['text'], is_file=False)
        return jsonify({"summary": summary})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
