# Documentación del Proyecto

## Estructura del Proyecto

```
  .cursorignore
  documentacion_proyecto.md
  config.py
  requirements.txt
  README.md
  .gitignore
  app.py
  generate_project_docs.py
app/
  __init__.py
  chat/
    __init__.py
    routes.py
  auth/
    routes.py
  models/
    user.py
    __init__.py
    chat.py
    document.py
  api/
    __init__.py
    routes.py
  templates/
    base.html
    widget/
      chat.html
    chat/
      index.html
    components/
      message.html
      navbar.html
  services/
    lmps.py
    ell_service.py
scripts/
  load_documents.py
instance/
```

## Código Fuente

### ./.cursorignore

```
# Directorios de dependencias
node_modules/
venv/
.env/
__pycache__/
.venv/
pip-log.txt
pip-delete-this-directory.txt

# Archivos de construcción y caché
dist/
build/
*.pyc
__pycache__/
.cache/
.pytest_cache/
.coverage
htmlcov/
.webassets-cache
.parcel-cache/

# Archivos de sistema
.DS_Store
Thumbs.db
*.bak

# Archivos de IDE y editor
.vscode/
.idea/
*.swp
*.swo
*.sublime-workspace
*.sublime-project

# Archivos de logs
*.log
logs/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Archivos de configuración local
.env
.env.local
*.local
instance/
.flaskenv
config.py

# Base de datos
*.db
*.sqlite
*.sqlite3
migrations/

# Git
.git/
.gitignore
.gitattributes

# Node/Frontend
node_modules/
.npm
.yarn/
dist/
.cache/
.parcel-cache/
tailwind.config.js.backup
package-lock.json
yarn.lock

# APIs y Secretos
*api_key*
*secret*
.secrets/
credentials.json
token.json

# Archivos temporales
tmp/
temp/
.temp/
.tmp/ 
```

### ./.gitignore

```
.env
__pycache__/
*.pyc
instance/
.pytest_cache/
.coverage
htmlcov/
dist/
build/
*.egg-info/ 
```

### ./README.md

```markdown
# 🤖 Bot Experto IA - Plantilla

Una plantilla moderna y eficiente para crear bots expertos con capacidad de procesamiento de documentación especializada y contexto personalizado. Diseñado para ser fácilmente integrable en sitios web existentes.

## ✨ Características

- 🧠 Procesamiento de documentación experta y conocimiento especializado
- 🌐 Interfaz web moderna y responsive con HTMX y DaisyUI
- 📚 Gestión de documentos y contexto personalizado
- 🔄 Actualizaciones en tiempo real sin recargar la página
- 🛠️ Fácil integración en sitios web existentes
- 🔒 Gestión segura de configuraciones y API keys

## 🛠️ Tecnologías

- **Backend**: Flask (Python)
- **Base de Datos**: SQLite
- **IA**: ell-ai (procesamiento y embeddings)
- **Frontend**:
  - HTMX para interactividad sin JavaScript
  - DaisyUI/Tailwind para diseño moderno
  - Componentes dinámicos sin framework

## 📋 Requisitos Previos

- Python 3.9+
- Node.js 16+
- pip
- npm o yarn

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone [url-del-repositorio]
cd [nombre-del-proyecto]
```

2. **Configurar el entorno virtual de Python**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Instalar dependencias de frontend**
```bash
npm install
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. **Inicializar la base de datos**
```bash
flask db upgrade
```

## 💻 Uso

1. **Iniciar el servidor de desarrollo**
```bash
flask run
```

2. **Cargar documentación experta**
```bash
python scripts/load_documents.py [ruta-a-documentos]
```

## 🔧 Configuración

### Estructura de Documentos
```
documents/
├── knowledge/
│   ├── domain1/
│   └── domain2/
└── config/
    └── bot_config.yaml
```

### Configuración del Bot
```yaml
# config/bot_config.yaml
name: "Bot Experto"
domains:
  - nombre: "Dominio1"
    fuentes: ["documents/knowledge/domain1"]
  - nombre: "Dominio2"
    fuentes: ["documents/knowledge/domain2"]
