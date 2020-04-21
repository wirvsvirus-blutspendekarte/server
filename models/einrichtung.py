from peewee import CharField, DoubleField, BooleanField, UUIDField, Model
from db import db


class Einrichtung(Model):
    id = UUIDField(primary_key=True)
    name = CharField(100)
    adresse = CharField(100)
    plz = CharField(7)
    ort = CharField(100)
    breitengrad = DoubleField()
    laengengrad = DoubleField()
    website = CharField(max_length=512, null=True)
    telefon = CharField(max_length=100, null=True)
    vollblutspende = BooleanField()
    thrombozytenspende = BooleanField()
    plasmaspende = BooleanField()
    erythrozytenspende = BooleanField()

    class Meta:
        database = db
