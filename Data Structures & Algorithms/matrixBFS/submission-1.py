class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
            return -1
        # set up a hash set for visited cells
        visit = set()
        # set up a queue to visit children one by one (start at root)
        queue = deque([(0, 0)])
        # visited root
        visit.add((0, 0))

        length = 0
        # while queue
        while queue:
            # traverse through all children
            for i in range(len(queue)):
                # pop from queue
                r, c = queue.popleft()
                # if we're at the bottom right, return
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length
                # for each direction (neighbors)
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direction:
                    # if not out of bounds
                    if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] == 0 and (r + dr, c+ dc) not in visit:
                        # append to queue 
                        queue.append((r + dr, c + dc))
                        # add to visit
                        visit.add((r + dr, c + dc))
            length += 1
        return -1