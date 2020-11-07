# Disable Flask's debugging features by default. Should be False in production
DEBUG = False

APPLICATION_NAME = "Blutspendekarte"
APPLICATION_ROOT = "/api"
VERSION = "0.1.0"

# Flask-User settings
USER_APP_NAME = APPLICATION_NAME  # Shown in and email templates and page footers
USER_ENABLE_EMAIL = True  # Enable email authentication
USER_ENABLE_USERNAME = False  # Disable username authentication
USER_EMAIL_SENDER_NAME = USER_APP_NAME
USER_EMAIL_SENDER_EMAIL = "turakar.debug@gmail.com"

# Flask-Alchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy deprecation warning. Responsibility of flask-user
