# debugger.py
# The use of this debugger requires setting the flask run command
# NOT to use the debugger or reloading
# flask run --no-debugger --no-reload


def initialize_flask_server_debugger_if_needed():
    import multiprocessing

    if multiprocessing.current_process().pid > 1:
        import debugpy

        debugpy.listen(("0.0.0.0", 5678))
        print(
            "⏳ Debugger can now be attached, press F5 in VS Code ⏳",
            flush=True,
        )
        debugpy.wait_for_client()
        print("🎉 VS Code debugger attached, enjoy debugging 🎉", flush=True)
