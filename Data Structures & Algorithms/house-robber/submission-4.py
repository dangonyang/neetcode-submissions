class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(nums))]
        # base case
        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            # choice: ignore + curr or took last house
            dp[i][1] = max(dp[i - 1][0] + nums[i], dp[i - 1][1])
            # have to ignore this house
            dp[i][0] = dp[i - 1][1]
        return dp[len(nums) - 1][1]
        