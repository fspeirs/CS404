#!/bin/python
from random import *

def rand_bool():
	return random() < 0.5
	

# Program to post random logic questions and track scores.
score = 0
streak = 0
longest_streak = 0

for i in range(0,20):
	x = rand_bool()
	y = rand_bool()
	answer = x and y
	input = raw_input("\n{2}: What is {0} AND {1}? [T/F] ".format(x, y, i))
	if input == "T":
		input = True
	else:
		input = False
		
	if input == answer:
		score+=1
		streak+=1
		if streak > longest_streak:
			longest_streak = streak
		print "Correct!\n"
	else:
		print "Sorry, the answer was {0}.\n".format(answer)
		streak = 0
	
	print "Current score: {0}/20. Current streak: {1}, Longest streak: {2}\n".format(score, streak, longest_streak)