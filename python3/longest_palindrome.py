"""Longest Pallindrome with naive solution.

and Dynamic Programming ( DP )
"""

def lps(str, i ,j):
	"""Recursive solution."""
	if i is j:
		return 1
	if str[i] is str[j] and i + 1 is j:
		return 2
	if str[i] is str[j]:
		return lps(str, i + 1, j - 1) + 2
	return max(lps(str, i + 1, j),
				lps(str, i, j-1))

def lps_dp(str):
	"""DP solution."""
	strlen = len(str)
	table = [[0 for x in range(strlen)] for x in range(strlen)] #Initializing a table

	for i in range(strlen):
		table[i][i] = 1

	for substr_len in range(2, strlen + 1):
		for i in range(strlen - substr_len + 1):
			j = i + substr_len - 1

			if str[i] is str[j] and substr_len is 2:
				table[i][j] = 2
			elif str[i] is str[j]:
				table[i][j] = table[i + 1][j - 1] + 2
			else:
				table[i][j] = max(table[i][j - 1], table[i + 1][j])
	return table[0][n - 1]
