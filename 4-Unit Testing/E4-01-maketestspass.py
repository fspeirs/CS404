#!/bin/python

# Topic 4: Unit Tests
# Exercise 4-01
#
# E4-01-maketestspass.py

#-------------------------------------------
# Instructions:
# 	The function number_of_slabs() computes the number of slabs
#	required to cover an area. It takes three parameters:
#
#	w - the width of the area in metres
#	h - the height of the area in metres
#	slab_width - the size of the (square) slab.
#
# This function doesn't quite work correctly but we know this because the unit tests
# are failing. Fix the function to make the tests pass.
#-------------------------------------------
def number_of_slabs(w, h, slab_width):
	area = w * h
	return area * slab_width


#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):

	def testNormal1(self):
		self.assertEquals(number_of_slabs(50,20,2), 250)
	def testNormal2(self):
		self.assertEquals(number_of_slabs(30,15,1), 450)
	def testNormal3(self):
		self.assertEquals(number_of_slabs(10,10,2), 25)
	def testNormal4(self):
		self.assertEquals(number_of_slabs(8,8,2), 16)
	def testNormal5(self):
		self.assertEquals(number_of_slabs(2,2,0.1), 400)
	def testNormal6(self):
		self.assertEquals(number_of_slabs(10,10,1), 100)
	def testNormal7(self):
		self.assertEquals(number_of_slabs(500,500,4), 15625)
		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."
