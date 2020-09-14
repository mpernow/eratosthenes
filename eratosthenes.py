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
    welcome_message = '\nWelcome to Eratosthenes!\n'
    help_message = '\nPossible commands:\n'\
                    '\tq\t Quit the program\n'\
                    '\tadd\t Add a new entry\n'\
                    '\tsearch\t Search the database\n'\
                    '\tget\t Retrieve a document\n'\
                    '\tdelete\t Delete an entry'
    print(welcome_message)
    print(help_message)

    status = ''
    while (status != 'q' or status != 'quit' or status != 'exit'):
        status = input('Please enter a command:\t')
        if status == 'add':
            new_entry = interfaces.create_entry()
            db_actions.add_entry_to_db(new_entry)
            print('\nDone!\n\n')
        elif status == 'search':
            interfaces.search()
        elif status == 'display':
            db_actions.display()
        elif status == 'get':
            interfaces.get()
        elif status == 'delete':
            interfaces.delete()
        elif (status == 'q' or status == 'quit' or status == 'exit'):
            break
        else:
            print(help_message)
            


if __name__ == "__main__":
    main()
