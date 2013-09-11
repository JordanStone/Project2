#!/usr/bin/env python
#test.py
#

import sys
import postfix
import prefix

def testPass(name,passed):
	if (passed):
		print "The function", name, "has passed."
	else:
		print "The function", name, "has failed."

def main():	
	post = ['67','12','+','45','-']
	pre = ['-','+','67','12','45']

	passed = True
	expected = 34
	
	for i in post:
		sys.stdout.write(i+" ")

	result = 	postfix.evalPost(post)
	print "=", result

	if result != expected:
		passed = False

	testPass("evalPost",passed)
	passed = True
	
	for i in pre:
		sys.stdout.write(i+" ")

	result2 = prefix.evalPre(pre)
	print "=", result2

	if result2 != expected:
		passed = False
	
	testPass("evalPre",passed)

if __name__ == "__main__":
	main()
