# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # can targetSum be negative? yes
        
        # [1,2,3], targetSum = 3: True
        # [1,1,0,1], targetSum = 2: False

        # input: root (list of nodes), targetSum (int)
        # output: boolean
        # goal: true if exists a path that sums to targetSum, false otherwise

        # initial approach:
        # go through each path
        # backtrack from leaf node when != to target sum

        curr_sum = 0

        def backtrack(root: Optional[TreeNode], path_sum: int) -> bool:
            if not root:
                return False

            path_sum += root.val
            if not root.left and not root.right:
                return path_sum == targetSum
            return backtrack(root.left, path_sum) or backtrack(root.right, path_sum)

        return backtrack(root, 0)