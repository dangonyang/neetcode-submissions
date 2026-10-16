class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]

        def dfs(grid, r, c, visit):
            if (min(r, c) < 0 or r == len(grid) or c == len(grid[0]) or (r, c) in visit or grid[r][c] != start_color):
                return
            if grid[r][c] == start_color:
                grid[r][c] = color
            
            visit.add((r, c))
            dfs(grid, r + 1, c, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r, c - 1, visit)
        dfs(image, sr, sc, set())
        return image