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

    MAIL_SERVER = 'smtp.gmail.com'
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
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = os.environ.get('SENDGRID_API_KEY')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    APPINSIGHTS_INSTRUMENTATIONKEY = environ.get('APPINSIGHTS_INSTRUMENTATIONKEY')
    APPINSIGHTS_CONNECTIONSTRING = environ.get('APPINSIGHTS_CONNECTIONSTRING')
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True
    TESTING = False
    MAIL_SUPPRESS_SEND = True


class TestConfig(Config):
    FLASK_ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True
    TESTING = True
    MAIL_SUPPRESS_SEND = True
