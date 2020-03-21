from flask import Flask
from flask_restful import Resource, Api
from app import app


class Version(Resource):
    def get(self):
        return {
            "version": app.config["VERSION"],
            "name": app.config["APPLICATION_NAME"]
        }
