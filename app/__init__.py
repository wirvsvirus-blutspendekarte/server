from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager
from flask_babel import Babel
import datetime

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object("config")
app.config.from_envvar("BLUTSPENDEKARTE_CFG")

# Internationalization
babel = Babel(app)

# Database setup
db = SQLAlchemy(app)
from app.models.user import User, Role, UserRoles

# Setup Flask-User and specify the User data-model
user_manager = UserManager(app, db, User)

db.create_all()

# Create default admin user
if not User.query.filter(User.email == app.config["ADMIN_EMAIL"]).first():
    user = User(
        email=app.config["ADMIN_EMAIL"],
        email_confirmed_at=datetime.datetime.utcnow(),
        password=user_manager.hash_password(app.config["ADMIN_EMAIL"]),
    )
    user.roles.append(Role(name='Admin'))
    db.session.add(user)
    db.session.commit()


api = Api(app)
from app.resources.version import Version
from app.resources.status import Status
api.add_resource(Version, "/api/version")
api.add_resource(Status, "/api/status")
