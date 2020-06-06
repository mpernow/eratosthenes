# Functions to perform actions/access the database
# Author: Marcus Pernow
# Date: February 2020


import sqlite3
import shutil
import db_entry

def copy_file(new_dir, current_dir):
    """
    Function to copy the file corresponding to DB_Entry 'entry',
    currently in current_dir
    """
    # TODO: Allow shorthand notation, eg ./ or ~
    try:
        shutil.copy(current_dir, new_dir)
    except IOError:
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


def display(db_name = './eratosthenes.db', table_name = 'alexandria'):
    """
    Displays the whole database
    """
    # Open connection to database
    conn = sqlite3.connect(db_name)

    # Create cursor
    c = conn.cursor()

    c.execute('SELECT * FROM ' + table_name)

    rows = c.fetchall()
    entries = []

    for row in rows:
        entries.append(db_entry.make_entry(row))

    for entry in entries:
        print(entry)



    # Close connection (note no commit since we made no changes)
    conn.close()

def search(query, db_name = './eratosthenes.db', table_name = 'alexandria'):
    """
    Displays the entries matching the search_word
    """
    # Open connection to database
    conn = sqlite3.connect(db_name)

    # Create cursor
    c = conn.cursor()

    entries = []

    t = ('%'+query+'%',)
    for row in c.execute('SELECT * FROM ' + table_name + ' WHERE keywords LIKE ?', t):
        entries.append(db_entry.make_entry(row))

    for entry in entries:
        print(entry)



    # Close connection (note no commit since we made no changes)
    conn.close()

def retrieve(id_num, db_name = './eratosthenes.db', table_name = 'alexandria'):
    """
    Retrieves the entry with id_num
    """
    # Open connection to database
    conn = sqlite3.connect(db_name)

    # Create cursor
    c = conn.cursor()

    entries = []

    t = (str(id_num),)
    for row in c.execute('SELECT * FROM ' + table_name + ' WHERE ID=?', t):
        entries.append(db_entry.make_entry(row))

    # Close connection (note no commit since we made no changes)
    conn.close()

    if len(entries) > 1:
        print('More than one entry was found. Will only retrieve the first one.')

    for entry in entries:
        print(entry)

    current_path = entries[0].get_path()
    new_path = '/Users/marcus/eratosthenes_downloads'+'/'+entries[0].get_title()+'.pdf'

    copy_file(new_path, current_path)

