from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    from .app.routes import webhook_route_blueprint

    app.register_blueprint(webhook_route_blueprint)

    return app
