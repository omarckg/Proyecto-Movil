from config.db import app, db, ma

class Categoria(db.Model):
    __tablename__ = 'Categoria'

    id  = db.Column(db.Integer, primary_key=True)
    id_bodega = db.Column(db.Integer, db.ForeignKey('Bodega.id'))
    nombre = db.Column(db.String(500))

    def __init__(self, id_bodega, nombre):
        self.id_bodega = id_bodega
        self.nombre = nombre

with app.app_context():
    db.create_all()

class CategoriasSchema(ma.Schema):
    class Meta:
        fields = ('id','id_bodega','nombre')