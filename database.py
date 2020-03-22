import psycopg2
import sys
import json
from convert2 import getData
import json
import requests


con = None

getData()

try:
    con = psycopg2.connect("host='blutspendekarte.de' dbname='blutspendekarte' user='blutspendekarte' password='IchBin1Alpaka'")
    cur = con.cursor()
    cur.execute("CREATE TABLE Blutspendezentren (Id INTEGER PRIMARY KEY, name VARCHAR(100), address VARCHAR(100), zip VARCHAR(7), city VARCHAR(100), lat VARCHAR(100), lon VARCHAR(100), mon VARCHAR(100), tue VARCHAR(100), wed VARCHAR(100), thu VARCHAR(100), fri VARCHAR(100), sat VARCHAR(100), sun VARCHAR(100), url VARCHAR(512), phone VARCHAR(100), whole_blood_donation VARCHAR(100), platelet_donation VARCHAR(100), plasma_donation VARCHAR(100), erythrocytes_donation VARCHAR(100))")

    importfile = open("output.json", "r")
    importlist = json.loads(importfile.read())
    importfile.close()

    i = 0

    for j in importlist[1:]:
        sql_string = 'INSERT INTO Blutspendezentren VALUES (' + str(i)
        for key in j:
            if not j[key] == '':
                sql_string = sql_string + ', \'' + j[key] + '\''
            else:
                sql_string = sql_string + ', NULL'
        sql_string = sql_string + ' )'
        # cur.execute("INSERT INTO Blutspendezentren VALUES (" + i + ", " + j['name'] + ", " + j['address'] + ", " + j['zip'] + ", " + j['city'], j['lat'], j['lon'], j['mon'], j['tue'], j['wed'], j['thu'], j['fri'], j['sat'], j['sun'], j['url'], j['phone'], j['whole_blood_donation'], j['platelet_donation'], j['plasma_donation'], j['erythrocytes_donation'])")
        cur.execute(sql_string)
        i += 1

    cur.execute("CREATE TABLE Spender (Id INTEGER PRIMARY KEY, vorname VARCHAR(50), nachname VARCHAR(50), email VARCHAR(100), handy VARCHAR(25), anmerkungen VARCHAR)")
    cur.execute("CREATE TABLE Termin (Id INTEGER PRIMARY KEY, Blutspendezentrum INTEGER REFERENCES Blutspendezentren(id), Spender INTEGER REFERENCES Spender(Id), Datum DATE, Uhrzeit TIME, Kategorie VARCHAR(12), Bestaetigt VARCHAR(4), Anmerkungen VARCHAR)")
    # Kategorie = Wunsch/ Alternativ 1/ Alternativ 2; Bestaetigt = Ja / Nein

    con.commit()

except psycopg2.DatabaseError as e:
    if con:
        con.rollback()

    print('Error %s' % e)
    sys.exit(1)

finally:
    if con:
        con.close()
