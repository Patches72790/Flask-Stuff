from pytest import fixture
from server.app import create_app


def outer(function, *fn_args, **fn_kwargs):
    print("mocked decorator")
    print(f"Here are my args: {fn_args}")
    print(f"Here are my kwargs: {fn_kwargs}")
    return function(*fn_args, **fn_kwargs)


def require_auth_mock(*args, **kwargs):
    def mock_decorator(f):
        def inner():
            return outer(f, arg_1="hello", **{"kwarg1": "world", "kwarg2": "!"})
        return inner
    return mock_decorator


@fixture
def app():
    test_app = create_app()
    yield test_app


@fixture
def client(app):
    test_client = app.test_client()
    from unittest.mock import patch

    patch("server.utils.outer", outer).start()

    return test_client
