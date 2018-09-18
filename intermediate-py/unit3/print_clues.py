import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute('SELECT text, answer, value FROM clue LIMIT 10')
results = cursor.fetchall()

for clue in results:
    text, answer, value = clue
    print('[${}]'.format(value, ))
    print('Question: What is: {} ?'.format(text, ))
    print('Answer: {}'.format(answer, ))
    print("")

    # [$200]
    # Question: What is ''
    # Answer: tkjfqjk
