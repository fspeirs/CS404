#!/bin/python

#-------------------------------------------
# Code review
# 	State the range of ages that get a discount.
#-------------------------------------------

def get_discount(age):
	if age < 16 or age > 70:
		return True
	else:
		return False