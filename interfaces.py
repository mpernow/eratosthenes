# Contains functions for interfacing with the user
# Author: Marcus Pernow
# Date: January 2020

from db_entry import *

def create_entry():
	"""
	Interface for adding an entry by querying user
	Also copies the file to its new location
	Return the DB_Entry object
	"""
	new_entry = DB_Entry() # Create instance of entry to add the info to
	print('Eratosthenes is ready to add your new entry.\n')
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
	current_path = input('Enter the current path to the file')
	new_entry.set_new_path()
	#TODO: Copy the file from current_path to new_path
	return new_entry()
