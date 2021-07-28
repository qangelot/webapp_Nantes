from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
import logging
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler


# Instantiate plugins globally
db = SQLAlchemy()
maill = Mail()
login_manager = LoginManager()
# crsf_protect = CSRFProtect()

def create_app():
    """Initialize the core application."""

    app = Flask(__name__, instance_relative_config=False)
    # Configure the flask app instance
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    maill.init_app(app)
    login_manager.init_app(app)
    # crsf_protect.init_app(app)

    with app.app_context():
        # Include our Routes
        from .canteen_bi import bi_routes
        from .canteen_predict import predict_routes
        from .home import routes

        # Register Blueprints
        app.register_blueprint(bi_routes.bi_bp)
        app.register_blueprint(predict_routes.predict_bp)        
        app.register_blueprint(routes.home_bp)

        # Register error handlers
        register_error_handlers(app)

        # Create Database Models
        db.create_all()

        return app


# customized error handlers
def register_error_handlers(app):

    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('400.html'), 400

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        return render_template('403.html'), 403

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('405.html'), 405

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500