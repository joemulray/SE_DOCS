#!/usr/bin/env python

#Joseph Mulray, SE 211 CSV Library
#CSV Library to read, parse, edit CSV files


import sys
import pydoc

#TODO:
	#write function definitions:
	#get pydoc working
	#write test cases


class csv:


	def __init__(self, file, delimeter =','):
		"""initialize csv file object upon creating an
		csv object"""

		self.file = file
		self.data = []
		self.delimeter = delimeter
		self.position = -1


		#want to move this to a load data function
		for row in self.file:
			self.data.append(row.split(self.delimeter))



	def refresh(self):
		"""used to reassign data, used when changing
		delimeter or changes made to a file and want a refresh
		of that data, change in delimeter, or other changes to data"""

		for row in self.file:
			self.data.append(row.split(self.delimeter))



	def setDelimeter(self, delimeter =','):
		"""purpose is to set comma seperated value to what
		ever input user wants by default set towards comma """

		self.delimeter = delimeter



	def search(self, value):
		"""search file for inputed value, return None if
		such value does not exist, if found returns coordinates in file"""

		for row in self.data:
			for column in row:
				if value == column:
					return True


		return False

	def read(self):
		"""reader object returns an iteratable list for the given
		csv file"""

		return self.data


	def readAll(self):
		"""creates one of csv values no row segmentation"""

		allItems = []

		for row in self.data:
			for column in row:
				allItems.append(column)

		return allItems


	def write(self, *argv):
		"""takes row or value inputed by user, and writes to
		the CSV file"""
		try:

			if argv:
				for item in argv:
					if argv[-1] != item:
						self.file.write(item + ",")
					else:
						self.file.write(item)

		except (TypeError, NameError, SyntaxError) as e:
			print 'Error %s: Could not write to file ' %e
			raise


	def writeRow(self, row):
		"""writer object, return object to write to file"""

		try:
			self.write('\n')
			for item in row:
				if row[-1] != item:
					self.file.write(item + ",")
				else:
					self.file.write(item)

		except (TypeError, NameError, SyntaxError) as e:
			raise
			print 'Error %s: Could not write to file ' %e
			raise


	def ignoreEmpty(self):
		"""ignore empty cells following values of csv, dont return empty
		cells with no values, does not return any value, sets iW to true or false """
		for row in self.data:
			try:

				index = row.index('')
				row.pop(index)

			except(ValueError):
				pass


	def rmNLC(self):
		"""removes new line character from end of csv file
		defualt does not do this, rmNLC()"""

		for row in self.data:
			row[-1] = row[-1].strip('\n')



	def next(self):
		"""returns the next row from the csv file object """
		try:
			self.position += 1
			nextRow = self.data[self.position]
			return nextRow

		except(IndexError):
			return


if __name__ == '__main__':

	"""
	===================================
	DEBUGGING PROGRAM: SEGMENT
	===================================
	USE LIBRARY:
	from csvlib import csv

	file = open('file.csv')
	csvfile = csv(file)
	===================================
	RUN TEST CASES:
	./csvlib or python csvlib
	===================================
	"""

	#How to declare object,
	#from another file just import csvlib and declare
	file = open('file.csv', 'r+')
	csvfile = csv(file)



	print '\n====================================================='
	print 'TESTING rmNLC()'
	#Example removing new line characters from end of line
	csvfile.rmNLC()
	print csvfile.data


	#csvfile.next() example
	print '\n====================================================='
	print "TESTING next() functionality"

	print csvfile.next()
	print csvfile.next()
	print csvfile.next()
	print csvfile.next()
	print csvfile.next()


	print '\n====================================================='
	print 'TESTING ignoreEmpty()'
	#ignore Empty Cells
	csvfile.ignoreEmpty()
	print csvfile.data

	print '\n====================================================='
	print 'TESTING read()'
	#Example of read row iteritable list
	print csvfile.read()


	print '\n====================================================='
	print 'TESTING readAll()'
	#Example of readall iteritable list
	print csvfile.readAll()


	print '\n====================================================='
	print 'TESTING write()'
	#Write any amount of attributes to a new row
	csvfile.write("this", "is a test for write()")
	print 'Added: "this", "is a test for write()"'

	print '\n====================================================='
	print 'TESTING search()'
	#Example of searching list returns a boolean
	csvfile.read()
	print csvfile.search("this")


	print '\n====================================================='
	print 'TESTING writeRow()'
	#Example of readall iteritable list
	csvfile.writeRow(["csvlib", "test", "writerow"])
	print 'Added: ["csvlib", "test", "writerow"]'

	print '\n====================================================='
	print "DONE TESTING"
	print '====================================================='
