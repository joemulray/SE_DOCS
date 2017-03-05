#!/usr/bin/env python

"""
Model Class for AlphaMobile
Allow for creation of mutilple models
with the following attributes
of name price and label
"""

class Model:
	def __init__(self, name = None, price = 0, label = None):
		self.name = name
		self.price = price
		self.label = label
	
	def setName(self, name):
		#function to set the name of Model 
		self.name = name

	def setPrice(self, price):
		#function to set the price of existing Model
		self.price = price

	
	def setLabel(self, label):
		#function used to set the label of the Model
		self.label = label

	def description(self):
		#Used to print the description of current Model
		print self	

	
	def getName(self):
		#returns the current name of model
		return self.name
	
	def getPrice(self):
		#function returns the price of the model
		return self.price
	
	def getLabel(self):
		#function to get the label of model
		return self.label


	def __str__(self):
		return  "Model %s\nPrice: %s\nLabel: %s\n" \
		%(self.name,  str(self.price), self.label)	
