import db
import psycopg2.extras
from flask import Blueprint, request
import json

blueprint = Blueprint('bloodDonorCentre', __name__)

@blueprint.route('/getAll')
def get_all():
    cursor = db.get_connection().cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM Blutspendezentren")
    return json.dumps(cursor.fetchall(), indent=4)

@blueprint.route('/getMatching')
def get_matching():
    search_string = '%%' + request.args.get('q') + '%%'
    cursor = db.get_connection().cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM Blutspendezentren WHERE Name LIKE %s", (search_string, ))
    return json.dumps(cursor.fetchall(), indent=4)
