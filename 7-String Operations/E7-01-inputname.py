#!/bin/python

# Topic 7: String Operations
# Exercise 7-01
#
# E7-01-inputname.py

#-------------------------------------------
# Instructions:
# 	Write a program that prompts a person for their 
#   name and tells them how many letters are in their name.
#-------------------------------------------

# Define your function here. Call it get_name_length()



#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('get_name_length' in globals(), "You have not implemented the method, or it is not named get_name_length()")

	def testNormalData(self):
		self.assertEqual(get_name_length("Fraser Speirs"), 13)
		# Write more unit tests here.
				
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."