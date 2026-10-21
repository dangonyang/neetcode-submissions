class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # nodes can be alone
        # does each node have more than two edges? no
        # no cycles

        # inputs: number of nodes (int), edges in form [src, dst] (list of int list))
        # output: int representing the label the node
        # goal: find the sole champion (exactly one)

        # initial approach:
        if n == 1:
            return 0

        # create an adjacency list for the edges [dst, arrows]
        adjList = {}
        arrows = [0] * n
        # arrows = [0, 0, 2]
        zeros = []
        for edge in edges:
            src, dst = edge[0], edge[1]
            # initialize arrows as 0
            if src not in adjList:
                adjList[src] = []
            adjList[src].append(dst)
        # adjList = {0: [2], 1: [2]}
        # go through each value in the adjacency list 
        for key in adjList:
            # iterate through its dst nodes
            for val in adjList[key]:
                # add 1 to # of arrows for dst node in adjacency list
                arrows[val] += 1 
        # check number of zeros at each node
        for i, num in enumerate(arrows):
            if num == 0:
                zeros.append(i)
                # zeros = [0, 1]
        # return the node where there is 0 arrows going into it, if there are multiple, return -1
        return zeros[0] if zeros and len(zeros) == 1 else -1