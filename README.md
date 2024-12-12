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