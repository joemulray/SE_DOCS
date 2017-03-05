#!/usr/bin env python
"""
Manufacturer Class
Takes in location specified and assembles
models specified by AlphaModel Class
Allows multiple different locations
without each having own class

Also included the functions for modifing
Models incase Manufacturer needed to change
or update specifcations on an existing model
without creating a new Model Object
"""


class Manufacturer:
	def __init__(self, location = None, model = None):
		self.location = location
		self.model = model


	def assemble(self, model):
		#Set the model for the current factory
		self.model = model
		
		return self.model
		
	
	def setPrice(self, price):
		#Set the current price of the model, if factory needs to change it
		self.model.setPrice(price)
	
	
	def setLabel(self, label):
		#Set label for current model in factory
		self.model.setLabe(label)
		
	def getLocation(self):
		#function to return location of factory
		return self.location


	def getModel(self):
		#function to return the current model in use at the factory
		return self.model
	

	def __str__(self):
		return "Factory Location: %s\nCurrent Model: %s\
		\nPrice of Model: %s\nLabel of Model: %s\n" \
		%(self.location, self.model.name, self.model.price \
		, self.model.label)
