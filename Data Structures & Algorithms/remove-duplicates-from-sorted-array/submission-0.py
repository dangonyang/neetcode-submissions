class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left pointer at start
        l = 1
        # have right pointer compare
        for r in range(1, len(nums)):
            # left indicates value to be swapped
            # so if right sees seen value, l = r
            # if right sees new value, swap
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
        
