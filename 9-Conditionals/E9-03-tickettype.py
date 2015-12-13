#!/bin/python

# Topic 9: Unit Tests
# Exercise 9-3
#
# E9-3-tickettype.py

#-------------------------------------------
# Instructions:
# 	Write a function that takes in an age and returns an 
#		integer indicating the type of ticket they can buy. 
#		Under 16: Child Ticket (type 1); 
#		16-55: Adult Ticket (Type 2); 
#		56-65: Senior Ticket (Type 3); 
#		Over 65: Pensioner Ticket (Type 4). 
#
#		Write unit tests to show that this function works.
#-------------------------------------------
def ticket_type(age):
	# Write code here. You will need to write an 
	# if..elsif..else starement and return one of the four
	# possible ticket types in each branch.

#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):

	def testNormal1(self):
		self.assertEqual(ticket_type(10),1)
		self.assertEqual(ticket_type(15),1)
		self.assertEqual(ticket_type(16),2)
		self.assertEqual(ticket_type(20),2)
		self.assertEqual(ticket_type(54),2)
		self.assertEqual(ticket_type(55),2)
		self.assertEqual(ticket_type(56),3)
		self.assertEqual(ticket_type(65),3)
		self.assertEqual(ticket_type(66),4)
		self.assertEqual(ticket_type(100),4)
		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."
