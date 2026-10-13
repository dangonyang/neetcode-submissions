class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # can nums be empty: no
        # can we assume all inputs are valid: yes
        # can there be more than one target in nums: no

        # input: array of int, sorted in ascending order
        # output: int
        # goal: return index of target in nums, otherwise -1

        # initial approach:
        # iterate through each number in the array
            # if current number is equal to target
                # return index
        # return -1

        # optimize approach:
        # run binary search on input
        # [-1, 2], target = 3: -1 x
        # [-1, 0, 2], target = 2: 2 x
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        # return -1 
        return -1