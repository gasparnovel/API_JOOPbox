from flask import Flask
from flask_restful import Resource, Api
from domain.return_data import Return_data

# copia de api.py para testear
def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Return_data, '/')
    api.add_resource(List, '/list')
    api.add_resource(Failed, '/failed')
    return app
    if __name__ == '__main__':
        app = create_app()
        app.run(debug=True)