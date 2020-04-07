# Functions to perform actions/access the database
# Author: Marcus Pernow
# Date: February 2020


import sqlite3
import shutil

def copy_file(entry, current_dir):
        """
        Function to copy the file corresponding to DB_Entry 'entry',
        currently in current_dir
        """
		# TODO: Allow shorthand notation, eg ./ or ~
        new_dir = entry.get_path()
		try:
        	shutil.copy(current_dir, new_dir)
		except IOError, e:
    		print('Unable to copy file')


def add_entry_to_db(entry, db_name = './eratosthenes.db', table_name = 'alexandria'):
        """
        Adds the DB_Entry object 'entry' to the SQLite database 'db_name'
        """
        # Extract the data from entry:
        id_num = entry.get_id()
        title = entry.get_title()
        authors = entry.get_authors()
        year = entry.get_year()
        pub_type = entry.get_pub_type()
        keyword_list = entry.get_keywords()
        path = entry.get_path()
        # Convert keyword list to string separated by ';'
        keywords = ';'.join(keyword_list)


        # Open connection to database
        conn = sqlite3.connect(db_name)

        # Create cursor
        c = conn.cursor()

        # Note: be secure from SQL injections.
        # Never just insert strings into database calls.
        # Instead put them in tuple and use the '?' placeholder (from DB API).

        new_entry = (id_num, title, authors, year, pub_type, keywords, path)
        c.executemany('INSERT INTO ' + table_name + ' VALUES (?,?,?,?,?,?,?)', (new_entry,))



        # Save (commit) the changes. MUST BE DONE BEFORE CLOSING CONNECTION
        conn.commit()

        # Close connection
        conn.close()


