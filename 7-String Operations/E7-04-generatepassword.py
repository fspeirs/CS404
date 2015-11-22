#!/bin/python

# Topic 7: String Operations
# Exercise 7-04
#
# E7-04-generatepassword.py

#-------------------------------------------
# Instructions:
# 	Write a function that takes in a sentence as a parameter.
#   Use this text to generate a password by combining the 
#	1st, 3rd, 5th, 7th, 9th and 11th letters
#-------------------------------------------

# Define your function here. Call it generate_password()

#-------------------------------------------
# Instructions:
#	Complete the main() function so that it:
#		- Prompts the user for a sentence
#		- Calls generate_password(), passing in the sentence as a parameter
#		- Prints out the resulting password
#-------------------------------------------
def main():
	# Complete the main function here.




#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('generate_password' in globals(), "You have not implemented the method, or it is not named generate_password()")

	def testNormalData(self):
		self.assertEqual(generate_password("Many years later, we fell asleep."), "Mn ea ")
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