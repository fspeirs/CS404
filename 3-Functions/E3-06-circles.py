#!/bin/python

# Topic 3: Functions
# Exercise 3-06
#
# Name: <# Your Name Here #>
#
# 3-06-circles.py

#-------------------------------------------
# Instructions:
# 	Write a program that has two functions. 
#	The first function calculates the circumference of a circle given its radius. 
#	The second function should calculate and return the area of a circle given its radius.
#
#	Name your functions circumference() and area().
#	The calculation for the circumference of a circle is 2 * 3.14 * radius
#	The calculation for the area of a circle is 3.14 * radius * radius
#-------------------------------------------

<# Write circumference() here. #>

<# Write area() here. #>


#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest
def testFunctionExists(self):
		self.assertTrue('circumference' in globals(), "You have not implemented the method, or it is not named circumference()")
		self.assertTrue('area' in globals(), "You have not implemented the method, or it is not named area()")

class MyTests(unittest.TestCase):

	def testCircumference(self):
		self.assertAlmostEquals(circumference(22), 138.16, 2)
		self.assertAlmostEquals(circumference(10), 62.8, 2)	
		self.assertAlmostEquals(circumference(99), 621.72, 2)
		self.assertAlmostEquals(circumference(77), 483.56, 2)
		self.assertAlmostEquals(circumference(120), 753.6, 2)
		self.assertAlmostEquals(circumference(375), 2355, 2)
		self.assertAlmostEquals(circumference(52), 326.56, 2)

	def testArea(self):
		self.assertAlmostEquals(area(22),  1519.76, 2)
		self.assertAlmostEquals(area(10),  314, 2)
		self.assertAlmostEquals(area(99),  30775.14, 2)
		self.assertAlmostEquals(area(77),  18617.06, 2)
		self.assertAlmostEquals(area(120), 45216, 2)
		self.assertAlmostEquals(area(375), 441562.5, 2)
		self.assertAlmostEquals(area(52),  8490.56, 2)
			
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."