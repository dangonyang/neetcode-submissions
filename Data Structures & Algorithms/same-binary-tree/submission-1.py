# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # input: two tree
        # output: bool

        # base case(s): if tree size is not equal -> false, if node has no children and is equal in both trees
        # goal: compare nodes in trees to see if trees are the same
        # method: check children (recursively)
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        if not p.left and not p.right and not q.left and not q.right:
            return True

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
