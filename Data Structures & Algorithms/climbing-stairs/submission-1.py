class Solution:
    def climbStairs(self, n: int) -> int:
        # input: int
        # output: int

        # goal: find the number of distinct ways to climb to the top (n)
        # method: break into two subproblems -> dynamic programming
        # 1.) take 1 step
        # 2.) take 2 steps

        # base case: n = 0 -> return 0, n = 1 -> return 0
        # recursively take 1 step
        # recursively take 2 steps
        # return res

        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]