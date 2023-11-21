from config.bd import app, db, ma
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

class Conductor(db.Model):
    __tablename__ = 'Conductor'

    id  = db.Column(db.Integer, primary_key=True)
    telefono = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    

    def __init__(self, telefono, nombre):
        self.telefono = telefono
        self.nombre = nombre
        
        
with app.app_context():
    db.create_all()

class ConductorSchema(ma.Schema):
    class Meta:
        fields = ('id','telefono', 'nombre')