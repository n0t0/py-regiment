import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute('SELECT game FROM category ORDER BY RANDOM() LIMIT 1')
results = cursor.fetchall()
game_id = results[0][0]
print('Categories for game #{:d}'.format(game_id, ))


query = """SELECT name, round FROM category 
WHERE game={:d} ORDER BY round""".format(game_id, )
cursor.execute(query)
results = cursor.fetchall()

for result in results:
    # round 0 = Jeapardy round 
    # round 1 = Double Jeopardy
    # round 3 = Final Jeorpardy 
    name, round = result
    # round 0: Category 
    print('Round {:d}: {}'.format(round, name))


connection.close()