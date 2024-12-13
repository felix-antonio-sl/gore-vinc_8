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
def query():
    """Endpoint para procesar consultas del chat."""
    try:
        query = request.form.get('query')
        if not query:
            raise BadRequest("Se requiere una consulta")
            
        if len(query) > 500:
            raise BadRequest("La consulta es demasiado larga")
        
        user_id = get_jwt_identity()
        current_app.logger.info(f"Consulta recibida de usuario {user_id}: {query}")
        
        # Crear mensajes usando las funciones helper de ell
        messages = [
            ell.system("You are a helpful assistant."),
            ell.user(query)
        ]
        
        try:
            # La respuesta será un Message del asistente
            assistant_message = ell_service.query_with_context(messages=messages)
            
            if not assistant_message:
                raise ValueError("No se recibió respuesta del modelo")
            
            # Extraer el contenido del mensaje del asistente
            response_text = assistant_message.content if hasattr(assistant_message, 'content') else str(assistant_message)
            
            return render_template('components/message.html',
                              message=response_text,
                              is_user=False,
                              timestamp=datetime.utcnow())
                                
        except Exception as e:
            current_app.logger.error(f"Error en ELL query: {str(e)}")
            return render_template('components/message.html',
                              error="Error al procesar la consulta"), 500
                             
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