```

## 🔌 Integración en Sitios Web

### Método 1: iFrame
```html
<iframe src="https://tu-bot.dominio/chat" width="400" height="600"></iframe>
```

### Método 2: Web Component
```html
<script src="https://tu-bot.dominio/static/bot-widget.js"></script>
<expert-bot domain="dominio1"></expert-bot>
```

## 📚 Estructura del Proyecto
```
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── templates/
├── documents/
├── migrations/
├── static/
├── tests/
└── config/
```

## 🛡️ Seguridad

- Autenticación mediante tokens JWT
- Rate limiting para prevenir abusos
- Sanitización de entrada de usuario
- Validación de documentos
- Cifrado de datos sensibles

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, revisa las guías de contribución antes de enviar un PR.

## 📄 Licencia

MIT License - ver [LICENSE](LICENSE) para más detalles.

## 🆘 Soporte

- Documentación completa en `/docs`
- Issues en GitHub
- Wiki del proyecto

---
⭐️ Si este proyecto te resulta útil, considera darle una estrella en GitHub. 
```

### ./app.py

```python
from app import create_app
from config import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run() 
```

### ./config.py

```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEFAULT_MODEL = "gpt-4o"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 
```

### ./documentacion_proyecto.md

```markdown

```

### ./generate_project_docs.py

```python
import os
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern

# Directorios que siempre queremos ignorar
DEFAULT_IGNORE = {
    'venv', 'env', '.env', '.venv', '__pycache__', 
    'node_modules', '.git', '.idea', '.vscode',
    'dist', 'build', 'eggs', '.eggs',
    'migrations', 'docsaux', 'ell_store'
}

def load_gitignore(path):
    """Carga las reglas del .gitignore"""
    gitignore_path = os.path.join(path, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            spec = PathSpec.from_lines(GitWildMatchPattern, f.readlines())
        return spec
    return None

def get_file_extension(filename):
    """Obtiene la extensión del archivo para el bloque de código"""
    ext = os.path.splitext(filename)[1].lower()
    ext_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.html': 'html',
        '.css': 'css',
        '.md': 'markdown',
        '.json': 'json',
        '.yml': 'yaml',
        '.yaml': 'yaml',
    }
    return ext_map.get(ext, '')

def generate_project_tree(start_path, output_file, relevant_files):
    """Genera un archivo Markdown con el árbol del proyecto y el contenido de archivos relevantes"""
    gitignore = load_gitignore(start_path)
    all_files = []
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('# Documentación del Proyecto\n\n')
        f.write('## Estructura del Proyecto\n\n```\n')
        
        for root, dirs, files in os.walk(start_path):
            # Filtrar directorios por defecto
            dirs[:] = [d for d in dirs if d not in DEFAULT_IGNORE]
            
            # Filtrar por gitignore
            rel_root = os.path.relpath(root, start_path)
            if gitignore:
                dirs[:] = [d for d in dirs if not gitignore.match_file(os.path.join(rel_root, d))]
                files = [f for f in files if not gitignore.match_file(os.path.join(rel_root, f))]
            
            # Guardar archivos para mostrar después
            for file in files:
                full_path = os.path.join(rel_root, file)
                if full_path != output_file:  # Evitar incluir el archivo de documentación
                    all_files.append(full_path)
            
            level = rel_root.count(os.sep)
            indent = '  ' * level
            if root != start_path:
                f.write(f'{indent}{os.path.basename(root)}/\n')
            subindent = '  ' * (level + 1)
            for file in files:
                f.write(f'{subindent}{file}\n')
        
        f.write('```\n\n')
        
        f.write('## Código Fuente\n\n')
        for file_path in sorted(all_files):
            if os.path.exists(file_path):
                ext = get_file_extension(file_path)
                f.write(f'### {file_path}\n\n```{ext}\n')
                try:
                    with open(file_path, 'r', encoding='utf-8') as source_file:
                        f.write(source_file.read())
                except UnicodeDecodeError:
                    f.write('// Archivo binario o con codificación no soportada\n')
                f.write('\n```\n\n')

if __name__ == '__main__':
    project_path = '.'
    relevant_files = [
        'app/chat/routes.py',
        'app/__init__.py',
        'app/chat/__init__.py'
    ]
    
    generate_project_tree(project_path, 'documentacion_proyecto.md', relevant_files)
```

### ./requirements.txt

```
flask
Flask-SQLAlchemy
Flask-Migrate
python-dotenv
ell-ai
openai
anthropic
flask-cors
flask-jwt-extended
gunicorn
python-magic
validators
tiktoken
tenacity
pyyaml
markdown
beautifulsoup4
Werkzeug
Jinja2
itsdangerous
click
blinker
cachelib

