#!/usr/bin/env python
#arraylist.py
#

import sys

MAXLENGTH = 1000000

class arrayList:

	def __init__(self, end = -1):
		self.arr = []
		self.last = end
		
	def FIRST(self):
		if self.last < 0:
			return -1
		else: 
			return 0

	def END(self):
		return (self.last + 1)

	def RETRIEVE(self, p):
		if (p > self.END()) or (p < 0):
			return "Error, position ", p, " is out of range."
		return self.arr[p]

	def LOCATE(self, x):
		for q in range(0, self.last + 1):
			if self.arr[q] == x:
				return q
		return (self.last + 1)

	def NEXT(self, p):
		if p > self.last + 1:
				return -1
		return (p + 1)

	def PREVIOUS(self, p):
		if p <= -1:
			return -1
		return (p - 1)

	def INSERT(self, x, p):
		if self.last >= MAXLENGTH:
			print "Error, list is full."
		elif (p > self.last + 1) or (p < 0):
			print "Error, position ", p, " is out of range."
		else:	
			self.arr.insert(p,x)
			self.last = self.last + 1

	def DELETE(self, p):
		if (p > self.last) or (p < 0):
			print "Error, position ", p, " is out of range."
		else:
			self.last = self.last - 1
			self.arr.pop(p)

	def MAKENULL(self):
		self.arr = []
		self.last = -1
		return self.END()
