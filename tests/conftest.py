from webapp.models import User
from webapp import create_app
import pytest


@pytest.fixture(scope='module')
def new_user():
    user = User(name='KeanugoesmadinNY', email='keanureeveslovesdogs@nantesmetropole.fr')
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