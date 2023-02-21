"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
def dfs(grid, i, j):
	#checking boundaries of my grid, and edge-case
	#make sure it has a check if is visited
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
		return
	grid[i][j] = "#"
	dfs(grid, i + 1, j)
	dfs(grid, i - 1, j)
	dfs(grid, i, j + 1)
	dfs(grid, i, j - 1)

def numIslands(grid):
	if not grid: 
		return grid
	R, C = len(grid), len(grid[0])
	count = 0
	for row in range(R):
		for col in range(C):
			if grid[row][col] == "1":
				dfs(grid, row, col)
				count += 1
	return count
	# traverse the grid and check for the 4-directions
	# if there is a '1' and the direction of it is also '1', then it is considered an island
	# continue to look for '1's until there isn't any
	# if there are nowhere to go through DFS with '1's in the 4-directions, then return counter
	# however, if it is done, but it finds another one, repeat the whole process and increase the counter by one
	# once it finishes to check the potential islands, keep it as a counter to track the total islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))