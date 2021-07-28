from flask import Blueprint


# Blueprint Configuration
predict_bp = Blueprint(
    "predict_bp", __name__, template_folder="templates", static_folder="static"
)

from . import predict_routes
