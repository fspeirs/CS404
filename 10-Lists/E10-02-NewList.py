# coding: utf-8
#!/bin/python

# Topic 10: Lists
# Exercise 10-01
#
# E10-02-newlist.py

#-------------------------------------------
# Instructions:
# 	Complete the function returnthird() to return 
#  the 1st, 3rd, 5th and 7th item of 
#	  the list parameter named "data".
#-------------------------------------------

def return_new_list(data):
	# Complete the code here.
	

#-------------------------------------------
# Do Not Edit Below
#-------------------------------------------
def main():
	x = [3,7,4,3,2,9,10,21]
	print(return_new_list(x))

import unittest
class MyTests (unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('return_new_list' in globals(), "You have not implemented the method, or it is not named return_new_list()")

	def test_integers(self):
		x = [3,7,4,3,2,9,10,21,30,50]
		new_list = return_new_list(x)
		self.assertEqual(new_list[0], x[0])
		self.assertEqual(new_list[1], x[2])
		self.assertEqual(new_list[2], x[4])
		self.assertEqual(new_list[3], x[6])


	
	def test_strings(self):
		x = ['hello', 'this', 'is', 'a', 'test', 'of', 'my', 'program', 'code']
		new_list = return_new_list(x)
		self.assertEqual(new_list[0], x[0])
		self.assertEqual(new_list[1], x[2])
		self.assertEqual(new_list[2], x[4])
		self.assertEqual(new_list[3], x[6])
	
	def test_booleans(self):
		x = [True, False, False,True,True, False, False, True, True]
		new_list = return_new_list(x)
		self.assertEqual(new_list[0], x[0])
		self.assertEqual(new_list[1], x[2])
		self.assertEqual(new_list[2], x[4])
		self.assertEqual(new_list[3], x[6])
		
	def test_floats(self):
		x = [1.1,3.4,2.2,9.8,7.0,6.3,9.9,18.2,21.1,10.1]
		new_list = return_new_list(x)
		self.assertEqual(new_list[0], x[0])
		self.assertEqual(new_list[1], x[2])
		self.assertEqual(new_list[2], x[4])
		self.assertEqual(new_list[3], x[6])
	
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."