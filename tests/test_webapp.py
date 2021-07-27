from webapp.models import User
from webapp import create_app
from flask import current_app as app
import math, json


def test_new_user(new_user):
    """
    upon user creation, checks name, email & hashed password are correct
    """
    
    assert new_user.name == 'KeanugoesmadinNY'
    assert new_user.email == 'keanureeveslovesdogs@nantesmetropole.fr'
    assert new_user.check_password != 'Daisythepuppy'


def test_home_get(test_client):
    """
    checks that a GET request to '/' page result in 200 status code
    """

    response = test_client.get('/')
    assert response.status_code == 200
    assert "Opti Canteen permet un suivi à 360 degrés".encode("utf-8") in response.data
    assert b"Se connecter" in response.data
    assert "Créer un compte".encode("utf-8") in response.data


def test_home_post(test_client):
    """
    checks that a POST request to '/' page result in 200 status code (login form)
    """

    response = test_client.post('/')
    assert response.status_code == 200
    assert "Opti Canteen permet un suivi à 360 degrés".encode("utf-8") in response.data
    assert b"Se connecter" in response.data
    assert "Créer un compte".encode("utf-8") in response.data


def test_valid_login_logout(test_client):
    """
    checks logging in and then logging out
    """

    response = test_client.post('/',
                                data=dict(email=app.config['ADMIN_EMAIL'], password=app.config['ADMIN_PWD']),
                                follow_redirects=True)
    assert response.status_code == 200
    assert "Opti Canteen mêle analyses descriptive, prédictive et prescriptive.".encode("utf-8") in response.data


    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Se connecter" in response.data
    assert "Créer un compte".encode("utf-8") in response.data


def test_valid_prediction(test_client):
    """
    checks prediction module and API response is valid 
    """

    response = test_client.post('/',
                                data=dict(email=app.config['ADMIN_EMAIL'], password=app.config['ADMIN_PWD']),
                                follow_redirects=True)
    assert response.status_code == 200
    assert "Opti Canteen mêle analyses descriptive, prédictive et prescriptive.".encode("utf-8") in response.data

    response = test_client.get('/predict', follow_redirects=True)
    assert response.status_code == 200

    response = test_client.post("/predict",
        data=dict(date="2018-09-03 00:00:00",
                prevision=189,
                cantine_nom="MAISDON PAJOT",
                annee_scolaire="2018-2019",
                effectif=201,
                quartier_detail="Zola",
                prix_quartier_detail_m2_appart=3424,
                prix_moyen_m2_appartement=3553,
                prix_moyen_m2_maison=4490,
                longitude=1.5848,
                latitude=47.2183,
                depuis_vacances=1,
                depuis_ferie=19,
                depuis_juives=43,
                ramadan_dans=245,
                depuis_ramadan=81), 
                follow_redirects=True
        )

    assert response.status_code == 200
    assert b"Opti Cantines"