```

### app/__init__.py

```python
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
    app.config["JWT_SECRET_KEY"] = app.config['SECRET_KEY']
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
    
    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Importar modelos
    from app.models import user, chat, document
    
    # Inicializar ell una sola vez
    ell.init(
        store=app.config.get('ELL_STORE_PATH', './ell_store'),
        verbose=True,
        autocommit=True
    )
    
    # Registrar blueprints
    from app.chat import bp as chat_bp
    app.register_blueprint(chat_bp, url_prefix='/chat')
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Ruta raíz
    @app.route('/')
    def index():
        return redirect(url_for('chat.widget'))
    
    return app 
```

### app/api/__init__.py

```python
from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import routes 
```

### app/api/routes.py

```python
from flask import jsonify, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import bp
from app.models.document import Document
from app.services.ell_service import ell_service

@bp.route('/health')
def health():
    """Endpoint para verificar el estado del servicio."""
    return jsonify({
        'status': 'ok',
        'service': 'bot-experto-api'
    })

@bp.route('/query', methods=['POST'])
@jwt_required()
async def query():
    """Endpoint para realizar consultas a través de la API."""
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({'error': 'Se requiere una consulta'}), 400
            
        query = data['query']
        if len(query) > 500:
            return jsonify({'error': 'La consulta es demasiado larga'}), 400
        
        user_id = get_jwt_identity()
        current_app.logger.info(f"API consulta recibida de usuario {user_id}: {query}")
            
        response = await ell_service.query_with_context(
            query=query,
            max_results=data.get('max_results', 5)
        )
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
                             
    except Exception as e:
        current_app.logger.error(f"Error en API query: {str(e)}")
        return jsonify({
            'error': 'Error interno del servidor',
            'details': str(e)
        }), 500

@bp.route('/documents', methods=['GET'])
@jwt_required()
def get_documents():
    """Endpoint para obtener documentos disponibles."""
    try:
        domain = request.args.get('domain')
        query = Document.query
        
        if domain:
            query = query.filter_by(domain=domain)
            
        documents = query.all()
        return jsonify({
            'documents': [
                {
                    'id': doc.id,
                    'title': doc.title,
                    'domain': doc.domain,
                    'created_at': doc.created_at.isoformat()
                }
                for doc in documents
            ]
        })
        
    except Exception as e:
        current_app.logger.error(f"Error obteniendo documentos: {str(e)}")
        return jsonify({
            'error': 'Error interno del servidor',
            'details': str(e)
        }), 500 
```

### app/auth/routes.py

```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    
    if user and user.check_password(data.get('password')):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    
    return jsonify({'error': 'Credenciales inválidas'}), 401

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(username=data.get('username')).first():
        return jsonify({'error': 'El usuario ya existe'}), 400
        
    user = User(
        username=data.get('username'),
        email=data.get('email')
    )
    user.set_password(data.get('password'))
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'Usuario registrado exitosamente'}), 201 
```

### app/chat/__init__.py

```python
from flask import Blueprint

bp = Blueprint('chat', __name__)

from app.chat import routes 
```

### app/chat/routes.py

```python
from flask import current_app, render_template, request, jsonify
from werkzeug.exceptions import BadRequest
from datetime import datetime
from . import bp
from app.services.ell_service import ell_service
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from config import Config
import ell
from ell import Message

@bp.route('/query', methods=['POST'])
@jwt_required()
async def query():
    """Endpoint para procesar consultas del chat."""
    try:
        query = request.form.get('query')
        if not query:
            raise BadRequest("Se requiere una consulta")
            
        if len(query) > 500:
            raise BadRequest("La consulta es demasiado larga")
        
        user_id = get_jwt_identity()
        current_app.logger.info(f"Consulta recibida de usuario {user_id}: {query}")
        
        # Crear mensajes según la documentación de ell
        messages = [
            Message(role="system", content="You are a helpful assistant."),
            Message(role="user", content=query)
        ]
        
        try:
            # Usar await correctamente
            response = await ell_service.query_with_context(
                query=messages,
                context=[]
            )
            
            # Renderizar template de manera síncrona (render_template no es async)
            return render_template('components/message.html',
                              message=response,
                              is_user=False,
                              timestamp=datetime.utcnow())
                                
        except Exception as e:
            current_app.logger.error(f"Error en ELL query: {str(e)}")
            raise
                             
    except BadRequest as e:
        current_app.logger.warning(f"Error de validación: {str(e)}")
        return render_template('components/message.html', 
                           error=str(e)), 400
    except Exception as e:
        current_app.logger.error(f"Error en query: {str(e)}")
        return render_template('components/message.html',
                           error="Error interno del servidor"), 500

