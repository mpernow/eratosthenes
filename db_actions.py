# Functions to perform actions/access the database
# Author: Marcus Pernow
# Date: February 2020


import sqlite3
import shutil
import os
import subprocess
import db_entry

from config import addr

def copy_file(new_dir, current_dir):
    """
    Function to copy the file corresponding to DB_Entry 'entry',
    currently in current_dir
    """
    # TODO: Allow shorthand notation, eg ./ or ~
    #current_dir = current_dir.replace(' ', '\ ')
    print(current_dir)
    try:
        subprocess.check_output(['scp', current_dir, addr+':'+new_dir])
    except subprocess.CalledProcessError as e:
        print(e.output)

def copy_to_local(new_dir, current_dir):
    """
    Function to copy the file corresponding to DB_Entry 'entry',
    currently in current_dir
    """
    # TODO: Allow shorthand notation, eg ./ or ~
    try:
        output = subprocess.call(["scp", addr+":"+current_dir, new_dir])
        #shutil.copy(current_dir, new_dir)
    except IOError:
        print('Unable to copy file')

def add_entry_to_db(entry, db_name = 'eratosthenes.db', table_name = 'alexandria'):
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


    # The commented out code is no longer in use because it is done on the pi
    ## Open connection to database
    #conn = sqlite3.connect(db_name)

    ## Create cursor
    #c = conn.cursor()

    ## Note: be secure from SQL injections.
    ## Never just insert strings into database calls.
    ## Instead put them in tuple and use the '?' placeholder (from DB API).

    #new_entry = (id_num, title, authors, year, pub_type, keywords, path)
    #c.executemany('INSERT INTO ' + table_name + ' VALUES (?,?,?,?,?,?,?)', (new_entry,))



    ## Save (commit) the changes. MUST BE DONE BEFORE CLOSING CONNECTION
    #conn.commit()

    ## Close connection
    #conn.close()
    
    title.replace(' ', '\ ')
    title = "'" + title + "'"
    authors.replace(' ', '\ ')
    authors.replace(';', '\;')
    authors = "'" + authors + "'"
    keywords.replace(' ', '\ ')
    keywords.replace(';', '\;')
    keywords = "'" + keywords + "'"
    args = [str(id_num), title, authors, str(year), pub_type, keywords, path]
    output = subprocess.check_output(['ssh', addr, 'python', 'eratosthenes/add_to_db.py'] + args)


def display(db_name = './eratosthenes.db', table_name = 'alexandria'):
    """
    Displays the whole database
    """
    ## Open connection to database
    #conn = sqlite3.connect(db_name)

    ## Create cursor
    #c = conn.cursor()

    #c.execute('SELECT * FROM ' + table_name)

    #rows = c.fetchall()

    ## Close connection (note no commit since we made no changes)
    #conn.close()
    
    rows = eval(subprocess.check_output(['ssh', addr, 'python', 'eratosthenes/display_db.py'])[:-1])
    entries = []

    for row in rows:
        entries.append(db_entry.make_entry(row))

    for entry in entries:
        print(entry)




def search(query, db_name = './eratosthenes.db', table_name = 'alexandria'):
    """
    Displays the entries matching the search_word
    """
    ## Open connection to database
    #conn = sqlite3.connect(db_name)

    ## Create cursor
    #c = conn.cursor()


    #t = ('%'+query+'%',)
    #for row in c.execute('SELECT * FROM ' + table_name + ' WHERE keywords LIKE ?', t):
    #    entries.append(db_entry.make_entry(row))

    ## Close connection (note no commit since we made no changes)
    #conn.close()

    entries = eval(subprocess.check_output(['ssh', addr, 'python', 'eratosthenes/search.py', query])[:-1])
    for entry in entries:
        entry = db_entry.make_entry(entry)
        print(entry)

    if len(entries) == 0:
        print('No entries found.')
    

def retrieve(id_num, db_name = './eratosthenes.db', table_name = 'alexandria'):
    """
    Retrieves the entry with id_num
    """
    ## Open connection to database
    #conn = sqlite3.connect(db_name)

    ## Create cursor
    #c = conn.cursor()

    entries = []

    #t = (str(id_num),)
    #for row in c.execute('SELECT * FROM ' + table_name + ' WHERE ID=?', t):
    #    entries.append(db_entry.make_entry(row))

    ## Close connection (note no commit since we made no changes)
    #conn.close()

    rows = eval(subprocess.check_output(['ssh', addr, 'python', 'eratosthenes/retrieve.py', str(id_num)])[:-1])
    for row in rows:
        entries.append(db_entry.make_entry(row))

    if len(entries) > 1:
        print('More than one entry was found. Will only retrieve the first one.')

    for entry in entries:
        print(entry)

    current_path = entries[0].get_path()
    new_path = '/Users/marcus/eratosthenes_downloads'+'/'+entries[0].get_title()+'.pdf'

    copy_to_local(new_path, current_path)

def remove(id_num, db_name = './eratosthenes.db', table_name = 'alexandria'):
    """
    Removes the entry with id_num from database and pdf folder
    """
    ## Open connection to database
    #conn = sqlite3.connect(db_name)

    ## Create cursor
    #c = conn.cursor()

    entries = []

    #t = (str(id_num),)
    #for row in c.execute('SELECT * FROM ' + table_name + ' WHERE ID=?', t):
    #    entries.append(db_entry.make_entry(row))

    #c.execute('DELETE FROM ' + table_name + ' WHERE ID=?', t)
    #conn.commit()

    ## Close connection (note no commit since we made no changes)
    #conn.close()

    rows = eval(subprocess.check_output(['ssh', addr, 'python', 'eratosthenes/remove.py', str(id_num)])[:-1])
    for row in rows:
        entries.append(db_entry.make_entry(row))

    for entry in entries:
        print(entry)

    if len(entries) > 0:
        path = entries[0].get_path()

        try:
            #os.remove(path)
            subprocess.check_output(['ssh', addr, 'rm', path])
        except OSError:
            print('File not found. No file was deleted.')

    else:
        print('No such entry was found')
