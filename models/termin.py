from datetime import date
from peewee import Model, UUIDField, ForeignKeyField, DateField, TimeField, CharField, IntegerField, BooleanField
from db import db
from models.einrichtung import Einrichtung
from models.person import Person


class Termin(Model):
    id = UUIDField(primary_key=True)
    einrichtung = ForeignKeyField(Einrichtung, backref='termine')
    spender = ForeignKeyField(Person, backref='termine')
    datum = DateField()
    uhrzeit = TimeField()
    kategorie = IntegerField(12)  # Wunsch = 0 / Alternativ 1 = 1 / Alternativ 2 = 2
    bestaetigt = BooleanField()  # Ja = True / Nein = False
    anmerkungen = CharField(null=True)

    class Meta:
        database = db
