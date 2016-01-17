#!/bin/python

# Topic 10: Unit Tests
# Exercise 10-5
#
# E10-5-SumList.py

#-------------------------------------------
# Instructions:
# 	Write a function that takes a list of
#		Integers and returns the sum of all 
#		numbers in it.
#-------------------------------------------
def sum_list(data):
	# Write code here

#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):

	def testNormal1(self):
		total = sum_list([1,3,5,7])
		self.assertEqual(total, 16)
		total = sum_list([2,4,6,8])
		self.assertEqual(total, 20)
		total = sum_list([10,20,30])
		self.assertEqual(total, 60)
		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."
