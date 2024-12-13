from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
import ell

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Configuración de JWT
    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
    app.config["JWT_SECRET_KEY"] = app.config['SECRET_KEY']  # Usa la misma clave secreta
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600  # 1 hora
    
    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Asegúrate de que las importaciones de los modelos estén aquí
    from app.models import user, chat, document
    
    ell.init(verbose=True)
    
    # Registrar blueprints
    from app.chat import bp as chat_bp
    app.register_blueprint(chat_bp, url_prefix='/chat')
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Ruta raíz
    @app.route('/')
    def index():
        return redirect(url_for('chat.widget'))
    
    ell.init(verbose=True)
    
    return app 