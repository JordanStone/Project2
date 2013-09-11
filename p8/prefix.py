#!/usr/bin/env python
#prefix.py - Reads in an expression in prefix form and evaluates the
#expression.
#

import sys

def is_op(op):
	oper = ['+','-','*','/','%']
	for i in oper:
		if op in oper:
			return True
	return False

def evalPre(expr):
	temp = expr
	i = temp.pop(0)

	if is_op(i):
		return eval(str(evalPre(temp)) + i + str(evalPre(temp)))
	else:
		return int(i)
