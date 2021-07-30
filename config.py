import os
from os import environ, path
from dotenv import load_dotenv


PACKAGE_ROOT = path.abspath(path.dirname(__file__))
load_dotenv(path.join(PACKAGE_ROOT, '.env'))


class Config:
    """Base config class."""
    PACKAGE_ROOT = PACKAGE_ROOT
    FLASK_APP = 'wsgi.py'
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'qadev54@gmail.com'
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_SUPPRESS_SEND = False

    DTWH = os.path.join(PACKAGE_ROOT, 'webapp/data', 'frequentation_dtwh.db')
    API_URL = environ.get('API')
    
    ADMIN_EMAIL = environ.get('ADMIN_EMAIL')
    ADMIN_PWD = environ.get('ADMIN_PWD')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False
    MAIL_SUPPRESS_SEND = True


class TestConfig(Config):
    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True
    MAIL_SUPPRESS_SEND = True
