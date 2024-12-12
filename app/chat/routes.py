from flask import current_app, render_template, request, jsonify
from werkzeug.exceptions import BadRequest
from datetime import datetime
from . import bp
from app.services.ell_service import ell_service
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import Config
import ell

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
            
        response = await ell_service.query_with_context(
            query=query,
            max_results=5
        )
        
        return render_template('components/message.html',
                             message=response,
                             is_user=False,
                             timestamp=datetime.utcnow())
                             
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
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Chat Experto</title>
        <script src="https://unpkg.com/htmx.org@2.0.3" 
                integrity="sha384-0895/pl2MU10Hqc6jd4RvrthNlDiE9U1tWmX7WRESftEDRosgxNsQG/Ze9YMRzHq" 
                crossorigin="anonymous"></script>
        <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.19/dist/full.min.css" rel="stylesheet" type="text/css" />
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            .chat-container {
                height: 100vh;
                display: flex;
                flex-direction: column;
            }
            .messages {
                flex-grow: 1;
                overflow-y: auto;
                padding: 1rem;
            }
        </style>
    </head>
    <body class="bg-base-200">
        <div class="chat-container">
            <div class="messages" id="chat-messages">
                <!-- Los mensajes se insertarán aquí -->
            </div>
            
            <form class="p-4 bg-base-100 shadow-lg"
                  hx-post="/chat/query"
                  hx-target="#chat-messages"
                  hx-swap="beforeend">
                <div class="flex gap-2">
                    <input type="text" 
                           name="query" 
                           class="input input-bordered flex-grow"
                           placeholder="Escribe tu pregunta...">
                    <button type="submit" class="btn btn-primary">Enviar</button>
                </div>
            </form>
        </div>
        
        <script>
            document.body.addEventListener('htmx:afterRequest', function(evt) {
                if (evt.detail.successful) {
                    evt.detail.target.scrollTop = evt.detail.target.scrollHeight;
                    evt.detail.elt.querySelector('input').value = '';
                }
            });
        </script>
    </body>
    </html>
    """

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