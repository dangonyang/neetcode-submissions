class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        on_edge = set()

        # check all (r, c) connected to edge
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in on_edge or board[r][c] != "O":
                return
            on_edge.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in on_edge:
                    board[r][c] = "X"