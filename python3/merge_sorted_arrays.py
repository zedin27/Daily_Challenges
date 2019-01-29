def mergeArrays(nums1, m, nums2, n):
	# arr3 = [None] * (m + n)
	# i = 0
	# j = 0
	# k = 0

	nums1[:] = sorted(nums1 + nums2)
	# nums1 = [x for x in nums1 if x != 0]
	# if nums1[:] is 0:
	# 	del nums1[:]

	# for i in range(len(nums1[:-1]) + 1):
	i = 0
	while (i < len(nums1[:-1])):
		if nums1[i] is 0:
			nums1.pop(i)
		if i > len(nums1):
			break
		i += 1
	print(nums1)
	# while i < m and j < n:
	# 	if nums1[j] < nums2[j]:
	# 		arr3[k] = nums1[i]
	# 		k += 1
	# 		i += 1
	# 	else:
	# 		arr3[k] = arr2[j]
	# 		k += 1
	# 		j += 1
    #
	# while i < m:
	# 	arr3[k] = nums1[i]
	# 	k += 1
	# 	j += 1
    #
	# while j < n:
	# 	arr3[k] = nums2[j]
	# 	k += 1
	# 	j += 1
	# nums1[:] = arr3
	# print("Array after merging")
	# for i in range(m + n):
	# print(str(nums1[), end = " ")

nums1 = [-49,-48,-48,-47,-45,-42,-39,-36,-33,-33,-28,-28,-23,-23,-7,-4,-3,0,0,4,6,21,29,29,31,34,36,38,40,43,45,46,47,0,0,0,0,0,0,0,0]
m = len(nums1)

nums2 = [-16,-5,-3,26,33,35,38,41]
n = len(nums2)
mergeArrays(nums1, m, nums2, n);
