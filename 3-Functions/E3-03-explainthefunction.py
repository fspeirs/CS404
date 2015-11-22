#!/bin/python

# Topic 3: Functions
# Exercise 3-03
#
# Name: <# Your Name Here #>
#
# 3-03-explainthefunction.py

#-------------------------------------------
# Instructions:
# 	There are three functions in this file, with empty comment boxes above them.
#	You don't have to change the code, but you have to read the code and write
#	the comments to explain what the parameters are called and how many there are.
#
#	Remember: 	Every comment line has to begin with #.
#				Run your code before submitting to make sure you didn't break it.
#-------------------------------------------

def main():
	add_numbers(3, 6, 9)
	say_hello_to('Alice', 'Bob')
	print_line_of_stars()

#-------------------------------------------
# Function: add_numbers()
# Description: <# Write what the function does here. #>
# Parameters:
#	<# State the name and type of each parameter here #>
#-------------------------------------------
def add_numbers(num1, num2, num3):
	total = num1 + num2 + num3
	print(total)

#-------------------------------------------
# Function: say_hello_to()
# Description: <# Write what the function does here. #>
# Parameters:
#	<# State the name and type of each parameter here #>
#-------------------------------------------
def say_hello_to(person, friend):
	print "Hello, " + person
	print "Hello, " + friend

#-------------------------------------------
# Function: print_line_of_stars()
# Description: <# Write what the function does here. #>
# Parameters:
#	<# State the name and type of each parameter here #>
#-------------------------------------------
def print_line_of_stars():
	print '*************************************'


if __name__ == '__main__':
	main()