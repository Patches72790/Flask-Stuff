def outer(function, *fn_args, **fn_kwargs):
    print("inside the decorator")
    return function(*fn_args, **fn_kwargs)


def fun_decorator(f):
    def inner():
        return outer(f)
    return inner
