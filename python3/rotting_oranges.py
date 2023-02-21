"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Constraints:
	m == grid.length
	n == grid[i].length
	1 <= m, n <= 10
	grid[i][j] is 0, 1, or 2.

"""

# Solution for a 1D array
def findChildrenArrayTheo(index, array):
	output = []
	if index < len(array) - 1 and array[index + 1] == 1:
		output.append(index + 1)
	if index > 0 and array[index - 1] == 1:
		output.append(index - 1)
	return output

# first bit of the code: https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
# Goals: doing it as a BFS, adding directions values
def isSafe(i, j, grid):
	if (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])):
		return True
	return False
def findChildrenDoubleArray(grid):
	# find all possible directions
	# size of my grid and check bounds
	# traverse my grid
	# check its neigbors
	# if neighbor is reachable and fresh orange, then add it to the list
	# return list of tuples ([(x1, y1), (x2, y2), ...])
	# directions = [(1, 0),(0, 1),(-1, 0),(0, -1)] # (x, y, -x, -y) are my directions that i want to use somehow
	list = []
	nonDup = []
	encountered = {}
	totalRotTime = 0
	row, col = len(grid), len(grid[0])
	isRotten = False
	while True:
		for i in range(row):
			for j in range(col):
				if grid[i][j] == 2 + totalRotTime:
					# check the 4-directions and bounds
					if (isSafe(i + 1, j, grid)) and grid[i + 1][j] == 1:
						list.append((i, j))
						grid[i + 1][j] = 2 + totalRotTime + 1
						isRotten = True
					if (isSafe(i, j + 1, grid)) and grid[i][j + 1] == 1:
						list.append((i, j))
						grid[i][j + 1] = 2 + totalRotTime + 1
						isRotten = True
					if (isSafe(i - 1, j, grid)) and grid[i - 1][j] == 1:
						list.append((i, j))
						grid[i - 1][j] = 2 + totalRotTime + 1
						isRotten = True
					if (isSafe(i, j - 1, grid)) and grid[i][j - 1] == 1:
						list.append((i, j))
						grid[i][j - 1] = 2 + totalRotTime + 1
						isRotten = True
		if not isRotten:
			break
		isRotten = False
		totalRotTime += 1

	# If I want the coordinates of the oranges that are rot only
	for coords in list:
		if coords not in encountered:
			encountered[coords] = True
			nonDup.append(coords)
	print("Rotten oranges grid spread: {}".format(list))
	print("Non duplicated coordinates rotten oranges: {}".format(nonDup))
	print("Grid after spread: {}".format(grid))
	
	for i in range(row):
		for j in range(col):
			if grid[i][j] == 1:
				return -1
	return totalRotTime

grid = [[2,1,1],
		[1,1,0],
		[0,1,1]]
print(findChildrenDoubleArray(grid))