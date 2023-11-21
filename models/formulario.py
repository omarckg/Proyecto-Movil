from config.db import db, ma, app

class Formulario(db.Model):
    __tablename__ = 'formulario'
    id = db.Column(db.Integer, primary_key=True)
    id_producto= db.Column(db.Integer, db.ForeignKey('Producto.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('User.id'))
    id_vehiculo = db.Column(db.Integer, db.ForeignKey('Vehiculo.id'))
    
    


    def __init__(self, id_producto, id_user, id_vehiculo):
        self.id = id
        self.id_producto = id_producto
        self.id_user = id_user
        self.vehiculo = id_vehiculo
        
       

with app.app_context():
    db.create_all()

class FormulariosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_producto', 'id_User','id_vehiculo')
        