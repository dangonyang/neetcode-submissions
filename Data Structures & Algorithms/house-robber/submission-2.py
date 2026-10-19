class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            tmp = max(dp[0] + nums[i], dp[1])
            dp[0] = dp[1]
            dp[1] = tmp
            i += 1
        return dp[1]