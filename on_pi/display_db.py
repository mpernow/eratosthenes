import sqlite3

# Open connection to database
conn = sqlite3.connect('/mnt/mystorage/eratosthenes.db')
# Create cursor
c = conn.cursor()
c.execute('SELECT * FROM ' + 'alexandria')
rows = c.fetchall()

# Close connection (note no commit since we made no changes)
conn.close()

print(str(rows))
