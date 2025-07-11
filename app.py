from flask import Flask
from flask_cors import CORS
from routes.summarize import summarize_bp
import os

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:8080"])  # Frontend port

    # Configuration
    app.config.update(
        UPLOAD_FOLDER=os.path.join(os.path.dirname(__file__), 'uploads'),
        MAX_CONTENT_LENGTH=16 * 1024 * 1024,  # 16MB
        ALLOWED_EXTENSIONS={'pdf', 'docx', 'txt'}
    )

    api_key = os.environ.get('GEMINI_API_KEY')  # Optional usage, currently unused

    # Create uploads directory
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register blueprint
    app.register_blueprint(summarize_bp, url_prefix='/api')

    return app

# ✅ Make it accessible to Gunicorn
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # fallback to 5000 for local dev
    app.run(host='0.0.0.0', port=port)
