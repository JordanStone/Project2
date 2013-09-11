#!/usr/bin/env python
#huff.py - takes in list of symbols and frequencies (in tuples), creates a
#huffman tree and can give the appropriate codes for a created tree.
#

import Queue

class Tree:
	def __init__(self,left=None,right=None):
		self.left = left
		self.right = right
	
def makeHuff(tup):
	p = Queue.PriorityQueue()
	for val in tup:
		p.put(val)
	while p.qsize() > 1:
		l = p.get()
		r = p.get()
		node = Tree(l[1],r[1])
		p.put((l[0] + r[0], node))
	return p.get()[1]

def encode(huff, prefix='', code={}):
	if isinstance(huff,str):
		code[huff] =  prefix 
	else:
		encode(huff.left, prefix + '0', code)
		encode(huff.right, prefix + '1', code)
	return code
