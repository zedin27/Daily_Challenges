"""
Given an string in roman no format (s) your task is to convert it to.
integer.

Input:
The first line of each test case contains the no of test cases T.
Then T test cases follow. Each test case contains a string s denoting the
Roman no.

Output:
For each test case in a new line print the integer representation of Roman
number s.

Constraints:
1<=T<=100
1<=roman no range<4000

Example:
Input
2
V
III

Output
5
3
"""

ROMAN = {"I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900}


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    res = 0

    """Original solution approach"""
    # while (s):
    #     if s[:2] in ROMAN:
    #         res += ROMAN[s[:2]]
    #         s = s[2:]
    #     elif s[:1] in ROMAN:
    #         res += ROMAN[s[:1]]
    #         s = s[1:]
    #     else:
    #         return -1
    # return res

    """First solution"""
    # while (i < len(s)):
    #     s1 = ROMAN[s[i]]
    #
    #     if (i + 1 < len(s)):
    #         s2 = ROMAN[s[i + 1]]
    #
    #         if (s1 >= s2):
    #             res += s1
    #             i += 1
    #         else:
    #             res += s2 - s1
    #             i += 2
    #     else:
    #         res += ROMAN[s[i]]
    #         i += 1
    # return res

print(romanToInt("IV")) #4
print(romanToInt("XXXIV")) #34
print(romanToInt("V")) #5
print(romanToInt("MMD")) #2500
print(romanToInt("MDCLXI")) #1761
print(romanToInt("")) #0
print(romanToInt("-I")) #-1
