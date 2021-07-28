from flask import Blueprint


# Blueprint Configuration
bi_bp = Blueprint(
    "bi_bp", __name__, template_folder="templates", static_folder="static"
)

from . import bi_routes
