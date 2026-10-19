class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # initial approach:
        # start from bottom right to top left
        # dynamic programming
        # use dfs to backtrack

        # initialize a previous row
        rowLen = len(obstacleGrid)
        colLen = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rowLen - 1][colLen - 1] == 1:
            return 0

        prevRow = [0] * (colLen + 1)
        # for each row starting from bottom
        for r in range(rowLen - 1, -1, -1):
            # initialize a curr Row
            curRow = [0] * (colLen + 1)
            curRow[colLen] = 0
            # for each col starting from right
            for c in range(colLen - 1, -1, -1):
                # if current cell is 0, look at prev row or the rightmost row and add them
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                elif r == rowLen - 1 and c == colLen - 1:
                    curRow[c] = 1
                else:
                    curRow[c] = prevRow[c] + curRow[c + 1]
            # set prevRow to currRow
            prevRow = curRow
        # return first element of prevRow
        return prevRow[0]