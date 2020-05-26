import json
import uuid

from flask import request, Blueprint

from models.person import Person

blueprint = Blueprint('person', __name__)


def map_to_dict(person):
    return{
        "id": str(person.id),
        "vorname": person.vorname,
        "nachname": person.nachname,
        "email": person.email,
        "handy": person.handy
    }


@blueprint.route('create', methods=['POST'])
def create():
    person = Person()
    person.id = uuid.uuid4()
    person.vorname = request.json["vorname"]
    person.nachname = request.json["nachname"]
    person.email = request.json["email"]
    person.handy = request.json["handy"]
    person.save(force_insert=True)

    return json.dumps(map_to_dict(person), indent=4)


@blueprint.route('edit', methods=['POST'])
def edit():
    person = Person.get_by_id(request.json["id"])
    person.vorname = request.json["vorname"]
    person.nachname = request.json["nachname"]
    person.email = request.json["email"]
    person.handy = request.json["handy"]
    person.save()

    return json.dumps(map_to_dict(person), indent=4)


@blueprint.route('delete', methods=['POST'])
def delete():
    person = Person.get_by_id(request.json["id"])
    person.delete_instance()

    return json.dumps(map_to_dict(person), indent=4)
