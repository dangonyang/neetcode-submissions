class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            count = 1
            # move right pointer to last value of streak
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            # append streak
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            # move right pointer to start of new streak
            r += 1
        return l