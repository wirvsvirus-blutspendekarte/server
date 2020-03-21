from flask import Flask
from flask_restful import Api
import os

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object("config")
app.config.from_envvar("BLUTSPENDEKARTE_CFG")

from app.resources.version import Version

api = Api(app)
api.add_resource(Version, "/api/version")
