from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail


# Globally accessible libraries
db = SQLAlchemy()
maill = Mail()
login_manager = LoginManager()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    maill.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Include our Routes
        from .canteen_bi import bi_routes
        from .canteen_predict import predict_routes
        from .home import routes
        from . import errors

        # Register Blueprints
        app.register_blueprint(bi_routes.bi_bp)
        app.register_blueprint(predict_routes.predict_bp)        
        app.register_blueprint(routes.home_bp)
        app.register_blueprint(errors.errors_bp)

        # Create Database Models
        db.create_all()

        return app
