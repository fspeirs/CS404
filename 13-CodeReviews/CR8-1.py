#!/bin/python

#-------------------------------------------
# Code review
# 	State the range of values the user can enter to win the game.
#-------------------------------------------

x = 10
y = int(raw_input('Please guess a number between 0 and 15:'))

if x > y:
	print('You have won!')
else
	print('Try again!')