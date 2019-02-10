"""Count possible ways to go through n'th staircase with DP."""

def staircase_dp(n):
    """Bottom-up approach."""
    dp = [0 for i in range(n + 1)]

    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        val = dp[i - 1] + dp[i - 2]
        dp.insert(i, val)
    return dp[n]


if __name__ == '__main__':
    steps = 6
    n = 2

    print("Number of ways to use the stairs = {0}".format(staircase_dp(steps)))
