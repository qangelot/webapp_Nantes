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
    app.config.from_object('config.ProdConfig')

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

        # Configure logging
        if app.config['FLASK_ENV'] == 'production':
            configure_logging(app)

        # Register error handlers
        register_error_handlers(app)

        # Create Database Models (run this for the first time)
        # to migrate db in production, use flask-migrate
        # db.create_all()

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


# Create a file handler for logging
def configure_logging(app):

    # Deactivate the default stream logger
    app.logger.removeHandler(default_handler)

    # File handler : new file created when actual reach 20000 bytes / limit max log file to 20
    file_handler = RotatingFileHandler('webapp.log', maxBytes=20000, backupCount=20)

    # Create a file formatter and add it to the handler
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')
    file_handler.setFormatter(file_formatter)

    # Add file handler object to the logger
    app.logger.addHandler(file_handler)
    
    # Set the logging level
    app.logger.setLevel(logging.INFO)