"""
31. Next Permutation

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

def swap(arr, pos1, pos2):
	arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
	return list

def nextPermutation(nums):
	size = len(nums)
	i, j = 0, 0
	for i in range(size - 2, -1, -1):
		if (nums[i] < arr[i + 1]):
			break
	
	if (i < 0):
		nums.reverse()
	else:
		for j in range(size - 1, i, -1):
			if (nums[j] > nums[i]):
				break
		
		swap(nums, i, j)
		start, end = i + 1, len(nums)
		nums[start:end] = arr[start:end][::-1]
	# print(len(nums))

arr = [1, 2, 3, 6, 5, 4]
nextPermutation(arr)
for i in arr:
	print(i, end=" ")