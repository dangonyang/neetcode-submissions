class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for num in nums:
            counts[num] += 1
        
        j = 0
        for i in range(len(counts)):
            while counts[i] != 0:
                nums[j] = i
                counts[i] -= 1
                j += 1
        return nums
            