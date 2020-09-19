import sqlite3
import sys

if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    query = ''

# Open connection to database
conn = sqlite3.connect('/mnt/mystorage/eratosthenes.db')
# Create cursor
c = conn.cursor()

t = ('%'+query+'%',)
rows = []
for row in c.execute('SELECT * FROM ' + 'alexandria' + ' WHERE keywords LIKE ?', t):
    rows.append(row)

# Close connection (note no commit since we made no changes)
conn.close()

print(str(rows))
