from flask import Blueprint, request, jsonify, json
from config.db import app, db, ma
from models.formulario import Formulario, FormulariosSchema


ruta_Formulario = Blueprint("ruta_Formulario",__name__)

Formulario_schema = FormulariosSchema()
Formularios_schema = FormulariosSchema(many=True)

@ruta_Formulario.route('/Formulario', methods=['GET'])
def formulario():
    resultall = Formulario.query.all() # Select * from Pasajeros
    resultado_Formulario = Formularios_schema.dump(resultall)
    return jsonify(resultado_Formulario)

@ruta_Formulario.route('/saveFormulario', methods=['POST'])
def save():
    id = request.json['id']
    id_producto = request.json['id_producto']
    id_user = request.json['id_user']
    id_vehiculo = request.json['id_vehiculo']
    
    new_formulario = Formulario(
        id_producto,
        id_user,
        id_vehiculo,


    )

    db.session.add(new_formulario)
    db.session.commit()
    return "Datos guardados con éxito"



@ruta_Formulario.route('/updateFormulario', methods=['PUT'])
def Update():
    id = request.json['id']
    id_producto = request.json['id_producto']
    id_user = request.json['id_user']
    id_vehiculo = request.json['id_vehiculo']

    formulario = Formulario.query.get(id)
    if formulario:
        print(formulario)
        formulario.id = id
        formulario.id_producto= id_producto
        formulario.id_user= id_user
        formulario.id_vehiculo= id_vehiculo
        
       
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_Formulario.route('/deleteFormulario/<id>', methods=['DELETE'])
def eliminar(id):
    formulario = Formulario.query.get(id)
    db.session.delete(Formulario_schema)
    db.session.commit()
    return jsonify(
        Formulario_schema.dump(Formulario_schema),
                   )