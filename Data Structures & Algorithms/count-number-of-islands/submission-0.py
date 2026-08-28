class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if not grid:
            return islands

        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    if (row + dr) in range(rows) and (col + dc) in range(cols) and grid[row + dr][col + dc] == "1" and (row + dr, col + dc) not in visit:
                        q.append((row + dr, col + dc))
                        visit.add((row + dr, col + dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands