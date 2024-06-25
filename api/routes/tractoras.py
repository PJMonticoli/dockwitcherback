from flask import Blueprint, jsonify
from flask_cors import CORS
from bson import json_util
from ..connection.db import get_collection

# Blueprints permite separar la lógica de diferentes partes de tu aplicación en módulos independientes
# objeto que registra rutas y otros aspectos de una aplicación Flask
tractoras_blueprint = Blueprint('tractoras', __name__)
CORS(tractoras_blueprint)

collection = get_collection('tractoras')


@tractoras_blueprint.route('/api/tractoras', methods=['GET'])
def get_tractoras():
    try:
        tractoras = list(collection.find())
        #  La función jsonify se utiliza para crear un objeto de respuesta de Flask con los datos JSON.
        # json_util.dumps(tractoras) convierte la lista de documentos (tractoras)
        # a una cadena JSON utilizando json_util de la biblioteca bson, que maneja el formato JSON extendido de MongoDB.
        return jsonify(json_util.dumps(tractoras)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
