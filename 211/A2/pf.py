#!/usr/bin/env python
"""
Joseph Mulray
SE 211: ComputerParts
Components of Computer
Gave each class of Computer Parts
attributes such as name, model, cost
for this case
"""



class ComputerPartsFactory:
	#Computer parts factory class
	def __init__(self):
		self.monitor = Monitor()
		self.keyboard = Keyboard()
		self.cpu = Cpu()


	def createMonitor(self):
		return self.monitor

	def createKeyboard(self):
		return self.keyboard

	def createCpu(self):
		return self.cpu


class AdvancedComputerPartsFactory:
	#Advanced Computer parts factory class
	def __init__(self):
		self.monitor = Monitor()
		self.keyboard = Keyboard()
		self.cpu = Cpu()

	def createMonitor(self):
		return self.monitor

	def createKeyboard(self):
		return self.keyboard

	def createCpu(self):
		return self.monitor



class Monitor:
	#Monitor class of a Computer component

	def __init__(self, name = None, model = None, cost=0):
		self.name = name
		self.model = model
		self.cost = cost

	def displayInformation(self):
		print "Name: %s" %self.name
		print "Model: %s" %self.model
		print "Cost: %s\n" %self.cost


class Cpu:
	#CPU class component

	def __init__(self, name = None, processor = None, series = None, cost =0):
		self.name = name
		self.processor = processor
		self.series = series
		self.cost = cost

	def displayInformation(self):
		print "Name: %s" %self.name
		print "Processor: %s" %self.processor
		print "Series: %s" %self.series
		print "Cost: %s\n" %self.cost


class Keyboard:
	#Keyboad class component

	def __init__(self, name = None, cost = 0):
		self.name = name
		self.cost = cost

	def displayInformation(self):
		print "Name: %s" %self.name
		print "Cost: %s\n" %self.cost



