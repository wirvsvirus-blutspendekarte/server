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
def get_all():
    selection = Einrichtung.select()
    if request.args.get('q'):
        search_string = '%' + (request.args.get('q').lower()) + '%'
        selection = selection.where(Einrichtung.name ** search_string)

    return json.dumps([map_to_dict(e) for e in selection], indent=4)
