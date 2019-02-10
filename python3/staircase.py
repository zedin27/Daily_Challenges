"""Count possible ways to go through n'th staircase with DP."""

def staircase(n):
    """Bottom-up approach."""
    dp = [0 for i in range(n + 1)]

    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        val = dp[i - 1] + dp[i - 2]
        dp.insert(i, val)
    return dp[n]


def staircase_set(n, steps):
    """Sum of all possible steps."""
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in steps if i - x > 0)
        cache[i] += 1 if i in steps else 0
    return cache[-1]

if __name__ == '__main__':
    n = 5
    steps = [1, 2]

    print("Number of ways to use the stairs = {0}".format(staircase_set(n, steps)))
    print("Number of ways to use the stairs = {0}".format(staircase(n)))
