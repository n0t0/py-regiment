import sqlite3

connection = sqlite3.connect("jeopardy.db")
# print(type(connection))
# print(help(connection))
# print(dir(connection))

cursor = connection.cursor()
# print(dir(cursor))

cursor.execute('SELECT name FROM category LIMIT 10')
results = cursor.fetchall()
print(results)
print(results[1][0])

for category in results: # category mean for tuple in this list
    print(category[0])

connection.close()