class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        q = deque([(0, 0, 1)]) # r, c, length
        visit = set([0, 0])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        while q:
            r, c, length = q.popleft()
            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in direction:
                if min(r + dr, c + dc) >= 0 and max(r + dr, c + dc) < N and grid[r + dr][c + dc] == 0 and (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        return -1