import sqlite3

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

c.execute("""CREATE TABLE MESSAGES (ID TEXT, MESSAGE TEXT)""")
c.execute("""CREATE TABLE USERS (ID TEXT, FIRST_NAME TEXT, LAST_NAME TEXT, USERNAME TEXT, REGISTERED INTEGER)""")

conn.commit()
conn.close()
