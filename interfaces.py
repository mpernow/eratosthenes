# Contains functions for interfacing with the user
# Author: Marcus Pernow
# Date: January 2020

import os

from db_entry import *
import db_actions

def create_entry():
    """
    Interface for adding an entry by querying user
    Also copies the file to its new location
    Return the DB_Entry object
    """
    new_entry = DB_Entry() # Create instance of entry to add the info to
    print('Eratosthenes is ready to add your new entry.\n')
    new_entry.set_id()
    title = input('Enter the title:\n')
    new_entry.set_title(title)
    authors = input('Enter the authors as list of surname, firstname separated by semicolons:\n')
    new_entry.set_authors(authors)
    try:
        year = int(input('Enter the year:\n'))
    except ValueError:
        try:
            year = int(input('Enter the year as an integer:\n'))
        except ValueError:
            print('You failed to follow basic instructions. The year is set to 2000\n')
            year = 2000
    new_entry.set_year(year)
    pub_type = input('Enter the publication type as article/review/book/other:\n')
    try:
        new_entry.set_type(pub_type)
    except ValueError:
        try:
            pub_type = input('Type must be one of article/review/book/other:\n')
        except ValueError:
            print('You failed to follow basic instructions. Type is now set to \'other\'\n')
            pub_type = 'other'
            new_entry.set_type(pub_type)
    keywords = input('Enter list of keywords separated by semicolons:\n')
    new_entry.set_keywords(keywords.split(';'))
    current_path = input('Enter the current path to the file\n')
    if not os.path.isfile(current_path):
        print('File not found. Please try again')
        current_path = input('Enter the current path to the file\n')
        if not os.path.isfile(current_path):
            print('File not found')
    new_entry.set_new_path()
    db_actions.copy_file(new_entry.get_path(), current_path)
    return new_entry


def search():
    """
    Interface for searching the database
    """
    query = input('Please enter your search query\n')
    # For now, we will just print the whole database
    #db_actions.display()
    db_actions.search(query)

def get():
    """
    Interface for downloading a pdf
    """
    id_num = int(input('Enter the ID number of the item you wish to retrieve\n'))
    db_actions.retrieve(id_num)

def delete():
    """
    Deletes an entry using ID number
    """
    print('Not yet implemented')