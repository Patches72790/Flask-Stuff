from ..server.routes import basic_routes


def register_routes(app):
    app.register_blueprint(basic_routes)
