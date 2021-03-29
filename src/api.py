from flask import Flask
from flask_restful import Resource, Api
from domain.return_data import Return_data
from domain.failed import Failed
from domain.list import List

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

api.add_resource(Return_data, '/')
api.add_resource(List, '/list')
api.add_resource(Failed, '/failed')

if __name__ == '__main__':
    app.run(debug=True)