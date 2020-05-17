from peewee import CharField, UUIDField, Model
from db import db


class Person(Model):
    id = UUIDField(primary_key=True)
    vorname = CharField(max_length=50, null=False)
    nachname = CharField(max_length=50, null=False)
    email = CharField(max_length=50, null=True)
    handy = CharField(max_length=25, null=True)

    class Meta:
        database = db
