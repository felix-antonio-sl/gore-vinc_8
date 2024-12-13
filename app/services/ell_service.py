import ell
from typing import List, Dict, Any
from flask import current_app, Flask
from PIL import Image

class EllService:
    def __init__(self, app: Flask = None):
        self.store_path = None
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
        
        # Opcional: registrar en extensiones de Flask
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['ell'] = self

    @ell.simple(model="gpt-4o")
    def basic_query(self, query: str):
        """You are a helpful assistant that provides clear and concise answers."""
        return query

    @ell.complex(model="gpt-4o")
    async def query_with_context(self, query: str, context: List[str]) -> str:
        """You are an expert assistant that provides detailed answers based on given context."""
        try:
            # Crear lista de mensajes según la documentación de ELL
            messages = [
                ell.Message(
                    content="Soy un asistente experto que proporciona respuestas detalladas basadas en el contexto dado.",
                    role="system"
                ),
                ell.Message(
                    content=[
                        "Contexto:\n" + "\n".join(context),
                        "Consulta: " + query
                    ],
                    role="user"
                )
            ]
            
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