class Solution:
    def numTrees(self, n: int) -> int:
        # number of bsts from i to j
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # cases where start is past end (j < i)
        # default tree is empty tree (so = 1)
        # n + 2 range includes n + 1, which can happen at [k + 1][j]
        for i in range(1, n + 2):
            for j in range(0, i):
                dp[i][j] = 1

        # range size
        for length in range(0, n):
            # where range starts
            for i in range(1, n - length + 1):
                # where range ends
                j = i + length
                # k is the root
                for k in range(i, j + 1):
                    dp[i][j] += dp[i][k - 1] * dp[k + 1][j]
        
        return dp[1][n]