class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Cannot have an empty input, must be at least of length 1
        # Only 1s and 0s

        # [0, 0, 0] -> 0 x
        # [0, 1, 0] -> 1 x
        # [1, 1, 0, 1, 1, 1] -> 3 x
        # [1, 0, 1, 1, 0, 1] -> 2 x

        # goal: find the maximum number of consecutive 1s
        # input: array of binary integers
        # output: integer

        # initial: check how many 1s follow if the current index is 1
        # nested for loop checking per index
        # compare the length for each nested loop
        # O(n^2) ^^
        # optimize: two pointer approach O(n)
        # start at left, right is end of 1s substring, check length and compare

        # left at beginning of the array
        left = 0
        length = 0
        # iterate through array with a for loop, with right as the tracking variable
        for right in range(len(nums)):
            # check if current length of substring is greater than max, if yes then current is new max
            if nums[right] == 1:
                length = max(length, right - left + 1)
            else:
                # left isn't start of substring
                if nums[left] == 0:
                    left += 1
                # left is start of substring
                else:
                    left = right + 1
        # return max
        return length