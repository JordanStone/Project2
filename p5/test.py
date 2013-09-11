#!/usr/bin/env python
#test.py
#

import concat
import arraylist

def testPass(name,passed):
	if (passed):
		print "The function", name, "has passed."
	else:
		print "The function", name, "has failed."

def main():
	L = arraylist.arrayList()
	for i in range(0,3):
		Q = arraylist.arrayList()
		for j in range(0,5):
			Q.INSERT((i+1)*j,j)
		L.INSERT(Q,i)

	print "Internal lists:"
	print L.arr[0].arr, L.arr[1].arr, L.arr[2].arr

	result = concat.concat(L)
	expected = [0,1,2,3,4,0,2,4,6,8,0,3,6,9,12]

	print "Result list:"
	print result.arr
	
	print "Expected list:"
	print expected

	if result.arr == expected:
		passed = True
	else:
		passed = False

	testPass("concat",passed)

if __name__ == "__main__":
	main()
