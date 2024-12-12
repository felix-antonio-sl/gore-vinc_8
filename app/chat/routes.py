from flask import render_template, jsonify, request
from app.chat import bp
from app.services.ell_service import ell_service
from flask_jwt_extended import jwt_required, get_jwt_identity

@bp.route('/query', methods=['POST'])
@jwt_required()
async def query():
    """Endpoint para realizar consultas al bot."""
    query = request.form.get('query')
    
    if not query:
        return render_template('components/message.html', 
                             error="Se requiere una consulta"), 400
    
    try:
        response = await ell_service.query_with_context(
            query=query,
            max_results=5
        )
        return render_template('components/message.html',
                             message=response,
                             is_user=False)
    except Exception as e:
        return render_template('components/message.html',
                             error=str(e)), 500

@bp.route('/widget')
def widget():
    """Retorna el HTML del widget del chat."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Chat Experto</title>
        <script src="https://unpkg.com/htmx.org"></script>
        <link href="https://cdn.jsdelivr.net/npm/daisyui@3.9.4/dist/full.css" rel="stylesheet">
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

@bp.route('/messages', methods=['GET'])
@jwt_required()
def get_messages():
    """Obtiene el historial de mensajes del usuario."""
    user_id = get_jwt_identity()
    # Aquí implementarías la lógica para obtener los mensajes del usuario
    return jsonify({'messages': []}) 