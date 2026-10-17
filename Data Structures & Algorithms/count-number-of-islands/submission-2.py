class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1s on diagonals are their own island? yes
        # can we assume that there is at least one valid input? no

        # input: matrix with 1s and 0s (2d array)
        # output: int
        # goal: find the number of islands in grid (island is 1s connected vertically and horizonally)

        # initial approach:
        # use dfs on matrix (up, down, right, left) -> helper function
        # mark 0 when visited
        # iterate through all rows and columns
            # if grid[r][c] == 1, then add 1 to islands and we use dfs
        # return islands

        if not grid:
            return 0

        def dfs(r, c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            
            # up
            dfs(r + 1, c)
            # down
            dfs(r - 1, c)
            # right
            dfs(r, c + 1)
            # left
            dfs(r, c - 1)
        
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        return islands