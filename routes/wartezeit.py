import json
import uuid
from datetime import datetime

from flask import request, Blueprint

from models.einrichtung import Einrichtung
from models.wartezeit import Wartezeit

blueprint = Blueprint('wartezeit', __name__)


def map_to_dict(wartezeit):
    return {
        "id": str(wartezeit.id),
        "einrichtung": wartezeit.einrichtung,
        "wartezeit": wartezeit.wartezeit,
        "meldezeit": wartezeit.meldezeit
    }


@blueprint.route('', methods=('POST',))
def create():
    wartezeit = Wartezeit()
    wartezeit.id = uuid.uuid4()
    wartezeit.einrichtung = Einrichtung.select().where(Einrichtung.id == request.form['einrichtung']).get()
    wartezeit.wartezeit = int(request.form['wartezeit'])
    wartezeit.meldezeit = datetime.now()
    wartezeit.save(force_insert=True)

    return json.dumps({"success": True})


@blueprint.route('edit', methods=['POST'])
def edit():
    wartezeit = Wartezeit.get_by_id(request.form['id'])
    wartezeit.wartezeit = int(request.form['wartezeit'])
    wartezeit.meldezeit = datetime.now()
    wartezeit.save()

    return json.dumps({"success": True})


@blueprint.route('delete', methods=['POST'])
def delete():
    wartezeit = Wartezeit.get_by_id(request.form["id"])
    wartezeit.delete_instance()

    return json.dumps({"success": True})
