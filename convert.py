import uuid
import requests
import csv
from io import StringIO
from db import db
from models.einrichtung import Einrichtung


def getData():
    db.connect()
    db.create_tables([ Einrichtung ])
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTbxaxdxBH9aYfQgsi7diiIJ-OBdIWo63BXlXOkv-hZiw_0H8cr2Ko0VDUAaH0TdpHOKWYz1pv9uloJ/pub?gid=0&single=true&output=csv'
    r = requests.get(url, allow_redirects=True)
    r.encoding = 'utf-8'

    reader = csv.DictReader(StringIO(r.text), delimiter=',')
    for row in reader:
        if len(row.get('Name')) == 0 or len(row.get('Longitude')) == 0:
            continue

        einrichtung = Einrichtung()
        einrichtung.id = str(uuid.uuid4())
        einrichtung.name = row.get('Name')
        einrichtung.adresse = row.get('Adresse')
        einrichtung.plz = row.get('PLZ')
        einrichtung.ort = row.get('Ort')
        einrichtung.laengengrad = row.get('Longitude')
        einrichtung.breitengrad = row.get('Latitude')
        einrichtung.website = row.get('Website')
        einrichtung.telefon = row.get('Telefon')
        einrichtung.vollblutspende = (row.get('Vollblutspende') == 'ja')
        einrichtung.thrombozytenspende = (row.get('Thrombozytenspende') == 'ja')
        einrichtung.plasmaspende = (row.get('Plasmaspende') == 'ja')
        einrichtung.erythrozytenspende = (row.get('Erythrozyten') == 'ja')
        einrichtung.save(force_insert=True)

getData()
