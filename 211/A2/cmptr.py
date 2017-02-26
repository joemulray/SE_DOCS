#!/usr/bin/env python
"""
Joseph Mulray
SE211
Computer Class:
Takes in Advanced or Simple
Factory Objects
"""

from pf import Monitor, Keyboard, Cpu, \
AdvancedComputerPartsFactory, ComputerPartsFactory


class Computer:
	#Computer class, initiated with computer parts factory
	def __init__(self, factory = None):
		self._factory = factory
		self._monitor = factory.monitor
		self._keyboard = factory.keyboard
		self._cpu = factory.cpu


	def displayMonitorInfo(self):
		self._monitor.displayInformation()

	def displayCpuInfo(self):
		self._cpu.displayInformation()

	def displayKeyboardInfo(self):
		self._keyboard.displayInformation()

	def displayCost(self):
		total = self._monitor.cost + self._cpu.cost + self._keyboard.cost
		print 'Total Cost: %s\n' % total




if __name__ == '__main__':

	"""
	###########################################
	DEBUGGING PART OF PROGRAM:
	tests each class and its attributes
	###########################################
	"""

	#Declaring variables to make code cleaner
	computer = ComputerPartsFactory()
	advComputer = AdvancedComputerPartsFactory()

	monitor = computer.createMonitor()	
	advMonitor = advComputer.createMonitor()


	keyboard = computer.createKeyboard()
	advKeyboard = advComputer.createKeyboard()

	cpu = computer.createCpu()
	advCpu = advComputer.createCpu()


	#Set each attribute for computer parts
	#make sure each function of class works
	monitor.name = "HP 23er"
	monitor.model = "1"
	monitor.cost = 150
	
	keyboard.name = "Razer Deathstalker"
	keyboard.cost = 50

	cpu.name = "AMD FX-8350 Black Edition"
	cpu.processor = "4.0"
	cpu.series = "FX-Series"
	cpu.cost = 300


	#Set each attribute for advanced parts
	advMonitor.name = "Acer V226HQL "
	advMonitor.model = "1040"
	advMonitor.cost = 200

	advKeyboard.name = "Corsair K70"
	advKeyboard.cost = 200

	advCpu.name = "Intel Core i5-7600K"
	advCpu.processor = "3.3"
	advCpu.series = "Core i5"
	advCpu.cost = 239	

	print '---------------------'
	print "Simple Components:\n"
	#Computer Parts Factory
	monitor.displayInformation()
	keyboard.displayInformation()
	cpu.displayInformation()

	print '---------------------'
	print "Advanced Components:\n"
	#Advanced Computer Parts Factory
	advMonitor.displayInformation()
	advKeyboard.displayInformation()
	advCpu.displayInformation()


	print '---------------------'
	print "Main Computer Class:\n"
	#Setting Computer class with advanced components
	#and testing attributes make sure 
	#connects to four "interfaces

	#tested with advanced computer parts
	computer = Computer(advComputer)

	computer._monitor.name = "Apple Thuderbolt"
	computer._monitor.model = "123"
	computer._monitor.cost = 800

	computer._keyboard.name = "Magic Keyboard"
	computer._keyboard.cost = 300

	computer._cpu.name = "Intel"
	computer._cpu.processor = "4.2"
	computer._cpu.cost = 400
	computer._cpu.series = "Core i7"	


	#Display computer attributes
	computer.displayMonitorInfo()
	computer.displayKeyboardInfo()
	computer.displayCpuInfo()
	computer.displayCost()



