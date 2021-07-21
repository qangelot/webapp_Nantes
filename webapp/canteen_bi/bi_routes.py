from flask import current_app as app
import json, plotly
import pandas as pd
from flask import url_for, redirect, render_template, \
request, make_response, Blueprint
from flask_login import login_required

from ..scripts.data_prep_freq import freq_figures
from ..scripts.data_prep_menus import menus_figures
from ..scripts.data_prep_tempo import tempo_figures
from ..scripts.data_prep_geo import geo_figures

from ..scripts.data_load import load_dataset


data = load_dataset(file_name="webapp/data/frequentation_dtwh.db")
data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d")
data.sort_values("date", inplace=True)

# Blueprint Configuration
bi_bp = Blueprint(
    "bi_bp", __name__, template_folder="templates", static_folder="static"
)


@bi_bp.route('/freq', methods=['POST', 'GET'])
@login_required
def freq():

    cantines = data.cantine_nom.sort_values().unique().tolist()
    selected_canteen = request.form.get('cantines')

    if (request.method == 'POST') and len(selected_canteen)>0 and len(request.form.get('start_date'))>0 \
        and len(request.form.get('end_date'))>0:
        figures = freq_figures(canteen=selected_canteen, start_date=request.form.get('start_date'),
        end_date=request.form.get('end_date'))

    else:
        selected_canteen = "AGENETS"        
        figures = freq_figures(canteen=selected_canteen, start_date="01/09/2018", end_date="07/07/2019")

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('freq.html',
                            ids=ids,
                            cantines=cantines,
                            figuresJSON=figuresJSON,
                            selected_canteen=selected_canteen
                            )


@bi_bp.route('/menus', methods=['POST', 'GET'])
@login_required
def menus():

    cantines = data.cantine_nom.sort_values().unique().tolist()
    selected_canteen = request.form.get('cantines')

    if (request.method == 'POST') and len(selected_canteen)>0 and len(request.form.get('start_date'))>0 \
        and len(request.form.get('end_date'))>0:
        figures = menus_figures(canteen=selected_canteen, start_date=request.form.get('start_date'),
        end_date=request.form.get('end_date'))

    else:
        selected_canteen = "AGENETS"
        figures = menus_figures(canteen=selected_canteen, start_date="01/09/2018", end_date="07/07/2019")

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('menus.html',
                            ids=ids,
                            cantines=cantines,
                            figuresJSON=figuresJSON,
                            selected_canteen=selected_canteen
                            )


@bi_bp.route('/tempo', methods=['POST', 'GET'])
@login_required
def tempo():

    cantines = data.cantine_nom.sort_values().unique().tolist()
    selected_canteen = request.form.get('cantines')

    if (request.method == 'POST') and len(selected_canteen)>0 and len(request.form.get('start_date'))>0 \
        and len(request.form.get('end_date'))>0:
        figures = tempo_figures(canteen=selected_canteen, start_date=request.form.get('start_date'),
        end_date=request.form.get('end_date'))

    else:
        selected_canteen = "AGENETS"
        figures = tempo_figures(canteen=selected_canteen, start_date="01/09/2018", end_date="07/07/2019")

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('tempo.html',
                            ids=ids,
                            cantines=cantines,
                            figuresJSON=figuresJSON,
                            selected_canteen=selected_canteen
                            )


@bi_bp.route('/geo', methods=['POST', 'GET'])
@login_required
def geo():

    cantines = data.cantine_nom.sort_values().unique().tolist()
    selected_canteen = request.form.get('cantines')

    if (request.method == 'POST') and len(selected_canteen)>0 and len(request.form.get('start_date'))>0 \
        and len(request.form.get('end_date'))>0:
        figures = geo_figures(canteen=selected_canteen, start_date=request.form.get('start_date'),
        end_date=request.form.get('end_date'))

    else:
        selected_canteen = "AGENETS"
        figures = geo_figures(canteen=selected_canteen, start_date="01/09/2018", end_date="07/07/2019")

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('geo.html',
                            ids=ids,
                            cantines=cantines,
                            figuresJSON=figuresJSON,
                            selected_canteen=selected_canteen
                            )