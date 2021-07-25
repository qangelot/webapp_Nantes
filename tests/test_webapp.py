from webapp.models import User
from webapp import create_app
from flask import current_app as app


def test_new_user(new_user):
    """
    upon user creation, checks name, email & hashed password are correct
    """
    
    assert new_user.name == 'KeanugoesmadNY'
    assert new_user.email == 'keanureeveslovesdogs@gmail.com'
    assert new_user.check_password != 'Daisythepuppy'


def test_home_get(test_client):
    """
    checks that a GET request to '/' page result in 200 status code
    """

    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Opti Canteen permet un suivi" in response.data
    assert b"Se connecter" in response.data
    assert b"compte" in response.data


def test_home_post(test_client):
    """
    checks that a POST request to '/' page result in 200 status code (login form)
    """

    response = test_client.post('/')
    assert response.status_code == 200
    assert b"Opti Canteen permet un suivi" in response.data
    assert b"Se connecter" in response.data
    assert b"compte" in response.data


def test_valid_login_logout(test_client):
    """
    checks logging in and then logging out
    """

    response = test_client.post('/',
                                data=dict(email='q.angelot@gmail.com', password=app.config['PWD']),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"cet outil doit permettre" in response.data
    assert b"gaspillage alimentaire" in response.data
    assert b"analyses descriptive" in response.data


    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Opti Canteen permet un suivi" in response.data
    assert b"Se connecter" in response.data
    assert b"compte" in response.data
