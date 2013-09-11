#!/usr/bin/env python
#test.py
#

from listconvert import preTree, postTree, postList, preList, inList, Tree

def testPass(name,passed):
	if (passed):
		print "The function", name, "has passed."
	else:
		print "The function", name, "has failed."

def main():
	
	pre = [('+','i'),(1,'l'),('*','i'),(2,'l'),('-','i'),(3,'l'),(5,'l')]
	pre2 = [('-','i'),('+','i'),(67,'l'),(12,'l'),(45,'l')] 	
	post = [(1,'l'),(2,'l'),(3,'l'),(5,'l'),('-','i'),('*','i'),('+','i')]
	post2 = [(67,'l'),(12,'l'),('+','i'),(45,'l'),('-','i')] 

	t = preTree(pre)
	u = preTree(pre2)
	v = postTree(post)
	w = postTree(post2)

	if t.car != '+' or \
	t.left.car != 1 or \
	t.right.car != '*' or \
	t.right.left.car != 2 or \
	t.right.right.left.car != 3 or \
	t.right.right.right.car != 5:
		passed = False
	else:
		passed = True

	testPass("preTree1",passed)
	passed = True

	if u.car != '-' or \
	u.left.car != '+' or \
	u.left.left.car != 67 or \
	u.left.right.car != 12 or \
	u.right.car != 45:
		passed = False

	testPass("preTree2",passed)
	passed = True

	if v.car != '+' or \
	v.left.car != 1 or \
	v.right.car != '*' or \
	v.right.left.car != 2 or \
	v.right.right.left.car != 3 or \
	v.right.right.right.car != 5:
		passed = False
	
	testPass("postTree1",passed)
	passed = True

	if w.car != '-' or \
	w.left.car != '+' or \
	w.left.left.car != 67 or \
	w.left.right.car != 12 or \
	w.right.car != 45:
		passed = False

	testPass("postTree2",passed)
	passed = True

	print '\n',"Post:"
	x = postList(t)
	y = postList(u)
	print x

	print y, '\n'

	exp1 = "1 2 3 5 - * + "
	exp2 = "67 12 + 45 - "
	if x != exp1:
		passed = False
	testPass("postList1",passed) #Fails due to preTree construction issue
	passed = True
	if y != exp2:
		passed = False
	testPass("postList2",passed)

	print '\n',"Pre:"
	x = preList(v)
	y = preList(w)
	print x

	print y, '\n'

	exp1 = "+ 1 * 2 - 3 5 "
	exp2 = "- + 67 12 45 "
	if x != exp1:
		passed = False	
	testPass("preList1",passed)
	passed = True
	if y != exp2:
		passed = False
	testPass("preList2",passed)

	print '\n',"In:"
	x = inList(t)
	y = inList(u)
	print x

	print y, '\n'

	exp1 = "1 + 2 * 3 - 5 "
	exp2 = "67 + 12 - 45 "
	if x != exp1:
		passed = False
	testPass("inList1",passed) #Fails due to preTree construction issue
	passed = True
	if y != exp2:
		passed = False
	testPass("inList2",passed)

if __name__ == "__main__":
	main()
