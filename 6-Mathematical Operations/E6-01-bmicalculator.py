#!/bin/python

# Topic 6: Mathematical Operations
# Exercise 6-01
#
# E6-01-bmicalculator.py

#-------------------------------------------
# Instructions:
# 	Write a function and unit tests that works out a person's Body Mass Index
# 	given their height in centimetres and their weight in kilograms.
#-------------------------------------------

# write your bmi() function here.

import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('bmi' in globals(), "You have not implemented the method, or it is not named bmi()")

	def testNormalData(self):
		self.assertEquals(<#functioncall#>, <#value#>)
	
#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."