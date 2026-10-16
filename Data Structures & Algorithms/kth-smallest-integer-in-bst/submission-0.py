# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # [2,1,3], k = 1: 1
        # [1], k = 1: 1
        # can tree ever be empty? -> no
        # are all values unique in the tree? -> yes

        # input: list of tree nodes, k representing smallest val
        # output: the kth smallest value (int)
        # goal: find the kth smallest value in the tree

        # initial approach:
        # start at root, traverse through every node in the tree
        # use min heap to append all nodes
        # pop k times to get val

        # optimize approach:
        # use in order dfs (adds left first)

        arr = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return arr[k - 1]

        