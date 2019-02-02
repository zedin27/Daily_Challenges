def mergeArrays(nums1, m, nums2, n):
    nums1[0: m + n] = [x for x in sorted(nums1[:m] + nums2[:n])]
