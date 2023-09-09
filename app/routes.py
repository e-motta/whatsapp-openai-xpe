from flask import Blueprint, Response


webhook_route_blueprint = Blueprint("webhook", __name__, url_prefix="/webhook")


@webhook_route_blueprint.route("/", methods=["GET"])
def webhook_get() -> Response:
    pass


@webhook_route_blueprint.route("/", methods=["POST"])
def webhook_post() -> Response:
    pass
