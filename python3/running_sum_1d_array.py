"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

def runningSum(nums):
	summs_arr = []
	size = len(nums) - 1
	res = 0

	for x in range(size):
		if x == 0:
			summs_arr.append(nums[x])
			print(summs_arr)
		summs_arr.append(nums[x] + nums[x + 1])
		print(summs_arr)
		# print(nums[x] + nums[x + 1])
	# return sums_arr


arr = [1, 2, 3, 4, 5]
runningSum(arr)