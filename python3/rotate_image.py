import random
def rotate(matrix):
	# Get matrix
	# Go through the 2D array one by one ([x][y])
	# Swap each value of the 2D array [y][x]
	# NOTE: values has to be in-place swap
	
	M = len(matrix)
	for row in range(M):
		for col in range(row):
			matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col] #Tuple packing
			# temp = matrix[row][col]
			# matrix[row][col] = matrix[col][row]
			# matrix[col][row] = temp
	
	for row in matrix:
		row.reverse()

def rotate_tuple(matrix):
	M = len(matrix)
	for row in range(M):
		for col in range(row):
			temp = matrix[row][col]
			matrix[row][col] = matrix[col][row]
			matrix[col][row] = temp
	
	for row in matrix:
		row.reverse()
# start = 1
# cols = 5
# rows = 5
# matrix = [[start + col + cols * row for col in range(cols)] for row in range(rows)] # Generate some values (try to randomize it)
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Original Image values: {0}\n".format(matrix))
rotate(matrix)
print("Rotation Image values: {0}\n".format(matrix))