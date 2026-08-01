import app

if __name__ == "__main__":
    if hasattr(app, "main") and callable(app.main):
        app.main()
    elif hasattr(app, "app"):
        flask_app = getattr(app, "app")
        if callable(flask_app):
            flask_app()
        elif hasattr(flask_app, "run"):
            flask_app.run()
    else:
        raise SystemExit("app.py does not expose a callable 'main' or a Flask 'app' instance")
