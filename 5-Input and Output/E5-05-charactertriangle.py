#!/bin/python

# Topic 5: Input and Output
# Exercise 5-05
#
# E5-05-charactertriangle.py

#-------------------------------------------
# Instructions:
# 	Write a program that asks the user to enter a character and draws
# 	a triangle using that character.
#-------------------------------------------

def main():
	# Write your code here.
	char = raw_input('Please enter a character:')

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