@bp.route('/messages', methods=['GET'])
@jwt_required()
def get_messages():
    """Obtiene el historial de mensajes del usuario."""
    user_id = get_jwt_identity()
    try:
        # Implementar lógica para obtener mensajes
        messages = []  # Obtener de la base de datos
        return render_template('components/message_history.html',
                             messages=messages)
    except Exception as e:
        current_app.logger.error(f"Error al obtener mensajes: {str(e)}")
        return render_template('components/message.html',
                             error="Error al cargar mensajes"), 500

@bp.route('/widget')
def widget():
    """Retorna el HTML del widget del chat."""
    # Generar un token de acceso para el widget
    access_token = create_access_token(identity="widget_user")
    
    return render_template('widget/chat.html', access_token=access_token)

@ell.simple(model=Config.DEFAULT_MODEL)
def generate_response(prompt: str):
    """You are a helpful AI assistant."""
    return prompt

@bp.route('/chat', methods=['POST'])
def chat():
    message = request.form.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
        
    try:
        response = generate_response(message)
        return render_template('components/message.html', 
                             message=response,
                             is_user=False)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

### app/models/__init__.py

```python
from app.models.user import User
from app.models.chat import Chat
from app.models.document import Document 
```

### app/models/chat.py

```python
from datetime import datetime
from app import db

class Chat(db.Model):
    __tablename__ = 'chats'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), 
                       nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    domain = db.Column(db.String(64), index=True)
    
    messages = db.relationship('Message', backref='chat', lazy='dynamic',
                             cascade='all, delete-orphan')
    
    __table_args__ = (
        db.Index('idx_chat_user_date', 'user_id', 'created_at'),
    )

class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id', ondelete='CASCADE'), 
                       nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    __table_args__ = (
        db.CheckConstraint(role.in_(['user', 'assistant']), name='valid_role'),
    )
```

### app/models/document.py

```python
from app import db

class Document(db.Model):
    __tablename__ = 'documents'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text, nullable=False)
    domain = db.Column(db.String(64), nullable=False)
    embedding = db.Column(db.PickleType)
    doc_metadata = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, server_default=db.func.now()) 
```

### app/models/user.py

```python
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    is_active = db.Column(db.Boolean, default=True)
    chats = db.relationship('Chat', backref='user', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password) 
```

### app/services/ell_service.py

```python
import ell
from typing import List, Dict, Any
from flask import current_app, Flask
from PIL import Image

class EllService:
    def __init__(self, app: Flask = None):
        self.store_path = None
        self.lmps = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        """Inicializa la extensión con la aplicación Flask."""
        # Registrar configuración por defecto
        app.config.setdefault('ELL_STORE_PATH', './ell_store')
        app.config.setdefault('DEFAULT_MODEL', 'gpt-4o')
        app.config.setdefault('VISION_MODEL', 'gpt-4o')
        
        self.store_path = app.config['ELL_STORE_PATH']
        
        # Inicializar ell con almacenamiento y autocommit
        ell.init(store=self.store_path, autocommit=True, verbose=True)
        
        # Inicializar LMPs
        self.lmps = self._create_lmps(app)
        
        # Opcional: registrar en extensiones de Flask
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['ell'] = self

    def _create_lmps(self, app):
        return {
            'basic': self._create_basic_lmp(app),
            'chat': self._create_chat_lmp(app),
            'creative': self._create_creative_lmp(app)
        }

    @staticmethod
    def _create_basic_lmp(app):
        @ell.simple(model=app.config['DEFAULT_MODEL'])
        def basic_query(query: str):
            """Asistente básico para consultas simples."""
            return query
        return basic_query

    @ell.complex(model="gpt-4o")
    async def query_with_context(self, query: List[ell.Message], context: List[str] = None) -> str:
        """You are an expert assistant that provides detailed answers based on given context."""
        try:
            # Si hay contexto, lo añadimos como mensaje de sistema adicional
            messages = query
            if context:
                context_message = ell.system(f"Context: {' '.join(context)}")
                messages.insert(1, context_message)
            
            # Obtener la respuesta del modelo
            response = await ell.chat(messages)
            
            # Extraer el contenido del mensaje
            if isinstance(response, ell.Message):
                return response.content
            return str(response)
            
        except Exception as e:
            current_app.logger.error(f"Error en ELL query: {str(e)}")
            raise

    @ell.complex(model="gpt-4o")
    def analyze_image(self, image: Image.Image, query: str) -> List[ell.Message]:
        """You are a vision expert that can analyze images and provide detailed descriptions."""
        return [
            ell.system("Analyze the image and answer the query about it."),
            ell.user([image, query])
        ]

    @ell.tool()
    def search_documents(self: 'EllService', query: str, max_results: int = 5) -> str:
        """Search through available documents and return relevant content."""
        return f"Relevant content for: {query}"

    @ell.complex(model="gpt-4", tools=[search_documents])
    def advanced_query(self, query: str) -> List[ell.Message]:
        """You are an advanced assistant that can search through documents and provide comprehensive answers."""
        return [
            ell.system("Use the search tool to find relevant information before answering."),
            ell.user(query)
        ]

# Instancia global del servicio
ell_service = EllService() 
```

