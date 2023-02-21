"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""
def twoSum(nums, target):
	# have two pointers that goes through the array of numbers
	# have pointer A and pointer B to add up
	# if both pointers are equal to the target, then return their indices
	# otherwise, continue searching
	# if the search is not found, then return 0
	# NO SAME ELEMENT TWICE
	res = []
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			if (nums[i] + nums[j] == target):
				res.append([i, j])
				return res
	return []

arr = [2,7,11,15]
arr1 = [7,7,11,15]
arr2 = [3,3]
print(twoSum(arr, 9))
print(twoSum(arr1, 26))
print(twoSum(arr2, 6))