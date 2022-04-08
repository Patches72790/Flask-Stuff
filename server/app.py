from flask import Flask

from . import register_routes



def create_app():
    import debugpy
    debugpy.log_to('./debugpy_log')
    debugpy.listen(5678)

    app: Flask = Flask(__name__)

    register_routes(app)
    return app
