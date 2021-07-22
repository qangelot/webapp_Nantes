from sys import version
from flask import current_app as app
import pandas as pd
import datetime as dt
from flask import url_for, redirect, render_template, \
request, make_response, Blueprint, flash
from wtforms.form import Form
from flask_login import login_required
import json
import requests
from ..forms import PredictForm


# connect to the model API 
URL = "http://localhost:8001/api/v1/predict"

# Blueprint Configuration
predict_bp = Blueprint(
    "predict_bp", __name__, template_folder="templates", static_folder="static"
)


@predict_bp.route('/predict', methods=['POST', 'GET'])
@login_required
def predict():
    """Prediction page.
    GET requests serve predict page.
    POST requests validate form & post request to API."""

    form = PredictForm()
    if form.validate_on_submit():
        date_str = dt.datetime.strptime(form.date.data, "%d/%m/%Y").strftime("%Y-%m-%d %H:%M:%S")
        DATA = {
        "inputs": [
                {
                    "date": date_str,
                    "prevision": form.prevision.data,
                    "cantine_nom": form.cantine_nom.data,
                    "annee_scolaire": form.annee_scolaire.data,
                    "effectif": form.effectif.data,
                    "quartier_detail": form.quartier_detail.data,
                    "prix_quartier_detail_m2_appart": form.prix_quartier_detail_m2_appart.data,
                    "prix_moyen_m2_appartement": form.prix_moyen_m2_appartement.data,
                    "prix_moyen_m2_maison": form.prix_moyen_m2_maison.data,
                    "longitude": form.longitude.data,
                    "latitude": form.latitude.data,
                    "depuis_vacances": form.depuis_vacances.data,
                    "depuis_ferie": form.depuis_ferie.data,
                    "depuis_juives": form.depuis_juives.data,
                    "ramadan_dans": form.ramadan_dans.data,
                    "depuis_ramadan": form.depuis_ramadan.data
                }
            ]
        }
        response = requests.post(URL, json=DATA)
        json_format = json.loads(response.text)

        return render_template(
                "predict.html",
                pred=round(json_format['predictions'][0],2),
                version=json_format['version'],
                form=form
            )

    return render_template(
        "predict.html",
        form=form
    )


@predict_bp.route('/analysis', methods=['POST', 'GET'])
@login_required
def analysis():
    pass