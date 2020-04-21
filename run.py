from flask import Flask
import routes.einrichtung
import routes.wartezeit
from db import db
from models.einrichtung import Einrichtung
from models.wartezeit import Wartezeit

app = Flask(__name__)
app.register_blueprint(routes.einrichtung.blueprint, url_prefix='/einrichtungen')
app.register_blueprint(routes.wartezeit.blueprint, url_prefix='/wartezeit')

db.connect()
db.create_tables([Einrichtung, Wartezeit])

if __name__ == "__main__":
    app.run()
