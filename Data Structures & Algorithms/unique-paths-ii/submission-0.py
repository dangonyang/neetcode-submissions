class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rowLen = len(obstacleGrid)
        colLen = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rowLen - 1][colLen - 1] == 1:
            return 0
        prevRow = [0] * colLen

        for r in range(rowLen - 1, -1, -1):
            curRow = [0] * colLen
            for c in range(colLen - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                elif r == rowLen - 1 and c == colLen - 1:
                    curRow[c] = 1
                else:
                    down = prevRow[c]
                    right = curRow[c + 1] if c + 1 < colLen else 0
                    curRow[c] = right + down
            prevRow = curRow
        return prevRow[0]
