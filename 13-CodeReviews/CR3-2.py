#!/bin/python

#-------------------------------------------
# Code review
# 	Based on the unit tests below, try and explain 
#	the age rule that func() is trying to enforce.
#-------------------------------------------


import unittest
class MyTests(unittest.TestCase):
	def testNormalData(self):
		self.assertTrue(allowed(3))
		self.assertTrue(allowed(5))
		self.assertFalse(allowed(10))
		self.assertFalse(allowed(15))
		
	def testExtremeData(self):
		self.assertTrue(allowed(7))
		self.assertTrue(allowed(8))
		self.assertFalse(allowed(9))

	def testExceptionalData(self):
		self.assertFalse(allowed('apple'))
		self.assertFalse(allowed('banana'))
		self.assertFalse(allowed(True))

if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."