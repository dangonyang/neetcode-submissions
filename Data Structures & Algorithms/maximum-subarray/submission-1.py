class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for val in nums:
            if curSum < 0:
                curSum = 0
            curSum += val
            maxSum = max(maxSum, curSum)
        return maxSum
