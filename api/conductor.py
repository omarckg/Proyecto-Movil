from flask import Blueprint, request, jsonify, json
from config.db import app, db, ma
from models.conductor import Conductor, ConductoresSchema


ruta_Conductor = Blueprint("ruta_Conductor",__name__)

Conductor_schema = ConductoresSchema()
Conductores_schema = ConductoresSchema(many=True)

@ruta_Conductor.route('/Conductor', methods=['GET'])
def conductor():
    resultall = Conductor.query.all() # Select * from Pasajeros
    resultado_Conductor = Conductores_schema.dump(resultall)
    return jsonify(resultado_Conductor)

@ruta_Conductor.route('/saveConductor', methods=['POST'])
def save():
    #id = request.json['id']
    telefono = request.json['telefono']
    nombre = request.json['nombre']
    new_conductor = Conductor(
        telefono,
        nombre,
    )
    db.session.add(new_conductor)
    db.session.commit()
    return "Datos guardados con éxito"



@ruta_Conductor.route('/updateconductor', methods=['PUT'])
def Update():
    id = request.json['id']
    telefono = request.json['telefono']
    nombre = request.json['nombre']

    conductor= Conductor.query.get(id)
    if conductor:
        print(conductor)
        conductor.id = id
        conductor.telefono = telefono
        conductor.nombre = nombre
       
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_Conductor.route('/deleteconductor/<id>', methods=['DELETE'])
def eliminar(id):
    conductor = Conductor.query.get(id)
    db.session.delete(conductor)
    db.session.commit()
    return jsonify(
        Conductor_schema.dump(conductor),
                   )