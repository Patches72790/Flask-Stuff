from flask import Flask

from .debugger import initialize_flask_server_debugger_if_needed
from . import register_routes

#initialize_flask_server_debugger_if_needed()


def create_app():
    app: Flask = Flask(__name__)

    register_routes(app)
    return app
