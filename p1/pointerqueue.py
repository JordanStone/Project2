#!/usr/bin/env python
#pointerqueue.py - pointer implementation of a queue ADT.
#

import sys

class Node:
	def __init__(self, cargo=None, link=None):
		self.car = cargo
		self.link = link
	def __str__(self):
		return str(self.car)

class pointerQueue:

	def __init__(self):
		self.front = None
		self.rear = None

	def FRONT(self):
		if self.EMPTY():
			print "Error, queue is empty."
		else:
			return self.front.car
	
	def ENQUEUE(self, x):
		newN = Node(x)
		newN.link = None
		if self.EMPTY():
			self.front = newN
			self.rear = newN
		else:
			last = self.rear
			last.link = newN
			self.rear = newN

	def DEQUEUE(self):
		x = self.front.car
		self.front= self.front.link
		if self.EMPTY():
			self.rear = None
	
	def EMPTY(self):
		if self.front == None:
			return True
		else:
			return False
	
	def MAKENULL(self):
		self.front = None
		self.rear = self.front

if __name__ == "__main__":
	main()
