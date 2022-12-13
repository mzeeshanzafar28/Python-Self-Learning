import sqlite3

conn = sqlite3.connect("student")
c = conn.cursor()

def get_data():
    c.execute("SELECT * FROM 'student' WHERE age>15;")
    data = c.fetchall()
    for d in data:
        print(d)

get_data()
c.close()
conn.close()