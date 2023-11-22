from flask import Blueprint, request, jsonify, json
from config.db import app, db, ma
from models.producto import Producto, ProductosSchema


ruta_Producto = Blueprint("ruta_Producto",__name__)

Producto_schema = ProductosSchema()
Productos_schema = ProductosSchema(many=True)

@ruta_Producto.route('/Producto', methods=['GET'])
def producto():
    resultall = Producto.query.all() # Select * from Pasajeros
    resultado_Producto = Productos_schema.dump(resultall)
    return jsonify(resultado_Producto)

@ruta_Producto.route('/saveProducto', methods=['POST'])
def save():
    #id = request.json['id']
    id_categoria= request.json['id_categoria']
    nombre = request.json['nombre']
    fecha_consumo = request.json['fecha_consumo']
    peso = request.json['peso']
    new_producto = Producto(
        id_categoria,
        nombre,
        fecha_consumo,
        peso,

    )

    db.session.add(new_producto)
    db.session.commit()
    return "Datos guardados con éxito"



@ruta_Producto.route('/updateProducto', methods=['PUT'])
def Update():
    id = request.json['id']
    id_categoria= request.json['id_categoria']
    nombre = request.json['nombre']
    fecha_consumo = request.json['fecha_consumo']
    peso = request.json['peso']

    producto= Producto.query.get(id)
    if producto:
        print(producto)
        producto.id = id
        producto.id_categoria= id_categoria
        producto.nombre= nombre
        producto.fecha_consumo= fecha_consumo
        producto.peso = peso
       
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_Producto.route('/deleteProducto/<id>', methods=['DELETE'])
def eliminar(id):
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify(
        Producto_schema.dump(producto),
                   )