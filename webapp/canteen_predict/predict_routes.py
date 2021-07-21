from flask import current_app as app
import pandas as pd
from flask import url_for, redirect, render_template, \
request, make_response, Blueprint
from flask_login import login_required


# Blueprint Configuration
predict_bp = Blueprint(
    "predict_bp", __name__, template_folder="templates", static_folder="static"
)


@predict_bp.route('/predict', methods=['POST', 'GET'])
@login_required
def predict():
    pass


@predict_bp.route('/analysis', methods=['POST', 'GET'])
@login_required
def analysis():
    pass