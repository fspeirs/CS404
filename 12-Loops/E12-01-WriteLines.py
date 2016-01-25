#!/bin/python

# Topic 12: Unit Tests
# Exercise 12-1
#
# E12-1-WrtieLines.py 
#-------------------------------------------
# Instructions:
# Write a function that takes one integer parameter
# and writes out lines of ten * characters.
# The number of lines should be controlled by 
# the Parameter.
# If you get done, modify the program to change
# the length of the line based on the parameter.
#-------------------------------------------
def write_lines(length):
	# Write code here

def main():
	write_lines(8)
#-------------------------------------------
# DO NOT EDIT BELOW THIS LINE
#-------------------------------------------
	
import unittest
		
if __name__ == '__main__':
	try:
		main()
	except NameError:
		print "No main() method. Trying Unit Tests."
			
	try:
		unittest.main()
	except NameError:
		print "No Unit Tests to run."

