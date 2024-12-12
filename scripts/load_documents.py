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