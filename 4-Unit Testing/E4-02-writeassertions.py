#!/bin/python

# Topic 4: Unit Testing
# Exercise 4-01
#
# Name: <# Your Name Here #>
#
# 4-01-designthetest.py

#-------------------------------------------
# Instructions:
# 	This program contains a function that returns True if the parameter is even and
#	False if the parameter is odd.
#
#	Write a series of unit tests to show that it works correctly.
#-------------------------------------------

def is_even(num):
	return num % 2 == 0
	
import unittest # Don't change this
class MyTests(unittest.TestCase):

	def testNormalData(self):
		<# Write a series of assertions to check that this function works correctly. #>
	
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
