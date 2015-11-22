#!/bin/python

# Topic 5: Input and Output
# Exercise 5-01
#
# E5-01-inputinteger.py

#-------------------------------------------
# Instructions:
# 	Write a function that asks the user for input, converts it to integer
#	and returns it to the calling program.
#-------------------------------------------

# Define your function here. Call it get_input()



#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('get_input' in globals(), "You have not implemented the method, or it is not named get_input()")

	def testNormalData(self):
		self.assertTrue(isinstance(get_input(), int))
		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."