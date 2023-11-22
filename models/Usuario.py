from config.db import app, db, ma


class Usuario(db.Model):
    __tablename__ = 'User'

    id  = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    

    def __init__(self, email, password_hash, nombre):
        self.email = email
        self.password_hash = password_hash
        self.nombre = nombre
        
        
   
with app.app_context():
    db.create_all()

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','email','password_hash', 'nombre')