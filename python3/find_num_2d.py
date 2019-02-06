"""Search element in a sorted matrix"""
import random

n = 5
m = 5

def findnum_arr(array, num):
    low = 0
    high = n * m - 1
    while (high >= low):
        mid = (low + high) // 2
        i = mid // m
        j = mid % m

        if (num == array[i][j]):
            return True
        if (num < array[i][j]):
            high = mid - 1
        else:
            low = mid + 1
    return False

if __name__ == '__main__':
    multi_array = [[random.randint(0, 20) for x in range(n)] for y in range(m)]
    x = 7

    print(multi_array)
    print (" ")
    if not findnum_arr(multi_array, x):
        print("Not Found")
    else:
        print("Found")
