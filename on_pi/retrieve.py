import sqlite3
import sys

id_num = int(sys.argv[1])

# Open connection to database
conn = sqlite3.connect('/mnt/mystorage/eratosthenes.db')

# Create cursor
c = conn.cursor()

rows = []

t = (str(id_num),)
for row in c.execute('SELECT * FROM ' + 'alexandria' + ' WHERE ID=?', t):
    rows.append(row)

conn.close()

print(str(rows))
