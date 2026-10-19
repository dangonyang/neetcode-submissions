class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # is grid always going to be valid? yes
        # can grid have 1s on either the start and end? yes

        # input: 2d matrix of int (0 or 1)
        # output: length of shortest path (-1 if doesn't exist)
        # goal: return the length of the shortest path
        
        # initial approach:
        # check if the starting or ending cell is blocked
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        # run bfs on grid
        # set up visit (set) and queue (to check parents one by one) -> add first cell to queue
        q = deque([(0, 0, 1)]) # r, c, length
        visit = set([0, 0])
        # add directions where we can traverse to
        directions = ([1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1])
        # iterate through each member in queue
        while q:
            # pop from queue
            r, c, length = q.popleft() # r, c length
            if r == n - 1 and c == n - 1:
                return length
            # iterate through each direction
            for dr, dc in directions:
                # check if out of bounds
                if min(r + dr, c + dc) >= 0 and max(r + dr, c + dc) < n and grid[r + dr][c + dc] == 0 and (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
                # if cell is equal to zero:
                    # add to queue
                    # add to length
        return -1
