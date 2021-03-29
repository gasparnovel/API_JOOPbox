from flask_restful import Resource
import json

# devuelve datos
class Return_data(Resource):
    def get(self):
        return {'Prueba': 'Inicial'}