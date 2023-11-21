from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.Bodega import Bodega, ruta_Bodega
from api.conductor import Conductor, ruta_Conductor
from api.Vehiculo import Vehiculo, ruta_Vehiculo
from api.categoria import Categoria, ruta_Categoria
from api.usuario import Usuario, ruta_Usuario
from api.producto import Producto, ruta_Producto
from api.formulario import Formulario, ruta_Formulario

@app.route('/')
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')