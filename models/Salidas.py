from config.bd import db, ma, app

class Salida(db.Model):
    __tablename__ = 'Salida'
    id = db.Column(db.Integer, primary_key=True)
    id_producto= db.Column(db.Integer, db.ForeignKey('Producto.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('User.id'))
    id_vehiculo = db.Column(db.Integer, db.ForeignKey('Vehiculo.id'))
    fecha = db.Column(db.String(50))
    cantidad_peso = db.Column(db.Integer)
    cantidad_unidades = db.Column(db.Integer)
    unidad_de_medida = db.Column(db.String(50))
    


    def __init__(self, id_producto, id_user, id_vehiculo ,fecha, cantidad_peso, 
                 cantidad_unidades, unidad_de_medida):
        #self.id = id
        self.id_producto = id_producto
        self.id_user = id_user
        self.vehiculo = id_vehiculo
        self.fecha = fecha
        self.cantidad_peso = cantidad_peso
        self.cantidad_unidades = cantidad_unidades
        self.unidad_de_medida = unidad_de_medida
       

with app.app_context():
    db.create_all()

class SalidaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_producto', 'id_User','id_vehiculo', 'fecha', 
                  'cantidad_peso', 'cantidad_unidades', 'unidad_de_medida')
        