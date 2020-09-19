import sys
import sqlite3

id_num = int(sys.argv[1])
title = sys.argv[2]
authors = sys.argv[3]
year = int(sys.argv[4])
pub_type = sys.argv[5]
keywords = sys.argv[6]
path = sys.argv[7]

# Open connection to database
conn = sqlite3.connect('/mnt/mystorage/eratosthenes.db')
# Create cursor
c = conn.cursor()
# Note: be secure from SQL injections.
# Never just insert strings into database calls.
# Instead put them in tuple and use the '?' placeholder (from DB API).
new_entry = (id_num, title, authors, year, pub_type, keywords, path)
c.executemany('INSERT INTO ' + 'alexandria' + ' VALUES (?,?,?,?,?,?,?)', (new_entry,))
# Save (commit) the changes. MUST BE DONE BEFORE CLOSING CONNECTION
conn.commit()
# Close connection
conn.close()

