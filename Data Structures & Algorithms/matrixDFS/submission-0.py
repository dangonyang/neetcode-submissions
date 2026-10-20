class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 1:
                return 0
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return 1
            grid[r][c] = 1
            total = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            grid[r][c] = 0
            return total
        return dfs(0, 0)