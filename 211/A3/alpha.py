#!/usr/bin/env python

"""
Joseph Mulray
SE211
Assignment 3:
AlphaMobile Class
Defines Factory Locations
and current Models of those Factories
"""

from manufact import Manufacturer
from model import Model

class AlphaMobile:
	def __init__(self):
		
		#Set the two manufacturing locations for AlphaMobile
		NYFact = Manufacturer("New York")
		SPFact = Manufacturer("Singapore")
		
		#Create the types of AlphaMobile will be producing
		Smart4 = Model()
		Smart5 = Model()
		Smart6 = Model()
		
		#Define the specifications for each Model
		Smart4.setName("SMART4")
		Smart4.setPrice(650.00)
		Smart4.setLabel("IntelT9: Android 5.3 : M35332 : AMOLED")

		Smart5.setName("SMART5")
		Smart5.setPrice(750.00)
		Smart5.setLabel("i7 : iOS 10.2 : M35334 : RETINA")
		
		Smart6.setName("SMART6")
		Smart6.setPrice(900.00)
		Smart6.setLabel("i7 Pro : Linux : M35336 : SUPER AMOLED")

		#Assemble each of the models in the Specificied Factories
		
		#Assemble Smart4 and Smart 5 in New York	
		NYFact4 = NYFact.assemble(Smart4)
		
		#status of the New York Factory
		print NYFact
		
		NYFact5= NYFact.assemble(Smart5)
		print NYFact

		#Assemble Smart 5 and Smart6 in Singapore
		SPFact5 = SPFact.assemble(Smart5)

		#status of the Singapore Factory
		print SPFact		

		SPFact6 = SPFact.assemble(Smart6)
		print SPFact		

		#Show the description for each of the Factory Models Made
		NYFact4.description()
		NYFact5.description()
		SPFact5.description()
		SPFact6.description()
			

if __name__ == '__main__':
	AlphaMobile()
