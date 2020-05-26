import json
import uuid

from flask import request, Blueprint

from models.einrichtung import Einrichtung
from models.person import Person
from models.termin import Termin


blueprint = Blueprint('termin', __name__)


def map_to_dict(termin):
    return{
        "id": str(termin.id),
        "einrichtung": termin.einrichtung,
        "spender": termin.spender,
        "datum": termin.datum,
        "uhrzeit": termin.uhrzeit,
        "kategorie": termin.kategorie,
        "bestaetigt": termin.bestaetigt,
        "anmerkungen": termin.anmerkungen
    }


@blueprint.route('create', methods=['POST'])
def create():
    termin = Termin()
    termin.id = uuid.uuid4()
    termin.einrichtung = Einrichtung.select().where(Einrichtung.id == request.json["einrichtung"]).get()
    try:
        termin.spender = Person.select().where(Person.id == request.json["spender"]).get()
    except Person.DoesNotExist:
        person_json = json.loads(Person.create())
        termin.spender = Person.select().where(Person.id == person_json["spender"]).get()
    termin.datum = request.json["datum"]
    termin.uhrzeit = request.json["uhrzeit"]
    termin.kategorie = request.json["kategorie"]
    termin.bestaetigt = request.json["bestaetigt"]
    termin.anmerkungen = request.json["anmerkungen"]
    termin.save(force_insert=True)

    return json.dumps(map_to_dict(termin), indent=4)


@blueprint.route('edit', methods=['POST'])
def edit():
    termin = Termin.get_by_id(request.json["id"])
    termin.einrichtung = Einrichtung.select().where(Einrichtung.id == request.json["einrichtung"]).get()
    try:
        termin.spender = Person.select().where(Person.id == request.json["spender"]).get()
    except Person.DoesNotExist:
        person_json = json.loads(Person.create())
        termin.spender = Person.select().where(Person.id == person_json["spender"]).get()
    termin.datum = request.json["datum"]
    termin.uhrzeit = request.json["uhrzeit"]
    termin.kategorie = request.json["kategorie"]
    termin.bestaetigt = request.json["bestaetigt"]
    termin.anmerkungen = request.json["anmerkungen"]
    termin.save()

    return json.dumps(map_to_dict(termin), indent=4)


@blueprint.route('delete', methods=['POST'])
def delete():
    termin = Termin.get_by_id(request.json["id"])
    termin.delete_instance()

    return json.dumps(map_to_dict(termin), indent=4)