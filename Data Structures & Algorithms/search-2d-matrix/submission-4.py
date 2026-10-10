class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check if target is lesser or greater than last element of previous row
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1
        while l <= r:
            mid = (r + l) // 2
            # integer division tells which row, get remainder for cols
            val = matrix[mid // cols][mid % cols]
            if target > val:
                l = mid + 1
            elif target < val:
                r = mid - 1
            else:
                return True
        return False