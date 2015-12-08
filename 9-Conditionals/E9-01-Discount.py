#coding: utf-8
#!/bin/python

# Topic 9: Unit Tests
# Exercise 9-01
#
# E9-01-Discount.py

#-------------------------------------------
# Instructions:
# 	Write a function that takes in a person’s age and returns 
#   True if they qualify for a discount (discounts are for over 65s only) 
#		and False if not. Write unit tests to show that this function 
#		works correctly. 
#-------------------------------------------

# Define your function here using an IF statement.
def discount(age):
	

#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):

	def testNormal1(self):
		self.assertTrue(discount(90))
		self.assertTrue(discount(100))
		
	def testExtreme(self):
		self.assertFalse(discount(64))
		self.assertFalse(discount(65))
		self.assertTrue(discount(66))
		
		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."


