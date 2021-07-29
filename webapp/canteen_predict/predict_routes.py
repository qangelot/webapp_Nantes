from sys import version
import numpy as np
import pandas as pd
import datetime as dt
from io import StringIO
import io, json, requests
from flask import current_app as app
from flask import url_for, redirect, render_template, \
request, make_response, Blueprint, flash
from wtforms.form import Form
from flask_login import login_required
from . import predict_bp

from ..forms import PredictForm
from werkzeug.utils import secure_filename


# connect to the model API 
URL = "http://localhost:8001/api/v1/predict"


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
        
        app.logger.info(f"Réalisation d'une prédiction sur les inputs suivant : {DATA}")

        try:
            response = requests.post(URL, json=DATA)
        # if API offline then 
        except requests.ConnectionError:
            flash('Erreur de connection à l\'API. Veuillez réessayer ultérieurement.')            
            return render_template(
            "predict.html",
            form=form
            )
        
        json_format = json.loads(response.text)
        app.logger.info(f"Résultat de la prédiction : {json_format['predictions'][0]}")

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


@predict_bp.route('/multi_predict', methods=['POST', 'GET'])
@login_required
def multi_predict():
    """ Batch predictions page.
    GET requests serve predict page.
    POST requests validate form & post request to API."""
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Postez un fichier au format CSV.')   
            return render_template(
            "multi_predict.html"
            )

        f = request.files['file']
        if f.filename == '':
            flash('Postez un fichier au format CSV.')   
            return render_template(
            "multi_predict.html"
            )

        if f and f.filename.rsplit('.', 1)[1].lower() == 'csv':
            stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)    
            stream.seek(0)
            result = stream.read()
            df = pd.read_csv(StringIO(result))
            cantine = df['cantine_nom'].iloc[0]
            date_début = df['date'].iloc[0]
            date_fin = df['date'].iloc[-1]
            df['date'] = df['date'].apply(lambda x : dt.datetime.strptime(x, "%d/%m/%Y").strftime("%Y-%m-%d %H:%M:%S"))

            # use to_dict instead of to_json
            DATA = {
                "inputs": df.replace({np.nan: None}).to_dict(orient='records') 
            }

            app.logger.info(f"Réalisation d'une prédiction par lots sur les inputs suivant : {DATA}")

            try:
                response = requests.post(URL, json=DATA)
            # if API offline then 
            except requests.exceptions.ConnectionError:
                flash('Erreur de connection à l\'API ou de format des données. Vérifier le format de vos données.')            
                return render_template(
                "multi_predict.html",
                )

            json_format = json.loads(response.text)
            preds=['%.2f' % elem for elem in json_format['predictions']]
            df_pred = pd.DataFrame(preds, columns=['predictions']).reset_index(drop=True)

            app.logger.info(f"Résultats de la prédiction par lots : {preds}")
            
            df_pred = pd.concat((df['date'].reset_index(drop=True), df_pred), axis=1)
            df_pred['date'] = df_pred['date'].apply(lambda x : dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y"))

            return render_template(
                    "multi_predict.html",
                    tables=[df_pred.to_html(classes='data')], 
                    titles=df_pred.columns.values,
                    version=json_format['version'],
                    cantine_nom=cantine,
                    date_début=date_début,
                    date_fin=date_fin
                )
        else:
            flash('Postez un fichier au format CSV.')   
            return render_template(
                "multi_predict.html"
                )

    return render_template(
            "multi_predict.html"
            )