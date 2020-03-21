import psycopg2
import sys
import json

con = None

try:
    con = psycopg2.connect("host='localhost' dbname='blutspendekartedb' user='postgres' password=''")
    cur = con.cursor()
    cur.execute("CREATE TABLE Blutspendezentren (Id INTEGER PRIMARY KEY, name VARCHAR(50), address VARCHAR(100), zip VARCHAR(5), city VARCHAR(50), lat FLOAT, lon FLOAT, mon VARCHAR(20), tue VARCHAR(20), wed VARCHAR(20), thu VARCHAR(20), fri VARCHAR(20), sat VARCHAR(20), sun VARCHAR(20), url VARCHAR(512), phone VARCHAR(25), whole_blood_donation VARCHAR(4), platelet_donation VARCHAR(4), plasma_donation VARCHAR(4), erythrocytes_donation VARCHAR(4))")

    importfile = open("output.json", "r")
    importdict = json.loads(importfile.read())
    importfile.close()

    i = 0

    for j in importdict[TODO]:
        cur.execute("INSERT INTO Blutspendezentren VALUES(i, j['name'], j['address'], j['zip'], j['city'], j['lat'], j['lon'], j['timings']['mon'], j['timings']['tue'], j['timings']['wed'], , j['timings']['thu'], j['timings']['fri'], j['timings']['sat'], j['timings']['sun'], j['url'], j['phone'], j['whole_blood_donation'], j['platelet_donation'], j['plasma_donation'], j['erythrocytes_donation'])")
        i += 1
    con.commit()

except psycopg2.DatabaseError as e:
    if con:
        con.rollback()

    print
    'Error %s' % e
    sys.exit(1)

finally:
    if con:
        con.close()
