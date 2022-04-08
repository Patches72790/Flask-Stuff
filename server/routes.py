from flask import Blueprint, request

# from ..server.utils import fun_decorator

basic_routes = Blueprint("basic_routes", __name__)


@basic_routes.route("/")
def index():
    return "<p>Hello world!</p>"


@basic_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "post"
    else:
        return "get"


@basic_routes.route("/fun_stuff", methods=["GET"])
#@fun_decorator
def fun_stuff():

    print("This is a fun route")
    return "OK"
