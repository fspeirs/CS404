#!/bin/python

# Topic 6: Mathematical Operations
# Exercise 6-03
#
# E6-03-pythagoras.py

#-------------------------------------------
# Instructions:
# 	 Write a function that works out the size of the square on the
# 	 hypotenuse of a triangle, given the lengths of the other two
# 	 sides. The general formula is a^2 = b^2 + c^2. Your function
# 	 should take in b and c, and return the value of a.
#
#	Use math.sqrt() to get the square root of a number.
#-------------------------------------------
import math # Do not edit this line.

# write your pythagoras() function here
	
#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('pythagoras' in globals(), "You have not implemented the method, or it is not named pythagoras()")

	def testNormalData(self):
		self.assertAlmostEquals(pythagoras(1,2), 2.236, 2)
		self.assertAlmostEquals(pythagoras(18,23), 29.2061637330205, 2)
		self.assertAlmostEquals(pythagoras(45,55),71.0633520177595, 2)
		self.assertAlmostEquals(pythagoras(100,200),223.606797749979, 2)
		self.assertAlmostEquals(pythagoras(1,3),3.16227766016838, 2)
		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."