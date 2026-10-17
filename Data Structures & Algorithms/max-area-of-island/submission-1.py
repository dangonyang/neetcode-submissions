class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # are we guaranteed grid exists? -> yes

        # input: 2D matrix with 1 and 0
        # output: max area (int)
        # goal: find the max area of all islands
        max_area = 0
        # inital approach:
        # run dfs on the matrix (helper function)
        def dfs(r, c):
            nonlocal max_area
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            # every time you find 1, remark to 0 and add 1 to island area
            grid[r][c] = 0
            # traverse all directions
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        # for each row and col:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
            # check if cell is an island
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
                # make area = 0
                # run dfs
        # return max area
        return max_area
