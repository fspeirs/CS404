#!/bin/python

# Topic 5: Input and Output
# Exercise 5-02
#
# E5-02-sayhello.txt

#-------------------------------------------
# Instructions:
# 	Write a program that takes a person’s name and says hello to them.
#-------------------------------------------

def main():
	# Write your code here.


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