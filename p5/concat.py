#!/usr/bin/env python
#concat.py - Concatenates a list of lists, returning a list containing all
#values from the concatenated lists.
#

import arraylist

def concat(L):
	M = arraylist.arrayList()
	count = 0
	for p in range (0,L.END()):
		for q in range (0,L.arr[p].END()):
			M.INSERT(L.arr[p].arr[q], count)
			count= count + 1
	return M
