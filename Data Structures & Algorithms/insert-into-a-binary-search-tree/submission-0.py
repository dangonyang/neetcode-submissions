# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # [5,3,9], val = 6 -> [5,3,9,6] x
        # [], val = 6 -> [6] x
        # guaranteed to have a root node? -> no
        # guarenteed that new value doesn't exist
            # every node is unique
        
        # goal: insert new node and return new list
        # input: list of nodes, val (int) to insert
        # output: new list of nodes w/ val

        # initial approach: 
        if not root:
            return TreeNode(val)
        # start from root
        # traverse left if val is < root
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # traverse right if val is > root
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        # find null to insert at
        return root
        # time: O(logn) because we're iterating through half the tree
        # space: O(1)

        