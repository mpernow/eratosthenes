# Main code for the eratosthenes database system
# Author: Marcus Pernow
# Date: February 2020

from db_entry import *
import interfaces
import db_actions



def main():
	"""
	Main function to run the eratosthened database system
	"""
	print('Welcome to Eratosthenes!\n')
	print('\nPossible commands:\n')
	print('\tq\t Quit the program\n')
	print('\tadd\t Add a new entry\n')
	print('\tsearch\t Search the database (to be implemented)\n')

	status = ''
	while (status != 'q' or status != 'quit' or status != 'exit'):
		status = input('Please enter a command:\t')
		if status = 'add':
			# Run the add interface and then add the entry
		elif status = 'search':
			print('Not yet implemented')

#TODO: Function to copy the file to library
#TODO: Function to add the new entry to database
#TODO: Way to search/browse the library

if __name__ == "__main__":
	main()
