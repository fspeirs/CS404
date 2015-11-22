#!/bin/python

# Topic 3: Functions
# Exercise 3-05
#
# E3-05-computeaverage.py

#-------------------------------------------
# Instructions:
# 	Write a function called average() that takes four parameters and
#	returns the average of the four numbers
#-------------------------------------------

# Write your function here.



#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('average' in globals(), "You have not implemented the method, or it is not named average()")

	def testNormalData(self):
		self.assertAlmostEquals(average(5,5,5,5), 5.0, 2)
		self.assertAlmostEquals(average(8,10,21,55), 23.5, 2)
		self.assertAlmostEquals(average(99,100,101,102), 100.5, 2)
		self.assertAlmostEquals(average(0,0,0,0), 0.0, 2)
		self.assertAlmostEquals(average(49,50,51,52), 50.5, 2)
		self.assertAlmostEquals(average(50,0,100,0), 37.5, 2)
		self.assertAlmostEquals(average(10,9,8,7), 8.5, 2)
		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."