#!/bin/python

# Topic 3: Functions
# Exercise 3-07
#
# E3-07-FunctionTest.py

#-------------------------------------------
# Instructions:
# 	The main() function in this program is complete but the functions it calls
#	do not yet exist.
#
#	Define and write the functions so the program operates correctly.
#-------------------------------------------
	
def main():
	width = 22
	height = 90
	a = area(width, height)
	print "Your floor area is {0} square metres.".format(a)
	
	total = sum(width, height)
	print "Width and height add up to {0} metres.".format(total)
	
	diff = difference(width, height)
	print "There are {0} metres difference between width and height.".format(diff)
	
# Instructions:
# 1. Read the code above
# 2. Decide which functions you need to write to make the program work.
# 3. Write those functions below.
#
# Hints: if you run the program and get a "global name 'XXXX' is not defined", you haven'total
# written the function or have named it differently from the call.
# There are three functions required.
# All functions must return a value.
# You can use all your iTunes U notes to complete this task.
# Submit a screenshot of your finished code.

# Write functions here

#-------------------------------------------
# Do Not Edit Below
#-------------------------------------------
if __name__ == '__main__':
	main()