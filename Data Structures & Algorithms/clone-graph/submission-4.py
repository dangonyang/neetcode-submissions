"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hm ={}
        hm[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n not in hm:
                    hm[n] = Node(n.val)
                    q.append(n)
                hm[curr].neighbors.append(hm[n])
        return hm[node]