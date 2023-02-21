"""
733. Flood Fill

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""
#Original approach
def isSafe(i, j, image):
	if (i >= 0 and i < len(image) and j >= 0 and j < len(image[0])):
		return True
	return False

def floodFillHelper(image, sr, sc, startColor, endColor):
	# Traverse the grid in a given sr and sc
	# when starting in [sr][sc] with the given color, all of the directions becomes the value of color
	# e.g. (1, 2) is my initial position and i want to add color '5', then all of the possible directions becomes 5
	# check my directions
	# return final list after everything is filled
	image[sr][sc] = endColor
	if isSafe(sr + 1, sc, image) and image[sr + 1][sc] == startColor:
		floodFillHelper(image, sr + 1, sc, startColor, endColor)
	if isSafe(sr - 1, sc, image) and image[sr - 1][sc] == startColor:
		floodFillHelper(image, sr - 1, sc, startColor, endColor)
	if isSafe(sr, sc + 1, image) and image[sr][sc + 1] == startColor:
		floodFillHelper(image, sr, sc + 1, startColor, endColor)
	if isSafe(sr, sc - 1, image) and image[sr][sc - 1] == startColor:
		floodFillHelper(image, sr, sc - 1, startColor, endColor)


def floodFill(image, sr, sc, color):
	floodFillHelper(image, sr, sc, image[sr][sc], color)


# Leetcode solution/approach
# def floodFill(image, sr, sc, newColor):
# 	R, C = len(image), len(image[0])
# 	color = image[sr][sc]
# 	if color == newColor:
# 		return image
# 	def dfs(row, col):
# 		if image[row][col] == color:
# 			image[row][col] = newColor
# 			if row >= 1:
# 				dfs(row - 1, col)
# 			if row + 1 < R:
# 				dfs(row + 1, col)
# 			if col >= 1:
# 				dfs(row, col - 1)
# 			if col + 1 < C:
# 				dfs(row, col + 1)
# 	dfs(sr, sc)
# 	return image


image = [[1, 2, 3, 5],
		[ 1, 1, 2, 1],
		[ 1, 3, 4, 2],
		[ 1, 3, 4, 2],
		[ 1, 3, 4, 2],
		[ 1, 3, 4, 2],
		[ 1, 3, 4, 2]]

floodFill(image, 1, 1, 3)
for x in image:
	print(x)

