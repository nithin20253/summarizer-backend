import os
from werkzeug.utils import secure_filename
from flask import current_app
from flask_cors import CORS
def save_uploaded_file(file) -> str:
    filename = secure_filename(file.filename)
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    return file_path

def validate_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']
