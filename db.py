from peewee import *
import os

db = PostgresqlDatabase(
    database='blutspendekarte',
    user='blutspendekarte',
    host='blutspendekarte.de',
    password=os.environ.get('BLUTSPENDEKARTE_PASSWORT')
)
