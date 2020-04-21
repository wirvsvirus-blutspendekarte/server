from datetime import datetime
from peewee import Model, UUIDField, ForeignKeyField, DateTimeField, IntegerField

from db import db
from models.einrichtung import Einrichtung


class Wartezeit(Model):
    id = UUIDField(primary_key=True)
    einrichtung = ForeignKeyField(Einrichtung, backref='wartezeiten')
    meldezeit = DateTimeField()
    wartezeit = IntegerField()

    class Meta:
        database = db
