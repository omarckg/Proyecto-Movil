from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.Bodega import Bodega, ruta_Bodega



@app.route('/')
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')