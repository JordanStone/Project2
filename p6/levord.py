#!/usr/bin/env python
#levord.py - Takes in a tree and outputs its nodes by level-order listing
#(i.e. breadth-first search)
#

class Tree():
	def __init__(self,car=None):
		self.car = car
		self.child = []

	def addchild(self,obj):
		self.child.append(obj)

def Levord(x):
	Q = []
	M = []
	Q.append(x)
	M.append(x)
	while Q:
		t = Q.pop(0)
		for e in t.child:
			u = e
			if u not in M:
				Q.append(u)
				M.append(u)
	return M
