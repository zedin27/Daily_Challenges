"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(str):
	#How would I track which bracket I'm using and the order too?
	#If there are 2 '(' and one ')', then it should be invalid because there are still left in my stack
	#Brackets must match with their mirrored version
	stack = []
	dict = {}
	size = len(str)

	for bracket in range(size):
		if bracket in ['(', '[', '{']:
			stack.append(bracket)
		elif bracket in [')', ']', '}']:
			if not stack:
				return False
			if bracket == ')' and stack[-1] != '(':
				return False
			if bracket == ']' and stack[-1] != '[':
				return False
			if bracket == '}' and stack[-1] != '{':
				return False
			stack.pop()
	return not stack