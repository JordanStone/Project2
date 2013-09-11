#!/usr/bin/env python
#test.py
#

import pointerqueue

def testPass(name,passed):
	if (passed):
		print "The method", name, "has passed."
	else:
		print "The method", name, "has failed."

def main():

	rqueue = pointerqueue.pointerQueue() 
	equeue = []

	print "Testing ENQUEUE  method."
	for n in range(1,11):
		rqueue.ENQUEUE(n)
		equeue.append(n)
		if rqueue.rear.car != n:
			passed = False
		else:
			passed = True
	
	testPass("ENQUEUE",passed)
	passed = True

	print "Testing FRONT method."
	if rqueue.FRONT() != equeue[0]:
		print rqueue.FRONT()
		print equeue[0]
		passed = False

	testPass("FRONT",passed)
	passed = True

	print "Testing DEQUEUE method."
	rqueue.DEQUEUE()
	equeue.pop(0)

	if rqueue.FRONT() != equeue[0]:
		print rqueue.FRONT()
		print equeue[0]
		passed = False
	
	testPass("DEQUEUE",passed)
	passed = True

	print "Testing MAKENULL method."
	rqueue.MAKENULL()
	del equeue[0:len(equeue)]
		
	if rqueue.front != None:
		print rqueue.FRONT()
		passed = False
	
	testPass("MAKENULL",passed)

if __name__ == "__main__":
	main()
