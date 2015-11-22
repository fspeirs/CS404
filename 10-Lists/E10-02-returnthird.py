#!/bin/python

# Topic 10: Lists
# Exercise 10-01
#
# S10-02-returnthird.py

#-------------------------------------------
# Instructions:
# 	Complete the function returnthird() to return the 3rd item of 
#	the list parameter named "data".
#-------------------------------------------

def returnthird(data):
	# Complete the code here.


#-------------------------------------------
# Do Not Edit Below
#-------------------------------------------
def main():
	x = [3,7,4,3,2,9,10,21]
	print(returnthird(x))

import unittest
class MyTests (unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('returnthird' in globals(), "You have not implemented the method, or it is not named returnthird()")

	def test_integers(self):
		x = [3,7,4,3,2,9,10,21]
		self.assertEqual(returnthird(x), 4)
	
	def test_strings(self):
		x = ['hello', 'this', 'is', 'a', 'test']
		self.assertEqual(returnthird(x), 'is')
	
	def test_booleans(self):
		x = [True, False, False,True,True]
		self.assertFalse(returnthird(x))
		
	def test_floats(self):
		x = [1.1,3.4,2.2,9.8,7.0,6.3]
		self.assertEqual(returnthird(x),2.2)
	
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."