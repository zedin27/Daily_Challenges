"""Search element in a sorted matrix"""
import random
import itertools

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
    x = 7
    multi_array = [[random.randint(0, 200) for x in range(n)] for y in range(m)]
    # one_array = sorted(list(itertools.chain.from_iterable(multi_array))) Another way
    one_array = sorted([x for row in multi_array for x in row])
    sorted_2d = [one_array[i:i+m] for i in range(0, len(one_array), n)]
    
    print("multi_array list is: \n{0}\n".format(multi_array))
    print("sorted 2D array: \n{0}\n".format(sorted_2d))
    if not findnum_arr(sorted_2d, x):
        print("Not Found")
    else:
        print("Found")
