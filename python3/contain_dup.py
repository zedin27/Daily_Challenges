# Resources:
# 			https://stackoverflow.com/a/1920179/6017248
# 			https://www.tutorialstonight.com/python-compare-two-lists
'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
def containsDuplicate(nums):
	# if appearing twice, then true : otherwise, false
	dict = {}
	for x in nums:
		if x in dict:
			return True
		else:
			dict[x] = 1
	return False

test = [1,2,3,1]
test1 = [1, 2, 3, 4]
test2 = [1,1,1,3,3,4,3,2,4,2]
test4 = [0]
containsDuplicate(test)
containsDuplicate(test1)
containsDuplicate(test2)
containsDuplicate(test4)