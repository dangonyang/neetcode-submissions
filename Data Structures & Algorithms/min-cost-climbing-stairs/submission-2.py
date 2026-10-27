class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        # base cases
        dp[0] = 0
        dp[1] = 0
        ways = [1, 2]

        for i in range(2, n + 1):
            # find min for each index by checking each way
            for w in ways:
                # makes sure no out of bounds in index
                if w <= i:
                    dp[i] = min(dp[i - w] + cost[i - w], dp[i])
        # return last index (top of stair)
        return dp[n]