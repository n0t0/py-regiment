import sqlite3

connection = sqlite3.connect("jeopardy.db")
print type(connection)

curson = connection.curson()
