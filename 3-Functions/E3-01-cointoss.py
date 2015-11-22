#!/bin/python

# Topic 3: Functions
# Exercise 3-01
#
# Name: <# Your Name Here #>
#
# 3-01-cointoss.py

#-------------------------------------------
# Instructions:
# 	You have been given a function called toss() that will print out "heads" or "tails"
#	at random.
#
#	You must modify the function called main() to call the toss() function three times.
#-------------------------------------------

def main():
	# Call the toss() function here.
	# Make sure your calls to toss() are indented to line up with this comment.
	
#-------------------------------------------
# Do not edit below this line
#-------------------------------------------

from random import *

# Function: toss()
# Purpose: 	Prints "heads" or "tails"
def toss():
	if random() <= 0.5:
		print "Heads"
	else:
		print "Tails"

if __name__ == "__main__":
	main()