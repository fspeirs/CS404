#!/bin/python

# Topic 7: String Operations
# Exercise 7-06
#
# E7-06-checkpassword.py

#-------------------------------------------
# Instructions:
# 	Write a function that takes in a password as a parameter, then checks to see if 
#	the user can enter one of its characters correctly.
#
#	Your function should choose a random character in the password. To do this, you have
#	to use randint() to generate a random number between 0 and the last index in the string.
#
#	Recall that len(x) will give you the *number of characters* in the string x, so you should
#	call randint(0, len(x)-1) to get a random number that you can use as an index into the string.
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