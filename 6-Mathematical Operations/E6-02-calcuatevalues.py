#!/bin/python

# Topic 6: Mathematical Operators
# Exercise 6-02
#
# E6-02-calcuatevalues.py

#-------------------------------------------
# Instructions:
# 	Write a function that calculates the average of three numbers and
# 	returns that value raised to the power of 5. Make sure you use
# 	parentheses in your calculation. Use the provided Unit Tests to
# 	show that the function works.
#-------------------------------------------

# Define your calculate() function here.

#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('calculate' in globals(), "You have not implemented the method, or it is not named calculate()")

	def testNormalData(self):
		self.assertEquals(calculate(3,4,5), 1024)
		self.assertEquals(calculate(18,23,22), 4084101)
		self.assertEquals(calculate(45,55,65), 503284375)
		self.assertEquals(calculate(100,200,300), 320000000000)
		self.assertEquals(calculate(1,3,5), 243)
		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."