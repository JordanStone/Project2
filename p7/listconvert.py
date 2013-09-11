#!/usr/bin/env python
#listconvert.py - takes a tree listed in preorder where every node has two
#children and converts it to postorder listing.
#

class Tree():
	def __init__(self,car=None,left=None,right=None):
		self.car = car
		self.left = left
		self.right = right

def preTree(tup):
	op = []
	stack = []	
	for i in tup:
		if i[1] == 'i':
			op.append(Tree(i[0]))
		elif i[1] == 'l':
			stack.append(Tree(i[0]))
			if len(stack) >= 2:
				right = stack.pop()
				left = stack.pop()
				node = op.pop() 
				node.left = left
				node.right = right
				stack.append(node)
	return stack.pop()

def postTree(tup):
	stack = []
	for i in tup:
		if i[1] == 'i':
			right = stack.pop()
			left = stack.pop()
			T = Tree(i[0],left,right)
			stack.append(T)
		elif i[1] == 'l':
			stack.append(Tree(i[0]))
	return stack.pop()

def postList(T):
	stack = []
	string = ""
	if T is not None:
		stack.append(postList(T.left))
		stack.append(postList(T.right))
		stack.append(str(T.car)+ ' ')
	for i in stack:
		string += str(i)
	return string

def preList(T):
	stack = []
	string = ""
	if T is not None:
		stack.append(str(T.car) + ' ')
		stack.append(preList(T.left))
		stack.append(preList(T.right))
	for i in stack:
		string += str(i)
	return string

def inList(T):
	stack = []
	string = ""
	if T is not None:
		stack.append(inList(T.left))
		stack.append(str(T.car) + ' ')
		stack.append(inList(T.right))
	for i in stack:
		string += i
	return string

