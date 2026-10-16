# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # saves inorder index
        indices = {val: idx for idx, val in enumerate(inorder)}
        # preorder index
        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            # work on one parent at a time
            root_val = preorder[self.pre_idx]
            # work on child (next parent)
            self.pre_idx += 1
            # create node with parent
            root = TreeNode(root_val)
            # find index for parent in inorder
            mid = indices[root_val]
            # left child
            root.left = dfs(l, mid - 1)
            # right child
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)