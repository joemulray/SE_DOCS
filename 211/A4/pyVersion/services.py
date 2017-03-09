#!/usr/bin/env python


class EmailService:
	def __init__(self, message = None):
		self.message = message


	def update(self,message):
		self.message = message

	def __str__(self):
		return "Message: %s" % self.message


class SmsService:
	def __init__(self, message = None):
		self.message = message

	def update(self, message):
		self.message = message

	def __str__(self):
		return "Message: %s" % self.message


class PhoneService:
	def __init__(self, message = None):
		self.message = message
	
	def upadte(self, message):
		self.message = message

	def __str__(self):
		return "Message: %s" % self.message
		
