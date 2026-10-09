class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # input: 2d array of 1s and 0s
        # output: int

        # goal: find the number of islands
        # method: dfs on land
        
        def dfs(r, c):
            # check if in 0
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return
            # update cell
            grid[r][c] = "0"
            # check up
            dfs(r + 1, c)
            # check left
            dfs(r, c - 1)
            # check right
            dfs(r, c + 1)
            # check down
            dfs(r - 1, c)
        
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands