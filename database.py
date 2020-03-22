import psycopg2
import psycopg2.extras
import sys
import json
import convert2


def initialize_database():
    convert2.getData()
    con = None

    try:
        con = psycopg2.connect("host='blutspendekarte.de' dbname='blutspendekarte' user='blutspendekarte' password='IchBin1Alpaka'")
        cur = con.cursor()
        cur.execute("CREATE TABLE Blutspendezentren (Id INTEGER PRIMARY KEY, name VARCHAR(100), address VARCHAR(100), zip VARCHAR(7), city VARCHAR(100), lat VARCHAR(100), lon VARCHAR(100), mon VARCHAR(100), tue VARCHAR(100), wed VARCHAR(100), thu VARCHAR(100), fri VARCHAR(100), sat VARCHAR(100), sun VARCHAR(100), url VARCHAR(512), phone VARCHAR(100), whole_blood_donation VARCHAR(100), platelet_donation VARCHAR(100), plasma_donation VARCHAR(100), erythrocyte_donation VARCHAR(100))")

        importfile = open("output.json", "r")
        importlist = json.loads(importfile.read())
        importfile.close()

        i = 0

        for j in importlist:
            sql_string = 'INSERT INTO Blutspendezentren VALUES (' + str(i)
            for key in j:
                if not j[key] == '':
                    sql_string = sql_string + ', \'' + j[key] + '\''
                else:
                    sql_string = sql_string + ', NULL'
            sql_string = sql_string + ' )'
            cur.execute(sql_string)
            i += 1

        cur.execute("CREATE TABLE Spender (Id INTEGER PRIMARY KEY, vorname VARCHAR(50), nachname VARCHAR(50), email VARCHAR(100), handy VARCHAR(25))")
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


def update_blutspendezentren_with_json():
    convert2.getData()
    con = None

    try:
        con = psycopg2.connect(
            "host='blutspendekarte.de' dbname='blutspendekarte' user='blutspendekarte' password='IchBin1Alpaka'")
        cur = con.cursor()

        importfile = open("output.json", "r")
        importlist = json.loads(importfile.read())
        importfile.close()

        cur.execute('SELECT name FROM Blutspendezentren')
        rows = cur.fetchall()
        table = []
        for r in rows:
            table.append(r[0])
        no_update = ['name', 'address', 'zip', 'city', 'lat', 'lon']
        cur.execute('SELECT MAX(Id) FROM Blutspendezentren')
        i = cur.fetchall()[0][0] + 1

        for j in importlist:
            if j['name'] in table:
                sql_string = 'UPDATE Blutspendezentren SET '
                for key in j:
                    if not key in no_update:
                        if not j[key] == '':
                            sql_string = sql_string + key +' = \'' + j[key] + '\', '
                        else:
                            sql_string = sql_string + key +' = NULL, '
                sql_string = sql_string[:-2]
                sql_string = sql_string + ' WHERE name = \'' + j['name'] + '\''
                cur.execute(sql_string)
            else:
                sql_string = 'INSERT INTO Blutspendezentren VALUES (' + str(i)
                for key in j:
                    if not j[key] == '':
                        sql_string = sql_string + ', \'' + j[key] + '\''
                    else:
                        sql_string = sql_string + ', NULL'
                sql_string = sql_string + ' )'
                cur.execute(sql_string)
                i +=1
        con.commit()

    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()

        print('Error %s' % e)
        sys.exit(1)

    finally:
        if con:
            con.close()


def get_blutspendezentren_json():
    con = None

    try:
        con = psycopg2.connect(
            "host='blutspendekarte.de' dbname='blutspendekarte' user='blutspendekarte' password='IchBin1Alpaka'")
        cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM Blutspendezentren")
        FOUT = open("blutspendezentren.json", "w")
        json.dump(cur.fetchall(), FOUT, indent=4)
        FOUT.close()

    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()

        print('Error %s' % e)
        sys.exit(1)

    finally:
        if con:
            con.close()


def add_appoitment(importfile):
    con = None

    try:
        con = psycopg2.connect(
        "host='blutspendekarte.de' dbname='blutspendekarte' user='blutspendekarte' password='IchBin1Alpaka'")
        cur = con.cursor()

        importfile = open("output.json", "r")
        importlist = json.loads(importfile.read())
        importfile.close()

        i = 0

        for j in importlist[1:]:
            sql_string = 'INSERT INTO Spender VALUES (' + str(i)
            for key in j:
                if not j[key] == '':
                    sql_string = sql_string + ', \'' + j[key] + '\''
                else:
                    sql_string = sql_string + ', NULL'
            sql_string = sql_string + ' )'
            cur.execute(sql_string)
            i += 1

        i = 0

        for j in importlist[1:]:
            sql_string = 'INSERT INTO Termine VALUES (' + str(i)
            for key in j:
                if not j[key] == '':
                    sql_string = sql_string + ', \'' + j[key] + '\''
                else:
                    sql_string = sql_string + ', NULL'
            sql_string = sql_string + ' )'
            cur.execute(sql_string)
            i += 1

        con.commit()

    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()

        print('Error %s' % e)
        sys.exit(1)

    finally:
        if con:
            con.close()


# Nur fur jetzt beim Entwickeln: Datenbank-Schema anpassen
def update():
    con = None

    try:
        con = psycopg2.connect(
            "host='localhost' dbname='blutspendekartedb' user='postgres' password=''")
        cur = con.cursor()
        cur.execute("ALTER TABLE Spender DROP COLUMN anmerkungen")
        con.commit()

    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()

        print('Error %s' % e)
        sys.exit(1)

    finally:
        if con:
            con.close()

update_blutspendezentren_with_json()
get_blutspendezentren_json()