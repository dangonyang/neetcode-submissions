# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # [5,3,9,1,4], key = 3: [5,4,9,1]
        # [], key = 3: return []
        # is the key always in the tree?: no
        # is root always going to have at least one node?: no

        # input: root (list of tree nodes), node to remove (int)
        # output: list of tree nodes without key
        # goal: remove key node in root, return new root

        # initial approach:
        # reconstruct the entire tree without key

        # optimize approach:
        if not root:
            return None
        
        # helper function to find min val of a subtree
        # keep iterating left until we find it
        def minRightNode(root: Optional[TreeNode]) -> Optional[TreeNode]:
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        # start from root and search for node to remove
        # if key < val, traverse left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # if key > val, traverse right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # if key == val, go two cases
        else:
            # if there is 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # if there are two children
            else:
                # take the minimum value of right tree and move it up (easier because its a leaf node)
                minRightNode = minRightNode(root.right)
                root.val = minRightNode.val
                root.right = self.deleteNode(root.right, minRightNode.val)
        return root