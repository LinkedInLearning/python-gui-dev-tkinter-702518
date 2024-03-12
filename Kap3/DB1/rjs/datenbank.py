import sqlite3
import os.path

class DB:
    def initDB(self):
        if not os.path.exists('sqldb.db'):
            connection=sqlite3.connect('sqldb.db')
            cursor=connection.cursor()
            cursor.execute(
                '''CREATE TABLE personen(name TEXT, vorname TEXT)''')
            return "Datenbank erstellt"
        else:
            return "Datenbank vorhanden"

    def leseDB(self):
        dbString=""
        counter = 0
        if os.path.exists('sqldb.db'):
            connection=sqlite3.connect('sqldb.db')
            cursor=connection.cursor()
            cursor.execute('''SELECT * FROM personen''')
            rows=cursor.fetchall()
            for row in rows:
                counter += 1
                dbString += row[0] + ", " + row[1] + "\n"
            connection.close()
            return [dbString,str(counter)]
        else:
            return "Datenbank nicht vorhanden"
        
        return dbString

    def schreibDB(self,n,v):
        if os.path.exists('sqldb.db'):
            connection=sqlite3.connect('sqldb.db')
            cursor=connection.cursor()
            cursor.execute(
                '''INSERT INTO personen VALUES(?,?)''',(n,v))
            connection.commit()
            connection.close()
            return "Daten geschrieben: " + n + ", " + v
        else:
            return "Datenbank nicht vorhanden"
