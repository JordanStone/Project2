#!/usr/bin/env python
#listmerge.py - Can take any number of lists and merge them into one list.
#

import arraylist

def merge(*L):
	M = arraylist.arrayList()
	count = 0
	for p in range(0,len(L)):	
		for q in range (0,L[p].END()):
			M.INSERT(L[p].arr[q], count)
			count = count + 1
	M.arr = sorted(M.arr)
	return M
