from config.db import app, db, ma

class Vehiculo(db.Model):
    __tablename__ = 'Vehiculo'

    id  = db.Column(db.Integer, primary_key=True)
    id_conductor = db.Column(db.Integer, db.ForeignKey('Conductor.id'))
    matricula = db.Column(db.String(6), unique=True)
    

    def __init__(self, id_conductor,matricula ):
        self.id_conductor = id_conductor
        self.matricula = matricula
        

with app.app_context():
    db.create_all()

class VehiculosSchema(ma.Schema):
    class Meta:
        fields = ('id','id_conductor' ,'matricula' )