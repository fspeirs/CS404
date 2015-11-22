#!/bin/python

# Topic 4: Unit testing
# Exercise 4-03
#
# Name: <# Your Name Here #>
#
# 4-03-disneytickets.py

#-------------------------------------------
# Instructions:
# 	This program contains a function that calculates the total cost of tickets 
#	to Disneyland, given a certain number of adults, children and pensioners.
#
#	Tickets cost:
#		£35 for an adult
#		£18 for a child
#		£20 for a pensioner
#
#	Write a comprehensive set of tests to show that this function is correct.
#
#	If any parameters are not integers (since you can't get half a person!) the
#	function should return zero. Make sure you test to see that all three parameters are
#	checked for being ints.
#-------------------------------------------

def ticket_price(adults, children, pensioners):
	if not isinstance(adults, int):
		return 0
	elif not isinstance(children, int):
		return 0
	elif not isinstance(pensioners, int):
		return 0
		
	return (adults * 35) + (children * 18) + (pensioners * 20)


import unittest
class MyTests(unittest.TestCase):
	def testNormalData(self):
		<# Write normal data assertions here. #>
	
	def testExtremeData(self):
		<# Write extreme data assertions here. #>
	
	def testExceptionalData(self):
		<# Write exceptional data assertions here. #>

#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
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