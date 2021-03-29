from flask_restful import Resource
from resources.data import Data
import json

# devuelve datos
class Return_data(Resource):
    def get(self):
        return Data.datos, 200