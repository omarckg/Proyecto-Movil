from config.bd import db, ma, app

class Producto(db.Model):
    __tablename__ = 'Producto'

    id  = db.Column(db.Integer, primary_key=True)
    id_categoria = db.Column(db.Integer,db.ForeignKey('Categoria.id'))
    nombre= db.Column(db.String(500))
    fecha_consumo = db.Column(db.String(500))
    peso = db.Column(db.Double)

    def __init__(self,id_categoria,nombre,fecha_consumo, peso):
        self.id_categoria = id_categoria
        self.nombre = nombre   
        self.fecha_consumo = fecha_consumo
        self.peso = peso

with app.app_context():
    db.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id','id_categoria','nombre','fecha_consumo', 'peso')