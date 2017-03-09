#!/usr/bin/env python


class ServiceNofifier:

	def __init__(self, pService = None):
		self.Services = []
	
	def attach(self, pService):
		self.Services.append(pService)
	
	def detach(self, pService):
		self.Services.remove(pService)

	def ServiceNotifier(self, message):

		if self.Services:
			for service in self.Services:
				service.update(message)



		
