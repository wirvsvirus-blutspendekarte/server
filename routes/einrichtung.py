import uuid

from flask import Blueprint, request
import json

from models.einrichtung import Einrichtung

blueprint = Blueprint('einrichtungen', __name__)

def map_to_dict(einrichtung):
    return {
        "id": str(einrichtung.id),
        "name": einrichtung.name,
        "adresse": einrichtung.adresse,
        "plz": einrichtung.plz,
        "ort": einrichtung.ort,
        "breitengrad": einrichtung.breitengrad,
        "laengengrad": einrichtung.laengengrad,
        "website": einrichtung.website,
        "telefon": einrichtung.telefon,
        "vollblutspende": einrichtung.vollblutspende,
        "thrombozytenspende": einrichtung.thrombozytenspende,
        "plasmaspende": einrichtung.plasmaspende,
        "erythrozytenspende": einrichtung.erythrozytenspende
    }


@blueprint.route('')
def index():
    selection = Einrichtung.select()
    if request.args.get('q'):
        search_string = '%' + (request.args.get('q').lower()) + '%'
        selection = selection.where(Einrichtung.name ** search_string)

    return json.dumps([map_to_dict(e) for e in selection], indent=4)

@blueprint.route('create', methods=['POST'])
def create():
    einrichtung = Einrichtung()
    einrichtung.id = str(uuid.uuid4())
    einrichtung.name = request.json["name"]
    einrichtung.adresse = request.json["adresse"]
    einrichtung.plz = request.json["plz"]
    einrichtung.ort = request.json["ort"]
    einrichtung.breitengrad = request.json["breitengrad"]
    einrichtung.laengengrad = request.json["laengengrad"]
    einrichtung.website = request.json["website"]
    einrichtung.telefon = request.json["telefon"]
    einrichtung.vollblutspende = request.json["vollblutspende"]
    einrichtung.thrombozytenspende = request.json["thrombozytenspende"]
    einrichtung.plasmaspende = request.json["plasmaspende"]
    einrichtung.erythrozytenspende = request.json["erythrozytenspende"]
    einrichtung.save(force_insert=True)

    return json.dumps(map_to_dict(einrichtung), indent=4)

@blueprint.route('edit', methods=['POST'])
def edit():
    einrichtung = Einrichtung.get_by_id(request.json["id"])
    einrichtung.name = request.json["name"]
    einrichtung.adresse = request.json["adresse"]
    einrichtung.plz = request.json["plz"]
    einrichtung.ort = request.json["ort"]
    einrichtung.breitengrad = request.json["breitengrad"]
    einrichtung.laengengrad = request.json["laengengrad"]
    einrichtung.website = request.json["website"]
    einrichtung.telefon = request.json["telefon"]
    einrichtung.vollblutspende = request.json["vollblutspende"]
    einrichtung.thrombozytenspende = request.json["thrombozytenspende"]
    einrichtung.plasmaspende = request.json["plasmaspende"]
    einrichtung.erythrozytenspende = request.json["erythrozytenspende"]
    einrichtung.save()

    return json.dumps(map_to_dict(einrichtung), indent=4)

@blueprint.route('delete', methods=['POST'])
def delete():
    einrichtung = Einrichtung.get_by_id(request.json["id"])
    einrichtung.delete_instance()

    return json.dumps(map_to_dict(einrichtung), indent=4)
