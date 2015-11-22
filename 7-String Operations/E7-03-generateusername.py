#!/bin/python

# Topic 7: String Operations
# Exercise 7-03
#
# E7-03-generateusername.py

#-------------------------------------------
# Instructions:
# 	Write a function that takes in two strings: a first name and surname.
# 	The function should create a username comprised of:
#		- The first 5 characters of the surname
#		- The first 3 characters of the first name.
#
#	For example, Benedict Cumberbatch would become CumbeBen.
#-------------------------------------------

# Write this function here. Call it generate_username()

#-------------------------------------------
# Instructions:
#	Complete the main() function so that it:
#		- Prompts the user for their first name
#		- Prompts the user for their second name
#		- Calls generate_username(), passing in both of those names as parameters
#		- Prints out the resulting username.
#-------------------------------------------
def main():
	# Complete the main function here.


#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('generate_username' in globals(), "You have not implemented the method, or it is not named generate_username()")

	def testNormalData(self):
		self.assertEqual(generate_username("Fraser Speirs"), "SpeirFra")
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