class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # base case
        dp[1][1] = 1
        # ways: down or right (rely on top and left to give data)
        ways = [(1, 0), (0, 1)]

        # start at 1 because r and c = 0 are extra row/col
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                # skip (our base case)
                if r == 1 and c == 1:
                    continue
                for dr, dc in ways:
                    if 0 <= r - dr < m + 1 and 0 <= c - dc < n + 1:
                        dp[r][c] = dp[r - dr][c] + dp[r][c - dc]
        return dp[m][n]
