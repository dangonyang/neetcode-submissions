class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # if infinity = land, find shortest path (BFS) to treasure
        # if -1 = water, so leave it be
        # if 0 treasure, so leave it be
        INF = 2147483647
        if not grid:
            return [[]]

        q = deque()
        visit = set()

        # append all treasure locations
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        path = 0
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = path
                for dr, dc in directions:
                    if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) and (row + dr, col + dc) not in visit and grid[row + dr][col + dc] != -1:
                        # append to queue (need to check)
                        visit.add((row + dr, col + dc))
                        q.append((row + dr, col + dc))
            # visited all children
            path += 1