NAME: Jordan Stone

CONTENTS: 
I submitted code for problems 1,4,5,6,7,8,9. All program code is
written in python and is stored in the .py format.

	Folder hw2Jls564:
		README.txt - text document detailing files submitted in this project and
		completeness of every section.

		REPORT.txt - Unneeded as I did not attempt the timing in problem 3.


	Folder p1:
		pointerqueue.py - contains code for the pointerQueue class, a pointer
		implementation of a queue ADT.

		test.py - test code that goes through all functions of pointerqueue and
		compares them to expected results from a built-in queue. (Python deque)

		Makefile - allows running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".


	Folder p4:
		listmerge.py - contains code for the merge function, which takes in n
		number of lists and will combine and sort them into a single list. Uses
		arraylist class created in project 1.

		test.py - test code that checks capability of listmerge by calling merge on
		multiple lists of differing values and sizes and comparing it to an
		expected list.

		arraylist.py - contains code for the arrayList class, an array
		implementation of a list ADT.

		Makefile - allows running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".


	Folder p5:
		concat.py - contains code for the concat function, which takes a list of
		lists and returns a concatenated list of values. Uses arraylist class
		created in project 1.

		test.py - test code that checks capability of the concat function by
		calling a list containing multiple seperate lists as elements and
		concatenating it into a list containing the values of those elements. This
		list is then compared to an expected list.

		arraylist.py - contains code for the arrayList class, an array
		implementation of a list ADT.

		Makefile - allows  running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".


	Folder p6:
		levord.py - contains code for the levord function and the Tree class that
		supports it. (We talked about allowing this tree class in the CLC earlier,
		as I am not trying problem 2 which would produce a more fully fledged tree
		class)
		The Tree class creates an object with a cargo and an array of children. It
		contains only 2 functions - the constructor and a method addchild, which
		adds a new child to the tree node called.
		levord takes in a tree node and returns a list of the tree's
		nodes in level-order listing.

		test.py - test code that checks capability of the levord function. Creates
		a tree based off of the tree in Figure 3.31 of Data Structures and
		Algorithms(p103), and calls levord on this tree. The result of levord is
		then compared to an expected list of node values.

		Makefile - allows  running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".


	Folder p7:
		listconvert.py - contains code preTree, postTree, postList, preList, and
		inList functions, as well as a binary tree class that supports these
		functions.

		test.py - test code to chec capability of functions in listconvert.py.
		Creates trees based off preorder and postorder expression lists of
		tuples, each tuple containing a value and an identifier character marking
		it as either an internal or external node. Resultant trees are compared to
		expected results. The preorder constructed trees are then traversed in
		postorder and inorder, while the postorder constructed trees are traversed
		in preorder. The results of these traversals are also compared to expected
		results.

		Makefile - allows  running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".

	Folder p8:
		postfix.py - contains code for the evalPost function and an internal
		is_op function. evalPost takes in a list of tokens for an expression 
		in postfix order and returns an evaluation of the expression.

		prefix.py - contains code for the evalPre function and an internal is_op
		function. evalPre takes in a list of tokens for an expression in prefix
		order and returns an evaluation of the expression.

		test.py - test code that checks capability of the evalPost and evalPre
		functions. Evaluates the same expression in both a postfix and prefix form,
		and checks that the correct value is returned from both the evalPost and
		evalPre calls.

		Makefile - allows  running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".


	Folder p9:
		huff.py - contains code for the makeHuff and encode functions, and a
		binary tree class that supports these functions. 
		makeHuff takes in a list of tuples, each containing a frequency and a
		symbol, and returns a Huffman tree corresponding to the list. 
		encode takes in a Huffman tree and constructs a unique code for each leaf
		ofthe tree. encode then returns the completed dict, which contains each
		symbol as a key matched to their respective Huffman code.

		test.py - test code that checks capability of the makeHuff and encode
		functions. Functions are tested using a list of symbols and probabilities
		from Exercise 3.20 in Data Structures and Algorithms(p106). This list of
		tuples is run through makeHuff to create a Huffman tree, and the resulting
		tree is run through encode to create the Huffman codes for the tree. All
		expected leaf positions and values on the tree are checked, and the
		resultant code dictionary is compared to the expected dictionary
		structure.

		Makefile - allows  running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".

 
COMPLETE:
	Problems p1, p4, p5, p6, p8, and p9 are complete.


UNFINISHED:
	Problem p7's preTree function has an issue with some preorder lists, and
	returns incorrectly constructed trees in these cases. This can be seen with
	the list "pre". From what I can see, the issue stems from operators being
	popped off the op list earlier than they should be. I have attempted fixing
	the issue but have not found a practical solution yet. 


COMPILATION & EXECUTION:
	As described above, every problem folder contains a Makefile that will run
	the test code by either "make" or "make test". This will run the test.py in
	all problem folders.


TEST CASES:
	Test for p1 makes use of Python list to compare the pointerqeueue object to.
	The list used in this test acts similarly to a queue in pushing and popping
	variables, displaying front value, and being made null.

	Test of p4 compares the merged arrayList to a Python list with the expected
	values and order.

	Test of p5 compares the concatenated arrayList to a Python list of the
	expected values and order.

	Test of p6 first puts the values from the list of nodes into a seperate
	list, then compares this list of values to a Python list of the expected
	values and order.

	Test of p7 compares each created tree to the expected values and positions
	of the proper tree. Currently, the first preorder tree fails this test. The
	traversal strings are compared to the expected traversal of the expected
	tree. As the first preorder constructed tree is not correct, its postorder
	and inorder traversals also fail.

	Test of p8 compares the result of both evalPost and evalPre to the same
	expected value, as both given token lists should describe the same
	expression and should return the same value.

	Test of p9 compares the resultant tree from makeHuff to an expected tree
	structure, and compares the resultant code dictionary from encode to an
	expected dictionary structure.


PROGRAM OUTPUT: 
	None of the class or function Python files (i.e., any Python file
	that is not a test.py), should output anything unless there is an error.

	Test.py for p1 will output the results of all method checks between the
	pointerqueue and the expected. 

	Test.py for p4 will output the test lists it is merging and the result of
	the merge, as well as the expected list. It will then output if the function
	was successful based on comparison of the above two lists.

	Test.py for p5 will output the internal lists of the list to be
	concateneated, then the result list and an expected list. Then the function
	success will be printed based on this list comparison.

	Test.py for p6 will print the result list and the expected list from the
	level-order reading of the tree. The function success will be printed based
	on list comparison.

	Test.py for p7 outputs 3 sections - postorder, preorder, and inorder. The
	postorder and inorder output come from traversing the trees created
	from preorder lists. 
	The preorder output is from traversing the trees created from postorder lists.

	Test.py for p8 outputs the original expressions for both postfix and prefix,
	followed by their evaluations. Also shown below each function is the
	respective function success.

	Test.py for p9 will output the result of both function comparisons, as well
	as a list of every symbol and their respective probability and code. 
	
	The tree and codes created by this program are correct by my own handwritten
	evaluation of the probabilities and symbols given. The resultant tree should
	be similar to the one below:

      / \
		0/   \1
	  /\1 0/\
  0/  \ /  \1
  d   e f 0/\
					/	 \1
				 c  0/\
					  /	 \1
				   a    b

	This is the tree produced for the frequencies given (a:.07, b:.09, c:.12,
	d:.22, e:.23, f:.27). 
	As per the tree, the codes for each symbol are:

	a:1110
	b:1111
	c:110
	d:00
	e:01
	f:10
	
	These are the codes produced by my program when given this list of
	symbols and probabilities.
