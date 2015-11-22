#!/bin/python

# Topic 5: Input and Output
# Exercise 5-03
#
# E5-03-longdate.py

#-------------------------------------------
# Instructions:
# 	Write  a function that takes three integer parameters: 
#	day, month and year and returns a formatted string that says 
#	"This is the 10th day of the 3rd month of the year 2015"
#  (with the numbers replaced with the passed in parameters).
#
#	Write unit tests to show that the function works.
#-------------------------------------------


# write your function here call it format_date()


import unittest
class MyTests(unittest.TestCase):
	def testFunctionExists(self):
		self.assertTrue('format_date' in globals(), "You have not implemented the method, or it is not named format_date()")

	def testNormalData(self):
		self.assertEquals(format_date(18,1,2020), 'This is day 18 of month 1 of the year 2020')
		# Add more unit tests here.
		
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