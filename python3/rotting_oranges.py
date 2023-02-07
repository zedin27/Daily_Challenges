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

from typing import List
import random


# arr: [0, 1, 1, 1, 2, 1, 0, 1]
# index: 4
# return -> [3, 5]

# arr:  [0, 2, 0]
# index: 1
# return -> []

[1, 2, 3, 4, 5]


def findChildrenArrayTheo(index, array):
	output = []
	if index < len(array) - 1 and array[index + 1] == 1:
		output.append(index + 1)
	if index > 0 and array[index - 1] == 1:
		output.append(index - 1)
	return output

# coor: (x, y)
# grid:
# [[1, 1, 2] (coor would be (0, 2))
#  [1, 0, 1]]
#
# return [(x1, y1), (x2, y2), ...]
# def bounds(i, j):
# 	if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
# 		return True
# 	return False

# first bit of the code: https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
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
	list = []
	nonDup = []
	encountered = {}
	totalRotTime = 0
	row, col = len(grid), len(grid[0])
	isRotten = False
	# directions = [(1, 0),(0, 1),(-1, 0),(0, -1)] # (x, y, -x, -y) are my directions that i want to use somehow
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
	# print(list)
	print(nonDup)
	print(grid)
	
	for i in range(row):
		for j in range(col):
			if grid[i][j] == 1:
				return -1
	return totalRotTime

# def findChildrenArray(index, array):
# 	list = []
# 	size = len(array) - 1
# 	leftFlag = 0
# 	rightFlag = 0
# 	i = index #maybe start at index?

# 	while i < size:
# 		if (arr[index - 1] == 0 or arr[index + 1] == 0) or (arr[index - 1] == 2 or arr[index + 1] == 2):
# 			list.append("")
# 		elif array[index - 1] == 1 and leftFlag == 0:
# 			list.append(index - 1)
# 			leftFlag+= 1
# 		elif array[index + 1] == 1 and rightFlag == 0:
# 			list.append(index + 1)
# 			rightFlag+= 1
# 		# check if the neighbor is 0

# 		i+= 1

# 	return list

grid = [[2,1,1],
		[1,1,0],
		[0,1,1]]
print(findChildrenDoubleArray(grid))

# arr = [0, 1, 1, 1, 2, 1, 0, 1]
# arr1 = [0, 2, 0]
# arr2 = [0, 2, 2]
# index = 4
# index1 = 1
# index2 = 1
# print(findChildrenArray(index, arr))
# print(findChildrenArrayTheo(index, arr))


# Grid:
# 0 1 1 0
# 0 2 1 0
# 1 0 0 0

# coordinate: (1, 1)

# return -> [(1, 0), (2, 1)]

# rottenCoordinate: (x, y)
# def findChildren(rottenCoordinate, grid):
# 	pass

# def findChildrenRottenList(rotten, grid):
# 	for rottenCoordinate in rotten:
# 		findChildren(rottenCoordinate, grid)


# def orangesRottingTheo(grid: List[List[int]]):
# 	rotten = [(0, 0)]
# 	while True:
# 		newRotten = findChildren(rotten, grid)
# 		if not newRotten:
# 			break
# 		rotten = newRotten

# def orangesRotting(grid: List[List[int]]):

# 	grid = [[0 for m in range(col)] for n in range(row)]
# 	print(grid)
# 	if List is None:
# 		return -1
# 	# print("test")

# orangesRotting(None)