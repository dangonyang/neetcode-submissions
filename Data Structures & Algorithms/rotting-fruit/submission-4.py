class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # is it possible to have more than one way? prob not?
        # will there always be one rotten fruit? no
        # is the number of rows == to cols? no 

        # input: 2d matrix of int (0, 1, 2)
        # output: int representing min minutes
        # goal: find the minimum number of minutes it takes to turn all fresh fruits (1) into rotten fruits (2)

        # initial approach:
        # run bfs on grid
        # count the number of fresh fruits
        # append all rotten fruits to queue
        q = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # set directions
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        # iterate through queue
        while fresh > 0 and q:
            # ensure we process all rotten fruits before proceeding
            for _ in range(len(q)):
                # check if fresh fruit is 0, then return minutes
                # pop queue 
                r, c = q.popleft()
                # iterate through all directions on popped node
                for dr, dc in directions:
                    # check bounds
                    # if cell is a fresh fruit, set to 2 then add to queue
                    # subtract number of fresh fruit
                    if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        q.append((r + dr, c + dc))
                        fresh -= 1
            # add 1 to time
            time += 1
        # return time if fresh is 0, otherwise -1
        return time if fresh == 0 else -1
