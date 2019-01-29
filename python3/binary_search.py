#Function taking left and right as arguments
def binarySearch(arr, l, r, x):
	if r >= l:
		mid = (l + r) // 2

		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binarySearch(arr, l, mid - 1, x)

		else:
			return binarySearch(arr, mid + 1, r, x)

	else:
		return -1

def search(arr, x):
	return binarySearch(arr, 0, len(arr) - 1, x)

def binary_search(arr, num):
	first = 0
	last = len(arr) - 1

	while first <= last and not False:
		mid = (first + last) // 2
		if arr[mid] == num:
			return arr.index(num)
		else:
			if arr[mid] > num:
				last = last - 1
			else:
				first = first + 1
	return -1

#This sort of works, I need to understand why is not properly working
# def binarySearch(arr, num):
# 	if len(arr) == 0:
# 		return 0
# 	else:
# 		mid = len(arr) // 2
# 		if arr[mid] == num:
# 			return arr.index(mid)
# 		else:
# 			if arr[mid] < num:
# 				return binarySearch(arr[:mid], num)
# 			else:
# 				return binarySearch(arr[mid+1:], num)
