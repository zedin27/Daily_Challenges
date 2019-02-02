"""Given a list of integers and a number K, return which contiguous elements of
the list sum to K.
"""

def sum_list(list, size, sum):
    """O(n^2) worst."""

    for i in range(size):
        current_sum = list[i]
        j = i + 1
        while j <= size:
            if sum is current_sum:
                print("Sum found between indexes %d and %d"%(i, j-1))
                return True
            if sum < current_sum or j == size:
                break
            current_sum = current_sum + list[j]
            j += 1
    print("Not found")
    return False
    # sum = 0
    # tmp = []
    #
    # for i in list:
    #     if sum is list[i] + list[i+1]
    # return sum

num = [1,2,3,4,5]
size =
k = 9
print(sum_list(num, k))
