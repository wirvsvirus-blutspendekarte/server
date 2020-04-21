import json
import uuid
from datetime import datetime

from flask import request, Blueprint

from models.einrichtung import Einrichtung
from models.wartezeit import Wartezeit

blueprint = Blueprint('wartezeit', __name__)


@blueprint.route('', methods=('POST',))
def create():
    wartezeit = Wartezeit()
    wartezeit.id = uuid.uuid4()
    wartezeit.einrichtung = Einrichtung.select().where(Einrichtung.id == request.form['einrichtung']).get()
    wartezeit.wartezeit = int(request.form['wartezeit'])
    wartezeit.meldezeit = datetime.now()
    wartezeit.save(force_insert=True)

    return json.dumps({"success": True})
