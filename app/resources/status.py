from flask_restful import Resource
from flask_user import roles_required, login_required
from app.models.user import User
from app import app, db


class Status(Resource):
    #@roles_required("Admin")
    @login_required
    def get(self):
        num_users = User.query.all().count()
        return {
            "version": app.config["VERSION"],
            "name": app.config["APPLICATION_NAME"],
            "numUsers": num_users
        }
