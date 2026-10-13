# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # is it possible for n to be 0?: no

        # input: a number (int)
        # output: the number picked (int)
        # goal: return the number that was picked given a range from 1 to n

        # initial approach:
        # iterate from 1 to n
            # if guess(n) is equal to 0, return n

        # optimize approach:
        # binary search from 1 to n
        # n = 1, p = 1: 1 x
        # n = 5, p = 3: 3 x
        l, r = 1, n
        while l <= n:
            m = (l + r) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                r = m - 1
            else:
                l = m + 1