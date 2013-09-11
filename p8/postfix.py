#!/usr/bin/env python
#postfix.py - Reads in an expression in postfix form and evaluates the
#expression.
#


def is_op(op):
	oper = ['+','-','*','/','%']
	for i in oper:
		if op in oper:
			return True
	return False

def evalPost(expr):
	x=[]
	y=[]
	op_stack=[]

	for i in expr:
		if is_op(i):
			y.append(op_stack.pop())
			x.append(op_stack.pop())
			string = (str(x.pop()) + i + str(y.pop()))
			op_stack.append(eval(string))
		elif i.isdigit():
			op_stack.append(i)
	return op_stack.pop()
