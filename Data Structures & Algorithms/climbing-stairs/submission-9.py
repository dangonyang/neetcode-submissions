class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        ways = [1, 2]
        # base cases
        dp[0] = 1

        for i in range(1, n + 1):
            for w in ways:
                if w <= i:
                    # add previous number of ways
                    dp[i] += dp[i - w]
        return dp[n]