### app/services/lmps.py

```python
from typing import List
import ell
from flask import current_app

def create_lmps(app=None):
    """Factory para crear Language Model Programs."""
    
    @ell.simple(model=app.config.get('DEFAULT_MODEL', 'gpt-4'), temperature=0.7)
    def chat_response(message: str):
        """You are a helpful and friendly assistant."""
        return message

    @ell.complex(model=app.config.get('DEFAULT_MODEL', 'gpt-4'))
    def structured_chat(message_history: List[ell.Message]) -> List[ell.Message]:
        """You are a professional assistant that maintains context through conversations."""
        return [
            ell.system("Maintain conversation context and provide helpful responses."),
        ] + message_history

    @ell.simple(model=app.config.get('DEFAULT_MODEL', 'gpt-4'), temperature=1.0, n=3)
    def generate_alternatives(prompt: str):
        """You are a creative assistant that generates multiple alternative responses."""
        return f"Generate three different responses for: {prompt}"

    @ell.complex(model=app.config.get('DEFAULT_MODEL', 'gpt-4'), temperature=0.1)
    def select_best_response(responses: List[str]) -> List[ell.Message]:
        """You are an expert at selecting the most appropriate response."""
        return [
            ell.system("Select the best response based on clarity, relevance, and helpfulness."),
            ell.user(f"Choose the best response from these options:\n{'\n'.join(responses)}")
        ]
    
    return {
        'chat_response': chat_response,
        'structured_chat': structured_chat,
        'generate_alternatives': generate_alternatives,
        'select_best_response': select_best_response
    } 
```

### app/templates/base.html

```html
<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Bot Experto{% endblock %}</title>
    
    <!-- HTMX con versión actualizada -->
    <script src="https://unpkg.com/htmx.org@2.0.3" 
            integrity="sha384-0895/pl2MU10Hqc6jd4RvrthNlDiE9U1tWmX7WRESftEDRosgxNsQG/Ze9YMRzHq" 
            crossorigin="anonymous"></script>
    
    <!-- Configuración global de HTMX -->
    <meta name="htmx-config" content='{
        "timeout": 10000,
        "historyCacheSize": 20,
        "defaultSwapStyle": "innerHTML",
        "defaultFocusScroll": true,
        "globalViewTransitions": true
    }'>
    
    <!-- DaisyUI actualizado -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.19/dist/full.min.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.tailwindcss.com"></script>
    
    {% block extra_head %}{% endblock %}
</head>
<body hx-boost="true" class="min-h-screen bg-base-200">
    <div id="content" class="container mx-auto px-4">
        {% block content %}{% endblock %}
    </div>
</body>
</html> 
```

### app/templates/chat/index.html

```html
{% extends "base.html" %}

{% block content %}
<div class="container mx-auto p-4">
    <div id="chat-messages" class="space-y-4 mb-4">
        <!-- Los mensajes se insertarán aquí -->
    </div>

    <form hx-post="{{ url_for('chat.query')|e }}"
          hx-target="#chat-messages"
          hx-swap="beforeend transition:true"
          hx-trigger="submit"
          hx-indicator=".htmx-indicator"
          hx-on::after-request="this.reset()"
          class="flex gap-2">
          
        <input type="text" 
               name="query" 
               maxlength="500"
               class="input input-bordered flex-grow"
               placeholder="Escribe tu pregunta..."
               hx-disable-element="button"
               required>
               
        <button type="submit" 
                class="btn btn-primary"
                data-loading-disable>
            <span class="htmx-indicator">
                <span class="loading loading-spinner"></span>
            </span>
            <span>Enviar</span>
        </button>
    </form>
</div>
{% endblock %} 
```

