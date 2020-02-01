# Code to interface the addition of new entry
# Author: Marcus Pernow
# Date: January 2020

import db_entry

status = ''

while not (status == 'q' or status == 'quit' or status == 'exit'):
	print('Welcome to the entry adder of eratosthenes\n')
	title = input('Enter the title:\n')
	print(title)
	status = 'q'
