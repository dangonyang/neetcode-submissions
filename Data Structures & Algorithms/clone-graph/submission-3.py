"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # is it possible to have a stand alone node?: yes?

        # input: a node with val and neighbors
        # output: return node
        # goal: create a deep copy using node

        # initial approach:
        if not node:
            return None
        # create hm of nodes
        hm = {}
        # start at node, create a copy of it
        # add it to hm, q
        hm[node] = Node(node.val)
        q = deque()
        q.append(node)
        # while q
        while q:
            curr = q.popleft()
            # iterate through all neighbors
            for n in curr.neighbors:
                # if neighbor not in seen
                if n not in hm:
                    # add neighbor to seen with node
                    hm[n] = Node(n.val)
                    q.append(n)
                hm[curr].neighbors.append(hm[n])
        # reutrn node
        return hm[node]