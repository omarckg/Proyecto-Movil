from flask import Blueprint, request, jsonify, json
from config.db import app, db, ma
from models.vehiculos import Vehiculo, VehiculosSchema


ruta_Vehiculo = Blueprint("ruta_Vehiculo",__name__)

Vehiculo_schema = VehiculosSchema()
Vehiculos_schema = VehiculosSchema(many=True)

@ruta_Vehiculo.route('/Vehiculo', methods=['GET'])
def vehiculo():
    resultall = Vehiculo.query.all() # Select * from Pasajeros
    resultado_Vehiculo = Vehiculos_schema.dump(resultall)
    return jsonify(resultado_Vehiculo)

@ruta_Vehiculo.route('/saveVehiculo', methods=['POST'])
def save():
    #id = request.json['id']
    id_conductor = request.json['id_conductor']
    matricula = request.json['matricula']
    new_vehiculo = Vehiculo(
        id_conductor,
        matricula,

    )

    db.session.add(new_vehiculo)
    db.session.commit()
    return "Datos guardados con éxito"



@ruta_Vehiculo.route('/updateVehiculo', methods=['PUT'])
def Update():
    id = request.json['id']
    id_conductor= request.json['id_conductor']
    matricula = request.json['matricula']

    vehiculo= Vehiculo.query.get(id)
    if vehiculo:
        print(vehiculo)
        vehiculo.id = id
        vehiculo.id_conductor= id_conductor
        vehiculo.matricula = matricula
       
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_Vehiculo.route('/deleteVehiculo/<id>', methods=['DELETE'])
def eliminar(id):
    vehiculo = Vehiculo.query.get(id)
    db.session.delete(vehiculo)
    db.session.commit()
    return jsonify(
        Vehiculo_schema.dump(vehiculo),
                   )