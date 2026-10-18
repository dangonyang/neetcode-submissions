class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # is the grid always going to be valid? yes
        
        # input: 2d matrix of integers (0, 1, 2)
        # output: integer representing the minimum minutes to no fresh fruits or -1 if impossible
        # goal: find the min minutes it takes for there to no longer be fresh fruit

        # initial approach:
        q = deque() # r, c, minutes
        fresh = 0
        time = 0

        # check for 1s and 2s
        # run bfs on 2s
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    if r + dr < 0 or r + dr >= len(grid) or c + dc < 0 or c + dc >= len(grid[0]) or grid[r + dr][c + dc] != 1:
                        continue
                    grid[r + dr][c + dc] = 2
                    q.append((r + dr, c + dc))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
                
        # return -1 if impossible