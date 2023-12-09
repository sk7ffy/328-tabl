import sqlite3 
conn = sqlite3.connect('quiziz')

cursor = conn.cursor()
#cursor.execute('DROP TABLE IF EXISTS quiziz')
#cursor.execute('DROP TABLE IF EXISTS questions')
#cursor.execute('DROP TABLE IF EXISTS quiz_content')
cursor.execute('''
CREATE TABLE IF NOT EXISTS quiziz(id INTEGER PRIMARY KEY,name VARCHAR)

''')

conn.commit()


cursor.execute('''
CREATE TABLE IF NOT EXISTS questions(id INTEGER PRIMARY KEY,question VARCHAR,answer VARCHAR,wrong1 VARCHAR,wrong2 VARCHAR,wrong3 VARCHAR)

''')

conn.commit()


cursor.execute('''
CREATE TABLE IF NOT EXISTS quiz_content(id INTEGER PRIMARY KEY,quiz_id INTEGER,question_id INTEGER,FOREIGN KEY(quiz_id) REFERENCES quiz (id),FOREIGN KEY(question_id) REFERENCES question (id))

''')

conn.commit()

questions = [
 ('33+33','66','77','22','11'),
 ('11+33','44','47','62','11')  
]

cursor.executemany(''' INSERT INTO questions (question,answer,wrong1,wrong2,wrong3)VALUES(?,?,?,?,?)''',questions)

quiziz = [
('math quiziz',),
('math quiziz',)
   
] 

cursor.executemany('''INSERT INTO quiziz (name) VALUES (?)''',quiziz)
conn.commit()

cursor.execute('''INSERT INTO quiz_content (quiz_id,question_id)VALUES (?,?)''',[1,2])
conn.commit()

cursor.execute('''SELECT * FROM questions,quiz_content WHERE questions.id == quiz_content.question_id AND quiz_content.quiz_id == ?''',[1])

data = cursor.fetchall()

print(data)