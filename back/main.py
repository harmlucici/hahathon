from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api()
base = {"info": "Some info", "num": 56}

class Main(Resource):
    def get(self):
        return base


api.add_resource(Main, "/api/base")
api.init_app(app)
if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")