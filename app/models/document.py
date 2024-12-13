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