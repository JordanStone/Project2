#!/usr/bin/env python
#test.py
#

import listmerge
import arraylist

def testPass(name,passed):
	if (passed):
		print "The function", name, "has passed."
	else:
		print "The function", name, "has failed."

def main():
	a = arraylist.arrayList()
	b = arraylist.arrayList()
	c = arraylist.arrayList()
	for i in range(0,5):
		a.INSERT(i+1,i)
	for i in range(0,7):
		b.INSERT(i+2,i)
	for i in range(0,3):
		c.INSERT(i-2,i)

	print "3 Lists to merge:"
	print "A: ", a.arr
	print "B: ", b.arr
	print "C: ", c.arr

	result = listmerge.merge(a,b,c)
	expected = [-2, -1, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]

	print "Result List:"
	print result.arr

	print "Expected List:"
	print expected

	if result.arr == expected:
		passed = True
	else:
		passed = False

	testPass("listmerge",passed)

if __name__ == "__main__":
	main()
