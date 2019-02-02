"""Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. X is the summation of values on each face when all the dice are thrown."""

def findWays_r(m, n, x):
    """Recursive simple solution (non DP and expensive)."""
    if x is 0 and n is 0:
        return 1
    if x is 0 and n is not 0:
        return 0
    if x is not 0 and n is 0:
        return 0

    result = 0

    for i in range(1, m):
        result += findWays_r(m, n-1, x-i) # Recursion, find a way to memoize or tab this
    return result


def findWays(n, m, x):
    """Dynamic Programming solution (Top-down)."""
    '''
    n = # of dice
    m = # of faces
    x = # of ways to sum the result.

    Base cases:
    Return 1: if there no dice and sum is 0, then that is one possible outcome.
    Return 0: n is negative, m is negative, or summation is negative.
    Return table[(m, n, x)]: Table with all the results given after calculatiing for each dice, side, and sum
    '''
    table = {}
    if n is 0 and x is 0:
        return 1
    if n < 0 or x < 0 or m is 0:
        return 0
    if table.get((m, n, x)) is not None:
        return table[(m, n, x)]
    res = findWays(n-1, m, x-m) + findWays(n, m-1, x)
    table[(m, n, x)] = res
    return res

print(findWays(3, 6, 7)) # Output is 4 because it ignores repeated combinations
