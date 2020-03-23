import json
from io import StringIO

import requests
import csv
import db

def getData():
    connection = db.get_connection()
    cursor = connection.cursor()

    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTbxaxdxBH9aYfQgsi7diiIJ-OBdIWo63BXlXOkv-hZiw_0H8cr2Ko0VDUAaH0TdpHOKWYz1pv9uloJ/pub?gid=0&single=true&output=csv'
    r = requests.get(url, allow_redirects=True)
    r.encoding = 'utf-8'

    mapping = {
        'name': (lambda row: row.get('Name')),
        'address': (lambda row: row.get('Adresse')),
        'zip': (lambda row: row.get('PLZ')),
        'city': (lambda row: row.get('Ort')),
        'lat': (lambda row: row.get('Latitude')),
        'lon': (lambda row: row.get('Longitude')),
        'mon': (lambda row: row.get('Mo')),
        'tue': (lambda row: row.get('Di')),
        'wed': (lambda row: row.get('Mi')),
        'thu': (lambda row: row.get('Do')),
        'fri': (lambda row: row.get('Fr')),
        'sat': (lambda row: row.get('Sa')),
        'sun': (lambda row: row.get('So')),
        'url': (lambda row: row.get('Website')),
        'phone': (lambda row: row.get('Telefon')),
        'whole_blood_donation': (lambda row: row.get('Vollblutspende')),
        'platelet_donation': (lambda row: row.get('Thrombozytenspende')),
        'plasma_donation': (lambda row: row.get('Plasmaspende')),
        'erythrocyte_donation': (lambda row: row.get('Erythrozyten'))
    }

    reader = csv.DictReader(StringIO(r.text), delimiter=',')
    for row in reader:
        keys = []
        values = []
        placeholders = []

        for key, value in mapping.items():
            keys.append(key)
            placeholders.append('%s')
            values.append(value(row))

        joinedKeys = ", ".join(keys)
        joinedPlaceholders = ", ".join(placeholders)

        cursor.execute(
            "insert into blutspendezentren (%s) values (%s)" % (joinedKeys, joinedPlaceholders),
            values
        )

    connection.commit()

getData()

