#!/bin/python

# Topic 8: Boolean Logic
# Exercise 8-04
#
# E8-04-alladults.py

#-------------------------------------------
# Instructions:
# 	Write a function called all_adults() that takes in two boolean values, 
#	each indicating if the person is an adult (True) or not (False). The function should return True 
#	if the party consists of all-adults (age is 18 or over). The function should 
#	return false if the party contains a child.
#-------------------------------------------

def all_adults(person1, person2):
	# Complete code

#-------------------------------------------
# Instructions:
# 	Write a second function called child_present() that takes two boolean values 
#	indicating whether the person is a child (True) or not (False)
#	and returns True if there are any children in the party. Write suitable unit tests 
#	for both functions that cover all possible combinations of two boolean values.	
#-------------------------------------------
def child_present(person1, person2):
	# Complete code

#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
import unittest

class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('all_adults' in globals(), "You have not implemented the method, or it is not named all_adults()")
		self.assertTrue('child_present' in globals(), "You have not implemented the method, or it is not named child_present()")

	def testAllAdults(self):
		self.assertTrue(all_adults(True, True))
		self.assertFalse(all_adults(True, False))
		self.assertFalse(all_adults(False, True))
		self.assertFalse(all_adults(False, False))
		
	def testChildPresent(self):
		# Complete tests for child_present()
				
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."