### app/templates/components/message.html

```html
<div class="chat-message {{ 'chat-message-user' if is_user else 'chat-message-assistant' }}"
     hx-swap-oob="true">
    {% if error %}
        <div class="alert alert-error shadow-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>{{ error|e }}</span>
        </div>
    {% else %}
        <div class="flex items-start gap-2 p-2 rounded-lg {{ 'bg-base-200' if not is_user else '' }}">
            <div class="avatar">
                <div class="w-8 rounded">
                    <img src="{{ url_for('static', filename='img/' + ('user.png' if is_user else 'assistant.png')) }}" 
                         alt="{{ 'Usuario' if is_user else 'Asistente' }}"
                         loading="lazy">
                </div>
            </div>
            <div class="flex-grow">
                <div class="prose max-w-none">
                    {{ message|safe }}
                </div>
                <div class="text-xs text-gray-500 mt-1">
                    {{ timestamp.strftime('%H:%M') }}
                </div>
            </div>
        </div>
    {% endif %}
</div> 
```

### app/templates/components/navbar.html

```html
<div class="navbar bg-base-100 shadow-lg">
    <div class="navbar-start">
        <div class="dropdown">
            <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
                <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" />
                </svg>
            </div>
            <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
                <li><a href="{{ url_for('chat.index') }}">Chat</a></li>
                <li><a href="{{ url_for('docs.index') }}">Documentación</a></li>
            </ul>
        </div>
        <a class="btn btn-ghost text-xl">Bot Experto</a>
    </div>
    
    <div class="navbar-center hidden lg:flex">
        <ul class="menu menu-horizontal px-1">
            <li><a href="{{ url_for('chat.index') }}">Chat</a></li>
            <li><a href="{{ url_for('docs.index') }}">Documentación</a></li>
        </ul>
    </div>
    
    <div class="navbar-end">
        <div class="dropdown dropdown-end">
            <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
                <div class="w-10 rounded-full">
                    <img alt="avatar" src="{{ url_for('static', filename='images/avatar.png') }}" />
                </div>
            </div>
            <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
                <li><a href="{{ url_for('auth.profile') }}">Perfil</a></li>
                <li><a href="{{ url_for('auth.logout') }}">Cerrar Sesión</a></li>
            </ul>
        </div>
    </div>
</div> 
```

### app/templates/widget/chat.html

```html
<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Widget</title>
    <script src="https://unpkg.com/htmx.org@2.0.3" 
            integrity="sha384-0895/pl2MU10Hqc6jd4RvrthNlDiE9U1tWmX7WRESftEDRosgxNsQG/Ze9YMRzHq" 
            crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.19/dist/full.min.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-transparent">
    <div class="card bg-base-100 shadow-xl h-full">
        <div class="card-body p-4">
            <div id="chat-messages" 
                 class="h-[400px] overflow-y-auto space-y-2 mb-4"
                 hx-get="/chat/messages"
                 hx-trigger="load"
                 hx-swap="innerHTML">
            </div>
            
            <form hx-post="/chat/query"
                  hx-target="#chat-messages"
                  hx-swap="beforeend"
                  hx-headers='{"Authorization": "Bearer {{ access_token }}"}'
                  class="flex gap-2">
                <input type="text" 
                       name="query" 
                       class="input input-bordered input-sm flex-grow"
                       placeholder="Escribe tu pregunta...">
                <button type="submit" 
                        class="btn btn-primary btn-sm">
                    Enviar
                </button>
            </form>
        </div>
    </div>
    
    <script>
        document.body.addEventListener('htmx:afterRequest', function(evt) {
            if (evt.detail.successful) {
                const messages = evt.detail.target;
                messages.scrollTop = messages.scrollHeight;
                evt.detail.elt.reset();
            }
        });
    </script>
</body>
</html> 
```

### scripts/load_documents.py

```python
import sys
import os
import yaml
from app import create_app, db
from app.models.document import Document
from app.services.ell_service import ell_service

def load_documents(path):
    app = create_app()
    with app.app_context():
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(('.txt', '.md', '.pdf')):
                    file_path = os.path.join(root, file)
                    domain = os.path.basename(os.path.dirname(file_path))
                    
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    doc = Document(
                        title=file,
                        content=content,
                        domain=domain
                    )
                    db.session.add(doc)
        db.session.commit()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python load_documents.py [ruta-a-documentos]")
        sys.exit(1)
    load_documents(sys.argv[1]) 
```

