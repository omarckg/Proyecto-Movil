from flask import Blueprint, request, jsonify, json
from config.db import app, db, ma
from models.usuario import Usuario, UsuariosSchema


ruta_Usuario = Blueprint("ruta_Usuario",__name__)

Usuario_schema = UsuariosSchema()
Usuarios_schema = UsuariosSchema(many=True)

@ruta_Usuario.route('/Usuario', methods=['GET'])
def usuario():
    resultall = Usuario.query.all() # Select * from Pasajeros
    resultado_Usuario = Usuarios_schema.dump(resultall)
    return jsonify(resultado_Usuario)

@ruta_Usuario.route('/saveUsuario', methods=['POST'])
def save():
    #id = request.json['id']
    email = request.json['email']
    password_hash= request.json['password_hash']
    nombre = request.json['nombre']
    new_usuario = Usuario(
        email,
        password_hash,
        nombre,
    )
    db.session.add(new_usuario)
    db.session.commit()
    return "Datos guardados con éxito"



@ruta_Usuario.route('/updateUsuario', methods=['PUT'])
def Update():
    id = request.json['id']
    email = request.json['email']
    password_hash= request.json['password_hash']
    nombre = request.json['nombre']

    usuario = Usuario.query.get(id)
    if usuario:
        print(usuario)
        usuario.id = id
        usuario.email = email
        usuario.password_hash = password_hash
        usuario.nombre = nombre
       
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_Usuario.route('/deleteUsuario/<id>', methods=['DELETE'])
def eliminar(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(
        Usuario_schema.dump( usuario),
                   )