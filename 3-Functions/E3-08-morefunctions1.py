#!/bin/python

# Topic 3: Functions
# Exercise 3-08
#
# untitled text

#-------------------------------------------
# Instructions:
# 	Below is a function that should return a number that is two greater than the number.
# 	Write the function
#-------------------------------------------
def return_two_more(the_value):
	# Complete the function here.
	

#-------------------------------------------
def main():
	# Below, create a variable and assign an integer to it.
	
	# Next, create a variable and assign the result of calling return_two_more 
	# with the value in the previous line.
	

#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('return_two_more' in globals(), "You have not implemented the method, or it is not named return_two_more()")

	def testNormalData(self):
		self.assertEquals(return_two_more(10), 12)
		self.assertEquals(return_two_more(99), 101)
		self.assertEquals(return_two_more(1000), 1002)
		self.assertEquals(return_two_more(-1), 1)

if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."
	