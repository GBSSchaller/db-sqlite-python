import sqlite3

connection = sqlite3.connect('db-sqlite-python\schule.db')
cursur = connection.cursor()

# Tabelle klasse erstellen
sql = """
CREATE TABLE klasse (
    id INTEGER  PRIMARY KEY Autoincrement,
    name TEXT
)

"""
cursur.execute(sql)
connection.commit()
connection.close()