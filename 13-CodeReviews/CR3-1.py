#!/bin/python

#-------------------------------------------
# Code review
# 	Based on the unit tests below, try and explain what func() does.
#-------------------------------------------


import unittest
class MyTests(unittest.TestCase):
	def testNormalData(self):
		self.assertEquals(func('Fraser', 'Speirs'), 'FS')
		self.assertEquals(func('Alan', 'Jones'), 'AJ')
		self.assertEquals(func('Jim', 'Bob'), 'JB')
		self.assertEquals(func('Slimy', 'Snake Eyes'), 'SS')
		self.assertEquals(func('Zoe', 'Zebra'), 'ZZ')
		