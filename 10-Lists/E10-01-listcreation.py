#!/bin/python

# Topic 10: Lists
# Exercise 10-01
#
# E10-01-listcreation.py

#-------------------------------------------
# Instructions:
# 	Write a function named createlist() that creates and returns a list of 10 integers.
#-------------------------------------------

# Complete code here


#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('createlist' in globals(), "You have not implemented the method, or it is not named createlist()")

	def test_list_length(self):
		self.assertEqual(len(createlist()), 10)
	
	def test_type(self):
		a = createlist()
		for x in a:
			self.assertTrue(isinstance(x, int))

if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."