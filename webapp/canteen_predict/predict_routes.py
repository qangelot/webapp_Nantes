from flask import current_app as app
import pandas as pd
from flask import url_for, redirect, render_template, \
request, make_response, Blueprint


# Blueprint Configuration
predict_bp = Blueprint(
    "predict_bp", __name__, template_folder="templates", static_folder="static"
)


@predict_bp.route('/predict', methods=['POST', 'GET'])
def home():
    pass


@predict_bp.route('/analysis', methods=['POST', 'GET'])
def canteen_bi():
    pass