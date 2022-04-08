loglevel = "info"
errorlog = "-"
accesslog = "-"

bind = "127.0.0.1:5000"

debug = True
workers = 2
worker_class = "sync"


def on_starting(server):
    import debugpy

    debugpy.configure(subProcess=False)
    debugpy.listen(5678)
    print("Debugpy listening on port 5678")
