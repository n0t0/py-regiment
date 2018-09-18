import sqlite3 

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

#### Select a random category 
cursor.execute('SELECT id, name FROM category ORDER BY RANDOM() LIMIT 1')
results = cursor.fetchall()

category_id, name = results[0]
print(name)

#### Get and print the clues for our random category 
query = '''SELECT text, answer, value FROM clue
WHERE category={} ORDER BY value'''.format(category_id, )
cursor.execute(query)
results = cursor.fetchall()

for clue in results:
    text, answer, value = clue 
    print('[${}]'.format(value, ))
    print('Question: {}?'.format(text, ))
    print('Answer: {}'.format(answer, ))
    print('')