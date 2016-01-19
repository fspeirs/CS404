#!/bin/python

# Topic 10: Unit Tests
# Exercise 10-6
#
# E10-6-StringLengths.py

#-------------------------------------------
# Instructions:
# 	Exercise 10-06: Write a function that 
#		takes a list of strings and returns the total 
#		number of characters in all the strings. 
#		Remember that len() can return the length 
#		of a string. Use unit tests to show that 
#		it works.    
#-------------------------------------------
def string_lengths(string_list):
	# Write code here

#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):

	def testNormal1(self):
		text = ['apple', 'banana', 'pear']
		self.assertEqual(string_lengths(text), 15)
		text = ['foo', 'bar', 'baz']
		self.assertEqual(string_lengths(text), 9)
		text = ['unit', 'tests', 'rule']
		self.assertEqual(string_lengths(text), 13)

		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."
# coding: utf-8
