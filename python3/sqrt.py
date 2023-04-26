"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
"""

def mySqrt(num):
	if num == 0:
		return 0
	if num == 1:
		return 1
	
	res = 0