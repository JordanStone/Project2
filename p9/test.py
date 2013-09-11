#!/usr/bin/env python
#test.py 
#

import huff

def testPass(name,passed):
	if (passed):
		print "The function", name, "has passed."
	else:
		print "The function", name, "has failed."

def main():
	symb = [(.07,'a'), (.09,'b'),(.12,'c'),(.22,'d'),(.23,'e'),(.27,'f')]

	tree = huff.makeHuff(symb)
	
	if tree.left.left != 'd' or \
	tree.left.right != 'e' or \
	tree.right.left != 'f' or \
	tree.right.right.left !='c' or \
	tree.right.right.right.left !='a' or \
	tree.right.right.right.right != 'b':
		passed = False
	else:
		passed = True

	testPass("makeHuff",passed)
	passed = True

	result =  huff.encode(tree)

	expected = {'a':'1110','c':'110','b':'1111','e':'01','d':'00','f':'10'}

	if result != expected:
		passed = False
	
	print "symb | prob | code"
	for i in sorted(symb):
		print i[1], "   |", (i[0]), "| ",  result[i[1]]

	testPass("encode",passed)

if __name__ == "__main__":
	main()
