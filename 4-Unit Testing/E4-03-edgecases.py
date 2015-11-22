#!/bin/python

# Topic 4: Unit Testing
# Exercise 4-02
#
# Name: <# Your Name Here #>
#
# 4-02-completetestsuite.py

#-------------------------------------------
# Instructions:
# 	This program contains a function that returns True if the passed in age is 
#	old enough to rent a car (usually age 25).
#
#	The function should only return true if:
#		1. the parameter passed in is an integer
#		2. the parameter has a value of 25 or greater.
#	
#	If either of these things is not true, the function should return False for safety.
#
# 	Your job is to write a comprehensive set of unit tests that prove that this
#	function is robust in the face of normal, exceptional and extreme data.
#-------------------------------------------
def can_rent(age):
	return age == 25



import unittest
class MyTests(unittest.TestCase):

	def testNormalData(self):
		<# Write a series of assertions that test normal data here. #>
	
	def testExtremeData(self):
		<# Write a series of assertions that test extreme data here. #>
	
	def testExceptionalData(self):
		<# Write a series of assertions that test exceptional data here. #>

#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
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