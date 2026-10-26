class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # move left if not 0
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                while l < r and nums[l] != 0:
                    l += 1

                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1