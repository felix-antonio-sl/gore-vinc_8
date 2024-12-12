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