import sqlite3

connection = sqlite3.connect("jeopardy.db")
# print(type(connection))
# print(help(connection))
# print(dir(connection))

cursor = connection.cursor()
# print(dir(cursor))

cursor.execute('SELECT name FROM category LIMIT 10')
results = cursor.fetchall()

print('Example categories:\n')
for category in results:
    print(category[0])

connection.close