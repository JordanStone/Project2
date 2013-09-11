#!/usr/bin/env python
#test.py 
#

import sys
from levord import Tree
from levord import Levord

def testPass(name,passed):
	if (passed):
		print "The function", name, "has passed."
	else:
		print "The function", name, "has failed."

def main():
	t = Tree('A') #root node, height 0
	passed = True

	#Height 1 nodes
	t.addchild(Tree('B'))
	t.addchild(Tree('C'))

	#Height 2 nodes
	t.child[0].addchild(Tree('D'))
	t.child[0].addchild(Tree('E'))

	t.child[1].addchild(Tree('F'))
	t.child[1].addchild(Tree('G'))
	t.child[1].addchild(Tree('H'))

	#Height 3 nodes
	t.child[0].child[1].addchild(Tree('I'))

	t.child[1].child[1].addchild(Tree('J'))
	t.child[1].child[1].addchild(Tree('K'))

	t.child[1].child[2].addchild(Tree('L'))

	#Height 4 nodes
	t.child[0].child[1].child[0].addchild(Tree('M'))
	t.child[0].child[1].child[0].addchild(Tree('N'))

	result = Levord(t)
	expected = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

	resultprint = []

	for i in result:
		resultprint.append(i.car)

	print "Result List:"
	print resultprint

	print "Expected List:"
	print expected
	
	if resultprint != expected:
			passed = False

	testPass("levord",passed)

if __name__ == "__main__":
	main()
