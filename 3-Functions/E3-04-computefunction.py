#!/bin/python

# Topic 3: Functions
# Exercise 3-04
#
# Name: <# Your Name Here #>
#
# 3-04-computefunction.py

#-------------------------------------------
# Instructions:
# 	Write a function that takes two integer parameters - call them a and b - and 
#	returns the value of a + 2 x b.
#	
#	Call your function compute()
#-------------------------------------------

<# Write your function here #>


#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('compute' in globals(), "You have not implemented the method, or it is not named compute()")

	def testNormalData(self):
		self.assertEquals(compute(10,20), 50)
		self.assertEquals(compute(5,10), 25)
		self.assertEquals(compute(2,22), 46)
		self.assertEquals(compute(9,18), 45)

if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."