# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None

            # iterate through each level
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    rightSide = curr
                    q.append(curr.left)
                    q.append(curr.right)
            # works because last iteration goes through rightmost
            if rightSide:
                res.append(rightSide.val)
        return res