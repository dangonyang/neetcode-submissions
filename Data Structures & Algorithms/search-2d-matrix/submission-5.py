class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # by non-decreasing, do you mean that one number in the same row can equal another? -> yes
        # can the input be empty? -> yes
        # are all inputs valid? -> yes

        # input: 2D array (list of int list), int target
        # output: boolean
        # goal: see if target exists in 2D array
        # constraints: each row in 2D array is sorted in non-decreasing order, first integer of every row is greater than the last integer of the previous row

        # initial approach:
        # iterate through all of the last values in each row, ascending
            # if not, we iterate through the length of the previously saved row
        # return false

        # [[0], [1]], target = 1: return True x
        # [[0, 1], [2, 3]] target = 4: return False
        # optimize approach:
        # binary search through first and last columns to find row
        l, r = 0, len(matrix) - 1
        row = 0
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                row = m
                break
            elif matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        # binary search through row
        l2, r2 = 0, len(matrix[0]) - 1
        while l2 <= r2:
            m2 = (l2 + r2) // 2
            if matrix[row][m2] == target:
                return True
            elif matrix[row][m2] < target:
                l2 = m2 + 1
            else:
                r2 = m2 - 1
        # return false if not found
        return False