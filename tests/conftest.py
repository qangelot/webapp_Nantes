from webapp.models import User
from webapp import create_app
import pytest


@pytest.fixture(scope='module')
def new_user():
    user = User(name='KeanugoesmadNY', email='keanureeveslovesdogs@gmail.com')
    user.set_password('Daisythepuppy')
    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    # Create a test client using the Flask application
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            # execution is being passed to the test functions 
            yield testing_client 


def test_valid_login_logout(test_client):
    """
    checks logging in and then logging out
    """
    response = test_client.post('/login',
                                data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for logging in, patkennedy79@gmail.com!" in response.data
    assert b"Welcome patkennedy79@gmail.com!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" in response.data
    assert b"Login" not in response.data
    assert b"Register" not in response.data
 
    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Goodbye!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data
