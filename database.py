import sqlite3

boglanish = sqlite3.connect("mydatabase.db")

malumot = boglanish.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS kompyuterlar(
    nomi TEXT
    narxi TEXT
    xotirasi TEXT
)
''')
