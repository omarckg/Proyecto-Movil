from flask import Blueprint, request, jsonify, json
from config.db import app, db, ma
from models.bodega import Bodega, BodegasSchema


ruta_Bodega = Blueprint("ruta_Bodega",__name__)

Bodega_schema = BodegasSchema()
Bodegas_schema = BodegasSchema(many=True)

@ruta_Bodega.route('/Bodega', methods=['GET'])
def bodega():
    resultall = Bodega.query.all() # Select * from Pasajeros
    resultado_Bodega = Bodegas_schema.dump(resultall)
    return jsonify(resultado_Bodega)

@ruta_Bodega.route('/saveBodega', methods=['POST'])
def save():
    id = request.json['id']
    nombre = request.json['nombre']
    new_bodega = Bodega(
        id,
        nombre,
    )
    db.session.add(new_bodega)
    db.session.commit()
    return "Datos guardados con éxito"



@ruta_Bodega.route('/updateBodega', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['idviaje']
    
    
    bodega= Bodega.query.get(id)
    if bodega:
        print(bodega)
        bodega.id = id
        bodega.nombre = nombre
       
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_Bodega.route('/deleteBodega/<id>', methods=['DELETE'])
def eliminar(id):
    bodega = Bodega.query.get(id)
    db.session.delete(Bodega_schema)
    db.session.commit()
    return jsonify(
        Bodega_schema.dump(Bodega),
                   )