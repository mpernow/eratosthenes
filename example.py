import sqlite3

# Establish connection to database
db_name = 'eratosthenes.db'
table_name = 'test_table'
conn = sqlite3.connect(db_name)

# Create cursor
c = conn.cursor()


### Perform some database actions

# Note: be secure from SQL injections.
# Never just insert strings into database calls.
# Instead put them in tuple and use the '?' placeholder (from DB API).

new_entries = [('Fantastic paper', 'Me Myself', 2020, 'best; great'),
	('Amazing follow-up paper', 'Me Myself', 2021, 'best2; great'),
	]
c.executemany('INSERT INTO ' + table_name + ' VALUES (?,?,?,?)', new_entries)
# Can do the same with only one. Then have just a tuple, i.e. not in a list

#To display:
for row in c.execute('SELECT * FROM '+ table_name):
	print(row)

###


# Save (commit) the changes
conn.commit()

# Close connection
# NOTE: commit any changes before closing
conn.close()


