# Implementation of class for database entry
# Author: Marcus Pernow
# Date: January 2020

import uuid # For random filenames

class DB_Entry():
	"""
	Definition of a database entry.
	Contains the required fields and methods
	"""

	def set_id(self):
		"""
		Sets the unique id of the entry, with an increasing counter
		"""
		# Open file and extract last id
		f = open('id_num', 'r')
		nums = f.readlines()
		num = int(nums[-1][:-1]) + 1
		f.close()
		# set the id
		self.id_num = num
		# Append to the fil
		f = open('id_num', 'a')
		f.write(str(num)+'\n')
		f.close()
	
	def set_id_manual(self, id_num):
		"""
		Manually sets the id
		"""
		self.id_num = id_num

	def set_title(self, title):
		"""
		Set the title of the entry
		"""
		self.title = title

	def set_authors(self, authors):
		"""
		Set the authors of the entry

		TODO: Put into correct format: "surname, firstname(s)"
		separated by semicolon
		"""
		self.authors = authors
	
	def set_year(self, year):
		"""
		Set the publication year
		"""
		if not type(year) == int:
			raise ValueError('Year must be an integer')
		self.year = year
	
	def set_keywords(self, kw_list):
		"""
		Sets keywords of entry
		"""
		# Check that it is a list of strings:
		if not all([type(i) == str for i in kw_list]):
			raise ValueError('Must be list of strings')
		for i in range(len(kw_list)):
			kw_list[i] = kw_list[i].lower()

		self.kw_list = kw_list

	def set_type(self, publication_type):
		"""
		Set the publication type to book/article/review/other
		"""
		publication_type = publication_type.lower()
		if not (publication_type == 'book' or publication_type == 'article' or publication_type == 'review' or publication_type == 'other'):
			raise ValueError('Type must be book/article/review/other')
		else:
			self.publication_type = publication_type
	
	def set_new_path(self, path = '/mnt/mystorage/pdfs/'):
		"""
		Sets the path of the entry with random file name
		'path' is the directory with default './pdfs/'

		TODO: Allow for non-pdf files
		"""
		f_name = uuid.uuid1().hex
		self.path = path + f_name + '.pdf'
	
	def set_path_manual(self, path):
		"""
		Manually set the path
		"""
		self.path = path

	def get_title(self):
		"""
		Return the title of self
		"""
		return self.title

	def get_authors(self):
		"""
		Return the authors of self
		"""
		return self.authors
		
	def get_year(self):
		"""
		Returns the year of self
		"""
		return self.year

	def get_keywords(self):
		"""
		Returns keyowrds of self as list of strings
		"""
		return self.kw_list
	
	def get_pub_type(self):
		"""
		Returns the publication type of self
		"""
		return self.publication_type

	def get_path(self):
		"""
		Returns the path of self
		"""
		return self.path
	
	def get_id(self):
		"""
		Return the id of the entry
		"""
		return self.id_num
	
	def __str__(self):
		"""
		Prints the entry nicely
		"""
		return str(self.id_num) + '\t|\t' + self.title + '\t|\t' + self.authors + '\t|\t' + str(self.year)


def make_entry(row):
	"""
	Takes a row from querying database and creates an entry object
	"""
	entry = DB_Entry()
	entry.set_id_manual(row[0])
	entry.set_title(row[1])
	entry.set_authors(row[2])
	entry.set_year(row[3])
	entry.set_type(row[4])
	entry.set_keywords(row[5].split(';'))
	entry.set_path_manual(row[6])
	return entry


if __name__ == "__main__":
	print("Testing the code:")
	test_entry = DB_Entry()
	title = 'Best article ever'
	print('Setting title to '+title)
	test_entry.set_title(title)
	author = 'Marcus Pernow'
	print('Setting author to '+author)
	test_entry.set_authors('Marcus Pernow')
	year = 2020
	print('Setting year to '+str(year))
	test_entry.set_year(year)
	keywords = ['physics','mathematics','truth','philosophy']
	print('Setting keywords list to \n\t'+',\n\t'.join(keywords))
	pub_type = 'article'
	print('Setting type to '+pub_type)
	test_entry.set_type(pub_type)
