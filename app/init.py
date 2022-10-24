#!/usr/bin/python
#start database
#https://gist.github.com/gwangjinkim/f13bf596fefa7db7d31c22efd1627c7a

import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgres", host = "database", port = "5432")
print("Opened database successfully")

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS flats;')

cur.execute('''CREATE TABLE IF NOT EXISTS flats
      (ID SERIAL PRIMARY KEY NOT NULL,
      NAME        TEXT    NOT NULL,
      IMG_URL       TEXT);''')
print ("Table created successfully")

conn.commit()
conn.close()