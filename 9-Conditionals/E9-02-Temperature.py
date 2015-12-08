#!/bin/python

# Topic 9: Unit Tests
# Exercise 9-2
#
# E9-02-Temperature.py

#-------------------------------------------
# Instructions:
# 	Write a function that takes in a temperature parameter 
#		and returns True if the heating should be turned on and 
#		False if it should be off. The threshold for turning on 
#		the heating is if the temperature is at or below 15 degrees. 
#		Use the unit tests to guide your programming. 
#-------------------------------------------

# Write your function here. Call it heating_on()
# The function takes one parameter.


#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):

	def testNormal1(self):
		self.assertTrue(heating_on(0))
		self.assertTrue(heating_on(5))
		self.assertTrue(heating_on(10))
		self.assertTrue(heating_on(12))
		self.assertTrue(heating_on(15))
		self.assertFalse(heating_on(16))
		self.assertFalse(heating_on(20))
		
		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."
