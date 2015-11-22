#!/bin/python

# Topic 7: String Operations
# Exercise 7-02
#
# E7-02-stringslicing.py

#-------------------------------------------
# Instructions:
# 	Complete this function that returns the first 
# 	letter of the string that's passed in
#-------------------------------------------

def initial(input_string):
	# Complete the code to do this



#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('initial' in globals(), "You have not implemented the method, or it is not named initial()")

	def testNormalData(self):
		self.assertEqual(initial("Fraser Speirs"), "F")
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