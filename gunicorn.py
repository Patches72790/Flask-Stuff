loglevel = "debug"
errorlog = "-"
accesslog = "-"

bind = "127.0.0.1:5000"

debug = False
workers = 1
worker_class = "eventlet"

def do_a_thing():
    thing = "stuff"
    print(thing)


def on_starting(server):
    import debugpy

    debugpy.log_to("./debugpy_log")
    debugpy.listen(5678)
    print("Debugpy listening on port 5678")

def pre_request(worker, req):
    do_a_thing()
