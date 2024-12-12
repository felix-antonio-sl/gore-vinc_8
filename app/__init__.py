from flask import Flask
from config import Config
import ell

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar ell con las API keys
    ell.init(
        openai_api_key=app.config['OPENAI_API_KEY'],
        anthropic_api_key=app.config['ANTHROPIC_API_KEY']
    )
    
    # Registrar blueprints
    from app.chat import chat_bp
    app.register_blueprint(chat_bp)
    
    return app 