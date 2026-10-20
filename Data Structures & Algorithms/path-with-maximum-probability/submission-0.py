class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # can we have cycles? no
        # can weights be negative? no

        # input: number of nodes (int), edges in form [src, dst] (list of int list), success probability (list of floats), start node (int), end_node (int)
        # output: maximum probability (float)
        # goal: find the maximum probability in the graph

        # initial approach:
        # create an adjacency list in the form of key = node number, value = [(dst, prob)]
        adjList = {}
        for i, edge in enumerate(edges):
            if edge[0] not in adjList:
                adjList[edge[0]] = []
            if edge[1] not in adjList:
                adjList[edge[1]] = []
            adjList[edge[0]].append((edge[1], succProb[i]))
            adjList[edge[1]].append((edge[0], succProb[i]))

        # run dijkstra's on the adjacency list (instead of adding weight, we multiply)
        # establish minHeap and shortest hm
        shortest = {}
        # max prob, node number
        maxHeap = [(-1, start_node)]
        # iterate through minHeap
        while maxHeap:
            # pop element for minHeap
            maxProb, node = heapq.heappop(maxHeap)
            # shortest (max prob) path of current element is weight
            if node in shortest:
                continue
            shortest[node] = abs(maxProb)
            # if popped node is in shortest, then continue
            # for neighbor in adjList[key]
            for neighbor, prob in adjList.get(node, []):
                # calculate max weight 
                # append neighbor to heap
                heapq.heappush(maxHeap, (-(abs(maxProb) * prob), neighbor))
        return shortest[end_node] if end_node in shortest else 0
            
        # adjList = { 0: [(1, 0.5), (2, 0.2)], 1: [(2, 0.5)]}
        # (-0.25, 2)
        # (-0.2, 2)

