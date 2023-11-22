from flask import Blueprint, request, jsonify, json
from config.db import app, db, ma
from models.categoria import Categoria, CategoriasSchema


ruta_Categoria = Blueprint("ruta_Categoria",__name__)

Categoria_schema = CategoriasSchema()
Categorias_schema = CategoriasSchema(many=True)

@ruta_Categoria.route('/Categoria', methods=['GET'])
def categoria():
    resultall = Categoria.query.all() # Select * from Pasajeros
    resultado_Categoria = Categorias_schema.dump(resultall)
    return jsonify(resultado_Categoria)

@ruta_Categoria.route('/saveCategoria', methods=['POST'])
def save():
    #id = request.json['id']
    id_bodega= request.json['id_bodega']
    nombre= request.json['nombre']
    new_categoria = Categoria(
        id_bodega,
        nombre,

    )

    db.session.add(new_categoria)
    db.session.commit()
    return "Datos guardados con éxito"



@ruta_Categoria.route('/updateCategoria', methods=['PUT'])
def Update():
    id = request.json['id']
    id_bodega= request.json['id_bodega']
    nombre = request.json['nombre']

    categoria= Categoria.query.get(id)
    if categoria:
        print(categoria)
        categoria.id = id
        categoria.id_bodega= id_bodega
        categoria.nombre = nombre
       
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_Categoria.route('/deleteCategoria/<id>', methods=['DELETE'])
def eliminar(id):
    categoria = Categoria.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify(
        Categoria_schema.dump(categoria),
                   )