#!/bin/python

# Topic 5: Input and Output
# Exercise 5-04
#
# E5-04-circlecalculator.py

#-------------------------------------------
# Instructions:
# 	Write a program that asks the user for the radius of a circle and
# 	prints out for them the circumference and area of the circle. The
# 	program should print out a single formatted string that reads:
# 	"You entered a radius of 8.2. The circumference of this circle is
# 	51.496 and the area is 21113.36." (with the numbers replaced with
# 	the correct values for the entered radius). You may wish to re-use
# 	your circle functions from the end of unit assessment in unit 3.
# 	Note that you will have to convert the result of raw_input() to a
# 	float.
#-------------------------------------------

def main():
	# Write your program here.
	
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