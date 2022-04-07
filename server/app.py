from flask import Flask

from ..debugger import initialize_flask_server_debugger_if_needed
from ..server import register_routes

initialize_flask_server_debugger_if_needed()


def create_app():
    app = Flask(__name__)

    register_routes(app)
    return app
