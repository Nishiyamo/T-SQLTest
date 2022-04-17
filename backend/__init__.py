import sys

from flask import Flask
from flask_restful import Api

from backend.adapters.api import routes as api_routes
from backend.settings import APP_PORT


def create_app():
    if sys.argv.__len__() > 1:
        port = sys.argv[1]
    print("Api running on port : {} ".format(APP_PORT))

    app = Flask(__name__)
    api = Api(app)

    for url, module in api_routes().items():
        api.add_resource(module, url)

    app.run(host="0.0.0.0", port=APP_PORT, debug=True)
