class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # bottom up approach
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf')] * m for _ in range(n)]
        # can move down or right
        ways = [(0, 1), (1, 0)]
        # base case:
        # ending state is cost
        dp[n - 1][m - 1] = grid[n - 1][m - 1]

        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                # already set, so skip
                if r == n - 1 and c == m - 1:
                    continue
                for dr, dc in ways:
                    if 0 <= r + dr < n and 0 <= c + dc < m:
                        # choose between current cost (default inf) or new
                        dp[r][c] = min(dp[r][c], dp[r + dr][c + dc] + grid[r][c])
        return dp[0][0]

