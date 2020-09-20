import sqlite3
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
conn.execute("select id from  Booked")
print("Opened database successfully")