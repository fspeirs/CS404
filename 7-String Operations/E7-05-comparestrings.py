#!/bin/python

# Topic 7: String Operations
# Exercise 7-05
#
# E7-05-comparestrings.py

#-------------------------------------------
# Instructions:
# 	Write a function that takes in two strings and returns True if the two words are 
#	comprised of the same characters, False if they are not.
#	Your function should treat upper and lower case characters the same.
#-------------------------------------------

# Define your function here. Call it compare_strings()



#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('compare_strings' in globals(), "You have not implemented the method, or it is not named compare_strings()")

	def testNormalData(self):
		self.assertTrue(compare_strings("SHOUT", "shout"))
		self.assertFalse(compare_strings("SHOUT", "SHOOT"))
		#-------------------------------------------
		# Write more unit tests here.
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