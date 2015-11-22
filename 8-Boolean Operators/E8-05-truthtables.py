#!/bin/python

# Topic 8: Boolean Logic
# Exercise 8-05
#
# E8-05-truthtables.py

#-------------------------------------------
# Instructions:
# 	Write three functions that calculate and print out the truth tables for And, Or and Not
#-------------------------------------------

def print_and_truth_table():
	x = True
	y = True
	print "{0} AND {1} = {2}".format(x, y, x and y)
	
	# Complete the rest of the truth table.
	
def print_or_truth_table():
	# Complete code
	
def print_not_truth_table():
	# Complete code

def main():
	print_and_truth_table()
	print_or_truth_table()
	print_not_truth_table()
	
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